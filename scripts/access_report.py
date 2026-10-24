"""基于真实阶段生成反爬／人工处理清单；浏览器诊断不能改变订阅资格。"""

import argparse
import json
import os
from pathlib import Path
import re

import cloud_audit as audit

ROOT = Path(__file__).resolve().parents[1]
BROWSER_LABELS = {
    "browser_accessible": "浏览器可取得页面",
    "manual_verification_required": "仍需人工验证",
    "http_blocked": "浏览器也被 HTTP 拒绝",
    "content_unconfirmed": "未确认取得正常内容",
    "network_failed": "浏览器网络失败",
    "redirect_unconfirmed": "跳转到其他站点，未认定可用",
}


def collect(payload):
    catalog = audit.load(ROOT / "monitor/catalog.json")
    assert payload["catalogSha256"] == audit.sha((ROOT / "monitor/catalog.json").read_bytes())
    items = {i["id"]: i for i in catalog["sources"]}
    rows = []
    for record in payload["records"] + payload.get("clientRecords", []):
        item = items[record["id"]]
        failures = [s for s in record["source"]["stages"] if s["status"] == "failed" and
                    s.get("category") in ("anti_bot", "rate_limited", "region_restricted", "auth_required")]
        if failures:
            # 仅使用受信任标识与固定类别，不复制异常原文或网络 URL。
            rows.append({
                "id": item["id"], "key": item["key"], "name": item["name"],
                "repository": item["repository"], "version": item["version"],
                "runtimeProfile": record["runtimeProfile"],
                "corePassed": audit.core(record["source"]),
                "failures": [{"stage": s["path"], "category": s["category"]} for s in failures],
            })
    return {
        "schemaVersion": 1, "checkedAt": payload["checkedAt"], "cli": payload["cli"],
        "catalogSha256": payload["catalogSha256"], "rows": rows,
        "patrolRunUrl": os.environ.get("PATROL_RUN_URL", payload.get("runUrl", "")),
    }


