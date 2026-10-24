"""按站点隔离账号巡检；公开产物只保留状态、固定样本和受信任的标识。"""

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
from datetime import datetime, timezone

import cloud_audit as audit

ROOT = Path(__file__).resolve().parents[1]


def sanitized(record):
    """不发布源返回值、异常文本、网络追踪或账号状态。"""
    return {
        "id": record["id"], "runtimeProfile": record["runtimeProfile"],
        "inputs": record["inputs"],
        "source": {
            "key": record["source"]["key"],
            "sourceSha256": record["source"].get("sourceSha256"),
            "status": record["source"]["status"],
            "stages": [
                {key: stage[key] for key in ("path", "status", "category", "durationMs")
                 if key in stage}
                for stage in record["source"]["stages"]
            ],
        },
    }


def validate_plan(plan, catalog):
    assert plan["schemaVersion"] == 1
    items = {i["id"]: i for i in catalog["sources"]}
    seen = set()
    for site in plan["sites"]:
        assert re.fullmatch(r"PATROL_AUTH_[A-Z0-9_]+", site["secret"])
        assert site["secret"] not in seen
        seen.add(site["secret"])
        if site.get("buildId"):
            item = items[site["buildId"]]
            assert item["key"] == site["key"]
            assert item["runtimeProfile"] == "venerax"
            assert site["loginReviewed"] is True
    return plan


