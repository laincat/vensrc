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
            self.assertEqual(set(p.name for p in target.iterdir()), {"ACCESS_RESULTS.md", "access-results.json"})

    def test_browser_results_cannot_inject_other_origins(self):
        payload = {"checkedAt": "2026-10-24", "rows": []}
        browser = {"schemaVersion": 1, "results": [{
            "key": "rawkuma", "origin": "https://wrong.invalid", "status": "browser_accessible",
        }]}
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(AssertionError):
                access.publish(payload, Path(directory), browser)
