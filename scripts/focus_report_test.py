import unittest

from focus_report import login_label


class LoginEvidenceTests(unittest.TestCase):
    def test_other_build_or_client_login_cannot_be_reused(self):
        records = {("build-a", "venerax"): {
            "source": {"stages": [{"path": "account.login", "status": "passed"}]}}}
        self.assertEqual(login_label(records, "build-a", "venerax"), "通过")
        self.assertIn("未对该构建执行", login_label(records, "build-b", "venerax"))
        self.assertIn("未对该构建执行", login_label(records, "build-a", "venera-next"))

    def test_skipped_missing_or_mixed_login_stages_never_pass(self):
        for stages in (
            [],
            [{"path": "account.login", "status": "skipped", "category": "credentials_missing"}],
            [{"path": "account.login", "status": "passed"},
             {"path": "account.login", "status": "failed", "category": "auth_required"}],
        ):
            records = {("build", "venerax"): {"source": {"stages": stages}}}
            self.assertNotEqual(login_label(records, "build", "venerax"), "通过")
