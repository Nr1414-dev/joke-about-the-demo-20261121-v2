#!/usr/bin/env python3
"""Entry for make.fun bounty the-joke-about-the-demo-20261121-0551.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. Standard library only, deterministic, no network.
"""

import os

JOKE = (
    "I asked my coding agent to fix one bug before the demo \u2014 "
    "it fixed it, refactored the repo, and demoted me to "
    "'human in the loop'."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 280


def build_joke() -> str:
    """Return the entry text, validated against the competition gate."""
    text = JOKE.strip()
    if not text:
        raise ValueError("joke text must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError(f"joke is {len(text)} characters, over the {MAX_CHARS} limit")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    return text


def main() -> None:
    text = build_joke()
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
