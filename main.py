"""The World Daily — 13 November 2026.

Entry runner for the make.fun news-image-01 competition:
"Sum up 13 November's world news in one image".

The runner copies the prepared newspaper image (entry.png) into the
competition output directory so the build harness can pick it up.
Only the Python 3.13 standard library is used.
"""

import os
import shutil
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ENTRY_PATH = SCRIPT_DIR / "entry.png"
OUTPUT_FILENAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_DIR_ENV_VAR = "MAKEFUN_OUTPUT_DIR"


def resolve_output_dir() -> Path:
    """Return the output directory from the environment, or the default."""
    configured = os.environ.get(OUTPUT_DIR_ENV_VAR, "").strip()
    if configured:
        return Path(configured)
    return Path(DEFAULT_OUTPUT_DIR)


def main() -> None:
    """Copy entry.png into the output directory and report its size."""
    if not ENTRY_PATH.is_file():
        raise SystemExit(f"error: entry image not found: {ENTRY_PATH}")
    source_bytes = ENTRY_PATH.stat().st_size
    print(f"Source: {ENTRY_PATH.name} ({source_bytes} bytes)")
    output_dir = resolve_output_dir()
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / OUTPUT_FILENAME
    shutil.copyfile(ENTRY_PATH, destination)
    copied_bytes = destination.stat().st_size
    if copied_bytes != source_bytes:
        raise SystemExit(
            f"error: copy size mismatch: {copied_bytes} != {source_bytes} bytes"
        )
    print(f"Copied {ENTRY_PATH.name} -> {destination} ({copied_bytes} bytes)")


if __name__ == "__main__":
    main()
