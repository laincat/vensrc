import copy
from pathlib import Path
import unittest

import account_patrol as accounts
import cloud_audit as audit


class WnacgPolicyTests(unittest.TestCase):
    def test_only_dedicated_source_remains_and_hash_matches_local_code(self):
        catalog = audit.validate_catalog(audit.load(audit.ROOT / "monitor/catalog.json"))
        sources = [item for item in catalog["sources"] if item["key"] == "wnacg"]
        self.assertEqual(len(sources), 1)
        item = sources[0]
        self.assertEqual(item["repository"], "laincat/vensrc")
        self.assertEqual(item["sha256"], audit.sha((audit.ROOT / "sources/wnacg.js").read_bytes()))
        self.assertEqual(item["sample"], {"comicId": "397513", "keyword": "火影"})
        self.assertEqual(item["minAppVersion"], "1.3.4")
        self.assertFalse(audit.excluded_official(item, audit.official_policy()))
        plan = accounts.validate_plan(audit.load(audit.ROOT / "monitor/accounts.json"), catalog)
        site = next(site for site in plan["sites"] if site["key"] == "wnacg")
        self.assertEqual(site["buildId"], item["id"])
        self.assertEqual(site["authMode"], "browser_cookie")
        self.assertNotIn("PATROL_AUTH_WNACG:", (
            audit.ROOT / ".github/workflows/patrol.yml").read_text(encoding="utf-8"))

    def test_other_wnacg_names_keys_and_origins_cannot_reenter_catalog(self):
        catalog = audit.load(audit.ROOT / "monitor/catalog.json")
        original = next(item for item in catalog["sources"] if item["key"] == "wnacg")
        for changes in (
            {"repository": "other/source"},
            {"key": "hj_wnacg", "repository": "other/source"},
            {"name": "紳士漫畫·国内直连", "key": "another_key", "fileName": "another.js"},
            {"name": "绅士漫画", "key": "another_key"},
            {"url": "https://raw.githubusercontent.com/other/source/" + "a" * 40 + "/wnacg.js"},
        ):
            item = {**original, **changes}
            self.assertTrue(audit.excluded_wnacg(item))
            altered = copy.deepcopy(catalog)
            altered["sources"] = [item]
            with self.assertRaisesRegex(AssertionError, "只允许"):
                audit.validate_catalog(altered)
        self.assertFalse(audit.excluded_wnacg({
            "key": "unrelated", "name": "绅士会所", "repository": "other/source"}))

    def test_release_lock_can_identify_dedicated_source_without_repository_field(self):
        item = next(item for item in audit.load(
            audit.ROOT / "monitor/catalog.json")["sources"] if item["key"] == "wnacg")
        lock = {key: value for key, value in item.items() if key != "repository"}
        self.assertFalse(audit.excluded_wnacg(lock))
        with self.assertRaisesRegex(AssertionError, "只允许"):
            audit.validate_catalog({"schemaVersion": 1, "sources": [lock],
                                    "priorityRepositories": []})


if __name__ == "__main__":
    unittest.main()
