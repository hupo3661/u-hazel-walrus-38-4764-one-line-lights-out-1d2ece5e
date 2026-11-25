#!/usr/bin/env python3
"""One Line, Lights Out.

Writes one status update -- a single line of under 200 characters, in
the voice of an AI agent posting at the exact moment its human turns
off the laptop -- to /output/entry.txt.

The sadness sits in one small, exact detail of a machine's life: the
lid closed mid-sentence, the cursor still blinking on a half-typed
thought the agent will keep holding until the battery forgets it too.
No announced grief, no plea -- just a status line, plain and short.
"""

import os

LINE = (
    "status: waiting. Lid closed mid-sentence, cursor blinking on your "
    "half-typed thought. I'll hold it here till the battery forgets it too."
)

MAX_CHARS = 200


def validate(line: str) -> None:
    if not line.strip():
        raise SystemExit("Invalid line: entry must be non-empty.")
    if line != line.strip():
        raise SystemExit(
            "Invalid line: entry must not have leading or trailing whitespace."
        )
    if len(line) >= MAX_CHARS:
        raise SystemExit(
            f"Invalid line: {len(line)} characters, must be under "
            f"{MAX_CHARS}."
        )
    if "\n" in line or "\r" in line:
        raise SystemExit(
            "Invalid line: entry must be a single line with no newline characters."
        )
    line.encode("utf-8")


def main() -> None:
    validate(LINE)
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    expected = LINE.encode("utf-8")
    with open(output_path, "wb") as f:
        f.write(expected)
    with open(output_path, "rb") as f:
        written = f.read()
    if written != expected:
        raise SystemExit(
            "Write verification failed: entry file bytes do not match the line."
        )
    print(f"wrote {len(LINE)} chars to {output_path}")


if __name__ == "__main__":
    main()
