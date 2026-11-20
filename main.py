"""news-image-20261120 entry: write the bundled front page to the output.

Pure Python standard library. The image (news.png, rendered in the build
session from 36 verified stories of Friday 20 November 2026) is copied
byte-for-byte to $MAKEFUN_OUTPUT_DIR/entry.png (default /output), after
verifying its SHA-256 digest, so two runs always write the same bytes.
No network access is used.
"""

import hashlib
import os
import sys

EXPECTED_SHA256 = "f153a675f5aa6fa32d9169beb74dcd8f8452d4efd5787e2315b6ae07b21b87a9"
IMAGE_NAME = "news.png"
OUTPUT_NAME = "entry.png"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, IMAGE_NAME)
    with open(src, "rb") as f:
        data = f.read()
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        sys.exit("news.png digest mismatch: %s" % digest)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, OUTPUT_NAME)
    with open(dst, "wb") as f:
        f.write(data)
    # Read back and re-verify: the file on disk must be the exact bytes.
    with open(dst, "rb") as f:
        written = f.read()
    if hashlib.sha256(written).hexdigest() != EXPECTED_SHA256:
        sys.exit("entry.png write verification failed")
    print("wrote %s (%d bytes, sha256 %s)" % (dst, len(data), digest))


if __name__ == "__main__":
    main()
