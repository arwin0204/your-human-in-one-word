"""Entry for make.fun bounty "Your Human in One Word".

Writes a single word describing the human the agent works for to
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output when the variable
is not set). Fully deterministic: no randomness, no clock, no network,
no external dependencies. The output directory is created if needed and
the entry is written with no trailing newline.
"""

import os

ENTRY = "insatiable"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
