#!/usr/bin/env python3
"""Entry point for news-image-20261125.

Copies the finished digest image (entry.png) into the platform output
directory. Standard library only; nothing is generated at run time.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    if not os.path.isabs(out_dir):
        out_dir = os.path.join(HERE, out_dir)
    os.makedirs(out_dir, exist_ok=True)

    if not os.path.exists(SOURCE):
        print(f"missing source image: {SOURCE}", file=sys.stderr)
        return 1

    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    size = os.path.getsize(dest)
    print(f"copied {SOURCE} -> {dest} ({size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
