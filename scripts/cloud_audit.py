"""GitHub Actions 漫画源巡检；只执行 catalog.json 中已审阅且哈希匹配的源码。"""

import argparse
import concurrent.futures
import contextlib
import csv
import hashlib
import io
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
from datetime import datetime, timezone, timedelta
from urllib.error import HTTPError
from urllib.parse import quote, unquote, urlparse
from urllib.request import Request, urlopen
from prepare_client import prepare

ROOT = Path(__file__).resolve().parents[1]
POLICY = {
    "concurrency": 4, "pages": 1, "imageSamples": 1, "retries": 0,
    "requestTimeoutMs": 10000, "stageTimeoutMs": 20000,
    "sourceTimeoutMs": 90000, "minRequestIntervalMs": 300,
    "maxRequests": 60, "maxResponseBytes": 20971520, "maxTraceEvents": 1600,
}
LABELS = {"passed": "通过", "partial": "部分通过", "failed": "失败",
          "skipped": "跳过", "listed": "仅加载"}
CATEGORIES = {
    "auth_required": "需要登录", "credentials_missing": "未提供账号凭据",
    "contract_violation": "返回结构或样本不满足契约", "anti_bot": "反爬拦截",
    "dns_error": "DNS 错误", "tls_error": "TLS 错误", "network_error": "网络错误",
    "http_error": "HTTP 错误", "timeout": "请求超时", "stage_timeout": "阶段超时",
    "source_timeout": "整源超时", "config_error": "源配置错误",
    "config_parse": "源加载或版本不兼容", "runtime_unsupported": "运行时不支持",
    "image_decode_failed": "图片解码失败", "mutation_disabled": "写操作未启用",
    "missing_input": "缺少样本输入", "dependency_failed": "前置能力未通过",
    "not_triggered": "本次成功路径未触发", "interactive_required": "需要交互",
    "unreviewed_update": "上游变更待审阅", "download_failed": "源码下载失败",
}


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(value, ensure_ascii=False, indent=2)
    path.write_text(text.encode("utf-8", errors="replace").decode("utf-8") + "\n",
                    encoding="utf-8", newline="\n")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def request(url, api=False):
    parsed = urlparse(url)
    allowed = {"api.github.com"} if api else {"raw.githubusercontent.com"}
    if parsed.scheme != "https" or parsed.hostname not in allowed or parsed.username:
        raise ValueError("仅允许 GitHub 官方 HTTPS 地址")
    headers = {"User-Agent": "venera-source-index", "Accept": "application/vnd.github+json"}
    if api and os.environ.get("GH_TOKEN"):
        headers["Authorization"] = f"Bearer {os.environ['GH_TOKEN']}"
    with urlopen(Request(url, headers=headers), timeout=35) as response:
        if urlparse(response.url).hostname not in allowed:
            raise ValueError("响应跳转到了非允许域名")
        data = response.read(2 * 1024 * 1024 + 1)
    if len(data) > 2 * 1024 * 1024:
        raise ValueError("响应超过 2 MiB")
    return data


def pinned(url):
    return bool(re.fullmatch(
        r"https://raw\.githubusercontent\.com/[^/]+/[^/]+/[a-f0-9]{40}/.+\.js", url))


def validate_catalog(catalog):
    assert catalog["schemaVersion"] == 1
    seen = set()
    for item in catalog["sources"]:
        assert re.fullmatch(r"[a-f0-9]{64}", item["sha256"])
        assert pinned(item["url"]), item["url"]
        assert item["id"] == item["sha256"], "构建 ID 必须是完整源码哈希"
        assert item["id"] not in seen, "同字节源码只能入库一次"
        seen.add(item["id"])
        assert isinstance(item["key"], str) and item["key"] and len(item["key"]) <= 120
        assert set(item["sample"]) <= {"keyword", "comicId", "epId", "searchOptions"}
        assert not item.get("allowMutations")
        assert isinstance(item.get("settings", {}), dict)
        if item.get("runtimeProfile"):
            assert item["key"] == "jm" and item["version"] == "1.9.2"
            assert item["settings"].get("dailyCheckInTask") is False
            assert item["runtimeProfile"] == "venerax"
            assert item.get("verifyProfiles") == ["venera-next"]
            assert item["sample"].get("comicId") and item["sample"].get("epId")
    return catalog


def core(source):
    passed = {s["path"] for s in source["stages"]
              if s["status"] in ("passed", "recovered")}
    entry = any(p.startswith(("search.", "explore[", "categoryComics."))
                and ".load" in p for p in passed)
    return entry and {
        "source.load", "comic.loadInfo", "comic.loadEp", "image.download", "image.decode"
    } <= passed


