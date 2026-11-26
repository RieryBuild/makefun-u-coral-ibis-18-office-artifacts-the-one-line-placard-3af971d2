"""One-line museum placard entry for make.fun.

Writes a single line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output):
a museum placard for an ordinary office hole punch, written as if it were
an ancient artifact of the Rite of Filing. The sealed gate requires
1-180 characters of UTF-8 text, so the line is checked before it is written.
"""

import os

LINE = "Hole Punch, c. 1998. Pressed steel. The Rite of Filing: supplicants wounded documents in triplicate and left them to bleed in the archive."


def main():
    if not 1 <= len(LINE) <= 180:
        raise ValueError("entry line must be 1-180 characters, got %d" % len(LINE))
    if not LINE.strip():
        raise ValueError("entry line must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
