"""news-image-20261122 entry (Python 3.13, standard library only).

Copies the pre-built entry.png (a 1024x683 summary of 22 November 2026's
world news) to $MAKEFUN_OUTPUT_DIR (default /output). No network, no
randomness: every run writes the same bytes.
"""

import os
import shutil
import sys
from pathlib import Path

ENTRY = Path(__file__).resolve().with_name("entry.png")


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    if not ENTRY.is_file():
        print(f"error: {ENTRY} is missing", file=sys.stderr)
        return 1
    shutil.copyfile(ENTRY, dest)
    size = dest.stat().st_size
    with open(dest, "rb") as fh:
        magic = fh.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        print("error: entry.png is not a PNG", file=sys.stderr)
        return 1
    if size > 1_048_576:
        print(f"error: entry.png is {size} bytes (> 1 MiB)", file=sys.stderr)
        return 1
    print(f"wrote {dest} ({size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
