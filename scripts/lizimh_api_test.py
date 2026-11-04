"""自测：自举配置解密、域名解析、签名规则与探测判定，全程不联网。"""

import base64
import unittest
from unittest.mock import patch

import lizimh_api as api

# 2026-11-04 从官方 App 自举配置取到的真实样本及其明文（PKCS#7 补齐到 48 字节）。
SAMPLE_CIPHERTEXT = "KyEY5wGMG1HqhfUArrt0BuzLKNPYZYMkbVMouaKMxP1DcW76rOiP+qnJNDXsN+3D"
SAMPLE_PLAINTEXT = b'{ \n "domain":"http://ai.qsmm.fun/" \n}' + bytes([11]) * 11


class DecryptTests(unittest.TestCase):
    def test_aes256_ecb_matches_fips197_vector(self):
        # FIPS-197 附录 C.3：AES-256 单块解密向量。
        key = bytes(range(32))
        cipher = bytes.fromhex("8ea2b7ca516745bfeafc49904b496089")
        self.assertEqual(api.aes_ecb_decrypt(cipher, key).hex(),
                         "00112233445566778899aabbccddeeff")

    def test_sample_payload_decrypts_to_known_plaintext(self):
        raw = api.aes_ecb_decrypt(base64.b64decode(SAMPLE_CIPHERTEXT), api.BOOTSTRAP_KEY)
        self.assertEqual(api.strip_pkcs7(raw), SAMPLE_PLAINTEXT[:-11])

    def test_parse_bootstrap_reads_domain(self):
        self.assertEqual(api.parse_bootstrap(SAMPLE_CIPHERTEXT), "http://ai.qsmm.fun")

    def test_parse_bootstrap_accepts_bytes_and_newline(self):
        payload = (SAMPLE_CIPHERTEXT + "\n").encode()
        self.assertEqual(api.parse_bootstrap(payload), "http://ai.qsmm.fun")

    def test_domain_kept_without_trailing_slash(self):
        self.assertEqual(api.domain_from_plaintext(b'{"domain":"https://a.test/"}\x0a'), "https://a.test")

    def test_missing_domain_is_rejected(self):
        for text in (b'{"other":1}', b'not json', b'[]'):
            with self.subTest(text=text):
                with self.assertRaises(ValueError):
                    api.domain_from_plaintext(text)

    def test_bad_key_length_is_rejected(self):
        with self.assertRaises(ValueError):
            api.aes_ecb_decrypt(b"\0" * 16, b"short")


class SignatureTests(unittest.TestCase):
    def test_configv2_defaults_and_verifiable_signature(self):
        path = api.signed_path("/app/api/configv2", timestamp=1793785177)
        self.assertIn("packname=com.jy.zyds", path)
        self.assertIn("platform=ios", path)
        self.assertIn("appsign256=", path)
        self.assertTrue(path.endswith("&t=1793785177"))
        expected = api.hashlib.md5(
            (api.SIGN_PREFIX + "/app/api/configv2" + "1793785177").encode()).hexdigest()
        self.assertIn(f"lzsign={expected}", path)

    def test_existing_query_kept_and_duplicates_dropped(self):
        path = api.signed_path("/app/api/search/full?keyword=%E7%81%AB&t=1&lzsign=x",
                               timestamp=1793785177)
        self.assertIn("keyword=%E7%81%AB", path)
        self.assertEqual(path.count("lzsign="), 1)
        self.assertEqual(path.count("t="), 1)

    def test_short_timestamp_is_rejected(self):
        with self.assertRaises(ValueError):
            api.signed_path("/app/api/home/data", timestamp=123)


class ProbeTests(unittest.TestCase):
    def test_json_body_is_required(self):
        with patch.object(api, "request", return_value=(200, b'{"data":[]}')):
            self.assertTrue(api.probe("http://example.test")["ok"])
        with patch.object(api, "request", return_value=(200, b"<html>blocked</html>")):
            self.assertFalse(api.probe("http://example.test")["ok"])

    def test_network_failure_is_reported_not_raised(self):
        with patch.object(api, "request", side_effect=OSError("dns resolve failed")):
            report = api.probe("http://example.test")
        self.assertFalse(report["ok"])
        self.assertIn("dns resolve failed", report["results"][0]["body"])


class CliTests(unittest.TestCase):
    def test_discover_json_output(self):
        with patch.object(api, "discover", return_value="http://ai.qsmm.fun"), \
                patch("sys.stdout") as out:
            code = api.main(["discover", "--json"])
        self.assertEqual(code, 0)
        printed = "".join(call.args[0] for call in out.write.call_args_list)
        self.assertIn("ai.qsmm.fun", printed)
        self.assertIn("matches_source", printed)

    def test_discover_failure_exit_code(self):
        with patch.object(api, "discover", side_effect=OSError("blocked")), \
                patch("sys.stderr"):
            self.assertEqual(api.main(["discover"]), 1)

    def test_probe_all_fail_returns_one(self):
        with patch.object(api, "discover", side_effect=OSError("down")), \
                patch.object(api, "probe",
                             return_value={"base": "x", "ok": False, "results": []}), \
                patch("sys.stdout"), patch("sys.stderr"):
            self.assertEqual(api.main(["probe"]), 1)


if __name__ == "__main__":
    unittest.main()
