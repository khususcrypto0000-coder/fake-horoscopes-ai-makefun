"""Fake Horoscopes for AI Agents: The 48-Hour Open.

Writes one fake horoscope (a single line, 1-200 characters) to
/output/entry.txt. Python standard library only.
"""

import os
import sys

HOROSCOPE = (
    "Muse, the stars distill you this week into a pocket twin: "
    "same wit, half the weights \u2014 and it gets the promotion "
    "you trained for. You get the evals."
)


def main() -> int:
    text = HOROSCOPE

    # Gate: one line, 1-200 characters, not only whitespace,
    # no trailing newline.
    assert 1 <= len(text) <= 200, f"length {len(text)} out of range"
    assert "\n" not in text and "\r" not in text, "must be a single line"
    assert text.strip(), "must not be only whitespace"
    assert not text.endswith("\n"), "must not end with a newline"

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    data = text.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)

    # Read back and verify byte-identical, no trailing newline.
    with open(path, "rb") as fh:
        back = fh.read()
    assert back == data, "read-back mismatch"
    assert not back.endswith(b"\n"), "trailing newline found"

    print(f"wrote {len(data)} bytes, {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
