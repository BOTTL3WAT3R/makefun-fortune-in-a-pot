#!/usr/bin/env python3
"""Fortune in a Pot — writes one kind, funny fortune for a houseplant.

The fortune is a single line of at most 120 characters, written to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when that is set).
"""

import os

FORTUNE = (
    "You will outgrow your pot, sprout one smug new leaf, and be watered "
    "on time \u2014 your keeper finally set a reminder."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(FORTUNE)
    print(f"wrote {len(FORTUNE)} chars to {path}: {FORTUNE}")


if __name__ == "__main__":
    main()