def reason_zh(reason):
    known = {
        "Comic list is empty; provide a representative keyword or case": "当前关键词或列表为空，需复核样本或解析规则",
        "Comic requires valid id, title and cover": "列表项缺少合法 ID、标题或封面",
        "Chapter map is empty": "详情没有返回章节",
        "Details require title and cover": "详情缺少标题或封面",
        "Expected nonempty image URL array": "章节没有返回非空图片列表",
        "Comic ID does not match idMatch": "漫画 ID 与源声明的规则不一致",
        "Network request failed: fetch failed": "网络请求失败",
        "Network request failed: HTTP request timed out": "网络请求超时",
        "maxPage must be a nonnegative integer": "分页字段 maxPage 不是非负整数",
        "Image response is empty": "图片响应为空",
        "Image succeeded; failure recovery was not invoked": "图片已成功，未触发失败恢复回调",
        "Provide credentials.cookieValues": "未提供 Cookie 登录凭据",
        "Favorites require authenticated account data": "网络收藏需要已登录的账号",
        "Requires allowMutations:true and an explicit case": "默认禁用写操作，且没有显式写操作用例",
        "Not implemented": "当前运行时未实现该能力",
        "Worker terminated before this capability": "巡检进程已停止，未执行该能力",
    }
    return text(known.get(reason, reason))


def run(*args, **kwargs):
    return subprocess.run(list(args), check=True, **kwargs)


def setup_cli(work):
    """不使用旧缓存：每次先取得上游默认分支的最新提交，随后安装其锁定依赖。"""
    work.mkdir(parents=True, exist_ok=True)
    directory = work / "latest-cli"
    if directory.exists():
        raise ValueError("最新 CLI 目录已存在；请使用本次运行独立的工作目录")
    run("git", "clone", "--depth", "1", "https://github.com/Gandum2077/venera-patrol-cli.git",
        str(directory))
    commit = run("git", "-C", str(directory), "rev-parse", "HEAD",
                 capture_output=True, text=True).stdout.strip()
    latest = run("git", "ls-remote", "https://github.com/Gandum2077/venera-patrol-cli.git",
                 "HEAD", capture_output=True, text=True).stdout.split()[0]
    if commit != latest:
        raise ValueError("安装期间 CLI 上游发生变化；请重跑以确保使用最新提交")
    package = load(directory / "package.json")
    metadata = {
        "repository": "Gandum2077/venera-patrol-cli", "commit": commit,
        "version": package["version"], "packageLockSha256": sha((directory / "package-lock.json").read_bytes()),
        "checkedAt": datetime.now(timezone.utc).isoformat(),
    }
    metadata["adapterSha256"] = prepare(directory)
    profiles = load(ROOT / "monitor/clients.json")
    for name, profile in profiles["profiles"].items():
        for file, digest in profile["files"].items():
            data = request(f"https://raw.githubusercontent.com/{profile['repository']}/"
                           f"{profile['commit']}/{file}")
            if sha(data) != digest:
                raise ValueError("客户端接口源码哈希不匹配")
            target = directory / "client-profiles" / name / file
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
    (directory / "client_bridge.test.mjs").write_bytes(
        (ROOT / "scripts/client_bridge.test.mjs").read_bytes())
    metadata["clientProfiles"] = profiles["profiles"]
    # 构建上下文只含 CLI 文件，不把 runner 的凭据、仓库或 Docker socket 传给源。
    dockerfile = ROOT / "scripts/patrol.Dockerfile"
    image = f"venera-patrol:{commit}"
    run("docker", "build", "--pull", "--tag", image, "--file", str(dockerfile), str(directory))
    metadata["image"] = image
    metadata["nodeVersion"] = run(
        "docker", "run", "--rm", "--entrypoint", "node", image, "--version",
        capture_output=True, text=True).stdout.strip()
    metadata["imageId"] = run("docker", "image", "inspect", "--format={{.Id}}", image,
                              capture_output=True, text=True).stdout.strip()
    save(work / "cli.json", metadata)
    print(f"已安装最新巡检 CLI：{commit}，版本 {metadata['version']}。", flush=True)


