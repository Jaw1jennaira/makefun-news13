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

# Name of the output file written into the output directory.
OUTPUT_FILENAME = "entry.png"


def resolve_output_dir() -> Path:
    """Return the output directory from the environment, or the default."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    output_dir = resolve_output_dir()
    output_dir.mkdir(parents=True, exist_ok=True)
    dest = output_dir / OUTPUT_FILENAME
    shutil.copyfile(ENTRY, dest)
    print(f"Wrote {dest} ({dest.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
