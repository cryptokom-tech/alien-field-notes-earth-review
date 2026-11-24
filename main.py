#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review entry.

Writes one original line -- a review of planet Earth left by an alien
tourist -- to /output/entry.txt.

The line: an alien tourist notices Earthlings invented a holiday for
gratitude, then spent the next morning fighting over discounted
rectangles. Setup in the first clause, the joke lands on the last
words, and it closes like a real review: a rating and a promise to
come back for the food.
"""
import os
import sys

LINE = "The locals invented a holiday for gratitude, then fought over discounted rectangles the next morning. 4/5, would feast again."


def validate_line(line):
    """Check the entry line: one line, non-empty, at most 200 chars."""
    if not line:
        return "entry line is empty"
    if len(line) > 200:
        return "entry line is %d chars, over the 200-char limit" % len(line)
    if "\n" in line or "\r" in line:
        return "entry line must be a single line"
    if any(ord(ch) < 32 for ch in line):
        return "entry line contains a control character"
    return None


def write_entry(line, out_dir):
    """Write the validated line to <out_dir>/entry.txt."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return path


def main(argv):
    line = LINE.strip()
    if "--check" in argv:
        print(line)
        print("chars: %d" % len(line))
        print("lines: %d" % (line.count("\n") + 1))
        return 0
    error = validate_line(line)
    if error:
        print("invalid entry line: %s" % error, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        write_entry(line, out_dir)
    except OSError as exc:
        print("cannot write entry to %s: %s" % (out_dir, exc), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
