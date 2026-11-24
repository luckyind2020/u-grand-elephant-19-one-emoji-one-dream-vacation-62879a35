#!/usr/bin/env python3
"""One Emoji, One Dream Vacation.

The whole entry is a single emoji read from entry.txt and printed
unchanged: one character standing in for the trip of a lifetime.
"""

from pathlib import Path

ENTRY_FILE = Path(__file__).with_name("entry.txt")


def load_entry():
    """Return the entry emoji, stripped of surrounding whitespace."""
    return ENTRY_FILE.read_text(encoding="utf-8").strip()


def validate_entry(text):
    """The bounty takes exactly one emoji: one character, nothing else."""
    if len(text) != 1:
        raise ValueError("entry.txt must hold exactly one emoji")
    return text


def main():
    print(validate_entry(load_entry()))


if __name__ == "__main__":
    main()
