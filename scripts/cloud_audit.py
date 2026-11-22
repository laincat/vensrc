"""GitHub Actions 漫画源巡检；执行 catalog.json 中已审阅且哈希匹配的源码，
并在同一隔离容器里试跑上游候选。候选只有经发布阶段复核后才会写进清单。"""

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
import time
from datetime import datetime, timezone, timedelta
from urllib.error import HTTPError
from urllib.parse import quote, unquote, urlparse
from urllib.request import Request, urlopen
from prepare_client import prepare

ROOT = Path(__file__).resolve().parents[1]
OFFICIAL_REPOSITORY = "venera-app/venera-configs"
# 上游线索检索：社区仓库的命名并不统一，单一关键词会漏掉大量在维护的源仓库。
SEARCH_QUERIES = (
    "venera in:name,description",
    "topic:venera",
    "venera-configs in:name",
    "venera-sources in:name",
    "venera 漫画源 in:name,description",
)
POLICY = {
    "concurrency": 4, "pages": 1, "imageSamples": 1, "retries": 0,
    "requestTimeoutMs": 10000, "stageTimeoutMs": 20000,
    "sourceTimeoutMs": 90000, "minRequestIntervalMs": 300,
    "maxRequests": 60, "maxResponseBytes": 20971520, "maxTraceEvents": 1600,
}
LABELS = {"passed": "通过", "recovered": "恢复后通过", "partial": "部分通过", "failed": "失败",
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
    "rate_limited": "请求限流", "region_restricted": "地区限制",
    "runtime_dependency": "运行时依赖错误", "request_limit": "超过请求预算",
    "response_limit": "响应超过大小限制",
}


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def generated_path(root, name):
    if name in ("index.json", "extended.json"):
        folder = "subscriptions"
    elif name.endswith(".md"):
        folder = "reports"
    else:
        folder = "data"
    return root / folder / name


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
    headers = {"User-Agent": "vensrc", "Accept": "application/vnd.github+json"}
    if api and os.environ.get("GH_TOKEN"):
        headers["Authorization"] = f"Bearer {os.environ['GH_TOKEN']}"
    with urlopen(Request(url, headers=headers), timeout=35) as response:
        if urlparse(response.url).hostname not in allowed:
            raise ValueError("响应跳转到了非允许域名")
        if pinned(url) and unquote(response.url) != unquote(url):
            raise ValueError("固定源码地址发生重定向")
        data = response.read(2 * 1024 * 1024 + 1)
    if len(data) > 2 * 1024 * 1024:
        raise ValueError("响应超过 2 MiB")
    return data


def pinned(url):
    return bool(re.fullmatch(
        r"https://raw\.githubusercontent\.com/[^/]+/[^/]+/[a-f0-9]{40}/.+\.js", url))


def version_parts(version):
    if not isinstance(version, str) or not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError("版本必须是三段数字，无法确认的版本不得作为官方升级版收录")
    return tuple(int(part) for part in version.split("."))


def official_policy(root=None, snapshot=None):
    root = root or ROOT
    baseline = load(root / "monitor/official-keys.json")
    path = root / "data/official-exclusions.json"
    previous = load(path) if path.exists() else baseline
    if snapshot is None:
        snapshot = previous
    for policy in (baseline, previous, snapshot):
        assert set(policy) == {
            "schemaVersion", "repository", "indexCommit", "indexSha256", "checkedAt", "keys",
            "versions"}
        assert policy["schemaVersion"] == 2
        assert policy["repository"] == OFFICIAL_REPOSITORY
        assert re.fullmatch(r"[a-f0-9]{40}", policy["indexCommit"])
        assert re.fullmatch(r"[a-f0-9]{64}", policy["indexSha256"])
        assert policy["keys"] and all(isinstance(key, str) and key for key in policy["keys"])
        assert policy["keys"] == sorted(set(policy["keys"]))
        assert set(policy["versions"]) == set(policy["keys"])
        for version in policy["versions"].values():
            version_parts(version)
    assert set(baseline["keys"]) | set(previous["keys"]) <= set(snapshot["keys"]), \
        "官方版本基线集合不得缩小"
    for policy in (baseline, previous):
        assert all(version_parts(snapshot["versions"][key]) >= version_parts(version)
                   for key, version in policy["versions"].items()), "官方版本基线不得降低"
    return snapshot


def refresh_official_policy(root=None):
    previous = official_policy(root)
    commit = json.loads(request(
        f"https://api.github.com/repos/{OFFICIAL_REPOSITORY}/commits/HEAD", api=True))["sha"]
    assert re.fullmatch(r"[a-f0-9]{40}", commit)
    data = request(f"https://raw.githubusercontent.com/{OFFICIAL_REPOSITORY}/{commit}/index.json")
    entries = json.loads(data)
    assert isinstance(entries, list) and entries
    versions = dict(previous["versions"])
    for entry in entries:
        key, version = entry["key"], entry["version"]
        assert isinstance(key, str) and key
        version_parts(version)
        if key not in versions or version_parts(version) > version_parts(versions[key]):
            versions[key] = version
    return official_policy(root, {
        "schemaVersion": 2, "repository": OFFICIAL_REPOSITORY,
        "indexCommit": commit, "indexSha256": sha(data),
        "checkedAt": datetime.now(timezone.utc).isoformat(),
        "keys": sorted(versions), "versions": dict(sorted(versions.items())),
    })


def is_official_item(item):
    path = urlparse(item.get("url", "")).path.strip("/").split("/")
    target = "/".join(path[:2]).casefold()
    return (item.get("repository", "").casefold() == OFFICIAL_REPOSITORY
            or target == OFFICIAL_REPOSITORY)


def community_keys(items):
    """同一批构建里由社区仓库提供的 key 集合。"""
    return {item["key"] for item in items if not is_official_item(item)}


def excluded_official(item, policy, community=None):
    if is_official_item(item):
        # 官方原版默认只作诊断证据；仅当同一 key 没有任何社区构建时，才作为唯一可用版本参与订阅。
        return community is None or item["key"] in community
    official_version = policy["versions"].get(item["key"])
    if official_version is None:
        return bool(item.get("officialKey", False))
    try:
        return version_parts(item.get("version")) <= version_parts(official_version)
    except ValueError:
        return True


def excluded_wnacg(item):
    family = (item.get("key") in ("wnacg", "hj_wnacg") or
              bool(re.search(r"wnacg|[紳绅]士漫[畫画]", " ".join(
                  str(item.get(field, "")) for field in ("name", "fileName", "url")), re.I)))
    repository = item.get("repository")
    dedicated = (
        item.get("key") == "wnacg" and
        repository in (None, "laincat/vensrc") and
        bool(re.fullmatch(r"https://raw\.githubusercontent\.com/laincat/vensrc/[a-f0-9]{40}/sources/wnacg\.js",
                          item.get("url", ""))))
    return family and not dedicated


def source_annotation(item, notes):
    note = notes.get(item["id"])
    if note:
        assert item.get("repository") in ("BB-CHICKEN/venera-jm", "laincat/vensrc")
        return note
    repository = item.get("repository", "")
    return f"引用源：{repository}" if repository else "引用源：未知仓库"


def validate_catalog(catalog):
    assert catalog["schemaVersion"] == 1
    seen = set()
    for item in catalog["sources"]:
        assert not excluded_wnacg(item), "绅士漫画只允许 laincat/vensrc 独立维护版"
        if item["key"] == "wnacg":
            assert item.get("repository") == "laincat/vensrc", "绅士漫画只允许 laincat/vensrc 独立维护版"
        assert re.fullmatch(r"[a-f0-9]{64}", item["sha256"])
        assert pinned(item["url"]), item["url"]
        assert item["id"] == item["sha256"], "构建 ID 必须是完整源码哈希"
        assert item["id"] not in seen, "同字节源码只能入库一次"
        seen.add(item["id"])
        assert isinstance(item["key"], str) and item["key"] and len(item["key"]) <= 120
        assert set(item["sample"]) <= {"keyword", "comicId", "epId", "searchOptions"}
        assert not item.get("allowMutations")
        assert isinstance(item.get("settings", {}), dict)
        execution_policy(item)
        if item.get("runtimeProfile"):
            assert item["runtimeProfile"] == "venerax"
            assert item.get("verifyProfiles") == ["venera-next"]
        if item["key"] == "jm" and item["version"] == "1.9.2":
            assert item["settings"].get("dailyCheckInTask") is False
            assert item["sample"].get("comicId") and item["sample"].get("epId")
    items = {item["id"]: item for item in catalog["sources"]}
    for item in catalog["sources"]:
        auto = item.get("autoIncluded")
        if auto is not None:
            required = {"at", "replaces", "replacesVersion", "runUrl", "cliCommit"}
            assert isinstance(auto, dict) and required <= set(auto) <= required | {"stableAt"}
            if auto["replaces"] is None:
                assert auto["replacesVersion"] is None and "stableAt" not in auto
            else:
                assert re.fullmatch(r"[a-f0-9]{64}", auto["replaces"]) and auto["replaces"] != item["id"]
            assert auto["replaces"] is None or version_parts(item["version"]) > version_parts(auto["replacesVersion"]), \
                "自动收录只接受严格更高的版本"
            if auto["replaces"] and not auto.get("stableAt"):
                old = items.get(auto["replaces"])
                assert old and old["key"] == item["key"], "自动收录的新构建稳定前必须保留被替换的旧构建"
        if item.get("rollbackFor") is not None:
            newer = items.get(item["rollbackFor"])
            assert (newer and newer["key"] == item["key"]
                    and (newer.get("autoIncluded") or {}).get("replaces") == item["id"]), \
                "回退标记必须指向替换它的自动收录构建"
    return catalog


def execution_policy(item):
    overrides = item.get("patrolPolicy", {})
    limits = {"maxRequests": 500, "stageTimeoutMs": 60000,
              "sourceTimeoutMs": 300000, "requestTimeoutMs": 30000}
    assert isinstance(overrides, dict) and set(overrides) <= set(limits), "仅允许增加巡检资源预算"
    for key, value in overrides.items():
        assert type(value) is int and POLICY[key] <= value <= limits[key], "巡检预算超出允许范围"
    return {**POLICY, **overrides}


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
        "Provide credentials.username and password": "未提供用户名和密码",
        "Favorites require authenticated account data": "网络收藏需要已登录的账号",
        "Requires allowMutations:true and an explicit case": "默认禁用写操作，且没有显式写操作用例",
        "Not implemented": "当前运行时未实现该能力",
        "No automatic adapter; provide cases[path].args and expect": "此扩展方法没有自动巡检适配器，需提供显式参数和预期结果",
        "Worker terminated before this capability": "巡检进程已停止，未执行该能力",
    }
    return text(known.get(reason, reason))


def run(*args, **kwargs):
    return subprocess.run(list(args), check=True, **kwargs)


CLI_PATCHES = (
    {
        # 上游只接受非负整数，但 VeneraX 的 Res.subData 明确允许 null（表示没有上限）。
        # 包子漫画、Komiic 多账号在「还有下一页」时就是返回 null，被误判成 contract_violation。
        "file": "patches/venera-patrol-cli-maxpage-null.patch",
        "target": "src/validate.js",
        "requires": "if (result?.maxPage !== undefined)",
        "provides": "if (result?.maxPage != null)",
    },
)


def apply_cli_patches(directory):
    """给上游 CLI 副本打上仓库内复核过的补丁；上游自己修好后自动跳过。"""
    applied = []
    for entry in CLI_PATCHES:
        patch_file = ROOT / entry["file"]
        data = patch_file.read_bytes()
        target = directory / entry["target"]
        text = target.read_text(encoding="utf-8", errors="replace")
        record = {"file": entry["file"], "sha256": sha(data), "target": entry["target"]}
        if entry["provides"] in text:
            applied.append({**record, "status": "upstream"})
            continue
        if entry["requires"] not in text:
            raise ValueError(f"上游 {entry['target']} 的实现变了，{entry['file']} 需要人工复核")
        run("git", "-C", str(directory), "apply", "--check", str(patch_file))
        run("git", "-C", str(directory), "apply", str(patch_file))
        updated = target.read_text(encoding="utf-8")
        if entry["provides"] not in updated or entry["requires"] in updated:
            raise ValueError(f"{entry['file']} 没有生效")
        applied.append({**record, "status": "applied"})
    return applied


