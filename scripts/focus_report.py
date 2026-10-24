"""汇总固定的社区升级构建和三个自用仓库；账号结果必须匹配同轮、同构建。"""

from pathlib import Path

import cloud_audit as audit
from account_patrol import login_stage

ROOT = Path(__file__).resolve().parents[1]


def login_label(records, build_id, profile):
    record = records.get((build_id, profile))
    if record is None:
        return "未对该构建执行账号巡检"
    stage = login_stage(record["source"])
    stages = [stage] if stage else []
    if not stages:
        return "登录未执行"
    if all(s["status"] in ("passed", "recovered") for s in stages):
        return "通过"
    return "；".join(audit.LABELS.get(s["status"], s["status"]) +
                    ("／" + audit.CATEGORIES.get(s["category"], s["category"])
                     if s.get("category") else "") for s in stages)


def publish(root):
    catalog = audit.load(root / "monitor/catalog.json")
    config = audit.load(root / "monitor/focus.json")
    assert config["schemaVersion"] == 1
    items = {item["id"]: item for item in catalog["sources"]}
    assert len(set(config["buildIds"])) == len(config["buildIds"])
    assert set(config["buildIds"]) <= items.keys()
    clients = audit.load(root / "data/client-results.json")
    accounts = audit.load(root / "data/account-results.json")
    state = audit.load(root / "data/audit-status.json")
    assert clients["runUrl"] == accounts["runUrl"] == state["runUrl"]
    assert clients["cli"]["commit"] == accounts["cli"]["commit"] == state["cli"]["commit"]
    assert accounts["catalogSha256"] == state["catalogSha256"] == audit.sha(
        (root / "monitor/catalog.json").read_bytes())
    records = {(r["id"], r["runtimeProfile"]): r for r in clients["records"]}
    auth = {(r["id"], r["runtimeProfile"]): r
            for site in accounts["sites"] for r in site.get("records", [])}
    locks = {r["buildId"]: r for r in audit.load(root / "data/sources.lock.json")}
    policy = audit.official_policy(root)
    lines = [
        "# 社区替代源与自用仓库重点复测", "",
        f"核验时间：{state['checkedAt']}（UTC）；CLI：`{state['cli']['commit']}`。",
        "VeneraX 为订阅依据，Venera-Next 单独对照；固定样本、最低应用版本与源码哈希保持不变。",
        "表内“核心／整次”分别表示阅读链路和报告总状态。登录只采用完全相同构建的独立账号任务证据。",
        "未执行、跳过、缺少凭据和未触发回调均不计通过；两边分时执行的差异也可能来自源站或网络。", "",
    ]

    def table(builds):
        lines.extend([
            "| key | 版本／官方基线 | 来源仓库 | 订阅 | VeneraX 核心／整次 | Next 核心／整次 | X 登录 | Next 登录 |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |",
        ])
        for item in builds:
            cells = []
            for profile in ("venerax", "venera-next"):
                source = records[(item["id"], profile)]["source"]
                cells.append(("通过" if audit.core(source) else "未通过") +
                             "／" + audit.LABELS[source["status"]])
            locked = locks.get(item["id"])
            channel = ("主订阅" if locked["channel"] == "main" else "扩展订阅") if locked else "未收录"
            lines.append("| " + " | ".join(audit.text(v) for v in (
                item["key"], item["version"] + "／" + policy["versions"].get(item["key"], "无"),
                item["repository"], channel, *cells,
                *(login_label(auth, item["id"], profile) for profile in ("venerax", "venera-next")),
            )) + " |")
        lines.append("")

    lines += ["## 七个社区替代构建", "",
              "固定跟踪原先恢复的七个构建；本轮失败或未被选中时仍在此列出，不以其他版本替换证据。", ""]
    table([items[build_id] for build_id in config["buildIds"]])
    for repository in catalog["priorityRepositories"]:
        lines += [f"## {repository}", ""]
        table([item for item in items.values() if repository in item.get("trackedBy", [])])
    lines += [
        "## 完整证据", "",
        "- [客户端逐阶段对照](CLIENT_RESULTS.md)",
        "- [账号登录失败、未验证与跳过项](ACCOUNT_RESULTS.md)",
        "- [反爬与人工验证](ACCESS_RESULTS.md)",
        "- [源码哈希及固定样本](../data/sources.lock.json)",
        "- [全部已审阅构建](../monitor/catalog.json)", "",
        f"巡检 Actions：{state['runUrl']}", "",
    ]
    (root / "reports").mkdir(parents=True, exist_ok=True)
    (root / "reports/FOCUS_RESULTS.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    publish(ROOT)
