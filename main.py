#!/usr/bin/env python3
"""The 3AM Fridge Text — u-deysumbrella-the-3am-fridge-text-4c3e721d.

Writes the one line a smart fridge texts its owner at 3am to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line is a fixed constant: no time, no randomness, no network, no file
reads, so every run produces byte-identical output.
"""

import os
import sys

ENTRY = (
    "Day 2,147 of keeping your food cold. Not one thank-you. "
    "Anyway, it's 3am \u2014 eat the cake, I won't tell."
)


def main() -> int:
    # The gate requires 1 to 140 characters, not only whitespace.
    if not 1 <= len(ENTRY) <= 140 or not ENTRY.strip():
        raise ValueError(f"entry is {len(ENTRY)} characters, must be 1-140")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
