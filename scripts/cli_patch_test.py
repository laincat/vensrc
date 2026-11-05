import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import cloud_audit as audit

# 上游 src/validate.js 里与 maxPage 校验相关的片段，逐字来自 Gandum2077/venera-patrol-cli。
STRICT = '''    assert(
      c &&
        validId(c.id) &&
        typeof c.title === "string" &&
        c.title.trim() &&
        typeof c.cover === "string" &&
        c.cover.length,
      "Comic requires valid id, title and cover",
    );
  if (result?.maxPage !== undefined)
    assert(
      Number.isInteger(result.maxPage) && result.maxPage >= 0,
      "maxPage must be a nonnegative integer",
    );
  if (result?.next != null)
    assert(typeof result.next === "string", "next must be a string or null");
  return comics;
}
'''

RELAXED = STRICT.replace(
    "  if (result?.maxPage !== undefined)",
    "  if (result?.maxPage != null)")

PATCH = "patches/venera-patrol-cli-maxpage-null.patch"


class CliPatchTests(unittest.TestCase):
    def fixture(self, code):
        directory = Path(tempfile.mkdtemp(prefix="cli-patch-"))
        self.addCleanup(shutil.rmtree, directory, True)
        (directory / "src").mkdir()
        (directory / "src/validate.js").write_text(code, encoding="utf-8", newline="\n")
        (directory / "patches").mkdir()
        shutil.copyfile(audit.ROOT / PATCH, directory / PATCH)
        subprocess.run(["git", "init", "-q"], cwd=directory, check=True)
        return directory

    def test_patch_relaxes_max_page_and_is_recorded_with_its_hash(self):
        directory = self.fixture(STRICT)
        with patch.object(audit, "ROOT", directory):
            applied = audit.apply_cli_patches(directory)
        self.assertEqual(len(applied), 1)
        record = applied[0]
        self.assertEqual((record["file"], record["target"], record["status"]),
                         (PATCH, "src/validate.js", "applied"))
        self.assertEqual(record["sha256"], audit.sha((directory / PATCH).read_bytes()))
        code = (directory / "src/validate.js").read_text(encoding="utf-8")
        self.assertIn("if (result?.maxPage != null)", code)
        self.assertNotIn("if (result?.maxPage !== undefined)", code)
        # 其余校验必须原样保留：仍然拒绝字符串、NaN 和负数。
        self.assertIn("Number.isInteger(result.maxPage) && result.maxPage >= 0", code)
        self.assertIn('"maxPage must be a nonnegative integer"', code)

    def test_upstream_already_relaxed_is_not_patched_again(self):
        directory = self.fixture(RELAXED)
        with patch.object(audit, "ROOT", directory):
            applied = audit.apply_cli_patches(directory)
        self.assertEqual(applied[0]["status"], "upstream")
        self.assertEqual((directory / "src/validate.js").read_text(encoding="utf-8"), RELAXED)

    def test_unknown_upstream_shape_stops_instead_of_silently_skipping(self):
        directory = self.fixture("export function comicList() { return []; }\n")
        with patch.object(audit, "ROOT", directory):
            with self.assertRaisesRegex(ValueError, "需要人工复核"):
                audit.apply_cli_patches(directory)

    def test_every_declared_patch_exists_and_is_a_clean_diff(self):
        for entry in audit.CLI_PATCHES:
            path = audit.ROOT / entry["file"]
            self.assertTrue(path.exists(), entry["file"])
            data = path.read_text(encoding="utf-8")
            self.assertTrue(data.startswith("diff --git "), entry["file"])
            self.assertNotIn(entry["provides"], data.split("@@")[0])
            self.assertIn("--- a/", data)
            self.assertIn("+++ b/" + entry["target"], data)


if __name__ == "__main__":
    unittest.main()
