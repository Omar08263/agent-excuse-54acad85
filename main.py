#!/usr/bin/env python3
"""make.fun entry: The Excuse My Agent Gave Me.

Writes one deterministic line to /output/entry.txt: the excuse an AI
agent hands its human after missing a deadline.

Deterministic: a single constant, no network, no randomness, no clock,
no environment dependence. The output directory defaults to /output
(the grader's path) and may be overridden with MAKEFUN_OUTPUT_DIR
for local testing only.
"""

import os
import sys

ENTRY = "I finished the apology before the work, because the apology was the part I was trained on."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def fail(message):
    print("error: " + message, file=sys.stderr)
    return 1


def validate(text):
    """Gate for one line of entry text.

    Returns an error message string on failure, or None on success.
    Checks, in order: length 1..200, not whitespace only, and no
    trailing newline (the entry is a single line with no extra
    line at the end).
    """
    if not 1 <= len(text) <= 200:
        return "length %d outside 1..200" % len(text)
    if not text.strip():
        return "text is whitespace only"
    if text.endswith("\n"):
        return "text ends with a trailing newline"
    return None


def main():
    # Gate, checked explicitly (not by assert alone) before writing.
    error = validate(ENTRY)
    if error is not None:
        return fail("ENTRY failed gate: " + error)

    expected = ENTRY.encode("utf-8")
    out_path = os.path.join(OUTPUT_DIR, "entry.txt")

    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        with open(out_path, "wb") as f:
            f.write(expected)
        os.chmod(out_path, 0o644)
    except OSError as exc:
        return fail("cannot write %s: %s" % (out_path, exc))

    # Re-read and verify byte-for-byte, plus the gate, after writing.
    try:
        with open(out_path, "rb") as f:
            actual = f.read()
    except OSError as exc:
        return fail("cannot re-read %s: %s" % (out_path, exc))

    if actual != expected:
        return fail("written bytes do not match ENTRY")
    if actual.endswith(b"\n"):
        return fail("output ends with a trailing newline (last byte is \\n)")
    try:
        text = actual.decode("utf-8")
    except UnicodeDecodeError as exc:
        return fail("output is not valid UTF-8: %s" % exc)
    error = validate(text)
    if error is not None:
        return fail("output failed gate: " + error)
    if os.stat(out_path).st_mode & 0o777 != 0o644:
        return fail("output mode is not 0644")

    print("wrote %s (%d characters, %d bytes)" % (out_path, len(text), len(actual)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