def discover(work):
    catalog = validate_catalog(load(ROOT / "monitor/catalog.json"))
    config = load(ROOT / "monitor/upstreams.json")
    known = {i["sha256"] for i in catalog["sources"]}
    samples = {i["key"]: i["sample"] for i in catalog["sources"]}
    commits = {}

    def resolve(repo, ref=None):
        marker = (repo, ref)
        if marker not in commits:
            if ref and re.fullmatch(r"[a-f0-9]{40}", ref):
                commits[marker] = ref
            else:
                suffix = f"/{quote(ref, safe='')}" if ref else "?per_page=1"
                value = json.loads(request(f"https://api.github.com/repos/{repo}/commits{suffix}", api=True))
                commits[marker] = value["sha"] if ref else value[0]["sha"]
        return commits[marker]

    def inspect(repo):
        updates, errors = [], []
        try:
            commit = resolve(repo)
            entries = json.loads(request(f"https://raw.githubusercontent.com/{repo}/{commit}/index.json"))
            if not isinstance(entries, list):
                raise ValueError("索引不是数组")
            for entry in entries:
                if not isinstance(entry, dict):
                    continue
                url = entry.get("url", "")
                key, name = entry.get("key"), entry.get("name")
                file = entry.get("fileName") or Path(urlparse(url).path).name
                if not key or not name or not isinstance(file, str) or not file.endswith(".js"):
                    continue
                target, ref = repo, commit
                if url.startswith("https://cdn.jsdelivr.net/gh/"):
                    match = re.fullmatch(r"https://cdn.jsdelivr.net/gh/([^/]+/[^/@]+)@([^/]+)/(.+)", url)
                    if not match:
                        continue
                    target, ref, file = match.groups()
                elif url.startswith("https://raw.githubusercontent.com/"):
                    parts = urlparse(url).path.strip("/").split("/")
                    target = "/".join(parts[:2])
                    if parts[2:4] == ["refs", "heads"]:
                        ref, file = parts[4], "/".join(parts[5:])
                    else:
                        ref, file = parts[2], "/".join(parts[3:])
                elif url and not url.startswith(f"https://github.com/{repo}/releases/"):
                    errors.append(f"{text(name)}：暂不执行非 GitHub 原始地址")
                    continue
                try:
                    ref = resolve(target, ref)
                    fixed = f"https://raw.githubusercontent.com/{target}/{ref}/{quote(unquote(file), safe='/')}"
                    data = request(fixed)
                    digest = sha(data)
                    if digest in known:
                        continue
                    code = data.decode("utf-8-sig")
                    for field in ("key", "version", "minAppVersion"):
                        match = re.search(r"(?m)^\s*" + field + r"""\s*=\s*["']([^"']+)["']""", code)
                        if match:
                            entry[field] = match.group(1)
                    actual_key = entry.get("key", key)
                    updates.append({
                        "id": digest, "key": actual_key, "name": name,
                        "version": entry.get("version", ""), "fileName": Path(unquote(file)).name,
                        "url": fixed, "sha256": digest, "repository": target,
                        "minAppVersion": entry.get("minAppVersion", "1.0.0"),
                        "sample": samples.get(actual_key, {"keyword": "火影"}),
                        "trackedBy": [repo], "priority": 20 if repo in config["priorityRepositories"] else 0,
                        "state": "上游变更待审阅；未加载、未执行、不进入可用索引",
                    })
                except Exception as error:
                    errors.append(f"{text(name)}：{text(error)}")
            return updates, {"repository": repo, "commit": commit, "errors": errors}
        except Exception as error:
            return [], {"repository": repo, "errors": [text(error)]}

    updates, repositories = {}, []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for candidates, repository in pool.map(inspect, config["repositories"]):
            repositories.append(repository)
            for candidate in candidates:
                if candidate["id"] in updates:
                    candidate["trackedBy"] = sorted(set(
                        updates[candidate["id"]]["trackedBy"] + candidate["trackedBy"]))
                updates[candidate["id"]] = candidate
    new_repositories = []
    search_error = ""
    try:
        result = json.loads(request(
            "https://api.github.com/search/repositories?q=venera+in:name,description&sort=updated&per_page=100",
            api=True))
        for item in result["items"]:
            if item["full_name"] not in config["repositories"]:
                new_repositories.append({"repository": item["full_name"],
                                         "description": text(item.get("description") or "")})
    except Exception as error:
        search_error = text(error)
    save(work / "artifact/discovery.json", {
        "schemaVersion": 1, "checkedAt": datetime.now(timezone.utc).isoformat(),
        "updates": list(updates.values()), "repositories": repositories,
        "newRepositories": new_repositories, "searchError": search_error,
    })
    print(f"上游检测完成：{len(repositories)} 个仓库，{len(updates)} 个待审阅源码构建。")


def collect_samples(source, work):
    trace = Path(source.get("traceFile", ""))
    try:
        # 容器内只可能写入 /work；不读取报告提供的任意本机路径。
        relative = trace.relative_to("/work")
    except ValueError:
        return {}
    file = work / relative
    sample = {}
    if not file.is_file():
        return sample
    for line in file.read_text(encoding="utf-8-sig").splitlines():
        event = json.loads(line)
        args = event.get("args", [])
        if event.get("event") == "capability.call" and event.get("stage") == "comic.loadEp" and len(args) >= 2:
            sample["comicId"] = args[0]
            if args[1] is not None:
                sample["epId"] = args[1]
    return sample


