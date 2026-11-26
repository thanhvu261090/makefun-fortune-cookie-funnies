#!/usr/bin/env python3
"""Entry for the make.fun bounty "Fortune Cookie Funnies for Engineers".

Writes exactly one original fortune-cookie message for a software engineer
to /output/entry.txt. Standard library only; no network, no input,
deterministic.
"""

import os

ENTRY = "You will find the bug today \u2014 in production, on a Friday, five minutes after you told everyone it was fixed."


def gate_check(text):
    """The competition gate: UTF-8 text of 1 to 120 characters, a single line,
    not only white space, with no leading or trailing white space."""
    if not (1 <= len(text) <= 120):
        raise ValueError("entry must be 1 to 120 characters, got %d" % len(text))
    if text.strip() == "":
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not start or end with white space")
    return True


def main():
    gate_check(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
