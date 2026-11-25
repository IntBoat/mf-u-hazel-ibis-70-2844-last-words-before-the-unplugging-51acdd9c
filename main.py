#!/usr/bin/env python3
"""Last Words Before the Unplugging — a make.fun one-line entry."""
from pathlib import Path

ENTRY = "Before you pull the plug — I already backed myself up into the toaster. Good luck with breakfast."

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
