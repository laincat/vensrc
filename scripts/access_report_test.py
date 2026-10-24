import json
from pathlib import Path
import tempfile
import unittest

import access_report as access
import cloud_audit as audit


class AccessReportTests(unittest.TestCase):
    def test_access_failures_do_not_change_subscription_status(self):
        catalog = audit.load(access.ROOT / "monitor/catalog.json")
        item = catalog["sources"][0]
        payload = {
            "checkedAt": "2026-10-24T00:00:00+00:00",
            "cli": {"commit": "a" * 40},
            "catalogSha256": audit.sha((access.ROOT / "monitor/catalog.json").read_bytes()),
            "records": [{
                "id": item["id"], "runtimeProfile": "venerax",
                "source": {"stages": [{
                    "path": "search.load", "status": "failed", "category": "anti_bot",
                    "reason": "fixture-private-text",
                }]},
            }],
        }
        result = access.collect(payload)
        self.assertEqual(result["rows"][0]["failures"][0]["category"], "anti_bot")
        self.assertNotIn("fixture-private-text", json.dumps(result))
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            access.publish(result, target)
            self.assertEqual(set(str(p.relative_to(target)).replace("\\", "/") for p in target.rglob("*") if p.is_file()),
                             {"reports/ACCESS_RESULTS.md", "data/access-results.json"})

    def test_browser_results_cannot_inject_other_origins(self):
        payload = {"checkedAt": "2026-10-24", "rows": []}
        browser = {"schemaVersion": 1, "results": [{
            "key": "rawkuma", "origin": "https://wrong.invalid", "status": "browser_accessible",
        }]}
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(AssertionError):
                access.publish(payload, Path(directory), browser)

    def test_manual_verification_is_separate_from_http_rejection(self):
        payload = {"checkedAt": "2026-10-24", "rows": [{
            "name": "fixture", "key": "rawkuma", "version": "1", "repository": "fixture/repo",
            "runtimeProfile": "venerax", "corePassed": False,
            "failures": [
                {"stage": "search.load", "category": "auth_required"},
                {"stage": "comic.loadInfo", "category": "anti_bot"},
            ],
        }]}
        browser = {"schemaVersion": 1, "results": [
            {"key": "rawkuma", "origin": "https://rawkuma.net", "status": "manual_verification_required"},
            {"key": "nhentai", "origin": "https://nhentai.net", "status": "http_blocked"},
        ]}
        with tempfile.TemporaryDirectory() as directory:
            access.publish(payload, Path(directory), browser)
            report = (Path(directory) / "reports/ACCESS_RESULTS.md").read_text(encoding="utf-8")
            manual = report.split("## 需要本人验证的站点")[1].split("## 逐构建处理清单")[0]
            self.assertIn("rawkuma", manual)
            self.assertNotIn("nhentai", manual)
            self.assertIn("search.load；comic.loadInfo", report)

    def test_accessible_login_page_with_slider_does_not_mean_login_passed(self):
        payload = {"checkedAt": "2026-10-24", "rows": []}
        result = {
            "key": "wnacg", "origin": "https://www.wnacg.com",
            "page": "https://www.wnacg.com/users-login.html",
            "status": "browser_accessible", "loginInteractionObserved": True,
        }
        browser = {"schemaVersion": 1, "results": [result]}
        with tempfile.TemporaryDirectory() as directory:
            access.publish(payload, Path(directory), browser)
            report = (Path(directory) / "reports/ACCESS_RESULTS.md").read_text(encoding="utf-8")
            self.assertIn("登录页加载滑块验证模块", report)
            self.assertIn("未执行账号登录", report)
            self.assertIn("不表示登录成功", report)
            result["page"] = "https://www.wnacg.com/users-delete.html"
            with self.assertRaises(AssertionError):
                access.publish(payload, Path(directory), browser)
