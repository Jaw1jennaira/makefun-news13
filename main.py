#!/usr/bin/env python3
"""make.fun news-image-01 entry: The World Daily — 13 November 2026.

Copies the pre-made entry image to the output directory.
Python 3.13 standard library only.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
# The pre-made entry image bundled in this repo.
ENTRY = HERE / "entry.png"


DEFAULT_OUTPUT_DIR = "/output"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR))
    output_dir.mkdir(parents=True, exist_ok=True)
    dest = output_dir / "entry.png"
    shutil.copyfile(ENTRY, dest)
    print(f"Wrote {dest} ({dest.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