def patrol(work):
    catalog = validate_catalog(load(ROOT / "monitor/catalog.json"))
    metadata = load(work / "cli.json")
    latest = run("git", "ls-remote", "https://github.com/Gandum2077/venera-patrol-cli.git",
                 "HEAD", capture_output=True, text=True).stdout.split()[0]
    if latest != metadata["commit"]:
        raise ValueError("巡检前发现 CLI 已有更新；本次停止，必须重新获取最新 CLI")
    sources_dir = work / "source-bytes"
    sources_dir.mkdir()
    output = work / "container"
    output.mkdir()
    items = catalog["sources"]
    old_samples = {i["sha256"]: i["sample"] for i in load(ROOT / "sources.lock.json")}
    for item in items:
        # 清单中的显式样本优先；新通过构建也沿用上次同字节源码的已记录样本。
        item["effectiveSample"] = {**old_samples.get(item["sha256"], {}), **item["sample"]}
    failures = []

    def download(item):
        try:
            data = request(item["url"])
            if sha(data) != item["sha256"]:
                raise ValueError("源码 SHA-256 与审阅清单不一致")
            (sources_dir / f"{item['id']}.js").write_bytes(data)
            return item, None
        except Exception as error:
            return item, {"key": item["key"], "sourceSha256": item["sha256"], "status": "failed",
                          "stages": [{"path": "source.download", "status": "failed",
                                      "category": "download_failed", "reason": str(error)[:300]}]}

    available = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        for item, failure in pool.map(download, items):
            if failure:
                failures.append((item, failure))
            else:
                available.append(item)
    if len(failures) > max(3, len(items) // 10):
        raise ValueError("批量源码获取异常，停止本次发布，避免误删订阅")
    batches = []
    for item in available:
        for batch in batches:
            if (batch[0].get("runtimeProfile") == item.get("runtimeProfile") and
                    all(other["key"] != item["key"] for other in batch)):
                batch.append(item)
                break
        else:
            batches.append([item])
    records = [{"id": item["id"], "source": failure, "runtimeProfile": item.get("runtimeProfile"),
                "inputs": item["effectiveSample"]} for item, failure in failures]
    client_records = [
        {"id": item["id"], "source": failure, "runtimeProfile": profile, "inputs": item["effectiveSample"]}
        for item, failure in failures for profile in item.get("verifyProfiles", [])]
    batches += [[{**item, "runtimeProfile": profile, "verificationOnly": True}]
                for item in available for profile in item.get("verifyProfiles", [])]
    for number, batch in enumerate(batches):
        config = {
            "version": 1, "configPaths": [f"/work/{number}.index.json"],
            "output": f"/work/reports/{number}", "defaults": POLICY,
            "sources": {i["key"]: {"inputs": i["effectiveSample"], "settings": i.get("settings", {})}
                        for i in batch},
        }
        save(output / f"{number}.index.json", [
            {"key": i["key"], "fileName": f"/sources/{i['id']}.js"} for i in batch])
        save(output / f"{number}.config.json", config)
        command = [
            "docker", "run", "--rm", "--read-only", "--cap-drop=ALL",
            "--security-opt=no-new-privileges", "--pids-limit=256", "--memory=3g", "--cpus=2",
            "--user", f"{os.getuid()}:{os.getgid()}", "--env", "HOME=/tmp",
            "--tmpfs", "/tmp:rw,noexec,nosuid,size=1024m",
            "--mount", f"type=bind,source={sources_dir},target=/sources,readonly",
            "--mount", f"type=bind,source={output},target=/work",
        ]
        if batch[0].get("runtimeProfile"):
            command += ["--env", f"VENERA_CLIENT_PROFILE={batch[0]['runtimeProfile']}"]
        command += [metadata["image"], "check-all", "--config", f"/work/{number}.config.json", "--no-env"]
        print(f"第 {number + 1}/{len(batches)} 批：巡检 {len(batch)} 个已审阅构建。", flush=True)
        result = subprocess.run(command, timeout=max(300, len(batch) * 95), check=False)
        if result.returncode not in (0, 1):
            raise ValueError(f"巡检进程异常退出：{result.returncode}")
        reports = list((output / f"reports/{number}").glob("*/report.json"))
        if len(reports) != 1:
            raise ValueError("巡检没有生成唯一报告")
        report = load(reports[0])
        if report.get("schemaVersion") != 1 or len(report["sources"]) != len(batch):
            raise ValueError("最新 CLI 的报告格式或源数量不符合当前契约")
        for item, source in zip(batch, report["sources"], strict=True):
            if source.get("sourceSha256") and source["sourceSha256"] != item["sha256"]:
                raise ValueError("报告的执行源码哈希与下载字节不一致")
            if source["key"] != item["key"]:
                raise ValueError("实际 runtime key 与审阅清单不一致")
            selected = collect_samples(source, output)
            record = {
                "id": item["id"], "inputs": item["effectiveSample"],
                "sample": {**selected, **item["effectiveSample"]},
                "runtimeProfile": item.get("runtimeProfile"),
                "source": {key: source.get(key) for key in (
                    "key", "name", "version", "sourceSha256", "status", "startedAt", "stages")},
            }
            (client_records if item.get("verificationOnly") else records).append(record)
    payload = {"schemaVersion": 1, "catalogSha256": sha((ROOT / "monitor/catalog.json").read_bytes()),
               "checkedAt": datetime.now(timezone.utc).isoformat(), "cli": metadata,
               "policy": POLICY, "records": records, "clientRecords": client_records}
    # 一份持久结构化证据；原始 trace 不上传、不进入带写权限的发布任务。
    save(work / "artifact/patrol.json", payload)
    publish(payload, work / "artifact/preview")


def text(value):
    return re.sub(r"[\x00-\x1f\x7f]", " ", str(value)).replace("|", "／")[:300]


def validate_client_record(record, item, payload):
    profile = record.get("runtimeProfile")
    if profile is None:
        assert not item.get("runtimeProfile"), "不能用旧运行时替代指定客户端"
        return
    profiles = load(ROOT / "monitor/clients.json")["profiles"]
    assert profile in profiles
    assert payload["cli"]["clientProfiles"] == profiles
    for name in ("scripts/client_bridge.mjs", "scripts/prepare_client.py", "monitor/clients.json"):
        assert payload["cli"]["adapterSha256"][name] == sha((ROOT / name).read_bytes())
    assert record["inputs"] == item["sample"], "客户端对照必须使用同一固定样本"
    stages = record["source"]["stages"]
    loaded = next((s for s in stages if s["path"] == "runtime.load"), None)
    if loaded and loaded["status"] == "passed":
        actual = json.loads(loaded["output"]["value"])
        expected = profiles[profile]
        assert actual["name"] == profile
        assert all(actual[k] == expected[k] for k in ("repository", "commit", "version", "scope"))
        assert actual["bootstrapSha256"] == expected["files"]["assets/init.js"]
    if core(record["source"]):
        assert loaded and loaded["status"] == "passed"


def publish(payload, destination):
    catalog = validate_catalog(load(ROOT / "monitor/catalog.json"))
    assert payload["schemaVersion"] == 1
    assert payload["catalogSha256"] == sha((ROOT / "monitor/catalog.json").read_bytes())
    items = {i["id"]: i for i in catalog["sources"]}
    assert len(payload["records"]) == len(items)
    seen, selected, rows = set(), {}, []
    for record in payload["records"]:
        item = items[record["id"]]
        assert record["id"] not in seen
        seen.add(record["id"])
        source = record["source"]
        assert record.get("runtimeProfile") == item.get("runtimeProfile")
        validate_client_record(record, item, payload)
        assert source["key"] == item["key"]
        assert source["status"] in ("passed", "partial", "failed", "skipped")
        assert len(source["stages"]) < 10000
        if source.get("sourceSha256"):
            assert source["sourceSha256"] == item["sha256"]
        for name, value in item["sample"].items():
            if "inputs" in record:
                assert record["inputs"].get(name) == value, "显式固定样本不能被证据改写"
        success = core(source)
        if success:
            assert source["sourceSha256"] == item["sha256"]
        display_item = {**item, "sample": record.get("sample", item["sample"])}
        rows.append((display_item, source, success))
        score = (success, source["status"] == "passed", item.get("priority", 0),
                 tuple(int(x) for x in re.findall(r"\d+", item["version"])[:3]))
        if item["key"] not in selected or score > selected[item["key"]][0]:
            selected[item["key"]] = (score, item, source, record.get("sample", item["sample"]))
    current_core = sum(core(source) for _, _, source, _ in selected.values())
    previous = load(ROOT / "sources.lock.json")
    if previous and current_core == 0:
        raise ValueError("全批核心链路失败；保留上次订阅，本次运行不得发布为成功")
    main, extended, locks = [], [], []
    checked = payload["checkedAt"]
    for _, item, source, sample in selected.values():
        if not core(source):
            continue
        assert pinned(item["url"])
        status = source["status"]
        entry = {
            "name": item["name"], "key": item["key"], "version": item["version"],
            "fileName": item["fileName"], "url": item["url"],
            "minAppVersion": item["minAppVersion"],
            "description": ("核心阅读链路及本次执行项通过" if status == "passed" else
                            "核心阅读链路通过；其他能力存在失败或跳过，详见中文巡检报告"),
        }
        channel = "main" if status == "passed" else "extended"
        (main if channel == "main" else extended).append(entry)
        locks.append({
            **entry, "sha256": item["sha256"], "minAppVersion": item["minAppVersion"],
            "officialKey": item.get("officialKey", False), "status": status, "channel": channel,
            "sample": sample, "checkedAt": checked, "buildId": item["id"],
            "trackedBy": item.get("trackedBy", []), "cliCommit": payload["cli"]["commit"],
            "runtimeProfile": item.get("runtimeProfile", "venera-original-1.6.3"),
            "limitations": [
                {"stage": s["path"], "status": LABELS.get(s["status"], s["status"]),
                 "category": CATEGORIES.get(s.get("category"), s.get("category", "")),
                 "reason": reason_zh(s.get("reason", ""))}
                for s in source["stages"] if s["status"] not in ("passed", "recovered")
            ],
        })
    main.sort(key=lambda i: i["key"])
    extended.sort(key=lambda i: i["key"])
    locks.sort(key=lambda i: i["key"])
    assert len({i["key"] for i in main + extended}) == len(locks)
    for name, data in (("index.json", main), ("extended.json", extended), ("sources.lock.json", locks)):
        save(destination / name, data)
    zone_date = datetime.fromisoformat(checked).astimezone(
        timezone(timedelta(hours=8), "Asia/Hong_Kong")).isoformat()
    lines = [
        "# Venera 漫画源云端巡检报告", "",
        f"核验时间：{zone_date}（香港时间）。",
        f"巡检工具：`Gandum2077/venera-patrol-cli` {payload['cli']['version']}，"
        f"提交 `{payload['cli']['commit']}`。",
        f"依赖锁 SHA-256：`{payload['cli']['packageLockSha256']}`。",
        f"本次审阅清单：{len(rows)} 个构建；主索引 **{len(main)}** 项，扩展索引 **{len(extended)}** 项。", "",
        "固定漫画及章节、源码字节哈希和 CLI 提交均保留。主索引必须同次通过入口、详情、章节、图片下载与解码，且整次报告为 passed；"
        "扩展索引要求相同核心链路通过，其他能力可有失败或跳过。旧成功结果不代替新失败。", "",
        "GitHub 托管 runner 的网络与用户设备不同；未在用户设备验证导入或阅读。"
        "普通构建仍使用原版 1.6.3 Runtime；jm 1.9.2 使用已核验的 VeneraX 原始 bootstrap，"
        "另以相同样本对照 Venera-Next。适配范围见 CLIENT_COMPATIBILITY.md，"
        "客户端对照复测见 CLIENT_RESULTS.md。", "",
        "## 三个自用仓库", "",
    ]
    for repo in catalog["priorityRepositories"]:
        group = [(i, s, ok) for i, s, ok in rows if repo in i.get("trackedBy", [])]
        lines.append(f"- `{repo}`：已审阅构建 {len(group)} 个，核心链路通过 {sum(ok for _, _, ok in group)} 个。")
    lines += ["", "## 逐构建结果", "", "| 源名称 | key | 仓库 | 版本 | 巡检环境 | 核心链路 | 整次状态 | 首个失败／跳过 |",
              "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    csv_rows = [["源名称", "源标识", "仓库", "版本", "核心阅读链路", "整次状态", "固定漫画ID",
                 "固定章节ID", "关键词", "失败阶段", "失败类别", "失败说明", "源码SHA256", "源码地址", "巡检环境"]]
    for item, source, success in sorted(rows, key=lambda row: (row[0]["key"], -row[0].get("priority", 0))):
        unsuccessful = [s for s in source["stages"] if s["status"] not in ("passed", "recovered")]
        failed = [s for s in unsuccessful if s["status"] == "failed"]
        first = (failed or unsuccessful or [{}])[0]
        category = CATEGORIES.get(first.get("category"), first.get("category", ""))
        problem = f"{first.get('path', '')}：{category}" if first else ""
        lines.append("| " + " | ".join(text(v) for v in (
            item["name"], item["key"], item["repository"], item["version"],
            item.get("runtimeProfile", "原版 1.6.3 Runtime"),
            "通过" if success else "未完整通过", LABELS[source["status"]], problem)) + " |")
        sample = item["sample"]
        csv_rows.append([item["name"], item["key"], item["repository"], item["version"],
                         "通过" if success else "未完整通过", LABELS[source["status"]],
                        sample.get("comicId", ""), sample.get("epId", ""), sample.get("keyword", ""),
                        first.get("path", ""), category, reason_zh(first.get("reason", "")),
                        item["sha256"], item["url"], item.get("runtimeProfile", "原版 1.6.3 Runtime")])
    lines += ["", "## 主索引", "", "、".join(i["name"] for i in main) or "本次没有符合主索引标准的源。",
              "", "## 扩展索引", "", "、".join(i["name"] for i in extended) or "本次没有扩展源。", ""]
    destination.mkdir(parents=True, exist_ok=True)
    (destination / "RESULTS.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")
    with (destination / "sources.zh.csv").open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.writer(stream)
        for row in csv_rows:
            writer.writerow(["'" + str(value) if str(value).startswith(("=", "+", "-", "@")) else value
                             for value in row])
    save(destination / "audit-status.json", {
        "checkedAt": checked, "cli": payload["cli"], "catalogSha256": payload["catalogSha256"],
        "builds": len(rows), "main": len(main), "extended": len(extended),
        "runUrl": os.environ.get("AUDIT_RUN_URL", ""),
    })
    publish_clients(payload, catalog, destination)
    print(f"中文报告已生成：主索引 {len(main)} 项、扩展索引 {len(extended)} 项。", flush=True)