def publish(payload, destination, browser=None):
    browser = browser or {"schemaVersion": 1, "results": []}
    assert browser["schemaVersion"] == 1
    if browser.get("browserCliCommit"):
        assert re.fullmatch(r"[a-f0-9]{40}", browser["browserCliCommit"])
    allowed = {i["key"]: i["url"].rstrip("/") for i in audit.load(
        ROOT / "monitor/access-targets.json")["targets"]}
    for result in browser["results"]:
        assert result["key"] in allowed and result["origin"] == allowed[result["key"]]
        assert result["status"] in BROWSER_LABELS
        assert set(result) <= {"key", "origin", "status", "httpStatus", "cloudflareHeaderObserved"}
    payload = {**payload, "browser": browser["results"],
               "browserCliCommit": browser.get("browserCliCommit"),
               "diagnosticRunUrl": os.environ.get("AUDIT_RUN_URL", "")}
    destination.mkdir(parents=True, exist_ok=True)
    audit.save(destination / "access-results.json", payload)
    lines = [
        "# 反爬、网络限制与人工处理清单", "",
        f"来源巡检时间：{payload['checkedAt']}（UTC）。",
        "anti_bot 表示检测到人机验证或反爬特征，未单凭 403 就认定 Cloudflare。",
        "auth_required 也可能是权限、地区或站点拒绝，不能据此认定密码错误。",
        "正常浏览器可访问不代表 CLI 阅读链路通过，本报告不修改主／扩展订阅。", "",
        "## 处理顺序", "",
        "1. 先使用源已提供的公开 API、域名刷新及正常请求头，避免重复登录或高频重试。",
        "2. VeneraX 出现验证窗口时，在该窗口完成正常验证；验证后保持相同网络及浏览器身份再重试。",
        "3. 需要点击、人机题或二步验证时由本人处理；不配置验证码代解服务。",
        "4. GitHub runner 无法复用本机浏览器身份。若云端持续受限，需要站点允许的访问方式、站点监控白名单，或独立且出口稳定的远程验证环境；不会假报通过。",
        "5. 429 应降低请求频率并尊重 Retry-After；地区限制与账号权限单独核对。", "",
        "## 正常浏览器对照", "",
        "仅对已审阅的公开站点首页做无账号诊断；不提交密码、不提取或发布 Cookie。",
        "Actions 使用无界面 Chromium；其 IP、浏览器身份和 VeneraX WebView 不同，结果分别记录。",
        "| key | 公开站点 | 浏览器结果 | 观察到 CF challenge 响应头 |",
        "| --- | --- | --- | --- |",
    ]
    for result in browser["results"]:
        lines.append("| " + " | ".join(audit.text(v) for v in (
            result["key"], result["origin"], BROWSER_LABELS[result["status"]],
            "是" if result.get("cloudflareHeaderObserved") else "否／未观察到")) + " |")
    manual_browser = [r for r in browser["results"] if r["status"] == "manual_verification_required"]
    anti_bot_keys = sorted({r["key"] for r in payload["rows"]
                            if any(f["category"] == "anti_bot" for f in r["failures"])})
    lines += ["", "## 需要本人验证的站点", ""]
    lines += [
        f"- `{r['key']}`（{r['origin']}）：Actions 正常浏览器等待后仍出现验证，需本人在 VeneraX 验证窗口处理并在同环境重试。"
        for r in manual_browser
    ] or ["本轮已诊断首页没有确认仍停留在人工验证的站点；网络失败和普通 HTTP 拒绝仍未验证。"]
    if anti_bot_keys:
        lines += ["", "CLI 检测到反爬的源 key：" + "、".join(f"`{audit.text(k)}`" for k in anti_bot_keys) + "。",
                  "未纳入首页浏览器对照的源仍未完成人工验证；首页诊断成功也不代表正文接口通过。"]
    lines += ["", "## 逐构建处理清单", "",
              "| 名称 | key | 版本 | 仓库 | 环境 | 核心阅读 | 受限阶段 | 类别／处理 |",
              "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    actions = {
        "anti_bot": "人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试",
        "rate_limited": "限流：降低频率并按站点要求延迟",
        "region_restricted": "地区限制：核对站点允许的访问地区",
        "auth_required": "权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误",
    }
    for row in payload["rows"]:
        lines.append("| " + " | ".join(audit.text(v) for v in (
            row["name"], row["key"], row["version"], row["repository"], row["runtimeProfile"],
            "通过（其他能力受限）" if row["corePassed"] else "未通过",
            "；".join(f["stage"] for f in row["failures"]),
            "；".join(actions[c] for c in dict.fromkeys(f["category"] for f in row["failures"])))) + " |")
    lines += ["", "## 依据与边界", "",
              "- VeneraX 固定源码：`lib/network/cloudflare.dart`；其验证窗口、Cookie 和请求头处理属于 Flutter 宿主，Node CLI 不具备相同的交互环境。",
              "- [Cloudflare 官方识别方法](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/detect-response/)：`cf-mitigated: challenge` 可确认挑战响应。",
              "- [Cloudflare 官方通行说明](https://developers.cloudflare.com/cloudflare-challenges/concepts/clearance/)：通行 Cookie 绑定访问者和设备，不能保证跨机器复用。",
              "- [挑战限制](https://developers.cloudflare.com/cloudflare-challenges/concepts/how-challenges-work/)：不同 IP 发起挑战和完成验证可能导致循环。",
              "", f"浏览器诊断 Actions：{payload['diagnosticRunUrl']}", ""]
    (destination / "ACCESS_RESULTS.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["collect", "publish"])
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("."))
    parser.add_argument("--browser", type=Path)
    args = parser.parse_args()
    if args.command == "collect":
        audit.save(args.output, collect(audit.load(args.input)))
    else:
        publish(audit.load(args.input), args.output,
                audit.load(args.browser) if args.browser else None)