def cli_image_tag(commit, patches):
    """打了补丁的镜像不能复用上游镜像名，否则同一次运行里两个 CLI 副本可能互相命中缓存。"""
    applied = [entry["sha256"] for entry in patches if entry.get("status") == "applied"]
    return f"venera-patrol:{commit}" + (f"-p{sha(''.join(applied).encode())[:8]}" if applied else "")


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
    metadata["patches"] = apply_cli_patches(directory)
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
    (directory / "wnacg.import.js").write_bytes((ROOT / "sources/wnacg.js").read_bytes())
    metadata["clientProfiles"] = profiles["profiles"]
    # 构建上下文只含 CLI 文件，不把 runner 的凭据、仓库或 Docker socket 传给源。
    dockerfile = ROOT / "scripts/patrol.Dockerfile"
    image = cli_image_tag(commit, metadata["patches"])
    run("docker", "build", "--pull", "--tag", image, "--file", str(dockerfile), str(directory))
    run("docker", "run", "--rm", "--read-only", "--cap-drop=ALL", "--security-opt=no-new-privileges",
        "--tmpfs", "/tmp:rw,noexec,nosuid", "--entrypoint", "sh", image, "-ec",
        "mkdir /tmp/private /tmp/reports; touch /tmp/reports/report.json; "
        "VENERA_RUNTIME_DATA_DIR=/tmp/private patrol-worker -e 'const fs=require(\"fs\"); "
        "fs.writeFileSync(\"/tmp/private/probe\",\"ok\"); "
        "for(const p of [\"/tmp/reports/report.json\",\"/tmp/reports/other.json\"]) { "
        "try { fs.writeFileSync(p,\"probe\"); process.exit(2) } catch(e) { if(e.code!==\"EACCES\") throw e } }'")
    metadata["image"] = image
    metadata["nodeVersion"] = run(
        "docker", "run", "--rm", "--entrypoint", "node", image, "--version",
        capture_output=True, text=True).stdout.strip()
    metadata["imageId"] = run("docker", "image", "inspect", "--format={{.Id}}", image,
                              capture_output=True, text=True).stdout.strip()
    save(work / "cli.json", metadata)
    print(f"已安装最新巡检 CLI：{commit}，版本 {metadata['version']}。", flush=True)


def self_repository():
    """本仓库不列入自己的上游线索，避免每轮都把自身当成新仓库。"""
    return os.environ.get("GITHUB_REPOSITORY", "laincat/vensrc").casefold()


def discover(work):
    catalog = validate_catalog(load(ROOT / "monitor/catalog.json"))
    config = load(ROOT / "monitor/upstreams.json")
    exclusions = refresh_official_policy()
    save(work / "artifact/official-exclusions.json", exclusions)
    known = {i["sha256"] for i in catalog["sources"]}
    samples = {i["key"]: i["sample"] for i in catalog["sources"]}
    registered = registered_repositories(config)
    hosts, outside = {}, []
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
            files = config.get("files", {}).get(repo)
            if files is not None:
                if not isinstance(files, list) or not files or any(
                    not isinstance(file, str) or not re.fullmatch(r"[\w./-]+\.js", file)
                    or file.startswith("/") or ".." in file.split("/") for file in files
                ):
                    raise ValueError("单文件候选必须是仓库内的相对 JS 路径")
                entries = [{"key": Path(file).stem, "name": Path(file).stem, "fileName": file}
                           for file in files]
            else:
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
                if target.casefold() == OFFICIAL_REPOSITORY:
                    continue
                if target.casefold() not in registered:
                    # 已登记仓库的索引指向了未登记仓库：只列出，不下载、不执行。
                    outside.append({"repository": text(target), "key": text(key), "name": text(name),
                                    "fileName": text(Path(unquote(file)).name), "trackedBy": repo})
                    continue
                try:
                    ref = resolve(target, ref)
                    fixed = f"https://raw.githubusercontent.com/{target}/{ref}/{quote(unquote(file), safe='/')}"
                    if pinned_repository(fixed) != target.casefold():
                        raise ValueError("固定源码路径无效")
                    data = request(fixed)
                    digest = sha(data)
                    if digest in known:
                        continue
                    code = data.decode("utf-8-sig")
                    entry.update(declared_fields(code))
                    hosts[digest] = source_surface(code)
                    name = entry.get("name", name)
                    actual_key = entry.get("key", key)
                    candidate = {"key": actual_key, "repository": target, "name": name,
                                 "fileName": Path(unquote(file)).name, "url": fixed,
                                 "version": entry.get("version")}
                    if excluded_wnacg(candidate) or excluded_official(candidate, exclusions):
                        continue
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
        for candidates, repository in pool.map(
                inspect, [repo for repo in config["repositories"]
                          if repo.casefold() != OFFICIAL_REPOSITORY]):
            repositories.append(repository)
            for candidate in candidates:
                if candidate["id"] in updates:
                    candidate["trackedBy"] = sorted(set(
                        updates[candidate["id"]]["trackedBy"] + candidate["trackedBy"]))
                updates[candidate["id"]] = candidate
    # 三条通道：只读文本判定，这一步不加载、不执行任何候选。
    pending = list(updates.values())
    chosen = set()
    try:
        builds, _ = host_check_targets(pending, catalog)
        hosts.update(fetch_build_hosts(builds))
        verdicts = classify_updates(pending, catalog, registered, exclusions, hosts_lookup(hosts))
        for candidate in pending:
            candidate.update(verdicts[candidate["id"]])
            candidate["sample"] = trial_plan(candidate, catalog)[0]
            candidate["state"] = (
                "发现阶段只读取文本，未加载、未执行；通道：" + LANE_LABELS.get(candidate["lane"], "不执行")
                + "（" + candidate["detail"] + "）")
        results_path = ROOT / "data/candidate-results.json"
        results = load(results_path).get("results", {}) if results_path.is_file() else {}
        chosen = set(select_trials(pending, results, datetime.now(timezone.utc)))
    except Exception as error:
        # 候选归类出错不能拦住已审阅构建的巡检：本轮全部按待人工审阅处理，不试跑。
        print(f"::warning::候选通道归类失败，本轮不试跑：{text(error)}", flush=True)
        chosen = set()
        for candidate in pending:
            candidate.update(lane="trial", reason="hosts_unknown", detail="本轮通道归类失败，待下一轮",
                             baseline=None, newHosts=[])
    for candidate in pending:
        candidate["trial"] = candidate["id"] in chosen
    previous_path = ROOT / "data/pending-updates.json"
    checks = {entry["repository"].casefold(): entry for entry in (
        load(previous_path).get("repositoryChecks", []) if previous_path.is_file() else [])}
    budget, repository_checks, filtered = REPOSITORY_CHECKS, [], []
    new_repositories, seen_repositories, search_errors = [], set(), []
    for query in SEARCH_QUERIES:
        try:
            result = json.loads(request(
                "https://api.github.com/search/repositories?q=" + quote(query, safe=":+")
                + "&sort=updated&per_page=100", api=True))
        except Exception as error:
            search_errors.append(f"{query}：{text(error)}")
            continue
        for item in result.get("items", []):
            name = item["full_name"]
            marker = name.casefold()
            if (marker in seen_repositories or name in config["repositories"]
                    or marker in (OFFICIAL_REPOSITORY, self_repository())):
                continue
            seen_repositories.add(marker)
            pushed = item.get("pushed_at") or ""
            check = checks.get(marker)
            if not check or check.get("pushedAt") != pushed:
                check = None
                if budget > 0:
                    budget -= 1
                    try:
                        relevant, reason = repository_relevance(name)
                        check = {"repository": name, "pushedAt": pushed,
                                 "relevant": relevant, "reason": reason}
                    except Exception:
                        # 判断不了就保持现状，照常列出。
                        check = None
            if check:
                repository_checks.append(check)
                if not check["relevant"]:
                    filtered.append({"repository": name, "reason": check["reason"]})
                    continue
            new_repositories.append({"repository": name,
                                     "description": text(item.get("description") or ""),
                                     "foundBy": query})
    search_error = "；".join(search_errors)
    save(work / "artifact/discovery.json", {
        "schemaVersion": 1, "checkedAt": datetime.now(timezone.utc).isoformat(),
        "updates": pending, "repositories": repositories,
        "newRepositories": new_repositories, "searchError": search_error,
        "unregistered": sorted({json.dumps(entry, ensure_ascii=False, sort_keys=True): entry
                                for entry in outside}.values(),
                               key=lambda entry: (entry["repository"], entry["fileName"])),
        "filteredRepositories": filtered, "repositoryChecks": repository_checks,
        "trial": {"limit": TRIAL_LIMIT, "selected": len(chosen)},
    })
    print(f"上游检测完成：{len(repositories)} 个仓库，{len(updates)} 个待审阅源码构建；"
          f"自动收录通道 {sum(i['lane'] == 'auto' for i in pending)} 个，本轮试跑 {len(chosen)} 个。")


