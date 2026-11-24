#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog — entry generator.

Writes exactly one patch-note line (1-160 chars) to /output/entry.txt.
Deterministic: stdlib only, no network, no randomness.
"""
import os

ENTRY = (
    "v2.4.1: fixed a bug where the brain replayed your most embarrassing "
    "moment from 2013 every night at 3 a.m. instead of sleeping."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    assert 1 <= len(ENTRY) <= 160, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY, "entry must be one line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the gate counts every character (1-160),
    # so the file holds exactly the entry line and nothing else.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
