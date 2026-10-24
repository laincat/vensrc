"""完整快照先上传草稿并回读校验，再发布和清理旧版；最终只保留一个 Release。"""

import argparse
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from urllib.request import Request, urlopen
import zipfile

import account_patrol as accounts
import cloud_audit as audit

ROOT = Path(__file__).resolve().parents[1]
FILES = (
    "index.json", "extended.json", "sources.lock.json", "sources.zh.csv",
    "client-compatibility.zh.csv", "audit-status.json", "RESULTS.md",
    "CLIENT_RESULTS.md", "ACCOUNT_RESULTS.md", "ACCESS_RESULTS.md",
)
ASSETS = (*FILES, "vensrc.zip", "SHA256SUMS.txt")


def gh(*args):
    result = subprocess.run(["gh", *args], capture_output=True, text=True, check=True)
    return result.stdout


def releases(repository):
    pages = json.loads(gh("api", "--paginate", "--slurp", f"repos/{repository}/releases"))
    return [release for page in pages for release in page]


def validate(root):
    for name in FILES:
        if not (root / name).is_file():
            raise ValueError(f"Release 附件缺失：{name}")
    catalog = audit.validate_catalog(audit.load(root / "monitor/catalog.json"))
    items = {item["id"]: item for item in catalog["sources"]}
    state = audit.load(root / "audit-status.json")
    assert state["catalogSha256"] == audit.sha((root / "monitor/catalog.json").read_bytes())
    assert state["builds"] == len(items)
    clients = audit.load(root / "client-results.json")
    assert state["runUrl"] == clients["runUrl"] and state["cli"] == clients["cli"]
    records = {(r["id"], r["runtimeProfile"]): r for r in clients["records"]}
    expected = {(i["id"], p) for i in items.values()
                for p in (i["runtimeProfile"], *i["verifyProfiles"])}
    assert len(records) == len(clients["records"]) == len(expected) and set(records) == expected
    for record in records.values():
        audit.validate_client_record(record, items[record["id"]], {"cli": state["cli"]})
    main, extended = audit.load(root / "index.json"), audit.load(root / "extended.json")
    locks = audit.load(root / "sources.lock.json")
    by_key = {row["key"]: row for row in locks}
    assert len(by_key) == len(locks) == len(main) + len(extended) > 0
    assert len({row["key"] for row in main + extended}) == len(locks)
    assert state["main"] == len(main) and state["extended"] == len(extended)
    for channel, entries in (("main", main), ("extended", extended)):
        for entry in entries:
            locked = by_key[entry["key"]]
            item = items[locked["buildId"]]
            record = records[(item["id"], "venerax")]
            assert locked["runtimeProfile"] == "venerax" and locked["channel"] == channel
            assert locked["sha256"] == item["sha256"] == record["source"]["sourceSha256"]
            assert locked["checkedAt"] == state["checkedAt"]
            assert locked["cliCommit"] == state["cli"]["commit"]
            assert locked["status"] == record["source"]["status"] and audit.core(record["source"])
            assert (locked["status"] == "passed") == (channel == "main")
            for key, value in entry.items():
                assert locked[key] == value
            for key in ("key", "name", "version", "url", "minAppVersion", "fileName"):
                assert entry[key] == item[key]
            for key, value in item["sample"].items():
                assert locked["sample"][key] == value
    account = audit.load(root / "account-results.json")
    plan = accounts.validate_plan(audit.load(root / "monitor/accounts.json"), catalog)
    assert account["catalogSha256"] == state["catalogSha256"]
    assert account["accountPlanSha256"] == audit.sha((root / "monitor/accounts.json").read_bytes())
    assert account["runUrl"] == state["runUrl"]
    assert [(s["site"], s["key"]) for s in account["sites"]] == [
        (s["site"], s["key"]) for s in plan["sites"]]
    for site, expected_site in zip(account["sites"], plan["sites"], strict=True):
        assert len(site["records"]) in (0, 2)
        for record in site["records"]:
            assert record == accounts.sanitized(record), "账号结果含非公开字段"
            assert record["id"] == expected_site["buildId"]
            assert record["inputs"] == items[record["id"]]["sample"]
    access = audit.load(root / "access-results.json")
    assert access["catalogSha256"] == state["catalogSha256"]
    assert access["patrolRunUrl"] == state["runUrl"], "诊断与订阅不是同轮结果，暂不发布"
    assert access["diagnosticRunUrl"]
    assert access["cli"]["commit"] == state["cli"]["commit"]
    assert account["cli"]["commit"] == state["cli"]["commit"]
    return state, access


