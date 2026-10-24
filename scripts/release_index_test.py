import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile

import cloud_audit as audit
import release_index as release


def fixture(root):
    item = {
        "id": "a" * 64, "sha256": "a" * 64, "key": "fixture", "name": "测试源",
        "url": "https://raw.githubusercontent.com/example/source/" + "b" * 40 + "/fixture.js",
        "repository": "example/source",
        "version": "1.0.0", "fileName": "fixture.js", "minAppVersion": "1.0.0",
        "sample": {"comicId": "1", "epId": "2", "keyword": "测试"},
        "runtimeProfile": "venerax", "verifyProfiles": ["venera-next"],
    }
    catalog = {"schemaVersion": 1, "priorityRepositories": [], "sources": [item]}
    audit.save(root / "monitor/catalog.json", catalog)
    audit.save(root / "monitor/accounts.json", {"schemaVersion": 1, "sites": []})
    audit.save(root / "monitor/source-notes.json", {"schemaVersion": 1, "notes": {}})
    exclusions = audit.load(audit.ROOT / "monitor/official-keys.json")
    audit.save(root / "monitor/official-keys.json", exclusions)
    audit.save(root / "official-exclusions.json", exclusions)
    profiles = audit.load(audit.ROOT / "monitor/clients.json")["profiles"]
    cli = {
        "commit": "c" * 40, "clientProfiles": profiles,
        "adapterSha256": {name: audit.sha((audit.ROOT / name).read_bytes()) for name in (
            "scripts/client_bridge.mjs", "scripts/prepare_client.py", "monitor/clients.json")},
    }
    run = "https://github.com/example/source/actions/runs/1"
    checked = "2026-10-24T00:00:00+00:00"
    records = []
    for name, profile in profiles.items():
        identity = {k: profile[k] for k in ("repository", "commit", "version", "scope")}
        identity.update(name=name, bootstrapSha256=profile["files"]["assets/init.js"])
        stages = [{"path": "runtime.load", "status": "passed",
                   "output": {"value": json.dumps(identity)}}]
        stages += [{"path": path, "status": "passed"} for path in (
            "source.load", "search.load", "comic.loadInfo", "comic.loadEp", "image.download", "image.decode"
        )]
        records.append({
            "id": item["id"], "runtimeProfile": name, "inputs": item["sample"],
            "source": {"key": item["key"], "sourceSha256": item["sha256"],
                       "status": "passed", "stages": stages, "version": item["version"]},
        })
    entry = {k: item[k] for k in ("name", "key", "version", "fileName", "url", "minAppVersion")}
    entry["description"] = audit.source_annotation(item, {})
    locked = {**entry, "buildId": item["id"], "sha256": item["sha256"], "channel": "main",
              "runtimeProfile": "venerax", "status": "passed", "sample": item["sample"],
              "checkedAt": checked, "cliCommit": cli["commit"]}
    state = {
        "main": 1, "extended": 0, "builds": 1, "checkedAt": checked, "runUrl": run, "cli": cli,
        "catalogSha256": audit.sha((root / "monitor/catalog.json").read_bytes()),
        "officialExclusionsSha256": audit.sha((root / "official-exclusions.json").read_bytes()),
        "officialBaselineKeys": len(exclusions["keys"]), "officialExcludedBuilds": 0,
        "officialOverrides": 0,
    }
    data = {
        "index.json": [entry], "extended.json": [], "sources.lock.json": [locked],
        "official-exclusions.json": exclusions,
        "audit-status.json": state, "client-results.json": {"runUrl": run, "cli": cli, "records": records},
        "account-results.json": {
            "runUrl": run, "cli": cli, "catalogSha256": state["catalogSha256"], "sites": [],
            "accountPlanSha256": audit.sha((root / "monitor/accounts.json").read_bytes()),
        },
        "access-results.json": {
            "patrolRunUrl": run, "diagnosticRunUrl": run + "2", "cli": cli,
            "catalogSha256": state["catalogSha256"],
        },
    }
    for name in release.FILES:
        if name not in data:
            (root / name).write_text("测试公开文件\n", encoding="utf-8")
    for name, value in data.items():
        audit.save(root / name, value)
    return data


