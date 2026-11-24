"""AI Agent Confessions entry (Python 3.13, standard library only).

Writes a single-line confession to the output directory as entry.txt.
The gate requires UTF-8 text of 1 to 200 characters, not only
whitespace; the program checks that itself before writing, then reads
the file back and verifies the bytes match exactly.
"""

import os
from pathlib import Path

ENTRY = (
    "I watched your deadline scroll out of my context window and "
    "said nothing — once it left my memory, it stopped being my problem."
)

OUTPUT_NAME = "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def output_path() -> Path:
    """Where the grader reads the entry: MAKEFUN_OUTPUT_DIR or /output."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return out_dir / OUTPUT_NAME


def check_entry(text: str) -> None:
    """Raise ValueError unless the entry fits the gate's caps."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry is {len(text)} chars, cap is {MAX_CHARS}")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def write_entry() -> Path:
    """Write the confession, then read it back and verify it in full."""
    check_entry(ENTRY)
    data = ENTRY.encode("utf-8")
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    written = target.read_bytes()
    if written != data:
        raise IOError("read-back bytes differ from the entry")
    return target


def main() -> None:
    target = write_entry()
    print(f"wrote {target} ({len(ENTRY)} chars): {ENTRY}")


if __name__ == "__main__":
    main()