def stage(root, destination, repository):
    state, access = validate(root)
    destination.mkdir(parents=True)
    for name in FILES:
        shutil.copyfile(root / name, destination / name)
    # 固定 ZIP 时间与权限，使相同订阅快照在重跑时产生相同字节。
    with zipfile.ZipFile(destination / "vensrc.zip", "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name in FILES:
            entry = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            entry.create_system = 3
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, (destination / name).read_bytes())
    checksums = "".join(
        f"{audit.sha((destination / name).read_bytes())}  {name}\n"
        for name in sorted((*FILES, "vensrc.zip")))
    (destination / "SHA256SUMS.txt").write_text(checksums, encoding="ascii", newline="\n")
    tag = "rolling-" + audit.sha(checksums.encode("ascii"))[:16]
    prefix = f"https://github.com/{repository}/releases/latest/download"
    notes = (
        "# Vensrc 最新订阅\n\n"
        f"巡检时间：{state['checkedAt']}（UTC）；已审阅构建 {state['builds']} 个。\n\n"
        f"主索引 **{state['main']}** 项；扩展索引 **{state['extended']}** 项。\n\n"
        f"- [主订阅 index.json]({prefix}/index.json)：核心阅读及整次执行通过。\n"
        f"- [扩展订阅 extended.json]({prefix}/extended.json)：核心阅读通过，其他能力可能受限。\n"
        f"- [全部附件 ZIP]({prefix}/vensrc.zip)\n"
        f"- [SHA-256 校验清单]({prefix}/SHA256SUMS.txt)\n\n"
        "稳定订阅地址不随快照标签变化。先上传草稿并回读核验全部附件，发布后才清理旧版，"
        "最终只保留一个 Release。\n\n"
        "附件只有生成索引、锁定清单、中文 CSV 和报告；JS 地址仍固定到已审阅的上游提交。"
        "不打包账号凭据、Cookie、Token、原始追踪、认证状态或漫画内容。\n\n"
        f"CLI：`{state['cli']['commit']}`（本轮巡检开始前获取的最新版本）。\n\n"
        f"巡检 Actions：{state['runUrl']}\n\n诊断 Actions：{access['diagnosticRunUrl']}\n"
    )
    (destination / "release-notes.md").write_text(notes, encoding="utf-8", newline="\n")
    return tag


def verify(repository, tag, destination):
    with tempfile.TemporaryDirectory(prefix="vensrc-release-check-") as directory:
        gh("release", "download", tag, "--repo", repository, "--dir", directory)
        downloaded = Path(directory)
        assert {p.name for p in downloaded.iterdir()} == set(ASSETS), "远端附件缺失或多出未审阅文件"
        for name in ASSETS:
            assert audit.sha((downloaded / name).read_bytes()) == audit.sha(
                (destination / name).read_bytes()), f"远端附件哈希不匹配：{name}"


def verify_public(repository, destination):
    for name in ("index.json", "extended.json"):
        request = Request(
            f"https://github.com/{repository}/releases/latest/download/{name}",
            headers={"User-Agent": "vensrc-release-check"})
        with urlopen(request, timeout=35) as response:
            assert response.status == 200
            assert audit.sha(response.read()) == audit.sha((destination / name).read_bytes())


def publish(repository, destination, tag):
    existing = releases(repository)
    current = next((r for r in existing if r["tag_name"] == tag), None)
    if current is None:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
        gh("release", "create", tag, "--repo", repository, "--draft", "--target", commit,
           "--title", "Vensrc 最新订阅", "--notes-file", str(destination / "release-notes.md"))
    if current is None or current["draft"]:
        gh("release", "upload", tag, "--repo", repository, "--clobber",
           *[str(destination / name) for name in ASSETS])
    verify(repository, tag, destination)
    # 完整回读成功后才更新 Latest；中途失败不动旧版。
    gh("release", "edit", tag, "--repo", repository, "--draft=false", "--latest")
    latest = json.loads(gh("api", f"repos/{repository}/releases/latest"))
    assert latest["tag_name"] == tag
    verify_public(repository, destination)
    for release in releases(repository):
        if release["tag_name"] != tag:
            gh("release", "delete", release["tag_name"], "--repo", repository,
               "--yes", "--cleanup-tag")
    remaining = releases(repository)
    assert len(remaining) == 1 and remaining[0]["tag_name"] == tag
    print(f"滚动 Release 发布完成：{tag}；{len(ASSETS)} 个附件，最终仅保留 1 个 Release。")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--publish", action="store_true")
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", args.repository):
        raise ValueError("仓库名称不合法")
    release_tag = stage(ROOT, args.output.resolve(), args.repository)
    print(f"快照已校验并打包：{release_tag}；主／扩展标准及固定样本未变。")
    if args.publish:
        publish(args.repository, args.output.resolve(), release_tag)