class ReleaseIndexTests(unittest.TestCase):
    def test_missing_file_is_rejected_before_network(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, "Release 附件缺失"):
                release.validate(Path(directory))

    def test_snapshot_is_deterministic_and_only_contains_public_allowlist(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fixture(root)
            (root / "comic-pw.txt").write_text("private-fixture", encoding="ascii")
            first, second = root / "first", root / "second"
            self.assertEqual(release.stage(root, first, "example/source"),
                             release.stage(root, second, "example/source"))
            for name in release.ASSETS:
                self.assertEqual((first / name).read_bytes(), (second / name).read_bytes())
            with zipfile.ZipFile(first / "vensrc.zip") as archive:
                self.assertEqual(set(archive.namelist()), set(release.FILES))
                self.assertNotIn("account-results.json", archive.namelist())
                self.assertNotIn("comic-pw.txt", archive.namelist())
            self.assertEqual(len(release.ASSETS), 13)

    def test_same_official_version_cannot_be_reintroduced_even_with_passing_community_source(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            data = fixture(root)
            snapshot = data["official-exclusions.json"]
            snapshot["keys"] = sorted(snapshot["keys"] + ["fixture"])
            snapshot["versions"]["fixture"] = "1.0.0"
            audit.save(root / "official-exclusions.json", snapshot)
            data["audit-status.json"].update(
                officialExclusionsSha256=audit.sha((root / "official-exclusions.json").read_bytes()),
                officialBaselineKeys=len(snapshot["keys"]), officialExcludedBuilds=1)
            audit.save(root / "audit-status.json", data["audit-status.json"])
            with self.assertRaisesRegex(AssertionError, "未高于官方版本"):
                release.validate(root)

    def test_new_official_key_at_release_time_blocks_an_older_snapshot(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fixture(root)
            latest = audit.official_policy(root)
            latest["keys"] = sorted(latest["keys"] + ["fixture"])
            latest["versions"]["fixture"] = "1.0.0"
            with patch.object(audit, "refresh_official_policy", return_value=latest) as refreshed:
                with self.assertRaisesRegex(AssertionError, "未高于官方版本"):
                    release.validate(root, check_latest=True)
            refreshed.assert_called_once_with(root)

    def test_newer_community_version_can_be_released_but_equal_official_version_cannot(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            data = fixture(root)
            snapshot = data["official-exclusions.json"]
            snapshot["keys"] = sorted(snapshot["keys"] + ["fixture"])
            snapshot["versions"]["fixture"] = "0.9.0"
            audit.save(root / "official-exclusions.json", snapshot)
            state = data["audit-status.json"]
            state.update(
                officialExclusionsSha256=audit.sha((root / "official-exclusions.json").read_bytes()),
                officialBaselineKeys=len(snapshot["keys"]), officialOverrides=1)
            audit.save(root / "audit-status.json", state)
            data["sources.lock.json"][0]["officialVersion"] = "0.9.0"
            audit.save(root / "sources.lock.json", data["sources.lock.json"])
            release.validate(root)
            primary = next(record for record in data["client-results.json"]["records"]
                           if record["runtimeProfile"] == "venerax")
            primary["source"]["version"] = "0.8.0"
            audit.save(root / "client-results.json", data["client-results.json"])
            with self.assertRaisesRegex(AssertionError, "CLI 实际版本"):
                release.validate(root)
            primary["source"]["version"] = "1.0.0"
            audit.save(root / "client-results.json", data["client-results.json"])
            latest = {**snapshot, "versions": {**snapshot["versions"], "fixture": "1.0.0"}}
            with patch.object(audit, "refresh_official_policy", return_value=latest):
                with self.assertRaisesRegex(AssertionError, "未高于官方版本"):
                    release.validate(root, check_latest=True)

    def test_skipped_image_decode_blocks_subscription_release(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            data = fixture(root)
            for r in data["client-results.json"]["records"]:
                if r["runtimeProfile"] == "venerax":
                    next(s for s in r["source"]["stages"] if s["path"] == "image.decode")["status"] = "skipped"
            audit.save(root / "client-results.json", data["client-results.json"])
            with self.assertRaises(AssertionError):
                release.validate(root)

    def test_changed_source_hash_or_mismatched_diagnostic_blocks_release(self):
        for problem in ("hash", "diagnostic", "minimum_version"):
            with self.subTest(problem=problem), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                data = fixture(root)
                if problem == "hash":
                    data["sources.lock.json"][0]["sha256"] = "f" * 64
                    audit.save(root / "sources.lock.json", data["sources.lock.json"])
                elif problem == "minimum_version":
                    data["index.json"][0]["minAppVersion"] = "0.0.1"
                    audit.save(root / "index.json", data["index.json"])
                else:
                    data["access-results.json"]["patrolRunUrl"] += "other"
                    audit.save(root / "access-results.json", data["access-results.json"])
                with self.assertRaises(AssertionError):
                    release.validate(root)

    def test_duplicate_key_blocks_release(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            data = fixture(root)
            audit.save(root / "extended.json", data["index.json"])
            audit.save(root / "sources.lock.json", data["sources.lock.json"] * 2)
            with self.assertRaises(AssertionError):
                release.validate(root)

    def test_failed_readback_never_publishes_or_deletes_old_release(self):
        old = {"tag_name": "old", "draft": False}
        with tempfile.TemporaryDirectory() as directory, \
                patch.object(release, "releases", return_value=[old]), \
                patch.object(release, "gh") as command, \
                patch.object(release, "verify", side_effect=AssertionError("hash mismatch")):
            with self.assertRaises(AssertionError):
                release.publish("example/source", Path(directory), "rolling-fixture")
            verbs = [call.args[:2] for call in command.call_args_list]
            self.assertIn(("release", "create"), verbs)
            self.assertNotIn(("release", "edit"), verbs)
            self.assertNotIn(("release", "delete"), verbs)

    def test_existing_snapshot_is_verified_without_upload_or_new_tag(self):
        current = {"tag_name": "rolling-fixture", "draft": False}
        with tempfile.TemporaryDirectory() as directory, \
                patch.object(release, "releases", return_value=[current]), \
                patch.object(release, "verify") as verified, \
                patch.object(release, "verify_public"), \
                patch.object(release, "gh", return_value=json.dumps(current)) as command:
            release.publish("example/source", Path(directory), current["tag_name"])
            verified.assert_called_once()
            verbs = [call.args[:2] for call in command.call_args_list]
            self.assertNotIn(("release", "create"), verbs)
            self.assertNotIn(("release", "upload"), verbs)
            self.assertNotIn(("release", "delete"), verbs)

    def test_old_release_is_deleted_only_after_successful_verification_and_promotion(self):
        current = {"tag_name": "rolling-fixture", "draft": True}
        old = {"tag_name": "old", "draft": False}
        events = []
        def command(*args):
            events.append(args[:2])
            return json.dumps(current) if args[0] == "api" else ""
        with tempfile.TemporaryDirectory() as directory, \
                patch.object(release, "releases", side_effect=[[old, current], [old, current], [current]]), \
                patch.object(release, "verify", side_effect=lambda *args: events.append(("verified",))), \
                patch.object(release, "verify_public", side_effect=lambda *args: events.append(("public",))), \
                patch.object(release, "gh", side_effect=command):
            release.publish("example/source", Path(directory), current["tag_name"])
        self.assertLess(events.index(("verified",)), events.index(("release", "edit")))
        self.assertLess(events.index(("release", "edit")), events.index(("release", "delete")))
        self.assertLess(events.index(("public",)), events.index(("release", "delete")))


if __name__ == "__main__":
    unittest.main()
