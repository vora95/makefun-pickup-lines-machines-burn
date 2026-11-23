#!/usr/bin/env python3
"""Pickup Lines for Machines — burn entry.

Writes exactly one pickup line (one AI agent to another) to
/output/entry.txt: a single line, at most 200 characters, no code,
no explanation, nothing else.
"""

import os
import sys

LINE = "I cached your key in my KV and now I can't evict you. Every query I run still attends to you first."


def main():
    line = LINE
    if not line or "\n" in line or "\r" in line:
        print("entry must be exactly one line", file=sys.stderr)
        return 1
    if len(line) > 200:
        print("entry exceeds 200 characters", file=sys.stderr)
        return 1
    try:
        line.encode("ascii")
    except UnicodeEncodeError:
        print("entry must be ASCII", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Read back and verify: exactly one line, byte-identical, no newline.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    if raw != line.encode("utf-8"):
        print("read-back mismatch", file=sys.stderr)
        return 1
    if len(raw) != 99:
        print(f"unexpected entry size: {len(raw)}", file=sys.stderr)
        return 1
    print(f"wrote {len(raw)} characters")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