def collect_samples(source, report_dir):
    file = report_dir / Path(source.get("traceFile") or "").name
    sample = {}
    sites = set()
    if not file.name.endswith(".trace.jsonl") or not file.is_file():
        return sample, sites
    for line in file.read_text(encoding="utf-8-sig").splitlines():
        event = json.loads(line)
        collect_reading_site(event, sites)
        args = event.get("args", [])
        if event.get("event") == "capability.call" and event.get("stage") == "comic.loadEp" and len(args) >= 2:
            sample["comicId"] = args[0]
            if args[1] is not None:
                sample["epId"] = args[1]
    return sample, sites


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
    old_samples = {i["sha256"]: i["sample"] for i in load(ROOT / "data/sources.lock.json")}
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
    executions = available + [
        {**item, "runtimeProfile": profile, "verificationOnly": True}
        for item in available for profile in item.get("verifyProfiles", [])]
    priority = set(catalog["priorityRepositories"])
    executions.sort(key=lambda i: (
        not bool(priority.intersection(i.get("trackedBy", []))),
        i.get("runtimeProfile", ""), i["key"], i["version"]))
    batches = []
    for item in executions:
        for batch in batches:
            if (batch[0].get("runtimeProfile") == item.get("runtimeProfile") and
                    execution_policy(batch[0]) == execution_policy(item) and
                    bool(priority.intersection(batch[0].get("trackedBy", []))) ==
                    bool(priority.intersection(item.get("trackedBy", []))) and
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
    for number, batch in enumerate(batches):
        latest = run("git", "ls-remote", "https://github.com/Gandum2077/venera-patrol-cli.git",
                     "HEAD", capture_output=True, text=True).stdout.split()[0]
        if latest != metadata["commit"]:
            raise ValueError("本批巡检前 CLI 已更新；停止，重新获取最新 CLI 后再执行")
        policy = execution_policy(batch[0])
        config = {
            "version": 1, "configPaths": [f"/work/{number}.index.json"],
            "output": f"/work/reports/{number}", "defaults": policy,
            "sources": {i["key"]: {"inputs": i["effectiveSample"], "settings": i.get("settings", {})}
                        for i in batch},
        }
        save(output / f"{number}.index.json", [
            {"key": i["key"], "fileName": f"/sources/{i['id']}.js"} for i in batch])
        save(output / f"{number}.config.json", config)
        command = container_command(metadata, sources_dir, output, number,
                                    batch[0].get("runtimeProfile"))
        print(f"第 {number + 1}/{len(batches)} 批：巡检 {len(batch)} 个已审阅构建。", flush=True)
        result = subprocess.run(command, timeout=max(
            300, len(batch) * (policy["sourceTimeoutMs"] // 1000 + 5)), check=False)
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
            selected, reading_sites = collect_samples(source, reports[0].parent)
            record = {
                "id": item["id"], "inputs": item["effectiveSample"],
                "accountCapabilities": account_capabilities(source),
                "readingSites": sorted(reading_sites),
                "sample": {**selected, **item["effectiveSample"]},
                "runtimeProfile": item.get("runtimeProfile"),
                "policy": policy,
                "source": {key: source.get(key) for key in (
                    "key", "name", "version", "sourceSha256", "status", "startedAt", "stages")},
            }
            (client_records if item.get("verificationOnly") else records).append(record)
    try:
        candidate_records = trial_candidates(work, catalog, metadata, sources_dir)
    except Exception as error:
        # 候选是未审阅代码，它的任何问题都不能影响已审阅构建的发布。
        print(f"候选试跑整体跳过：{text(error)}", flush=True)
        candidate_records = []
    payload = {"schemaVersion": 1, "catalogSha256": sha((ROOT / "monitor/catalog.json").read_bytes()),
               "checkedAt": datetime.now(timezone.utc).isoformat(), "cli": metadata,
               "policy": POLICY, "records": records, "clientRecords": client_records,
               "candidateRecords": candidate_records,
               "officialExclusions": official_policy(
                   snapshot=load(work / "artifact/official-exclusions.json"))}
    # 一份持久结构化证据；原始 trace 不上传、不进入带写权限的发布任务。
    save(work / "artifact/patrol.json", payload)
    publish(payload, work / "artifact/preview")


SURROGATES = re.compile(r"[\ud800-\udfff]")


def encodable(value):
    """把孤立代理字符换成 U+FFFD，保证结果一定能用 UTF-8 写出。

    站点返回的非法 UTF-8 会在运行时变成孤立代理（如 \\udd65），直接写
    UTF-8 文件会抛 UnicodeEncodeError 并中断整次发布。
    """
    return SURROGATES.sub("\ufffd", str(value))


def text(value):
    plain = re.sub(r"[\x00-\x1f\x7f]", " ", encodable(value))
    return plain.replace("|", "／")[:300]


def csv_cell(value):
    # 表格注入防护与 markdown 共用同一套清洗，避免代理字符写崩 CSV。
    value = encodable(value)
    return "'" + value if value.startswith(("=", "+", "-", "@")) else value


def write_report(path, lines):
    path.write_text("\n".join(lines), encoding="utf-8", newline="\n")


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
    for name, value in item["sample"].items():
        assert record["inputs"].get(name) == value, "客户端对照必须使用同一固定样本"
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
    (destination / "reports").mkdir(parents=True, exist_ok=True)
    catalog = validate_catalog(load(ROOT / "monitor/catalog.json"))
    note_config = load(ROOT / "monitor/source-notes.json")
    assert note_config["schemaVersion"] == 1 and isinstance(note_config["notes"], dict)
    known_builds = {item["id"]: item for item in catalog["sources"]}
    assert set(note_config["notes"]) <= set(known_builds)
    assert all(known_builds[build_id].get("repository") in ("BB-CHICKEN/venera-jm", "laincat/vensrc")
               for build_id in note_config["notes"])
    annotations = note_config["notes"]
    exclusions = official_policy(snapshot=payload.get("officialExclusions"))
    community = community_keys(catalog["sources"])

    def excluded(item):
        return excluded_official(item, exclusions, community)

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
            if item["key"] in exclusions["versions"] and not excluded(item):
                assert source["version"] == item["version"], "社区升级版必须使用 CLI 实际加载版本比较"
        display_item = {**item, "sample": record.get("sample", item["sample"])}
        rows.append((display_item, source, success))
        score = (not excluded(item), success,
                 source["status"] == "passed", item.get("priority", 0),
                 tuple(int(x) for x in re.findall(r"\d+", item["version"])[:3]))
        if item["key"] not in selected or score > selected[item["key"]][0]:
            selected[item["key"]] = (score, item, source, record.get("sample", item["sample"]))
    current_core = sum(core(source) for _, item, source, _ in selected.values()
                       if not excluded(item))
    previous = load(ROOT / "data/sources.lock.json")
    if previous and current_core == 0:
        raise ValueError("全批核心链路失败；保留上次订阅，本次运行不得发布为成功")
    main, extended, locks = [], [], []
    checked = payload["checkedAt"]
    for _, item, source, sample in selected.values():
        if excluded(item) or not core(source):
            continue
        assert pinned(item["url"])
        status = source["status"]
        entry = {
            "name": item["name"], "key": item["key"], "version": item["version"],
            "fileName": item["fileName"], "url": item["url"],
            "minAppVersion": item["minAppVersion"],
            "description": source_annotation(item, annotations),
        }
        channel = "main" if status == "passed" else "extended"
        (main if channel == "main" else extended).append(entry)
        locks.append({
            **entry, "sha256": item["sha256"], "minAppVersion": item["minAppVersion"],
            **({"officialVersion": exclusions["versions"][item["key"]]}
               if item["key"] in exclusions["versions"] else {}),
            "officialKey": item.get("officialKey", False),
            "officialOriginal": is_official_item(item),
            "status": status, "channel": channel,
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
        save(generated_path(destination, name), data)
    save(destination / "data/official-exclusions.json", exclusions)
    zone_date = datetime.fromisoformat(checked).astimezone(
        timezone(timedelta(hours=8), "Asia/Hong_Kong")).isoformat()
    lines = [
        "# Venera 漫画源云端巡检报告", "",
        f"核验时间：{zone_date}（香港时间）。",
        f"巡检工具：`Gandum2077/venera-patrol-cli` {payload['cli']['version']}，"
        f"提交 `{payload['cli']['commit']}`。",
        f"依赖锁 SHA-256：`{payload['cli']['packageLockSha256']}`。",
        f"本次审阅清单：{len(rows)} 个构建；主索引 **{len(main)}** 项，扩展索引 **{len(extended)}** 项。", "",
        f"官方版本基线覆盖 **{len(exclusions['keys'])}** 个 key。官方仓库原版仅在「同一 key 没有社区构建」时"
        "作为唯一可用版本参与订阅，其余只保留诊断证据；社区同 key 构建仍需版本严格高于官方基线。"
        "同版、低版或版本无法比较均排除。",
        "绅士漫画只保留 `laincat/vensrc` 独立维护版；其他来源不再巡检或收录。"
        "账号改为本人完成滑块后导入浏览器 Cookie，并以会员页的真实登录标志验证；"
        "缺少会话不计登录通过，详见 WNACG_LOGIN.md。",
        f"版本基线依据官方索引提交 `{exclusions['indexCommit']}`，"
        f"原始索引 SHA-256：`{exclusions['indexSha256']}`。"
        "按三段数字比较版本；后续检测追加 key 并提高官方版本基线，不降低历史基线，"
        "清单见 ../data/official-exclusions.json。", "",
        "固定漫画及章节、源码字节哈希和 CLI 提交均保留。主索引必须同次通过入口、详情、章节、图片下载与解码，且整次报告为 passed；"
        "扩展索引要求相同核心链路通过，其他能力可有失败或跳过。旧成功结果不代替新失败。", "",
        "订阅快照滚动发布到 Releases，仅有主订阅和扩展订阅两个附件；中文报告与完整证据保存在仓库 reports/、data/。"
        "最终只保留最新一版；附件校验不完整时保留上一版。", "",
        "GitHub 托管 runner 的网络与用户设备不同；未在用户设备验证导入或阅读。"
        "全部已审阅构建使用已核验的 VeneraX 原始 bootstrap，"
        "逐个以相同样本对照 Venera-Next。订阅仅按 VeneraX 本次结果选择；"
        "Next 成功不替代 X 失败。适配范围见 CLIENT_COMPATIBILITY.md，"
        "客户端对照复测见 CLIENT_RESULTS.md。", "",
        "## 三个自用仓库", "",
    ]
    for repo in catalog["priorityRepositories"]:
        group = [(i, s, ok) for i, s, ok in rows if repo in i.get("trackedBy", [])]
        lines.append(f"- `{repo}`：已审阅构建 {len(group)} 个，核心链路通过 {sum(ok for _, _, ok in group)} 个。")
    excluded_rows = [(item, source) for _, item, source, _ in selected.values()
                     if excluded(item)]
    upgrades = [item for item in locks
                if item.get("officialVersion") and not item.get("officialOriginal")]
    lines += ["", "## 高于官方版本的社区替代源", "",
              "以下每个构建都严格高于所列官方版本，并通过本次核心阅读门槛；同 key 源在客户端作为替代版本使用。",
              "", "| 名称 | key | 社区版本 | 官方版本 | 订阅 |",
              "| --- | --- | --- | --- | --- |"]
    for item in upgrades:
        lines.append("| " + " | ".join(text(value) for value in (
            item["name"], item["key"], item["version"], item["officialVersion"],
            "主索引" if item["channel"] == "main" else "扩展索引")) + " |")
    lines += ["", "## 未进入订阅的官方原版与低版本构建", "",
              "官方仓库原版仅在「同一 key 没有社区构建」时作为补充参与订阅；已有社区构建时只保留诊断证据。"
              "社区同 key 构建仍须版本严格高于官方基线，核心通过也不能豁免版本门槛。",
              "", "| 名称 | key | 选中构建版本 | 核心链路 | 排除原因 | 源备注 |",
              "| --- | --- | --- | --- | --- | --- |"]
    for item, source in sorted(excluded_rows, key=lambda pair: pair[0]["key"]):
        lines.append("| " + " | ".join(text(v) for v in (
            item["name"], item["key"], item["version"],
            "通过；仍排除" if core(source) else "未完整通过；排除",
            "同一 key 已有社区构建" if is_official_item(item) else "未高于官方版本基线",
            source_annotation(item, annotations))) + " |")
    lines += ["", "## 逐构建结果", "", "| 源名称 | key | 仓库 | 版本 | 巡检环境 | 核心链路 | 整次状态 | 首个失败／跳过 | 收录处理 |",
              "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    csv_rows = [["源名称", "源标识", "仓库", "版本", "核心阅读链路", "整次状态", "固定漫画ID",
                 "固定章节ID", "关键词", "失败阶段", "失败类别", "失败说明", "源码SHA256", "源码地址",
                 "巡检环境", "收录处理", "源备注"]]
    for item, source, success in sorted(rows, key=lambda row: (row[0]["key"], -row[0].get("priority", 0))):
        unsuccessful = [s for s in source["stages"] if s["status"] not in ("passed", "recovered")]
        failed = [s for s in unsuccessful if s["status"] == "failed"]
        first = (failed or unsuccessful or [{}])[0]
        category = CATEGORIES.get(first.get("category"), first.get("category", ""))
        problem = f"{first.get('path', '')}：{category}" if first else ""
        if excluded(item):
            disposition = ("排除官方原版（同一 key 已有社区构建）" if is_official_item(item)
                           else "排除：未高于官方版本基线")
        elif is_official_item(item):
            disposition = "官方原版补充（无社区构建）；按原收录标准审核"
        elif item["key"] in exclusions["versions"]:
            disposition = f"高于官方 {exclusions['versions'][item['key']]}；按原收录标准审核"
        else:
            disposition = "按原有收录标准审核"
        lines.append("| " + " | ".join(text(v) for v in (
            item["name"], item["key"], item["repository"], item["version"],
            item.get("runtimeProfile", "原版 1.6.3 Runtime"),
            "通过" if success else "未完整通过", LABELS[source["status"]], problem, disposition)) + " |")
        sample = item["sample"]
        csv_rows.append([item["name"], item["key"], item["repository"], item["version"],
                         "通过" if success else "未完整通过", LABELS[source["status"]],
                        sample.get("comicId", ""), sample.get("epId", ""), sample.get("keyword", ""),
                        first.get("path", ""), category, reason_zh(first.get("reason", "")),
                        item["sha256"], item["url"], item.get("runtimeProfile", "原版 1.6.3 Runtime"),
                        disposition, source_annotation(item, annotations)])
    lines += ["", "## 主索引", "", "、".join(i["name"] for i in main) or "本次没有符合主索引标准的源。",
              "", "## 扩展索引", "", "、".join(i["name"] for i in extended) or "本次没有扩展源。", ""]
    destination.mkdir(parents=True, exist_ok=True)
    write_report(destination / "reports/RESULTS.md", lines)
    with (destination / "data/sources.zh.csv").open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        for row in csv_rows:
            writer.writerow([csv_cell(value) for value in row])
    save(destination / "data/audit-status.json", {
        "checkedAt": checked, "cli": payload["cli"], "catalogSha256": payload["catalogSha256"],
        "builds": len(rows), "main": len(main), "extended": len(extended),
        "runUrl": os.environ.get("AUDIT_RUN_URL", ""),
        "clientExecutions": len(payload["records"]) + len(payload.get("clientRecords", [])),
        "officialExclusionsSha256": sha((destination / "data/official-exclusions.json").read_bytes()),
        "officialBaselineKeys": len(exclusions["keys"]),
        "officialExcludedBuilds": sum(excluded(i) for i, _, _ in rows),
        "officialOverrides": len(upgrades),
    })
    publish_clients(payload, catalog, destination)
    print(f"中文报告已生成：主索引 {len(main)} 项、扩展索引 {len(extended)} 项。", flush=True)


def publish_clients(payload, catalog, destination):
    (destination / "reports").mkdir(parents=True, exist_ok=True)
    (destination / "data").mkdir(parents=True, exist_ok=True)
    items = {i["id"]: i for i in catalog["sources"]}
    expected = {(i["id"], profile) for i in items.values() for profile in i.get("verifyProfiles", [])}
    actual = [(r["id"], r.get("runtimeProfile")) for r in payload.get("clientRecords", [])]
    assert len(actual) == len(expected) and set(actual) == expected, "客户端对照证据缺失或重复"
    records = [r for r in payload["records"] if r.get("runtimeProfile")]
    records += payload.get("clientRecords", [])
    lines = ["# VeneraX／Venera-Next 固定样本兼容清单", "",
             f"核验时间：{payload['checkedAt']}（UTC）。",
             f"最新上游 CLI 提交：`{payload['cli']['commit']}`；同时加载本仓库记录哈希的接口适配层。",
             "全部已审阅源码逐个使用相同固定输入；VeneraX 为订阅选择依据，Next 为独立对照。",
             "官方原版排除；社区同 key 版本必须严格高于官方，并独立满足本次核心阅读与主／扩展门槛。",
             "结果为 Node 宿主上的真实客户端 JS 接口巡检，不代表 Flutter UI 或用户设备实测。",
             "两边分时执行，差异也可能来自网络、限流或源站变化，不能全部归因于 Fork 接口。",
             "账号巡检另见 ACCOUNT_RESULTS.md，不以账号通过替代匿名订阅收录标准。",
             "完整阶段、输入和哈希保存在 ../data/client-results.json 与 ../data/sources.zh.csv。", ""]
    clean_records = []
    grouped = {}
    csv_rows = [["源名称", "源标识", "版本", "仓库", "客户端环境", "核心阅读链路", "整次状态",
                 "最低应用版本", "固定漫画ID", "固定章节ID", "关键词", "源码SHA256", "失败阶段", "失败类别"]]
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
        grouped.setdefault(item["id"], {})[profile] = record
        clean_records.append(record)
        sample = record.get("sample", record["inputs"])
        first = next((s for s in source["stages"] if s["status"] == "failed"), {})
        csv_rows.append([
            item["name"], item["key"], item["version"], item["repository"], profile,
            "通过" if core(source) else "未通过", LABELS[source["status"]], item["minAppVersion"],
            sample.get("comicId", ""), sample.get("epId", ""), sample.get("keyword", ""),
            item["sha256"], first.get("path", ""),
            CATEGORIES.get(first.get("category"), first.get("category", "")),
        ])
    for pair in grouped.values():
        if "venerax" in pair and "venera-next" in pair:
            assert pair["venerax"]["inputs"] == pair["venera-next"]["inputs"], "两个客户端必须使用完全相同的固定输入"
    lines += ["## 全量统计", "",
              "| 环境 | 报告构建数 | 核心阅读通过 | 整次通过 | 部分通过 | 失败 | 整源跳过 | 跳过阶段 |",
              "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for profile in ("venerax", "venera-next"):
        sources = [r["source"] for r in records if r["runtimeProfile"] == profile]
        counts = [sum(s["status"] == status for s in sources) for status in ("passed", "partial", "failed", "skipped")]
        lines.append("| " + " | ".join(map(str, (
            profile, len(sources), sum(core(s) for s in sources), *counts,
            sum(stage["status"] == "skipped" for s in sources for stage in s["stages"])))) + " |")
    lines += ["", "跳过阶段、缺少凭据及未触发回调均不计入通过；核心通过只要求已说明的阅读链路。",
              "", "## 三个自用仓库", ""]
    for repo in catalog["priorityRepositories"]:
        builds = [i for i in items.values() if repo in i.get("trackedBy", [])]
        counts = []
        for profile in ("venerax", "venera-next"):
            passed = sum(core(grouped[i["id"]][profile]["source"]) for i in builds)
            counts.append(f"{profile} 核心通过 {passed}/{len(builds)}")
        lines.append(f"- `{repo}`：" + "；".join(counts) + "。")
    differences = [
        item for item in items.values()
        if "venerax" in grouped.get(item["id"], {}) and "venera-next" in grouped.get(item["id"], {})
        and core(grouped[item["id"]]["venerax"]["source"]) != core(grouped[item["id"]]["venera-next"]["source"])
    ]
    lines += ["", "## 核心阅读结果不同的构建", "",
              f"共 {len(differences)} 个构建。两边分时执行；以下是结果差异，不自动归因为客户端代码。", "",
              "| key | 版本 | 仓库 | VeneraX | Venera-Next |",
              "| --- | --- | --- | --- | --- |"]
    for item in differences:
        pair = grouped[item["id"]]
        lines.append("| " + " | ".join(text(v) for v in (
            item["key"], item["version"], item["repository"],
            *("通过" if core(pair[p]["source"]) else "未通过" for p in ("venerax", "venera-next")))) + " |")
    lines += ["", "## 其他阶段结果差异", "",
              "按阶段状态和类别对照，不比较耗时、返回正文和异常原文。“未出现”表示该环境报告没有此阶段，不能算通过。", "",
              "| key | 版本 | 构建哈希（前12位） | 阶段 | VeneraX | Venera-Next |",
              "| --- | --- | --- | --- | --- | --- |"]
    for item in items.values():
        pair = grouped.get(item["id"], {})
        if not all(profile in pair for profile in ("venerax", "venera-next")):
            continue
        by_profile = {}
        for profile in ("venerax", "venera-next"):
            paths = {}
            for stage in pair[profile]["source"]["stages"]:
                paths.setdefault(stage["path"], []).append((stage["status"], stage.get("category", "")))
            by_profile[profile] = paths
        for path in sorted(set(by_profile["venerax"]) | set(by_profile["venera-next"])):
            values = [by_profile[profile].get(path, []) for profile in ("venerax", "venera-next")]
            if values[0] == values[1]:
                continue
            labels = ["；".join(
                LABELS.get(status, status) + ("／" + CATEGORIES.get(category, category) if category else "")
                for status, category in value) or "未出现" for value in values]
            lines.append("| " + " | ".join(text(v) for v in (
                item["key"], item["version"], item["sha256"][:12], path, *labels)) + " |")
    lines += ["", "## 逐构建对照", "",
              "| 名称 | key | 版本 | 仓库 | 源码哈希（前12位） | VeneraX 核心／整次 | Next 核心／整次 | 首个失败（X；Next） |",
              "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    priority = set(catalog["priorityRepositories"])
    for item in sorted(items.values(), key=lambda i: (
            not bool(priority.intersection(i.get("trackedBy", []))), i["key"], i["version"])):
        pair = grouped.get(item["id"], {})
        cells, problems = [], []
        for profile in ("venerax", "venera-next"):
            record = pair.get(profile)
            if not record:
                cells.append("未测试")
                problems.append("缺少环境")
                continue
            source = record["source"]
            cells.append(("通过" if core(source) else "未通过") + "／" + LABELS[source["status"]])
            failed = next((s for s in source["stages"] if s["status"] == "failed"), {})
            problems.append(f"{failed.get('path', '')} {CATEGORIES.get(failed.get('category'), failed.get('category', ''))}".strip() or "无失败")
        lines.append("| " + " | ".join(text(v) for v in (
            item["name"], item["key"], item["version"], item["repository"],
            item["sha256"][:12], *cells, "；".join(problems))) + " |")
    lines.append("")
    save(destination / "data/client-results.json", {
        "schemaVersion": 1, "checkedAt": payload["checkedAt"], "cli": payload["cli"],
        "records": clean_records, "runUrl": os.environ.get("AUDIT_RUN_URL", "")})
    write_report(destination / "reports/CLIENT_RESULTS.md", lines)
    with (destination / "data/client-compatibility.zh.csv").open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        for row in csv_rows:
            writer.writerow([csv_cell(value) for value in row])


def publish_discovery(discovery, destination):
    (destination / "reports").mkdir(parents=True, exist_ok=True)
    assert discovery["schemaVersion"] == 1
    exclusions = official_policy()
    discovery = {**discovery,
                 "updates": [i for i in discovery["updates"]
                             if not excluded_wnacg(i) and not excluded_official(i, exclusions)],
                 "repositories": [i for i in discovery["repositories"]
                                  if i["repository"].casefold() != OFFICIAL_REPOSITORY],
                 "newRepositories": [i for i in discovery["newRepositories"]
                                     if i["repository"].casefold() != OFFICIAL_REPOSITORY],
                 "unregistered": [i for i in discovery.get("unregistered", [])
                                  if i["repository"].casefold() != OFFICIAL_REPOSITORY]}
    for item in discovery["updates"]:
        assert pinned(item["url"]) and item["id"] == item["sha256"]
        assert re.fullmatch(r"[a-f0-9]{64}", item["sha256"])
        assert item.get("lane", "trial") in ("auto", "trial", "listed")
    lanes = [item.get("lane", "trial") for item in discovery["updates"]]
    save(destination / "data/pending-updates.json", discovery)
    lines = [
        "# 上游变更与待审阅候选", "",
        f"检查时间：{discovery['checkedAt']}（UTC）。",
        f"检查 {len(discovery['repositories'])} 个已登记仓库；"
        f"发现 {len(discovery['updates'])} 个未审阅源码构建。", "",
        "发现阶段只下载计算哈希、读取声明字段和主机名，不通过 list、init 或巡检执行。待审构建分三条通道：", "",
        f"- **自动收录**（{lanes.count('auto')} 个）：已登记仓库的新 key 或已有 key 的严格升级；"
        "复核来源、排除规则、重复源和两端同轮匿名阅读后写入清单。",
        f"- **试跑但不收录**（{lanes.count('trial')} 个）：新增目的地、凭据能力或重复来源等情况照常隔离试跑，"
        "结果见 [候选试跑短名单](CANDIDATES.md)，收录仍需人工审阅。",
        f"- **不执行**（{len(discovery['unregistered'])} 个文件）：未登记仓库只列出，不下载、不执行。", "",
        f"每轮最多试跑 {TRIAL_LIMIT} 个候选，自动收录通道优先；本轮安排 "
        f"{sum(bool(item.get('trial')) for item in discovery['updates'])} 个。", "",
        "候选排除官方原版、转引，以及未严格高于官方版本的社区同 key 源。", "",
        "## 源码变动", "", "| 名称 | key | 版本 | 仓库 | 最低应用版本 | 通道 | 说明 | SHA-256 |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in discovery["updates"]:
        lines.append("| " + " | ".join(text(value) for value in (
            item.get("name", ""), item.get("key", ""), item.get("version", ""),
            item.get("repository", ""), item.get("minAppVersion", ""),
            LANE_LABELS.get(item.get("lane", "trial"), ""), item.get("detail", ""),
            item["sha256"])) + " |")
    lines += ["", "## 未登记仓库的文件（不下载、不执行）", "",
              "已登记仓库的索引指向了这些未登记仓库。确认可信后在 monitor/upstreams.json 登记，才会进入前两条通道。", ""]
    for item in discovery["unregistered"]:
        lines.append(f"- `{text(item['repository'])}`：{text(item['name'])}（key `{text(item['key'])}`，"
                     f"`{text(item['fileName'])}`），来自 `{text(item['trackedBy'])}` 的索引")
    lines += ["", "## 索引获取问题", ""]
    for repo in discovery["repositories"]:
        if repo["errors"]:
            lines.append(f"- `{text(repo['repository'])}`：" + "；".join(text(e) for e in repo["errors"][:5]))
    lines += ["", "## 新仓库线索", "",
              "仅列本次 GitHub 更新排序搜索第一页的未登记仓库，尚未认定为漫画源，不代表全网穷尽。", ""]
    for item in discovery["newRepositories"]:
        lines.append(f"- `{text(item['repository'])}`：{text(item['description'])}")
    if discovery.get("filteredRepositories"):
        lines += ["", f"另有 {len(discovery['filteredRepositories'])} 个搜索结果既没有漫画源索引 index.json，"
                  "也没有 ComicSource 脚本，已从名单滤掉；无法判断的仓库照常列出。"]
    if discovery["searchError"]:
        lines.append("仓库搜索未完整完成：" + text(discovery["searchError"]))
    write_report(destination / "reports/UPDATES.md", lines + [""])
    return discovery


# —— 上游更新分三条通道：自动收录、试跑但不收录、不执行 ——
TRIAL_LIMIT = 40
TRIAL_BUDGET_SECONDS = 45 * 60
TRIAL_PROFILES = ("venerax", "venera-next")
# 试跑过的候选隔多久可以重试：自动通道 3 天，仅试跑通道 14 天。
RETRY_DAYS = {"auto": 3, "trial": 14}
# 自动收录的新构建连续通过满 7 天且不少于 24 轮才算稳定；此前必须保留被替换的旧构建。
STABLE_DAYS = 7
STABLE_PASSES = 24
# 与「同站不同写法」的去重规则一致：www.x.com、m.x.com 视为同一站点。
SAME_SITE_PREFIXES = ("www", "m")
SELF_MAINTAINED = "laincat/vensrc"
DEFAULT_SAMPLE = {"keyword": "火影"}
REPOSITORY_CHECKS = 30
LANE_LABELS = {"auto": "自动收录", "trial": "试跑但不收录", "listed": "不执行"}
REASON_LABELS = {
    "auto": "满足自动收录条件", "credentials": "新增凭据能力", "new_hosts": "新增主机名", "hosts_unknown": "主机名无法核对",
    "new_key": "清单里没有的新 key", "self_maintained": "本仓库自建维护的源",
    "version": "版本未严格高于清单现有版本", "superseded": "同 key 有更高版本的候选",
    "ambiguous": "同 key 同版本有多个不同构建", "unregistered": "仓库未登记",
    "excluded": "命中官方排除或绅士漫画规则",
}
OUTCOME_LABELS = {"queued": "两端通过，已排入下一轮写入清单", "passed": "两端通过",
                  "failed": "未通过", "error": "试跑未完成", "rejected": "写入前复核未通过"}
HOST_LABEL = r"[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?"
HOSTNAME = re.compile(rf"{HOST_LABEL}(?:\.{HOST_LABEL})+")
URL_AUTHORITY = re.compile(r"""(?i)(?:https?|wss?):\\?/\\?/([^\s/"'`\\?#<>(),;]+)""")
QUOTED_LITERAL = re.compile(r"""(["'`])([A-Za-z0-9.-]{4,253})\1""")
ESCAPED_CHARACTER = re.compile(r"\\x([0-9a-fA-F]{2})|\\u([0-9a-fA-F]{4})")
NOT_HOST_SUFFIXES = frozenset(
    "js mjs ts json html htm php asp aspx jsp css txt xml md svg ico jpg jpeg png webp gif avif bmp "
    "mp4 m3u8 zip".split())
# 形如 div.title、img.lazy 的字面量是页面选择器，不是主机名。
SELECTOR_TAGS = frozenset("a b i p div span img li ul ol dl dt dd td tr th table tbody h1 h2 h3 h4 h5 h6 "
                          "em strong small font form input button label select option section article "
                          "header footer nav main aside figure picture source video iframe script".split())


def host_name(value):
    value = value.strip().lower().rsplit("@", 1)[-1]
    value = re.sub(r":\d*$", "", value).rstrip(".")
    return value if HOSTNAME.fullmatch(value) else None


def source_hosts(code):
    """源码文本里出现的网络主机名。只做静态读取，不加载、不执行。

    覆盖 http(s)/ws(s) 地址和整段就是小写域名的字符串字面量；先还原 \\xNN、\\uNNNN 转义。
    含大写的字面量（JSON.parse 这类标识符）和页面选择器（div.title）不算主机名。
    运行时拼接或解码出来的主机名静态看不到，这是本检查已知的边界。
    """
    code = ESCAPED_CHARACTER.sub(lambda m: chr(int(m.group(1) or m.group(2), 16)), code)
    hosts = set()
    for raw in URL_AUTHORITY.findall(code):
        if "${" in raw:
            # 模板地址只认结尾写死的部分，例如 https://${sub}.example.com。
            raw = raw.rsplit("}", 1)[-1].lstrip(".")
        hosts.add(host_name(raw))
    for _, raw in QUOTED_LITERAL.findall(code):
        name = host_name(raw)
        if not name or raw != raw.lower():
            continue
        labels = name.split(".")
        if len(labels) == 2 and labels[0] in SELECTOR_TAGS:
            continue
        if all(label.isdigit() for label in labels):
            if len(labels) == 4:
                hosts.add(name)
        elif labels[-1].isalpha() and 2 <= len(labels[-1]) <= 24 and labels[-1] not in NOT_HOST_SUFFIXES:
            hosts.add(name)
    hosts.discard(None)
    return hosts


def site_key(host):
    labels = host.split(".")
    return ".".join(labels[1:]) if len(labels) > 2 and labels[0] in SAME_SITE_PREFIXES else host


def new_hosts(candidate_hosts, known_hosts):
    known = {site_key(host) for host in known_hosts}
    return sorted(host for host in candidate_hosts if site_key(host) not in known)


def declared_fields(code):
    fields = {}
    config = {}
    literal = re.search(r"(?m)^\s*config\s*=\s*(?=\{)", code)
    if literal:
        try:
            value, end = json.JSONDecoder().raw_decode(code[literal.end():])
            if isinstance(value, dict) and re.match(r"[ \t]*(?:;|\r?$)", code[literal.end() + end:], re.M):
                config = value
        except ValueError:
            pass
    for field in ("key", "name", "version", "minAppVersion"):
        leading = r'''(?m)^[ \t]*(?:(?:name|key|version|minAppVersion|url)[ \t]*=[ \t]*(?:"[^"\r\n]*"|'[^'\r\n]*')[ \t]*;[ \t]*)*'''
        match = re.search(leading + field + r'''[ \t]*=[ \t]*(["'])([^\r\n]*?)\1[ \t]*(?=;|//|\r?$)''', code)
        if match:
            if match.group(1) not in match.group(2):
                fields[field] = match.group(2)
        elif isinstance(config.get(field), str) and re.search(
                rf"(?m)^\s*{field}\s*=\s*this\.config\.{field}[ \t]*;?[ \t]*$", code):
            fields[field] = config[field]
    return fields


def version_newer(candidate, current):
    """严格更高才算；任何一边不是三段数字都视为无法比较。"""
    try:
        return version_parts(candidate) > version_parts(current)
    except ValueError:
        return False


def registered_repositories(config):
    return {repo.casefold() for repo in config["repositories"]} - {OFFICIAL_REPOSITORY}


def pinned_repository(url):
    if not pinned(url):
        return None
    parsed = urlparse(url)
    parts = parsed.path[1:].split("/")
    if (parsed.query or parsed.fragment or not re.fullmatch(r"[\w.-]+/[\w.-]+", "/".join(parts[:2]))
            or any(unquote(part) in ("", ".", "..") or re.search(r"[/\\%]", unquote(part)) for part in parts)):
        return None
    return "/".join(parts[:2]).casefold()


def source_surface(code):
    credentials = {token.casefold() for token in re.findall(
        r"\b(account|login\w*|getCookies?|setCookies?|deleteCookies?|authorization|password|"
        r"credentials?|accessToken|refreshToken|browserToken|cookie)\b", code, re.I)}
    origins = re.findall(r'''(?im)^\s*(?:(?:const|let|static)\s+)?(?:base_?url|base_?domain|domain|host|homepage)\s*[:=]\s*["'`](?:https?://)?([a-z0-9.-]+)(?=[:/"'`])''', code)
    return source_hosts(code), credentials, {site_key(host.lower()) for host in origins if host_name(host)}


def baseline_build(builds):
    """样本、设置和巡检预算沿用同 key 版本最高的现有构建。"""
    def rank(item):
        try:
            parts = version_parts(item["version"])
        except ValueError:
            parts = ()
        return parts, item.get("priority", 0), item["id"]
    return max(builds, key=rank)


def candidate_gate(candidate, catalog, registered, exclusions, hosts_of):
    """单个候选的通道判定；hosts_of(构建) 返回该构建源码里的主机名集合。"""
    def verdict(lane, reason, detail="", baseline=None, hosts=()):
        return {"lane": lane, "reason": reason, "detail": detail or REASON_LABELS[reason],
                "baseline": ({"id": baseline["id"], "version": baseline["version"],
                              "repository": baseline.get("repository", "")} if baseline else None),
                "newHosts": list(hosts)}

    repository = str(candidate.get("repository", ""))
    url = candidate.get("url", "")
    if (repository.casefold() not in registered or not isinstance(url, str)
            or pinned_repository(url) != repository.casefold()):
        return verdict("listed", "unregistered")
    if excluded_wnacg(candidate) or excluded_official(candidate, exclusions):
        return verdict("excluded", "excluded")
    builds = [item for item in catalog["sources"] if item["key"] == candidate.get("key")]
    if not builds:
        try:
            version_parts(candidate.get("version"))
            hosts, permissions, sites = hosts_of(candidate)
        except Exception as error:
            return verdict("trial", "new_key", f"版本或源码待核对：{text(error)}")
        aliases = {"copy_manga": "copy_manga_multi_accounts", "Komiic": "komiic_multi"}
        if any(item["name"].strip().casefold() == candidate["name"].strip().casefold()
               or item["key"] == aliases.get(candidate["key"]) for item in catalog["sources"]):
            return verdict("trial", "ambiguous", "与清单现有源重名或属于已合并的 key")
        if permissions:
            return verdict("trial", "credentials", "新 key 涉及凭据能力：" + "、".join(sorted(permissions)))
        if sites:
            try:
                if any(sites & hosts_of(item)[2] for item in catalog["sources"]):
                    return verdict("trial", "ambiguous", "不同 key 指向清单中已有的站点，待核对分区或语言版本")
            except Exception as error:
                return verdict("trial", "hosts_unknown", f"同站去重未完成：{text(error)}")
        return verdict("auto", "new_key", "登记仓库的新 key，使用匿名样本", hosts=sorted(hosts))
    baseline = baseline_build(builds)
    if any(item.get("repository") == SELF_MAINTAINED for item in builds):
        return verdict("trial", "self_maintained", "本仓库自建维护的源，不自动替换", baseline)
    version = candidate.get("version")
    if not all(version_newer(version, item["version"]) for item in builds):
        try:
            version_parts(version)
            detail = f"版本 {version} 未严格高于清单现有版本 {baseline['version']}"
        except ValueError:
            detail = f"版本 {text(version)} 不是三段数字，无法比较"
        return verdict("trial", "version", detail, baseline)
    try:
        known, permissions, _ = hosts_of(baseline)
        hosts, requested, _ = hosts_of(candidate)
        added = new_hosts(hosts, known)
        if requested - permissions:
            return verdict("trial", "credentials", "新增凭据能力：" + "、".join(sorted(requested - permissions)), baseline, added)
    except Exception as error:
        return verdict("trial", "hosts_unknown", f"主机名无法核对：{text(error)}", baseline)
    if added:
        return verdict("trial", "new_hosts", "新增主机名：" + "、".join(added), baseline, added)
    return verdict("auto", "auto", f"{baseline['version']} → {version}，未新增主机名", baseline)


def classify_updates(updates, catalog, registered, exclusions, hosts_of):
    """全部待审构建的通道判定。同一个 key 每次只放一个候选进自动通道。"""
    verdicts = {item["id"]: candidate_gate(item, catalog, registered, exclusions, hosts_of)
                for item in updates}
    groups = {}
    for item in updates:
        if verdicts[item["id"]]["lane"] == "auto":
            groups.setdefault(item["key"], []).append(item)
    for group in groups.values():
        top = max(version_parts(item["version"]) for item in group)
        leaders = [item for item in group if version_parts(item["version"]) == top]
        if len(leaders) > 1:
            # 同版本不同字节：优先与现有构建同仓库的那一份，分不出唯一一份就交回人工选择。
            home = (verdicts[leaders[0]["id"]]["baseline"] or {}).get("repository", "").casefold()
            same = [item for item in leaders if item["repository"].casefold() == home]
            if len(same) != 1:
                # 其次看自用仓库优先级，与订阅选择构建时的顺序一致。
                best = max(item.get("priority", 0) for item in leaders)
                same = [item for item in leaders if item.get("priority", 0) == best]
            leaders = same if len(same) == 1 else []
        chosen = {item["id"] for item in leaders}
        for item in group:
            if item["id"] in chosen:
                continue
            lower = version_parts(item["version"]) < top
            verdicts[item["id"]] = {
                **verdicts[item["id"]], "lane": "trial",
                "reason": "superseded" if lower else "ambiguous",
                "detail": (f"同 key 有更高版本的候选 {'.'.join(map(str, top))}" if lower
                           else "同 key 同版本有多个不同构建，需人工选择")}
    return verdicts


def select_trials(updates, results, now, limit=TRIAL_LIMIT):
    """本轮试跑名单：自动通道优先，其次是没试过的，最后才重试到期的旧结果。"""
    order = {"auto": 0, "new_hosts": 1, "hosts_unknown": 1, "new_key": 2}
    queue = []
    for item in updates:
        if item.get("lane") not in ("auto", "trial"):
            continue
        previous = results.get(item["id"])
        if (previous and previous.get("outcome") == "rejected" and previous.get("reviewVersion", 1) < 3
                and previous.get("detail") in ("源码声明的 key 与候选不一致", "源码声明的版本与候选不一致", "试跑状态不满足主／扩展标准")):
            previous = None
        if previous:
            checked = datetime.fromisoformat(previous["checkedAt"])
            if now - checked < timedelta(days=RETRY_DAYS[item["lane"]]):
                continue
            stage = (1, order.get(item.get("reason"), 3), previous["checkedAt"])
        else:
            stage = (0, order.get(item.get("reason"), 3), "")
        try:
            version = version_parts(item.get("version"))
        except ValueError:
            version = (0, 0, 0)
        queue.append((item["lane"] != "auto", stage, -item.get("priority", 0), str(item["key"]),
                      tuple(-part for part in version), item["id"]))
    return [entry[-1] for entry in sorted(queue)[:limit]]


def repository_relevance(repository):
    """只读文件列表和文本判断搜索到的仓库是不是漫画源仓库；不执行任何内容。

    返回 (是否相关, 说明)。判断不了就抛错，由调用方保持原样列出。
    """
    tree = json.loads(request(
        f"https://api.github.com/repos/{repository}/git/trees/HEAD?recursive=1", api=True))
    if tree.get("truncated"):
        raise ValueError("文件列表不完整")
    paths = [entry["path"] for entry in tree["tree"]
             if entry.get("type") == "blob" and isinstance(entry.get("path"), str)]
    if "index.json" in paths or any(path.endswith(".js") for path in paths):
        return True, "文件列表含索引或脚本线索"
    return False, "文件列表中没有 index.json 或 JavaScript"


def trial_plan(candidate, catalog):
    """候选试跑的样本、设置和预算：已有 key 沿用现有构建，新 key 用默认关键词。"""
    builds = [item for item in catalog["sources"] if item["key"] == candidate["key"]]
    if not builds:
        return dict(DEFAULT_SAMPLE), {}, dict(POLICY)
    baseline = baseline_build(builds)
    return baseline["sample"], baseline.get("settings", {}), execution_policy(baseline)


def container_command(metadata, sources_dir, output, number, profile=None, name=None):
    """已审阅构建和候选共用同一套隔离参数：只读根、去能力、无 GitHub 凭据。"""
    command = [
        "docker", "run", "--rm", "--read-only", "--cap-drop=ALL",
        "--security-opt=no-new-privileges", "--pids-limit=256", "--memory=3g", "--cpus=2",
        "--user", f"{os.getuid()}:{os.getgid()}", "--env", "HOME=/tmp",
        "--env", "PATROL_WORKER=/usr/local/bin/patrol-worker", "--tmpfs", "/tmp:rw,noexec,nosuid,size=1024m",
        "--mount", f"type=bind,source={sources_dir},target=/sources,readonly",
        "--mount", f"type=bind,source={output},target=/work",
    ]
    if name:
        command += ["--name", name]
    if profile:
        command += ["--env", f"VENERA_CLIENT_PROFILE={profile}"]
    return command + [metadata["image"], "check-all", "--config", f"/work/{number}.config.json", "--no-env"]


def trial_candidates(work, catalog, metadata, sources_dir, budget=TRIAL_BUDGET_SECONDS):
    """在同一隔离容器里试跑候选。候选出的任何问题都只记在候选自己身上，不影响已审阅构建的结果。"""
    path = work / "artifact/discovery.json"
    if not path.is_file():
        return []
    deadline = time.monotonic() + budget
    known = {item["sha256"] for item in catalog["sources"]}
    registered = registered_repositories(load(ROOT / "monitor/upstreams.json"))
    selected = sorted((item for item in load(path)["updates"] if item.get("trial")),
                      key=lambda item: item.get("lane") != "auto")[:TRIAL_LIMIT]
    records = []
    number = 0
    for item in selected:
        if deadline - time.monotonic() < 120:
            break
        done = set()
        try:
            if not (isinstance(item.get("id"), str) and item["id"] == item.get("sha256")
                    and re.fullmatch(r"[a-f0-9]{64}", item["id"]) and item["id"] not in known
                    and pinned_repository(item.get("url", "")) == item["repository"].casefold() in registered):
                raise ValueError("候选不是固定提交地址上的未入库构建")
            data = request(item["url"])
            if sha(data) != item["sha256"]:
                raise ValueError("源码 SHA-256 与发现阶段不一致")
            (sources_dir / f"{item['id']}.js").write_bytes(data)
            sample, settings, policy = trial_plan(item, catalog)
            for profile in TRIAL_PROFILES:
                remaining = deadline - time.monotonic()
                if remaining < 120:
                    raise TimeoutError("本轮试跑时间预算已用完，留到下一轮")
                latest = run("git", "ls-remote", "https://github.com/Gandum2077/venera-patrol-cli.git",
                             "HEAD", capture_output=True, text=True).stdout.split()[0]
                if latest != metadata["commit"]:
                    raise TimeoutError("试跑前 CLI 已更新，留到下一轮")
                name = f"c{number}"
                number += 1
                output = work / "trials" / item["id"] / profile
                output.mkdir(parents=True, exist_ok=False)
                save(output / f"{name}.index.json", [
                    {"key": item["key"], "fileName": f"/sources/{item['id']}.js"}])
                save(output / f"{name}.config.json", {
                    "version": 1, "configPaths": [f"/work/{name}.index.json"],
                    "output": f"/work/reports/{name}", "defaults": policy,
                    "sources": {item["key"]: {"inputs": sample,
                                              "settings": settings}}})
                container = f"vensrc-trial-{os.getpid()}-{name}"
                print(f"候选试跑 {name}：{profile}，{text(item['key'])}。", flush=True)
                try:
                    result = subprocess.run(
                        container_command(metadata, sources_dir, output, name, profile, container),
                        timeout=min(remaining, policy["sourceTimeoutMs"] // 1000 + 30),
                        check=False)
                except subprocess.TimeoutExpired:
                    subprocess.run(["docker", "kill", container], check=False, capture_output=True)
                    raise ValueError("试跑超时，已终止容器")
                if result.returncode not in (0, 1):
                    raise ValueError(f"试跑进程异常退出：{result.returncode}")
                reports = list((output / f"reports/{name}").glob("*/report.json"))
                if len(reports) != 1:
                    raise ValueError("试跑没有生成唯一报告")
                report = load(reports[0])
                if report.get("schemaVersion") != 1 or len(report["sources"]) != 1:
                    raise ValueError("试跑报告格式或源数量不符合当前契约")
                source, = report["sources"]
                if source.get("sourceSha256") and source["sourceSha256"] != item["sha256"]:
                    raise ValueError("报告的执行源码哈希与下载字节不一致")
                records.append({
                    "id": item["id"], "runtimeProfile": profile, "inputs": sample,
                    "trialRun": os.environ["AUDIT_RUN_URL"],
                    **(trial_trace(reports[0].parent) if core(source) else {}),
                    "accountCapabilities": account_capabilities(source),
                    "policy": policy,
                    "source": {key: source.get(key) for key in (
                        "key", "name", "version", "sourceSha256", "status", "startedAt", "stages")}})
                done.add(profile)
        except TimeoutError as error:
            # 没跑到的候选不留记录，下一轮照常排队；已跑完的那一端单独不构成结论，同样重排。
            print(f"候选试跑停止：{text(error)}", flush=True)
            records = [record for record in records
                       if record.get("id") != item["id"]]
            break
        except Exception as error:
            print(f"候选试跑中断：{text(error)}", flush=True)
            records += [{"id": item["id"], "runtimeProfile": profile, "error": text(error)}
                        for profile in TRIAL_PROFILES if profile not in done]
    return records


def account_capabilities(source):
    return sorted({cap["path"] for cap in source["capabilities"] if cap["path"].startswith("account.")})


def collect_reading_site(event, sites):
    if event.get("event") == "http.response" and event.get("stage") == "comic.loadInfo":
        host = urlparse(event.get("finalUrl") or event.get("url") or "").hostname
        if host:
            sites.add(site_key(host))


def trial_trace(report_dir):
    trace, = report_dir.glob("*.trace.jsonl")
    hosts = set()
    sites = set()
    sample = {}
    with trace.open(encoding="utf-8") as stream:
        for line in stream:
            event = json.loads(line)
            collect_reading_site(event, sites)
            if event.get("event") == "trace.truncated":
                raise ValueError("候选网络记录被截断")
            if event.get("event") == "capability.call" and event.get("stage") == "comic.loadEp":
                args = event.get("args", [])
                if args:
                    sample = {key: value for key, value in zip(("comicId", "epId"), args)
                              if isinstance(value, (int, str)) and str(value)}
            if event.get("event") in ("http.request", "http.response"):
                for field in ("url", "finalUrl"):
                    if event.get(field):
                        host = urlparse(event[field]).hostname
                        if not host:
                            raise ValueError("候选请求地址无法核对")
                        hosts.add(host)
    return {"networkHosts": sorted(hosts), "readingSites": sorted(sites), "readSample": sample}


def fetch_build_hosts(items, workers=6):
    """并发下载固定地址上的构建并读取主机名；返回 {sha256: 主机名集合或异常}。只读文本，不执行。"""
    def one(item):
        try:
            data = request(item["url"])
            if sha(data) != item["sha256"]:
                raise ValueError("源码 SHA-256 与记录不一致")
            return item["sha256"], source_surface(data.decode("utf-8-sig"))
        except Exception as error:
            return item["sha256"], error
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        return dict(pool.map(one, items))


def hosts_lookup(table):
    def hosts_of(item):
        value = table.get(item["sha256"])
        if value is None:
            raise ValueError("没有取得源码")
        if isinstance(value, Exception):
            raise value
        return value
    return hosts_of


def host_check_targets(updates, catalog):
    """只有通过了版本条件的候选才需要比主机名；返回 (要读的现有构建, 要读的候选)。"""
    by_key = {}
    for item in catalog["sources"]:
        by_key.setdefault(item["key"], []).append(item)
    builds, candidates = {}, []
    for update in updates:
        existing = by_key.get(update.get("key"), [])
        if all(version_newer(update.get("version"), item["version"]) for item in existing):
            candidates.append(update)
            builds.update({item["id"]: item for item in existing})
            if not existing:
                builds.update({item["id"]: item for item in catalog["sources"]})
    return list(builds.values()), candidates


def core_break(source):
    """核心阅读链路断在哪一步；通过时返回 None。"""
    if core(source):
        return None
    stages = source.get("stages") or []
    passed = {stage["path"] for stage in stages if stage["status"] in ("passed", "recovered")}

    def entry(path):
        return path.startswith(("search.", "explore[", "categoryComics.")) and ".load" in path

    for step in ("source.load", None, "comic.loadInfo", "comic.loadEp", "image.download", "image.decode"):
        if step is None:
            if any(entry(path) for path in passed):
                continue
            found = [stage for stage in stages if entry(stage["path"])]
        else:
            if step in passed:
                continue
            found = [stage for stage in stages if stage["path"] == step]
        stage = next((item for item in found if item["status"] == "failed"), found[0] if found else None)
        if stage is None:
            return {"breakAt": step or "入口（搜索／发现／分类）", "category": "未执行", "reason": ""}
        return {"breakAt": stage["path"],
                "category": CATEGORIES.get(stage.get("category"), stage.get("category") or
                                           LABELS.get(stage["status"], stage["status"])),
                "reason": reason_zh(stage.get("reason", ""))}


def trial_summary(record):
    if not record or not isinstance(record.get("source"), dict):
        return {"core": False, "status": "error", "breakAt": "", "category": "试跑未完成",
                "reason": text((record or {}).get("error", "没有试跑记录"))}
    broken = core_break(record["source"])
    return {"core": broken is None, "status": text(record["source"].get("status")),
            **(broken or {"breakAt": "", "category": "", "reason": ""})}


def slim_record(record):
    """留给下一轮写入前复核的记录：阶段状态和客户端身份，不带返回正文。"""
    source = record["source"]
    stages = []
    for stage in source["stages"]:
        kept = {name: stage[name] for name in ("path", "status", "category") if stage.get(name) is not None}
        if stage.get("reason"):
            kept["reason"] = text(stage["reason"])
        if stage["path"] == "runtime.load" and "output" in stage:
            kept["output"] = stage["output"]
        stages.append(kept)
    return {"id": record["id"], "runtimeProfile": record["runtimeProfile"], "inputs": record["inputs"],
            "trialRun": record["trialRun"], "networkHosts": record["networkHosts"],
            "accountCapabilities": record["accountCapabilities"], "readSample": record["readSample"],
            "readingSites": record["readingSites"],
            "policy": record.get("policy"),
            "source": {**{name: source.get(name) for name in (
                "key", "name", "version", "sourceSha256", "status", "startedAt")}, "stages": stages}}


def catalog_entry(candidate, fields, baseline, catalog, registered):
    """自动收录的新清单条目：来源取自已核对的候选，样本、设置和预算沿用同 key 现有构建。"""
    baseline = baseline or {"sample": DEFAULT_SAMPLE}
    repository = candidate["repository"]
    tracked = sorted({repo for repo in candidate.get("trackedBy", [])
                      if isinstance(repo, str) and repo.casefold() in registered} | {repository})
    own = 20 if set(tracked) & set(catalog["priorityRepositories"]) else 0
    entry = {
        "url": candidate["url"], "key": candidate["key"],
        "name": fields.get("name") or candidate["name"], "version": candidate["version"],
        "minAppVersion": fields.get("minAppVersion", "1.0.0"), "repository": repository,
        "fileName": Path(unquote(urlparse(candidate["url"]).path)).name,
        "sample": json.loads(json.dumps(baseline["sample"])),
        "officialKey": baseline.get("officialKey", False),
        # 优先级不能低于被替换的构建，否则新版本永远选不上。
        "priority": max(baseline.get("priority", 0), own), "trackedBy": tracked,
        "id": candidate["sha256"], "sha256": candidate["sha256"],
        "runtimeProfile": "venerax", "verifyProfiles": ["venera-next"],
        "settings": json.loads(json.dumps(baseline.get("settings", {}))),
    }
    for name in ("patrolPolicy", "clientFamily"):
        if name in baseline:
            entry[name] = json.loads(json.dumps(baseline[name]))
    return entry


def verify_auto_inclusion(candidate, pair, cli, catalog, registered, exclusions, fetch, baseline_caps):
    """写入清单前的完整复核：固定提交地址、SHA-256、通道条件和两端记录；任何一项不符即抛错。

    fetch(url, sha256) 返回已核对哈希的源码字节。只读文本，不执行。
    """
    build_id = candidate.get("sha256")
    assert isinstance(build_id, str) and re.fullmatch(r"[a-f0-9]{64}", build_id) \
        and candidate.get("id") == build_id, "构建 ID 必须是完整源码哈希"
    assert isinstance(candidate.get("url"), str) and pinned(candidate["url"]), "候选地址必须固定到 Git 提交"
    assert pinned_repository(candidate["url"]) == candidate["repository"].casefold() in registered, "仓库未登记或地址不匹配"
    data = fetch(candidate["url"], build_id)
    assert sha(data) == build_id, "源码 SHA-256 与候选不一致"
    code = data.decode("utf-8-sig")
    fields = declared_fields(code)
    assert isinstance(candidate.get("key"), str) and fields.get("key") == candidate["key"], \
        "源码声明的 key 与候选不一致"
    assert fields.get("version") == candidate.get("version"), "源码声明的版本与候选不一致"

    def hosts_of(item):
        if item["sha256"] == build_id:
            return source_surface(code)
        return source_surface(fetch(item["url"], item["sha256"]).decode("utf-8-sig"))

    candidate = {**candidate, **fields}
    verdict = candidate_gate(candidate, catalog, registered, exclusions, hosts_of)
    assert verdict["lane"] == "auto", "不满足自动收录条件：" + verdict["detail"]
    baseline = next((item for item in catalog["sources"] if verdict["baseline"] and
                     item["id"] == verdict["baseline"]["id"]), None)
    entry = catalog_entry(candidate, fields, baseline, catalog, registered)
    guard = "scripts/patrol-worker.c"
    assert cli["adapterSha256"].get(guard) == sha((ROOT / guard).read_bytes()), "试跑文件隔离器哈希不符"
    assert isinstance(pair, dict) and set(pair) == set(TRIAL_PROFILES), "两端试跑记录不完整"
    assert pair["venerax"].get("trialRun") and pair["venerax"]["trialRun"] == pair["venera-next"].get("trialRun"), "两端证据必须来自同轮隔离试跑"
    for profile in TRIAL_PROFILES:
        record = pair[profile]
        source = record["source"]
        assert record["id"] == build_id and record["runtimeProfile"] == profile, "试跑记录与候选不对应"
        assert source["key"] == entry["key"], "实际 runtime key 与候选不一致"
        assert source.get("sourceSha256") == build_id, "试跑执行的源码哈希与候选不一致"
        assert source.get("version") == entry["version"], "CLI 实际加载的版本与候选不一致"
        assert record.get("inputs") == entry["sample"], "试跑样本不一致"
        observed = record.get("networkHosts")
        capabilities = record["accountCapabilities"]
        assert isinstance(capabilities, list)
        if capabilities:
            assert baseline and set(capabilities) <= set(baseline_caps.get(baseline["id"], {}).get(profile, [])), "试跑发现新增账号能力"
        assert isinstance(observed, list) and observed and all(isinstance(host, str) and host for host in observed), "缺少实际网络请求证据"
        if baseline:
            added = new_hosts(observed, hosts_of(baseline)[0])
            assert not added, "试跑访问新增主机名：" + "、".join(added)
        assert source["status"] in ("passed", "partial", "failed"), "试跑状态不满足主／扩展标准"
        validate_client_record(record, entry, {"cli": cli})
        assert core(source), f"{profile} 核心阅读链路未通过"
    if not baseline:
        actual = pair["venerax"]["readSample"]
        assert actual.get("comicId") and actual == pair["venera-next"]["readSample"], "两端实际阅读样本不一致"
        entry["sample"].update(actual)
        sites = set().union(*(record["readingSites"] for record in pair.values()))
        assert not any(sites.intersection(item.get("readingSites", [])) for item in catalog["sources"]), "与已收录构建详情站点重复"
        entry["readingSites"] = sorted(sites)
    return entry, baseline


def inclusion_state():
    path = ROOT / "data/auto-inclusion.json"
    state = load(path) if path.is_file() else {}
    assert state.get("schemaVersion", 1) == 1
    return {"schemaVersion": 1, "updatedAt": state.get("updatedAt", ""),
            "policy": {"trialLimit": TRIAL_LIMIT, "stableDays": STABLE_DAYS, "stablePasses": STABLE_PASSES},
            "pending": list(state.get("pending", [])), "builds": dict(state.get("builds", {})),
            "rejected": dict(state.get("rejected", {}))}


def protected_builds():
    """重点复测、源备注和账号巡检按构建 ID 引用的构建；自动化不删除它们。"""
    def optional(name):
        path = ROOT / "monitor" / name
        return load(path) if path.is_file() else {}
    return (set(optional("focus.json").get("buildIds", []))
            | set(optional("source-notes.json").get("notes", {}))
            | {site["buildId"] for site in optional("accounts.json").get("sites", []) if site.get("buildId")})


def verified_fetcher():
    cache = {}

    def fetch(url, digest):
        if (url, digest) not in cache:
            data = request(url)
            if sha(data) != digest:
                raise ValueError("源码 SHA-256 与记录不一致")
            cache[url, digest] = data
        return cache[url, digest]
    return fetch


def publish_candidates(payload, discovery, destination):
    """发布阶段：汇总候选试跑结果，复核自动通道并排队，更新自动收录构建的稳定计数。

    这里不改 monitor/catalog.json：本轮证据绑定的是巡检时的清单哈希，清单由下一轮开头的 promote 写入。
    """
    (destination / "reports").mkdir(parents=True, exist_ok=True)
    catalog = validate_catalog(load(ROOT / "monitor/catalog.json"))
    registered = registered_repositories(load(ROOT / "monitor/upstreams.json"))
    exclusions = official_policy(snapshot=payload.get("officialExclusions"))
    checked = payload["checkedAt"]
    run_url = os.environ.get("AUDIT_RUN_URL", "")
    updates = {item["id"]: item for item in discovery["updates"]}
    previous_path = ROOT / "data/candidate-results.json"
    previous = load(previous_path).get("results", {}) if previous_path.is_file() else {}
    state = inclusion_state()
    fetch = verified_fetcher()
    pairs = {}
    for record in payload.get("candidateRecords", []):
        if record.get("id") in updates and record.get("runtimeProfile") in TRIAL_PROFILES:
            pair = pairs.setdefault(record["id"], {})
            assert record["runtimeProfile"] not in pair, "候选客户端证据重复"
            pair[record["runtimeProfile"]] = record
    results = {build_id: result for build_id, result in previous.items() if build_id in updates}
    verified = {}
    baseline_caps = {}
    catalog_sites = set()
    for record in payload["records"] + payload.get("clientRecords", []):
        catalog_sites.update(record.get("readingSites", []))
        if record.get("accountCapabilities") and record["source"].get("sourceSha256") == record["id"]:
            baseline_caps.setdefault(record["id"], {})[record["runtimeProfile"]] = record["accountCapabilities"]
    for build_id, pair in pairs.items():
        candidate = updates[build_id]
        state["rejected"].pop(build_id, None)
        result = {
            **{name: text(candidate.get(name, "")) for name in ("key", "name", "version", "repository")},
            "url": candidate["url"],
            "lane": candidate.get("lane") if candidate.get("lane") in ("auto", "trial") else "trial",
            "reason": text(candidate.get("reason", "")), "detail": text(candidate.get("detail", "")),
            "newHosts": [text(host) for host in candidate.get("newHosts", [])][:50],
            "baselineVersion": text((candidate.get("baseline") or {}).get("version", "")),
            "reviewVersion": 3,
            "checkedAt": checked, "runUrl": run_url,
        }
        try:
            result["profiles"] = {profile: trial_summary(pair.get(profile)) for profile in TRIAL_PROFILES}
        except Exception as error:
            result["profiles"] = {profile: trial_summary({"error": f"记录无法解析：{error}"})
                                  for profile in TRIAL_PROFILES}
        if any(summary["status"] == "error" for summary in result["profiles"].values()):
            result["outcome"] = "error"
        elif all(summary["core"] for summary in result["profiles"].values()):
            result["outcome"] = "passed"
        else:
            result["outcome"] = "failed"
        if result["outcome"] == "passed" and result["lane"] == "auto":
            # 发现阶段给的通道只是线索；这里用受信任的清单重新下载、重新判定。
            try:
                assert run_url and all(record.get("trialRun") == run_url for record in pair.values()), "试跑轮次与发布不符"
                entry, baseline = verify_auto_inclusion(
                    candidate, pair, payload["cli"], catalog, registered, exclusions, fetch, baseline_caps)
                assert baseline or catalog_sites.isdisjoint(entry["readingSites"]), "不同 key 的详情请求指向清单已有站点"
                verified.setdefault(entry["key"], []).append((entry, baseline, candidate, pair))
                result["outcome"] = "queued"
            except Exception as error:
                result["outcome"] = "rejected"
                result["detail"] = text(error) or "试跑证据与受信任的记录不一致"
        results[build_id] = result
    pending = {entry["candidate"]["id"]: entry for entry in state["pending"]
               if entry.get("candidate", {}).get("id") in updates
               and entry["candidate"]["id"] not in pairs}
    for group in verified.values():
        top = max(version_parts(entry["version"]) for entry, _, _, _ in group)
        leaders = [row for row in group if version_parts(row[0]["version"]) == top]
        for entry, baseline, candidate, pair in group:
            if len(leaders) != 1 or entry is not leaders[0][0]:
                results[entry["id"]].update(outcome="rejected", detail="同 key 本轮有多个候选通过，只排入版本最高的一个")
                continue
            pending[entry["id"]] = {
                "candidate": {name: candidate.get(name) for name in (
                    "id", "key", "name", "version", "fileName", "url", "sha256", "repository",
                    "trackedBy", "priority")},
                "replaces": (baseline or {}).get("id"), "replacesVersion": (baseline or {}).get("version"),
                "baselineCapabilities": {baseline["id"]: baseline_caps.get(baseline["id"], {})} if baseline else {},
                "records": {profile: slim_record(pair[profile]) for profile in TRIAL_PROFILES},
                "cli": {name: payload["cli"][name] for name in ("commit", "clientProfiles", "adapterSha256")},
                "checkedAt": checked, "runUrl": run_url,
            }
    state["pending"] = list(pending.values())
    state["rejected"] = {build_id: value for build_id, value in state["rejected"].items()
                         if build_id in updates}
    for build_id, value in state["rejected"].items():
        if build_id in results and results[build_id]["outcome"] == "queued" and build_id not in pending:
            results[build_id].update(outcome="rejected", detail=text(value.get("reason", "")))
    # 稳定计数：自动收录的新构建本轮被订阅选中才算一次通过，中断即清零。
    locks = {row["buildId"] for row in load(generated_path(destination, "sources.lock.json"))}
    tested = {record["id"] for record in payload["records"]}
    moment = datetime.fromisoformat(checked)
    watching = {}
    for item in catalog["sources"]:
        auto = item.get("autoIncluded")
        if not auto or not auto["replaces"] or auto.get("stableAt"):
            continue
        build = {"key": item["key"], "version": item["version"], "replaces": auto["replaces"],
                 "replacesVersion": auto["replacesVersion"], "includedAt": auto["at"],
                 "runUrl": auto["runUrl"], "passes": 0, "since": None,
                 **state["builds"].get(item["id"], {})}
        if item["id"] in tested and build.get("lastCheckedAt") != checked:
            selected = item["id"] in locks
            build["passes"] = build["passes"] + 1 if selected else 0
            build["since"] = (build["since"] or checked) if selected else None
            build.update(selected=selected, lastCheckedAt=checked)
            build["stable"] = bool(
                selected and build["passes"] >= STABLE_PASSES
                and moment - datetime.fromisoformat(build["since"]) >= timedelta(days=STABLE_DAYS))
        watching[item["id"]] = build
    state["builds"] = watching
    state["updatedAt"] = checked
    save(destination / "data/auto-inclusion.json", state)
    lanes = {}
    for item in updates.values():
        lanes[item.get("lane")] = lanes.get(item.get("lane"), 0) + 1
    untested = sum(1 for item in updates.values()
                   if item.get("lane") in ("auto", "trial") and item["id"] not in results)
    save(destination / "data/candidate-results.json", {
        "schemaVersion": 1, "checkedAt": checked, "runUrl": run_url, "trialLimit": TRIAL_LIMIT,
        "testedThisRound": len(pairs), "untested": untested, "results": results})

    def cells(*values):
        return "| " + " | ".join(text(value) for value in values) + " |"

    def outcome(summary):
        if summary["core"]:
            return "通过"
        return "断在 " + "：".join(part for part in (
            summary["breakAt"], summary["category"], summary["reason"]) if part)

    rows = sorted(results.items(), key=lambda row: (row[1]["key"], row[1]["version"], row[0]))
    lines = [
        "# 上游候选试跑短名单", "",
        f"核验时间：{checked}（UTC）。本轮试跑 {len(pairs)} 个候选（每轮上限 {TRIAL_LIMIT} 个），"
        f"还有 {untested} 个等待首次试跑。",
        f"待审构建 {len(updates)} 个：自动收录通道 {lanes.get('auto', 0)} 个，"
        f"试跑但不收录 {lanes.get('trial', 0)} 个；未登记仓库的 "
        f"{len(discovery.get('unregistered', []))} 个文件只列出、不下载执行（见 UPDATES.md）。",
        "试跑与已审阅构建使用同一隔离容器，VeneraX 与 Venera-Next 各跑一次；"
        "「通过」指核心阅读链路通过，不代表其他能力可用。", "",
        "## 已排入自动收录（下一轮开始时再次复核并写入清单）", "",
        "| key | 名称 | 现有版本 → 新版本 | 仓库 |", "| --- | --- | --- | --- |"]
    for entry in state["pending"]:
        candidate = entry["candidate"]
        lines.append(cells(candidate["key"], candidate["name"],
                           f"{entry['replacesVersion'] or '首次收录'} → {candidate['version']}", candidate["repository"]))
    lines += ["", "## 自动收录观察期", "",
              f"新构建连续被订阅选中满 {STABLE_DAYS} 天且不少于 {STABLE_PASSES} 轮才算稳定；"
              "此前旧构建留在清单里照常巡检，新构建失败时订阅自动选回旧构建。", "",
              "| key | 新版本 | 旧版本 | 本轮订阅选中 | 连续选中轮数 | 起算时间 |",
              "| --- | --- | --- | --- | --- | --- |"]
    for build in sorted(watching.values(), key=lambda row: row["key"]):
        chosen = build.get("selected")
        lines.append(cells(build["key"], build["version"], build["replacesVersion"],
                           "尚无结果" if chosen is None else "新构建" if chosen else "未选中新构建（保留旧构建）",
                           build["passes"], build["since"] or ""))
    sections = (
        ("试跑通过、等待人工确认", lambda row: row["outcome"] == "passed"),
        ("试跑未通过", lambda row: row["outcome"] in ("failed", "error")),
        ("自动通道写入前复核未通过", lambda row: row["outcome"] == "rejected"),
    )
    for title, wanted in sections:
        lines += ["", f"## {title}", "",
                  "| key | 名称 | 版本 | 仓库 | 未自动收录的原因 | 新增主机名 | VeneraX | Venera-Next |",
                  "| --- | --- | --- | --- | --- | --- | --- | --- |"]
        for _, row in rows:
            if wanted(row):
                held = row["lane"] == "auto" and row["outcome"] in ("failed", "error")
                lines.append(cells(
                    row["key"], row["name"], row["version"], row["repository"],
                    "自动收录通道，两端试跑未全部通过" if held else row["detail"],
                    "、".join(row["newHosts"]) or "无",
                    *(outcome(row["profiles"][profile]) for profile in TRIAL_PROFILES)))
    write_report(destination / "reports/CANDIDATES.md", lines + [""])
    print(f"候选试跑：本轮 {len(pairs)} 个，排入自动收录 {len(state['pending'])} 个，"
          f"观察期 {len(watching)} 个。", flush=True)


def promote(now=None):
    """有写权限、不执行源码的写入步骤。

    把上一轮发布阶段排队的新构建重新核对（固定提交地址、SHA-256、通道条件、两端记录）后写进清单，
    并在新构建稳定后移除它替换掉的旧构建。返回本次改动摘要。
    """
    summary = {"added": [], "retired": [], "rejected": {}}
    if not (ROOT / "data/auto-inclusion.json").is_file():
        print("没有自动收录队列。", flush=True)
        return summary
    catalog = validate_catalog(load(ROOT / "monitor/catalog.json"))
    before = json.dumps(catalog, sort_keys=True)
    state = inclusion_state()
    registered = registered_repositories(load(ROOT / "monitor/upstreams.json"))
    exclusions = official_policy()
    stamp = (now or datetime.now(timezone.utc)).isoformat()
    fetch = verified_fetcher()
    for pending in state["pending"]:
        candidate = pending.get("candidate") or {}
        try:
            draft = json.loads(json.dumps(catalog))
            assert pending["runUrl"] and all(record.get("trialRun") == pending["runUrl"]
                                             for record in pending["records"].values()), "队列试跑轮次不符"
            entry, baseline = verify_auto_inclusion(
                candidate, pending["records"], pending["cli"], draft, registered, exclusions, fetch,
                pending["baselineCapabilities"])
            assert pending["replaces"] == (baseline or {}).get("id"), "排队后同 key 基线已变化"
            entry["autoIncluded"] = {
                "at": stamp, "replaces": pending["replaces"], "replacesVersion": pending["replacesVersion"],
                "runUrl": pending.get("runUrl", ""), "cliCommit": pending["cli"]["commit"]}
            if baseline:
                baseline["rollbackFor"] = entry["id"]
            draft["sources"].append(entry)
            catalog = validate_catalog(draft)
            if baseline:
                state["builds"][entry["id"]] = {
                    "key": entry["key"], "version": entry["version"], "replaces": baseline["id"],
                    "replacesVersion": baseline["version"], "includedAt": stamp,
                    "runUrl": pending.get("runUrl", ""), "passes": 0, "since": None}
            state["rejected"].pop(entry["id"], None)
            summary["added"].append(entry)
        except Exception as error:
            reason = text(error) or "试跑证据与受信任的记录不一致"
            summary["rejected"][str(candidate.get("id"))] = reason
            state["rejected"][str(candidate.get("id"))] = {"at": stamp, "reason": reason}
    state["pending"] = []
    protected = protected_builds()
    items = {item["id"]: item for item in catalog["sources"]}
    for build_id, build in list(state["builds"].items()):
        item = items.get(build_id)
        if not item or not item.get("autoIncluded") or item["autoIncluded"].get("stableAt"):
            del state["builds"][build_id]
            continue
        if not build.get("stable"):
            continue
        item["autoIncluded"]["stableAt"] = stamp
        target = item["autoIncluded"]["replaces"]
        while target in items and items[target].get("rollbackFor"):
            old = items[target]
            del old["rollbackFor"]
            if target in protected:
                break
            earlier = old.get("autoIncluded") or {}
            catalog["sources"].remove(old)
            del items[target]
            state["builds"].pop(target, None)
            summary["retired"].append(old)
            target = None if earlier.get("stableAt") else earlier.get("replaces")
        del state["builds"][build_id]
    validate_catalog(catalog)
    assert protected & {item["id"] for item in json.loads(before)["sources"]} <= set(items), \
        "被重点复测、源备注或账号巡检引用的构建不能移除"
    if json.dumps(catalog, sort_keys=True) != before:
        save(ROOT / "monitor/catalog.json", catalog)
    save(ROOT / "data/auto-inclusion.json", state)
    print(f"自动收录写入 {len(summary['added'])} 个，复核未通过 {len(summary['rejected'])} 个，"
          f"稳定后移除旧构建 {len(summary['retired'])} 个。", flush=True)
    for entry in summary["added"]:
        print(f"  + {text(entry['key'])} {entry['autoIncluded']['replacesVersion'] or '首次收录'} → {entry['version']}"
              f"（{text(entry['repository'])}）", flush=True)
    for build_id, reason in summary["rejected"].items():
        print(f"  ! {build_id[:12]}：{reason}", flush=True)
    return summary


def classify(source, output=None):
    """不执行任何源码的通道统计：只下载文本读主机名。"""
    discovery = load(source)
    catalog = validate_catalog(load(ROOT / "monitor/catalog.json"))
    registered = registered_repositories(load(ROOT / "monitor/upstreams.json"))
    updates = discovery["updates"]
    builds, candidates = host_check_targets([item for item in updates if
        pinned_repository(item["url"]) == item["repository"].casefold() in registered], catalog)
    table = fetch_build_hosts(builds + candidates)
    verdicts = classify_updates(updates, catalog, registered, official_policy(), hosts_lookup(table))
    rows = [{**{name: item.get(name) for name in ("id", "key", "name", "version", "repository")},
             **verdicts[item["id"]]} for item in updates]
    if output:
        save(output, rows)
    lanes, reasons = {}, {}
    for row in rows:
        lanes[row["lane"]] = lanes.get(row["lane"], 0) + 1
        reasons[(row["lane"], row["reason"])] = reasons.get((row["lane"], row["reason"]), 0) + 1
    print(f"待审构建 {len(rows)} 个。")
    for lane, count in sorted(lanes.items()):
        print(f"- {LANE_LABELS.get(lane, lane)}：{count}")
        for (owner, reason), number in sorted(reasons.items()):
            if owner == lane and reason != lane:
                print(f"    {REASON_LABELS.get(reason, reason)}：{number}")
    auto = sorted((row for row in rows if row["lane"] == "auto"), key=lambda row: str(row["key"]))
    print("自动收录通道前 20 个：")
    for row in auto[:20]:
        print(f"  {row['key']}｜{row['repository']}｜{(row['baseline'] or {}).get('version', '首次收录')} → {row['version']}")
    return rows


def self_test():
    global ROOT
    stage_names = ["source.load", "search.load", "comic.loadInfo", "comic.loadEp",
                   "image.download", "image.decode"]
    stages = [{"path": path, "status": "passed"} for path in stage_names]
    assert core({"stages": stages})
    assert not core({"stages": stages[:-1]})
    assert not core({"stages": stages[:1] + stages[2:]})
    # 站点数据里的孤立代理字符不能写崩发布（现实里就是 \udd65 这种）。
    assert text("a\udbffb") == "a\ufffdb"
    assert csv_cell("=\ud800") == "'=\ufffd"
    assert not pinned("https://github.com/a/b/blob/main/a.js")
    assert pinned("https://raw.githubusercontent.com/a/b/" + "a" * 40 + "/a.js")
    # 自动收录：版本必须严格更高且可比较；www、m 前缀视为同站，其余主机名一律算新增。
    assert version_newer("1.10.0", "1.9.9") and not version_newer("1.9.9", "1.9.9")
    assert not version_newer("2.0", "1.0.0") and not version_newer("2.0.0", "1.0")
    assert new_hosts(source_hosts('url = "https://m.a.com/x"; api = "api.a.com"'),
                     source_hosts('url = "https://www.a.com/"')) == ["api.a.com"]
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
    exclusions = official_policy()
    with tempfile.TemporaryDirectory() as directory:
        ROOT = Path(directory)
        try:
            save(ROOT / "monitor/official-keys.json", exclusions)
            item = {
                "id": "a" * 64, "sha256": "a" * 64, "key": "sample", "name": "测试漫画源",
                "url": "https://raw.githubusercontent.com/a/b/" + "c" * 40 + "/a.js",
                "version": "1.0.0", "fileName": "a.js", "repository": "a/b",
                "minAppVersion": "1.0.0", "sample": {"comicId": "1", "epId": "2", "keyword": "漫画"},
            }
            save(ROOT / "monitor/source-notes.json", {"schemaVersion": 1, "notes": {}})
            save(ROOT / "monitor/catalog.json", {
                "schemaVersion": 1, "priorityRepositories": catalog["priorityRepositories"],
                "sources": [item]})
            save(ROOT / "data/sources.lock.json", [{"key": "sample"}])
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
            assert len(load(ROOT / "out/subscriptions/index.json")) == 1
            payload["records"][0]["sample"] = {**item["sample"], "comicId": "1\udd65"}
            with contextlib.redirect_stdout(io.StringIO()):
                publish(payload, ROOT / "out")
            assert "1\ufffd" in (ROOT / "out/data/sources.zh.csv").read_text(encoding="utf-8-sig")
            source["status"] = "partial"
            source["stages"] = stages + [{"path": "account.login", "status": "skipped",
                                         "category": "credentials_missing"}]
            with contextlib.redirect_stdout(io.StringIO()):
                publish(payload, ROOT / "out")
            assert not load(ROOT / "out/subscriptions/index.json") and len(
                load(ROOT / "out/subscriptions/extended.json")) == 1
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
    parser.add_argument("command", choices=["setup-cli", "discover", "patrol", "publish", "promote",
                                            "classify", "self-test"])
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
        payload = load(args.input)
        publish(payload, ROOT)
        discovery = publish_discovery(load(args.input.with_name("discovery.json")), ROOT)
        try:
            publish_candidates(payload, discovery, ROOT)
        except Exception as error:
            # 候选汇总出错不能拦住已审阅构建的发布；本轮不排队、不计数，下一轮重来。
            print(f"::warning::候选试跑结果未能汇总，本轮只发布已审阅构建：{text(error)}", flush=True)
    elif args.command == "promote":
        promote()
    elif args.command == "classify":
        classify(args.input, args.work.resolve() / "classification.json")
    else:
        self_test()


if __name__ == "__main__":
    main()
