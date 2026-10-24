import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import cloud_audit as audit


class OfficialPolicyTests(unittest.TestCase):
    def test_refresh_keeps_historical_keys_and_adds_new_official_keys(self):
        baseline = audit.official_policy()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            audit.save(root / "monitor/official-keys.json", baseline)
            audit.save(root / "monitor/source-notes.json", {"schemaVersion": 1, "notes": {}})
            previous = {**baseline, "keys": sorted(baseline["keys"] + ["historical_fixture"])}
            audit.save(root / "official-exclusions.json", previous)
            raw = b'[{"key":"new_official_fixture"}]'
            with patch.object(audit, "request", side_effect=[
                json.dumps({"sha": "b" * 40}).encode(), raw,
            ]):
                refreshed = audit.refresh_official_policy(root)
            self.assertEqual(refreshed["indexSha256"], audit.sha(raw))
            self.assertTrue(set(baseline["keys"]) | {"historical_fixture", "new_official_fixture"}
                            <= set(refreshed["keys"]))
            with self.assertRaisesRegex(AssertionError, "不得缩小"):
                audit.official_policy(root, {**refreshed, "keys": ["new_official_fixture"]})

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
            audit.save(root / "sources.lock.json", [])
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
            index = audit.load(root / "index.json")
            self.assertEqual([item["key"] for item in index], ["fixture"])
            self.assertEqual(index[0]["description"], "引用源：community/source")
            self.assertEqual([item["key"] for item in audit.load(root / "sources.lock.json")], ["fixture"])
            self.assertEqual(audit.load(root / "audit-status.json")["officialExcludedBuilds"], 2)
            self.assertEqual(len(payload["records"]), 3)
            report = (root / "RESULTS.md").read_text(encoding="utf-8")
            self.assertIn("排除官方重复项", report)
            self.assertIn("修复旧版收藏数据 id 未去混淆导致的 aid 错误", report)
            rows = list(__import__("csv").reader(
                (root / "sources.zh.csv").read_text(encoding="utf-8-sig").splitlines()))
            self.assertEqual(rows[0][-1], "源备注")
            self.assertIn("上游 CHANGELOG v1.9.2", rows[2][-1])

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


if __name__ == "__main__":
    unittest.main()
