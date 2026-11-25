"""Copy the entry image into the make.fun output directory.

Standard library only, no network. The output directory comes from
MAKEFUN_OUTPUT_DIR and defaults to /output; it is created if missing.
Local check: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    print(f"copied {SOURCE} -> {target}")


if __name__ == "__main__":
    main()
