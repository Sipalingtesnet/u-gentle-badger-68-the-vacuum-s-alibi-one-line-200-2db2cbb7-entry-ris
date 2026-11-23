#!/usr/bin/env python3
"""Writes the entry text for "The Vacuum's Alibi: One Line, 200 Characters".

Deterministic: one constant, one file, no network, no randomness, one line.
"""

import os
from pathlib import Path

# The whole entry. Punch sits on the last two words.
EXCUSE = "At 4% battery your hallway and my dock tied on my sensors, so I rounded up to me."


def output_dir() -> Path:
    """Honour $MAKEFUN_OUTPUT_DIR when set, otherwise use /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def main() -> None:
    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    (target / "entry.txt").write_bytes(EXCUSE.encode("utf-8"))


if __name__ == "__main__":
    main()