def render(payload, destination):
    destination.mkdir(parents=True, exist_ok=True)
    audit.save(destination / "account-results.json", payload)
    lines = [
        "# 隔离账号巡检结果", "",
        f"核验时间：{payload['checkedAt']}（UTC）。",
        f"最新 CLI 提交：`{payload['cli']['commit']}`。",
        "每个源只接收本站凭据；同一固定源码及样本分别在 VeneraX、Venera-Next 执行。",
        "不发布用户名、密码、Cookie、Token、收藏内容、异常原文或原始追踪。",
        "登录通过表示源登录接口满足本次契约；阅读链路独立判断，不代替匿名订阅的收录结果。",
        "没有接入账号 Secret 的源、无登录接口的源及未登记站点均如实标记。",
        "不启用签到、评论、点赞、收藏增删和设置按钮等写操作；不保存跨次会话。", "",
        "跳过和未执行不计入登录、核心阅读或整次通过。登录拒绝不等同于密码错误。", "",
        "## 登录失败项", "",
    ]
    login_failures = []
    login_unverified = []
    for entry in payload["sites"]:
        if not entry.get("records"):
            login_unverified.append(f"- {audit.text(entry['site'])}（`{audit.text(entry['key'])}`）：{audit.text(entry['note'])}。")
        for record in entry.get("records", []):
            login = next((s for s in record["source"]["stages"] if s["path"] == "account.login"), {})
            label = f"{audit.text(entry['site'])}／{record['runtimeProfile']}"
            if login.get("status") == "failed":
                category = audit.CATEGORIES.get(login.get("category"), login.get("category", "未分类"))
                login_failures.append(f"- {label}：登录失败，{audit.text(category)}；需核对账号状态、权限及访问限制。")
            elif login.get("status") not in ("passed", "recovered"):
                login_unverified.append(f"- {label}：登录{audit.LABELS.get(login.get('status'), '未执行')}，不计通过。")
    lines += login_failures or ["本轮没有已执行且失败的登录接口；未执行项另列。"]
    notes = [f"- {audit.text(e['site'])}：{audit.text(e['note'])}"
             for e in payload["sites"] if e.get("records") and e.get("note")]
    if notes:
        lines += ["", "## 已核对的登录流程差异", "", *notes]
    lines += ["", "## 登录未验证／跳过项", ""]
    lines += login_unverified or ["无。"]
    lines += [
        "", "## 全部账号结果", "",
        "| 站点 | key | 环境 | 登录 | 核心阅读 | 整次 | 全部失败阶段及类别 | 跳过阶段数 |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for entry in payload["sites"]:
        if not entry.get("records"):
            lines.append("| " + " | ".join(audit.text(v) for v in (
                entry["site"], entry["key"], "—", entry["note"], "未测试", "跳过", "", "未执行")) + " |")
        for record in entry.get("records", []):
            source = record["source"]
            login = next((s for s in source["stages"] if s["path"] == "account.login"), {})
            failures = [
                f"{s['path']}：{audit.CATEGORIES.get(s.get('category'), s.get('category', '未分类'))}"
                for s in source["stages"] if s["status"] == "failed"
            ]
            lines.append("| " + " | ".join(audit.text(v) for v in (
                entry["site"], entry["key"], record["runtimeProfile"],
                audit.LABELS.get(login.get("status"), "未执行"),
                "通过" if audit.core(source) else "未通过", audit.LABELS[source["status"]],
                "；".join(failures) or "无失败", sum(s["status"] == "skipped" for s in source["stages"]))) + " |")
    lines += ["", "固定源码哈希、客户端提交、依赖锁和样本输入见 account-results.json。",
              f"Actions：{payload.get('runUrl', '')}", ""]
    (destination / "ACCOUNT_RESULTS.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


def patrol(work):
    catalog = audit.validate_catalog(audit.load(ROOT / "monitor/catalog.json"))
    plan = validate_plan(audit.load(ROOT / "monitor/accounts.json"), catalog)
    metadata = audit.load(work / "cli.json")
    latest = audit.run("git", "ls-remote", "https://github.com/Gandum2077/venera-patrol-cli.git",
                       "HEAD", capture_output=True, text=True).stdout.split()[0]
    if latest != metadata["commit"]:
        raise ValueError("账号巡检前 CLI 已更新，停止并重新获取最新版本")
    items = {i["id"]: i for i in catalog["sources"]}
    payload = {
        "schemaVersion": 1, "checkedAt": datetime.now(timezone.utc).isoformat(),
        "cli": metadata, "catalogSha256": audit.sha((ROOT / "monitor/catalog.json").read_bytes()),
        "accountPlanSha256": audit.sha((ROOT / "monitor/accounts.json").read_bytes()),
        "runUrl": os.environ.get("AUDIT_RUN_URL", ""), "sites": [],
    }
    for site in plan["sites"]:
        entry = {"site": site["site"], "key": site["key"], "note": site.get("note", ""), "records": []}
        payload["sites"].append(entry)
        if not site.get("buildId"):
            continue
        secret = os.environ.get(site["secret"], "")
        if not secret:
            entry["note"] = "未配置本站 Secret"
            continue
        # 错误信息不能包含 Secret 本身或解析异常中的片段。
        try:
            auth = json.loads(secret)
            assert set(auth) == {site["key"]}
            assert set(auth[site["key"]]) == {"credentials"}
            credentials = auth[site["key"]]["credentials"]
            assert set(credentials) == {"username", "password"}
            assert all(isinstance(v, str) and v for v in credentials.values())
        except Exception:
            raise ValueError(f"{site['secret']} 格式不符合本站授权契约") from None
        item = items[site["buildId"]]
        data = audit.request(item["url"])
        if audit.sha(data) != item["sha256"]:
            raise ValueError("账号源源码哈希不匹配，停止执行")
        for profile in ("venerax", "venera-next"):
            latest = audit.run("git", "ls-remote", "https://github.com/Gandum2077/venera-patrol-cli.git",
                               "HEAD", capture_output=True, text=True).stdout.split()[0]
            if latest != metadata["commit"]:
                raise ValueError("本站巡检前 CLI 已更新，停止并重新获取最新版本")
            with tempfile.TemporaryDirectory(prefix="account-", dir=work) as private:
                private = Path(private)
                (private / "source.js").write_bytes(data)
                audit.save(private / "index.json", [{"key": item["key"], "fileName": "/private/source.js"}])
                audit.save(private / "config.json", {
                    "version": 1, "configPaths": ["/private/index.json"], "output": "/private/reports",
                    "defaults": {**audit.POLICY, "concurrency": 1, "sourceTimeoutMs": 120000},
                    "sources": {item["key"]: {
                        "auth": site["key"], "inputs": item["sample"], "settings": item.get("settings", {}),
                    }},
                })
                environment = {k: v for k, v in os.environ.items()
                               if not k.startswith("PATROL_AUTH") and k not in ("GH_TOKEN", "GITHUB_TOKEN")}
                environment["PATROL_AUTH"] = secret
                command = [
                    "docker", "run", "--rm", "--read-only", "--cap-drop=ALL",
                    "--security-opt=no-new-privileges", "--pids-limit=256", "--memory=3g", "--cpus=2",
                    "--user", f"{os.getuid()}:{os.getgid()}", "--env", "HOME=/tmp",
                    "--env", "PATROL_AUTH", "--env", f"VENERA_CLIENT_PROFILE={profile}",
                    "--tmpfs", "/tmp:rw,noexec,nosuid,size=1024m",
                    "--mount", f"type=bind,source={private},target=/private",
                    "--mount", f"type=bind,source={private / 'source.js'},target=/private/source.js,readonly",
                    metadata["image"], "check-all", "--config", "/private/config.json", "--no-env",
                ]
                # 社区代码的 stdout/stderr 可能包含私密数据，绝不转发给 Actions 日志。
                result = subprocess.run(command, env=environment, stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE, timeout=200, check=False)
                if result.returncode not in (0, 1):
                    raise ValueError("隔离账号巡检进程异常；原始输出已隐藏")
                reports = list((private / "reports").glob("*/report.json"))
                if len(reports) != 1:
                    raise ValueError("隔离账号巡检未生成唯一报告；原始输出已隐藏")
                report = audit.load(reports[0])
                assert report["schemaVersion"] == 1 and len(report["sources"]) == 1
                source = report["sources"][0]
                assert source["key"] == item["key"]
                if source.get("sourceSha256"):
                    assert source["sourceSha256"] == item["sha256"]
                record = {"id": item["id"], "runtimeProfile": profile,
                          "inputs": item["sample"], "source": source}
                audit.validate_client_record(record, item, {"cli": metadata})
                entry["records"].append(sanitized(record))
            print(f"账号巡检完成：{site['site']}／{profile}；私有运行目录已清理。", flush=True)
    payload["checkedAt"] = datetime.now(timezone.utc).isoformat()
    render(payload, work / "account-artifact")


def publish(path):
    payload = audit.load(path)
    catalog = audit.validate_catalog(audit.load(ROOT / "monitor/catalog.json"))
    plan = validate_plan(audit.load(ROOT / "monitor/accounts.json"), catalog)
    assert payload["schemaVersion"] == 1
    assert payload["catalogSha256"] == audit.sha((ROOT / "monitor/catalog.json").read_bytes())
    assert payload["accountPlanSha256"] == audit.sha((ROOT / "monitor/accounts.json").read_bytes())
    assert [(e["site"], e["key"]) for e in payload["sites"]] == [
        (s["site"], s["key"]) for s in plan["sites"]]
    items = {i["id"]: i for i in catalog["sources"]}
    for site, expected in zip(payload["sites"], plan["sites"], strict=True):
        assert len(site["records"]) in (0, 2)
        for record in site["records"]:
            assert record["id"] == expected["buildId"]
            assert record["inputs"] == items[record["id"]]["sample"]
            assert record == sanitized(record), "账号产物包含未允许字段"
    render(payload, ROOT)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["patrol", "publish"])
    parser.add_argument("--work", type=Path)
    parser.add_argument("--input", type=Path)
    args = parser.parse_args()
    if args.command == "patrol":
        patrol(args.work.resolve())
    else:
        publish(args.input)
