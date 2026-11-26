#!/usr/bin/env python3
"""Print the six-word entry exactly as written in entry.txt."""

import sys
from pathlib import Path


def main() -> int:
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    text = entry_path.read_text(encoding="utf-8")
    # sys.stdout.write, not print: print would append a newline the
    # entry does not have, and the output must match the file exactly.
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
