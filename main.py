"""The World Daily — 13 November 2026.

Entry runner for the make.fun news-image-01 competition ("Sum up
13 November's world news in one image"). It places the finished
newspaper front page into the directory requested by the harness so
the image can be collected as the competition submission.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ENTRY_PATH = HERE / "entry.png"
OUTPUT_FILENAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"


def resolve_output_dir():
    """Return the output directory from MAKEFUN_OUTPUT_DIR, else default."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    return Path(chosen)


def main():
    out_dir = resolve_output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    destination = out_dir / OUTPUT_FILENAME
    shutil.copyfile(ENTRY_PATH, destination)
    copied_bytes = destination.stat().st_size
    print(f"Wrote {destination} ({copied_bytes} bytes)")


if __name__ == "__main__":
    main()
