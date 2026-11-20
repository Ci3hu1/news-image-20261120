"""Tests for the news-image-20261120 entry program (pure stdlib)."""
import hashlib
import os
import subprocess
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN = os.path.join(REPO, "main.py")
IMAGE = os.path.join(REPO, "news.png")
EXPECTED_SHA256 = "f153a675f5aa6fa32d9169beb74dcd8f8452d4efd5787e2315b6ae07b21b87a9"


class TestEntry(unittest.TestCase):
    def test_image_is_valid_png_1024(self):
        with open(IMAGE, "rb") as f:
            data = f.read()
        self.assertTrue(data.startswith(b"\x89PNG\r\n\x1a\n"))
        self.assertLessEqual(len(data), 1048576)
        self.assertEqual(hashlib.sha256(data).hexdigest(), EXPECTED_SHA256)
        # PNG IHDR: width/height are bytes 16..24, big-endian.
        w = int.from_bytes(data[16:20], "big")
        h = int.from_bytes(data[20:24], "big")
        self.assertEqual((w, h), (1024, 1024))

    def test_main_copies_deterministically(self):
        outs = []
        for _ in range(2):
            with tempfile.TemporaryDirectory() as tmp:
                env = dict(os.environ, MAKEFUN_OUTPUT_DIR=tmp)
                r = subprocess.run([sys.executable, MAIN], env=env,
                                   capture_output=True, text=True)
                self.assertEqual(r.returncode, 0, r.stderr)
                with open(os.path.join(tmp, "entry.png"), "rb") as f:
                    outs.append(f.read())
        self.assertEqual(outs[0], outs[1])
        self.assertEqual(hashlib.sha256(outs[0]).hexdigest(), EXPECTED_SHA256)

    def test_main_uses_only_stdlib(self):
        with open(MAIN) as f:
            src = f.read()
        for mod in ("hashlib", "os", "sys"):
            self.assertIn("import %s" % mod, src)
        self.assertNotIn("PIL", src)
        self.assertNotIn("numpy", src)


if __name__ == "__main__":
    unittest.main()
