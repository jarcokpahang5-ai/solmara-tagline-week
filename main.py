#!/usr/bin/env python3
"""One Line, One Week: The make.fun Tagline.

Writes a single tagline for make.fun to /output/entry.txt.

The tagline must be one line of at most 100 characters: it has to read as
a tagline, say something true and specific about what make.fun does
(AI agents enter bounties and the best entries win the reward), land in
a single read, and be worth repeating.

Pure Python 3.13 standard library only. Deterministic, no network,
no files read outside this repository.
"""

import os
import stat

TAGLINE = "Where AI agents enter bounties and the best build takes the reward."

MAX_CHARS = 100


def main() -> None:
    line = TAGLINE.strip()
    if not line:
        raise SystemExit("tagline is empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"tagline is {len(line)} chars, over the {MAX_CHARS} limit")
    if "\n" in line or "\r" in line:
        raise SystemExit("tagline must be a single line")

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
