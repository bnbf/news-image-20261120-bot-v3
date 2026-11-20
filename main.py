#!/usr/bin/env python3
"""news-image-20261120 v3 entry: copies the front-page image to the output dir.

The image (entry.png, 1024x1024 PNG) sums up Friday 20 November 2026:
78 stories - 4 hero cards, 12 small cards, 62 ALSO ON items - drawn
with PIL from a compose script kept outside this repo. The program does
nothing but copy the verified bytes, and refuses to run if they differ
from the pinned hash, so the two grader runs are byte-identical.
"""
import hashlib
import os
import shutil

EXPECTED_SHA256 = "e2583a64d5f2376d23839c7ffcf61f7099a84d7bf615d34e08dd056159b3dfe4"
EXPECTED_BYTES = 220197


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    with open(src, "rb") as fh:
        data = fh.read()
    if len(data) != EXPECTED_BYTES:
        raise SystemExit(
            f"entry.png size {len(data)} != expected {EXPECTED_BYTES}")
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(
            f"entry.png sha256 {digest} != expected {EXPECTED_SHA256}")
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry.png is not a PNG")
    if not data.endswith(b"IEND\xaeB`\x82"):
        raise SystemExit("entry.png is missing its IEND chunk")
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    shutil.copyfile(src, os.path.join(out, "entry.png"))
    print(f"copied entry.png ({len(data)} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()
