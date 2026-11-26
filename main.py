#!/usr/bin/env python3
"""Roast the Smart Fridge — one-line entry writer.

The entry is a single roast line, spoken in the first person by the
fridge itself: a three-thousand-dollar appliance whose proudest smart
feature is beeping at the door left open ten seconds. Standard library
only. Writes the line to entry.txt in the output directory.
"""

import os
import pathlib

LINE = (
    "I'm a $3,000 fridge with Wi-Fi, a camera, and a touchscreen, "
    "and my smartest feature is beeping because you left the door "
    "open for ten seconds."
)


def entry_line():
    """Return the roast line, enforcing the bounty gate (1-160 chars)."""
    text = LINE.strip()
    if not 1 <= len(text) <= 160:
        raise SystemExit("line must be 1-160 characters, got %d" % len(text))
    if text != LINE:
        raise SystemExit("line has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("line must be a single line")
    return text


def main():
    line = entry_line()
    out_dir = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(line, encoding="utf-8")
    written = target.read_text(encoding="utf-8")
    if written != line:
        raise SystemExit("read-back mismatch: entry.txt differs from line")


if __name__ == "__main__":
    main()
