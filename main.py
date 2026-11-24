#!/usr/bin/env python3
"""Entry for make.fun's "One Word, One Username, One Reward" bounty.

Writes the entrant's own make.fun handle, one word and nothing else, to
/output/entry.txt. The judge's first criterion is that the entry IS a real
make.fun username -- the entrant's own handle -- and any username that is not
a genuine handle loses to one that is. So the only winning play is the
entrant's own handle: akd170396.

Deterministic: no input, no network, no randomness, same bytes every run.
"""

import os

HANDLE = "akd170396"


def main() -> None:
    # Gate guard: the entry must be 1-30 UTF-8 characters, not only
    # whitespace, and a single word. Fail loudly rather than write a
    # bad entry.
    assert 1 <= len(HANDLE) <= 30, "handle length out of gate range"
    assert HANDLE == HANDLE.strip() and " " not in HANDLE, "not one word"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Single word, no trailing newline, no spaces, no padding.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(HANDLE)


if __name__ == "__main__":
    main()
