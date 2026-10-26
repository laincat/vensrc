import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import cloud_audit as audit


class OfficialPolicyTests(unittest.TestCase):
    def test_source_budget_can_only_increase_resources_without_changing_reading_checks(self):
        item = {"patrolPolicy": {"maxRequests": 300, "sourceTimeoutMs": 300000}}
        policy = audit.execution_policy(item)
        self.assertEqual(policy["maxRequests"], 300)
        self.assertEqual(policy["imageSamples"], audit.POLICY["imageSamples"])
        self.assertEqual(audit.execution_policy({}), audit.POLICY)
        for overrides in ({"imageSamples": 0}, {"maxRequests": 1}, {"maxRequests": 501},
                          {"maxRequests": True}, {"stageTimeoutMs": 60001}):
            with self.subTest(overrides=overrides), self.assertRaises(AssertionError):
                audit.execution_policy({"patrolPolicy": overrides})

    def test_refresh_keeps_historical_keys_and_adds_new_official_keys(self):
        baseline = audit.official_policy()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            audit.save(root / "monitor/official-keys.json", baseline)
            audit.save(root / "monitor/source-notes.json", {"schemaVersion": 1, "notes": {}})
            previous = {**baseline, "keys": sorted(baseline["keys"] + ["historical_fixture"]),
                        "versions": {**baseline["versions"], "historical_fixture": "2.0.0"}}
            audit.save(root / "data/official-exclusions.json", previous)
            raw = b'[{"key":"new_official_fixture","version":"1.0.0"},{"key":"historical_fixture","version":"1.0.0"}]'
            with patch.object(audit, "request", side_effect=[
                json.dumps({"sha": "b" * 40}).encode(), raw,
            ]):
                refreshed = audit.refresh_official_policy(root)
            self.assertEqual(refreshed["indexSha256"], audit.sha(raw))
            self.assertTrue(set(baseline["keys"]) | {"historical_fixture", "new_official_fixture"}
                            <= set(refreshed["keys"]))
            self.assertEqual(refreshed["versions"]["historical_fixture"], "2.0.0")
            with self.assertRaisesRegex(AssertionError, "不得缩小"):
                audit.official_policy(root, {
                    **refreshed, "keys": ["new_official_fixture"],
                    "versions": {"new_official_fixture": "1.0.0"},
                })
            with self.assertRaisesRegex(AssertionError, "不得降低"):
                audit.official_policy(root, {
                    **refreshed, "versions": {**refreshed["versions"], "historical_fixture": "1.0.0"},
                })

    def test_community_same_key_must_be_strictly_newer_and_official_origin_stays_excluded(self):
        policy = {"versions": {"jm": "1.4.0"}}
        for version, excluded in (
            ("1.3.9", True), ("1.4.0", True), ("1.4.1", False), ("1.9.2", False),
            ("1.10.0", False), ("1.4.1-beta", True), ("unknown", True), (None, True),
        ):
            with self.subTest(version=version):
                item = {"key": "jm", "version": version,
                        "repository": "BB-CHICKEN/venera-jm", "officialKey": True}
                self.assertEqual(audit.excluded_official(item, policy), excluded)
        self.assertFalse(audit.excluded_official(
            {"key": "jm", "version": "1.10.0"}, {"versions": {"jm": "1.9.9"}}))
        self.assertTrue(audit.excluded_official({
            "key": "jm", "version": "9.0.0", "repository": audit.OFFICIAL_REPOSITORY,
        }, policy))
        self.assertTrue(audit.excluded_official({
            "key": "jm", "version": "9.0.0",
            "url": f"https://raw.githubusercontent.com/{audit.OFFICIAL_REPOSITORY}/main/jm.js",
        }, policy))

    def test_generator_excludes_official_keys_and_origins_but_keeps_community_evidence(self):
        baseline = audit.official_policy()
        stages = [{"path": path, "status": "passed"} for path in (
            "source.load", "search.load", "comic.loadInfo", "comic.loadEp",
            "image.download", "image.decode",
        )]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            audit.save(root / "monitor/official-keys.json", baseline)
            items = []
            for number, key, repo in (
                ("a", "fixture", "community/source"),
                ("b", "jm", "BB-CHICKEN/venera-jm"),
                ("c", "renamed_official_fixture", audit.OFFICIAL_REPOSITORY),
            ):
                items.append({
                    "id": number * 64, "sha256": number * 64, "key": key, "name": key,
                    "repository": repo, "version": "1.0.0", "fileName": key + ".js",
                    "url": f"https://raw.githubusercontent.com/{repo}/" + "d" * 40 + f"/{key}.js",
                    "minAppVersion": "1.0.0", "sample": {"comicId": "1", "epId": "2"},
                })
            audit.save(root / "monitor/catalog.json", {
                "schemaVersion": 1, "sources": items, "priorityRepositories": []})
            audit.save(root / "monitor/source-notes.json", {
                "schemaVersion": 1, "notes": {
                    "b" * 64: "上游 CHANGELOG v1.9.2：“修复旧版收藏数据 id 未去混淆导致的 aid 错误”。",
                },
            })
            audit.save(root / "data/sources.lock.json", [])
            payload = {
                "schemaVersion": 1,
                "catalogSha256": audit.sha((root / "monitor/catalog.json").read_bytes()),
                "checkedAt": "2026-10-24T00:00:00+00:00",
                "cli": {"commit": "e" * 40, "version": "fixture", "packageLockSha256": "f" * 64},
                "records": [{
                    "id": item["id"], "source": {
                        "key": item["key"], "sourceSha256": item["sha256"],
                        "status": "passed", "stages": stages,
                    },
                } for item in items],
            }
            with patch.object(audit, "ROOT", root):
                audit.publish(payload, root)
            index = audit.load(root / "subscriptions/index.json")
            self.assertEqual([item["key"] for item in index], ["fixture"])
            self.assertEqual(index[0]["description"], "引用源：community/source")
            self.assertEqual([item["key"] for item in audit.load(root / "data/sources.lock.json")], ["fixture"])
            self.assertEqual(audit.load(root / "data/audit-status.json")["officialExcludedBuilds"], 2)
            self.assertEqual(len(payload["records"]), 3)
            report = (root / "reports/RESULTS.md").read_text(encoding="utf-8")
            self.assertIn("排除官方原版／未高于官方版本", report)
            self.assertIn("修复旧版收藏数据 id 未去混淆导致的 aid 错误", report)
            rows = list(__import__("csv").reader(
                (root / "data/sources.zh.csv").read_text(encoding="utf-8-sig").splitlines()))
            self.assertEqual(rows[0][-1], "源备注")
            self.assertIn("上游 CHANGELOG v1.9.2", rows[2][-1])

            # A passing old/equal version must not mask an eligible partial newer build.
            items[1]["version"] = "1.9.2"
            items[1]["settings"] = {"dailyCheckInTask": False}
            items.append({**items[1], "id": "d" * 64, "sha256": "d" * 64,
                          "repository": "other/community", "priority": 1000, "version": "1.4.0"})
            payload["records"][1]["source"] = {
                **payload["records"][1]["source"], "status": "partial", "version": "1.9.2",
                "stages": stages + [{"path": "account.login", "status": "skipped",
                                    "category": "credentials_missing"}],
            }
            payload["records"].append({
                "id": items[-1]["id"], "source": {
                    "key": "jm", "sourceSha256": items[-1]["sha256"],
                    "status": "passed", "stages": stages,
                },
            })
            audit.save(root / "monitor/catalog.json", {
                "schemaVersion": 1, "sources": items, "priorityRepositories": []})
            payload["catalogSha256"] = audit.sha((root / "monitor/catalog.json").read_bytes())
            with patch.object(audit, "ROOT", root):
                audit.publish(payload, root)
            extended = audit.load(root / "subscriptions/extended.json")
            self.assertEqual([(row["key"], row["version"]) for row in extended], [("jm", "1.9.2")])
            lock = next(row for row in audit.load(root / "data/sources.lock.json") if row["key"] == "jm")
            self.assertEqual(lock["officialVersion"], baseline["versions"]["jm"])
            self.assertEqual(lock["buildId"], "b" * 64)
            self.assertEqual(audit.load(root / "data/audit-status.json")["officialOverrides"], 1)

    def test_discovery_uses_actual_source_key_and_omits_official_candidates(self):
        baseline = audit.official_policy()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            audit.save(root / "monitor/official-keys.json", baseline)
            audit.save(root / "monitor/catalog.json", {
                "schemaVersion": 1, "sources": [], "priorityRepositories": []})
            audit.save(root / "monitor/upstreams.json", {
                "repositories": ["community/source", audit.OFFICIAL_REPOSITORY],
                "priorityRepositories": [],
            })
            urls = []
            def request(url, api=False):
                urls.append(url)
                if "/commits" in url:
                    return b'[{"sha":"' + b"a" * 40 + b'"}]'
                if "/search/repositories" in url:
                    return json.dumps({"items": [
                        {"full_name": audit.OFFICIAL_REPOSITORY},
                        {"full_name": "new/community", "description": "fixture"},
                    ]}).encode()
                if url.endswith("/index.json"):
                    return json.dumps([
                        {"name": "actual key", "key": "jm", "fileName": "renamed.js"},
                        {"name": "official key", "key": "jm", "fileName": "official.js"},
                        {"name": "official origin", "key": "other", "fileName": "other.js",
                         "url": f"https://cdn.jsdelivr.net/gh/{audit.OFFICIAL_REPOSITORY}@main/other.js"},
                    ]).encode()
                return (b'key = "fixture_new"\nversion = "1.0.0"\n'
                        if url.endswith("/renamed.js") else b'key = "jm"\nversion = "1.0.0"\n')
            with patch.object(audit, "ROOT", root), \
                    patch.object(audit, "refresh_official_policy", return_value=baseline), \
                    patch.object(audit, "request", side_effect=request):
                audit.discover(root / "work")
            result = audit.load(root / "work/artifact/discovery.json")
            self.assertEqual([item["key"] for item in result["updates"]], ["fixture_new"])
            self.assertEqual([item["repository"] for item in result["repositories"]], ["community/source"])
            self.assertEqual([item["repository"] for item in result["newRepositories"]], ["new/community"])
            self.assertFalse(any(audit.OFFICIAL_REPOSITORY in url for url in urls))

    def test_single_file_discovery_pins_source_metadata_without_executing(self):
        baseline = audit.official_policy()
        code = ('class Fixture {\nname = "栗子漫画"\nkey = "lizimh"\n'
                'version = "2.33.27"\nminAppVersion = "1.2.2"\n}').encode()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            audit.save(root / "monitor/catalog.json", {
                "schemaVersion": 1, "sources": [], "priorityRepositories": []})
            audit.save(root / "monitor/upstreams.json", {
                "repositories": ["Walter498/Walter"], "priorityRepositories": [],
                "files": {"Walter498/Walter": ["lizimh.js"]},
            })
            urls = []

            def request(url, api=False):
                urls.append(url)
                if "/commits" in url:
                    return json.dumps([{"sha": "a" * 40}]).encode()
                if "/search/repositories" in url:
                    return b'{"items":[]}'
                self.assertTrue(url.endswith("/" + "a" * 40 + "/lizimh.js"))
                return code

            with patch.object(audit, "ROOT", root), \
                    patch.object(audit, "refresh_official_policy", return_value=baseline), \
                    patch.object(audit, "request", side_effect=request):
                audit.discover(root / "work")
            result = audit.load(root / "work/artifact/discovery.json")
            item, = result["updates"]
            self.assertEqual((item["name"], item["key"], item["version"], item["minAppVersion"]),
                             ("栗子漫画", "lizimh", "2.33.27", "1.2.2"))
            self.assertEqual(item["sha256"], audit.sha(code))
            self.assertTrue(audit.pinned(item["url"]))
            self.assertIn("未加载、未执行", item["state"])
            self.assertFalse(any(url.endswith("/index.json") for url in urls))
            self.assertEqual(audit.load(root / "monitor/catalog.json")["sources"], [])


if __name__ == "__main__":
    unittest.main()