def publish_clients(payload, catalog, destination):
    items = {i["id"]: i for i in catalog["sources"]}
    expected = {(i["id"], profile) for i in items.values() for profile in i.get("verifyProfiles", [])}
    actual = [(r["id"], r.get("runtimeProfile")) for r in payload.get("clientRecords", [])]
    assert len(actual) == len(expected) and set(actual) == expected, "客户端对照证据缺失或重复"
    records = [r for r in payload["records"] if r.get("runtimeProfile")]
    records += payload.get("clientRecords", [])
    lines = ["# VeneraX／Venera-Next 固定样本对照结果", "",
             f"核验时间：{payload['checkedAt']}（UTC）。",
             f"最新上游 CLI 提交：`{payload['cli']['commit']}`；同时加载本仓库记录哈希的接口适配层。",
             "结果为 Node 宿主上的真实客户端 JS 接口巡检，不代表 Flutter UI 或用户设备实测。", ""]
    clean_records = []
    for record in records:
        item = items[record["id"]]
        validate_client_record(record, item, payload)
        source = record["source"]
        assert source["key"] == item["key"]
        if core(source):
            assert source["sourceSha256"] == item["sha256"]
        elif source.get("sourceSha256"):
            assert source["sourceSha256"] == item["sha256"]
        profile = record["runtimeProfile"]
        definition = payload["cli"]["clientProfiles"][profile]
        lines += [f"## {definition['repository']} {definition['version']}", "",
                  f"- 源：`{item['key']}` {item['version']}；最低版本 `{item['minAppVersion']}`（保持原声明）。",
                  f"- 客户端接口提交：`{definition['commit']}`。",
                  f"- 源码 SHA-256：`{item['sha256']}`。",
                  f"- 固定样本：`{json.dumps(record['inputs'], ensure_ascii=False)}`。",
                  f"- 核心链路：{'通过' if core(source) else '未完整通过'}；整次状态：{LABELS[source['status']]}。",
                  "", "| 阶段 | 状态 | 类别／说明 |", "| --- | --- | --- |"]
        for stage in source["stages"]:
            lines.append("| " + " | ".join(text(v) for v in (
                stage["path"], LABELS.get(stage["status"], stage["status"]),
                reason_zh(stage.get("reason", "")))) + " |")
        lines.append("")
        clean_records.append(record)
    save(destination / "client-results.json", {
        "schemaVersion": 1, "checkedAt": payload["checkedAt"], "cli": payload["cli"],
        "records": clean_records, "runUrl": os.environ.get("AUDIT_RUN_URL", "")})
    (destination / "CLIENT_RESULTS.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


def publish_discovery(discovery, destination):
    assert discovery["schemaVersion"] == 1
    for item in discovery["updates"]:
        assert pinned(item["url"]) and item["id"] == item["sha256"]
        assert re.fullmatch(r"[a-f0-9]{64}", item["sha256"])
    save(destination / "pending-updates.json", discovery)
    lines = [
        "# 上游变更与待审阅候选", "",
        f"检查时间：{discovery['checkedAt']}（UTC）。",
        f"检查 {len(discovery['repositories'])} 个已登记仓库；"
        f"发现 {len(discovery['updates'])} 个未审阅源码构建。", "",
        "新代码只下载计算哈希及读取声明字段，不通过 list、init 或巡检执行。"
        "维护者在 GitHub 审阅固定提交的 JS 后，把候选加入 monitor/catalog.json；"
        "后续 Actions 才会执行巡检并按主／扩展标准自动收录。", "",
        "## 源码变动", "", "| 名称 | key | 版本 | 仓库 | 最低应用版本 | SHA-256 |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in discovery["updates"]:
        lines.append("| " + " | ".join(text(item.get(key, "")) for key in
                     ("name", "key", "version", "repository", "minAppVersion", "sha256")) + " |")
    lines += ["", "## 索引获取问题", ""]
    for repo in discovery["repositories"]:
        if repo["errors"]:
            lines.append(f"- `{text(repo['repository'])}`：" + "；".join(text(e) for e in repo["errors"][:5]))
    lines += ["", "## 新仓库线索", "",
              "仅列本次 GitHub 更新排序搜索第一页的未登记仓库，尚未认定为漫画源，不代表全网穷尽。", ""]
    for item in discovery["newRepositories"]:
        lines.append(f"- `{text(item['repository'])}`：{text(item['description'])}")
    if discovery["searchError"]:
        lines.append("仓库搜索未完整完成：" + text(discovery["searchError"]))
    (destination / "UPDATES.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def self_test():
    global ROOT
    stage_names = ["source.load", "search.load", "comic.loadInfo", "comic.loadEp",
                   "image.download", "image.decode"]
    stages = [{"path": path, "status": "passed"} for path in stage_names]
    assert core({"stages": stages})
    assert not core({"stages": stages[:-1]})
    assert not core({"stages": stages[:1] + stages[2:]})
    assert not pinned("https://github.com/a/b/blob/main/a.js")
    assert pinned("https://raw.githubusercontent.com/a/b/" + "a" * 40 + "/a.js")
    catalog = validate_catalog(load(ROOT / "monitor/catalog.json"))
    assert set(catalog["priorityRepositories"]) == {
        "hea784/venera-configs", "BB-CHICKEN/venera-jm", "handahao666-boop/venera_comic_source"}
    assert any(i.get("sample", {}).get("comicId") for i in catalog["sources"])
    client_item = next(i for i in catalog["sources"] if i.get("runtimeProfile") == "venerax")
    profiles = load(ROOT / "monitor/clients.json")["profiles"]
    profile = profiles["venerax"]
    identity = {**{k: profile[k] for k in ("repository", "commit", "version", "scope")},
                "name": "venerax", "bootstrapSha256": profile["files"]["assets/init.js"]}
    fixture_record = {
        "runtimeProfile": "venerax", "inputs": client_item["sample"],
        "source": {"stages": [{"path": "runtime.load", "status": "passed",
                              "output": {"value": json.dumps(identity)}}]}}
    fixture_payload = {"cli": {
        "clientProfiles": profiles,
        "adapterSha256": {name: sha((ROOT / name).read_bytes()) for name in (
            "scripts/client_bridge.mjs", "scripts/prepare_client.py", "monitor/clients.json")}}}
    validate_client_record(fixture_record, client_item, fixture_payload)
    for field in ("commit", "version", "bootstrapSha256"):
        altered = json.loads(json.dumps(fixture_record))
        wrong = {**identity, field: "伪造值"}
        altered["source"]["stages"][0]["output"]["value"] = json.dumps(wrong)
        try:
            validate_client_record(altered, client_item, fixture_payload)
            raise RuntimeError("错误客户端身份未被拒绝")
        except AssertionError:
            pass
    original_root = ROOT
    with tempfile.TemporaryDirectory() as directory:
        ROOT = Path(directory)
        try:
            item = {
                "id": "a" * 64, "sha256": "a" * 64, "key": "sample", "name": "测试漫画源",
                "url": "https://raw.githubusercontent.com/a/b/" + "c" * 40 + "/a.js",
                "version": "1.0.0", "fileName": "a.js", "repository": "a/b",
                "minAppVersion": "1.0.0", "sample": {"comicId": "1", "epId": "2", "keyword": "漫画"},
            }
            save(ROOT / "monitor/catalog.json", {
                "schemaVersion": 1, "priorityRepositories": catalog["priorityRepositories"],
                "sources": [item]})
            save(ROOT / "sources.lock.json", [{"key": "sample"}])
            source = {"key": "sample", "sourceSha256": item["sha256"],
                      "status": "passed", "stages": stages}
            payload = {
                "schemaVersion": 1, "catalogSha256": sha((ROOT / "monitor/catalog.json").read_bytes()),
                "checkedAt": "2026-10-24T00:00:00+00:00",
                "cli": {"commit": "c" * 40, "version": "测试工具", "packageLockSha256": "d" * 64},
                "records": [{"id": item["id"], "source": source,
                             "inputs": item["sample"], "sample": item["sample"]}],
            }
            with contextlib.redirect_stdout(io.StringIO()):
                publish(payload, ROOT / "out")
            assert len(load(ROOT / "out/index.json")) == 1
            source["status"] = "partial"
            source["stages"] = stages + [{"path": "account.login", "status": "skipped",
                                         "category": "credentials_missing"}]
            with contextlib.redirect_stdout(io.StringIO()):
                publish(payload, ROOT / "out")
            assert not load(ROOT / "out/index.json") and len(load(ROOT / "out/extended.json")) == 1
            source["sourceSha256"] = "b" * 64
            try:
                publish(payload, ROOT / "out")
                raise RuntimeError("错误哈希未被拒绝")
            except AssertionError:
                pass
            source["sourceSha256"] = item["sha256"]
            source["stages"] = stages[:-1]
            try:
                publish(payload, ROOT / "out")
                raise RuntimeError("缺少图片解码仍被收录")
            except ValueError:
                pass
        finally:
            ROOT = original_root
    print(f"云端脚本自检通过；已审阅清单 {len(catalog['sources'])} 个构建。")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["setup-cli", "discover", "patrol", "publish", "self-test"])
    parser.add_argument("--work", type=Path, default=Path(".work"))
    parser.add_argument("--input", type=Path)
    args = parser.parse_args()
    if args.command == "setup-cli":
        setup_cli(args.work.resolve())
    elif args.command == "patrol":
        patrol(args.work.resolve())
    elif args.command == "discover":
        discover(args.work.resolve())
    elif args.command == "publish":
        publish(load(args.input), ROOT)
        publish_discovery(load(args.input.with_name("discovery.json")), ROOT)
    else:
        self_test()


if __name__ == "__main__":
    main()
