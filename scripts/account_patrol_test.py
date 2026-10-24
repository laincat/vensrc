import json
import unittest

import account_patrol as accounts
import cloud_audit as audit


class AccountIsolationTests(unittest.TestCase):
    def test_private_output_and_errors_are_removed(self):
        private = "fixture-private-value"
        record = {
            "id": "a" * 64, "runtimeProfile": "venerax", "inputs": {"keyword": "漫画"},
            "source": {
                "key": "fixture", "sourceSha256": "a" * 64, "status": "failed",
                "traceFile": private, "data": {"password": private},
                "stages": [{
                    "path": "account.login", "status": "failed", "category": "auth_required",
                    "durationMs": 1, "reason": private, "output": {"value": private},
                }],
            },
        }
        clean = accounts.sanitized(record)
        self.assertNotIn(private, json.dumps(clean))
        self.assertEqual(clean, accounts.sanitized(clean))
        self.assertEqual(clean["source"]["stages"][0]["status"], "failed")

    def test_account_whitelist_is_bound_to_reviewed_source_hash(self):
        catalog = audit.load(accounts.ROOT / "monitor/catalog.json")
        plan = audit.load(accounts.ROOT / "monitor/accounts.json")
        accounts.validate_plan(plan, catalog)
        altered = json.loads(json.dumps(plan))
        site = next(s for s in altered["sites"] if s.get("buildId"))
        site["key"] = "wrong_site"
        with self.assertRaises(AssertionError):
            accounts.validate_plan(altered, catalog)

    def test_all_catalog_sources_have_both_client_profiles(self):
        catalog = audit.load(accounts.ROOT / "monitor/catalog.json")
        for item in catalog["sources"]:
            self.assertEqual(item["runtimeProfile"], "venerax")
            self.assertEqual(item["verifyProfiles"], ["venera-next"])


if __name__ == "__main__":
    unittest.main()
