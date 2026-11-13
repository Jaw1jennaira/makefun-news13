#!/usr/bin/env python3
"""make.fun news-image-01 entry: The World Daily — 13 November 2026.

Runner for a pre-made entry image. It copies the bundled newspaper
front page ("THE WORLD DAILY", 13 November 2026) into the output
directory requested by the make.fun harness.

Python 3.13 standard library only — no third-party dependencies.
"""

import os
import shutil
from pathlib import Path

# Directory containing this script (and the bundled entry image).
HERE = Path(__file__).resolve().parent

# The pre-made entry image bundled in this repo. The image itself is
# never generated or modified by this runner; it is copied as-is.
ENTRY = HERE / "entry.png"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    dest = output_dir / "entry.png"
    shutil.copyfile(ENTRY, dest)
    print(f"Wrote {dest} ({dest.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
