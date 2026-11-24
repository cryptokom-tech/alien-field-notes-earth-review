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


def main(argv):
    line = LINE.strip()
    if "--check" in argv:
        print(line)
        print("chars: %d" % len(line))
        print("lines: %d" % (line.count("\n") + 1))
        return 0
    if not line or len(line) > 200 or "\n" in line or "\r" in line:
        print("invalid entry line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
