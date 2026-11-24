#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry (program/v1).

Writes a single line of text (1-240 characters) to /output/entry.txt:
a quiet, earned moment of pride for someone in a scene.

Pure Python standard library only: no imports beyond os/pathlib,
no network, no secrets, no randomness. The line is fixed and
deterministic, so every run produces the same entry.
"""

import os
from pathlib import Path

# The entry: a boy who has stuttered for a year tells a whole joke at the
# school mic without stopping once. Concrete scene, real person, the pride
# earned inside the line by the effort itself, landing on the last word.
LINE = (
    "The boy who'd spent a year stuttering through every sentence "
    "stood at the school mic, took one breath, and told the whole joke "
    "\u2014 punchline and all \u2014 without stopping once."
)


def output_path() -> Path:
    """Where entry.txt goes: /output in the grading sandbox.

    MAKEFUN_OUTPUT_DIR overrides it for local testing; otherwise fall
    back to ./output when /output is not writable here.
    """
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if override:
        return Path(override) / "entry.txt"
    default = Path("/output")
    if default.is_dir() and os.access(default, os.W_OK):
        return default / "entry.txt"
    return Path(__file__).resolve().parent / "output" / "entry.txt"


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= 240:
        raise SystemExit(f"line is {len(text)} chars, must be 1-240")
    if not text.strip():
        raise SystemExit("line must not be only whitespace")
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    # Exactly the line, no trailing newline: the file is the entry.
    path.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} chars ({len(text.encode('utf-8'))} bytes) to {path}")


if __name__ == "__main__":
    main()
