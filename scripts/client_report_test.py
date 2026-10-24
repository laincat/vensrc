from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import cloud_audit as audit


class ClientReportTests(unittest.TestCase):
    def test_skipped_core_stage_is_not_a_pass_and_differences_are_listed(self):
        stages = [{"path": path, "status": "passed"} for path in (
            "source.load", "search.load", "comic.loadInfo", "comic.loadEp", "image.download", "image.decode"
        )]
        passed = {"key": "fixture", "sourceSha256": "a" * 64, "status": "passed", "stages": stages}
        skipped = {**passed, "status": "partial", "stages": [
            {**stage, "status": "skipped"} if stage["path"] == "image.decode" else stage
            for stage in stages
        ]}
        self.assertTrue(audit.core(passed))
        self.assertFalse(audit.core(skipped))
        item = {
            "id": "a" * 64, "sha256": "a" * 64, "name": "fixture", "key": "fixture",
            "version": "1.0", "repository": "fixture/repo", "minAppVersion": "1.0",
            "verifyProfiles": ["venera-next"],
        }
        def record(profile, source):
            return {"id": item["id"], "runtimeProfile": profile, "source": source, "inputs": {}}
        payload = {
            "checkedAt": "2026-10-24", "cli": {"commit": "b" * 40},
            "records": [record("venerax", skipped)],
            "clientRecords": [record("venera-next", passed)],
        }
        with tempfile.TemporaryDirectory() as directory, patch.object(audit, "validate_client_record"):
            audit.publish_clients(payload, {"sources": [item], "priorityRepositories": []}, Path(directory))
            report = (Path(directory) / "CLIENT_RESULTS.md").read_text(encoding="utf-8")
            self.assertIn("| venerax | 1 | 0 | 0 | 1 | 0 | 0 | 1 |", report)
            self.assertIn("共 1 个构建", report)
            self.assertIn("| fixture | 1.0 | fixture/repo | 未通过 | 通过 |", report)
