#!/usr/bin/env python3
"""One-Star Review of Something Essential.

Writes a single deadpan one-star review of sleep, an everyday essential,
to /output/entry.txt. The review is one line of 1-160 characters: a real
complaint, filed in earnest, against a thing that cannot be fixed.

Why sleep: it is the essential everyone pays for nightly in hours, gets
nothing keepable back from, and still wakes up tired from. The review
treats it the way a customer treats a subscription that never delivers:
eight hours a night, nothing back, tired in the morning, would not renew.
"""

import os
import sys

# The review. 135 characters, one line, deadpan throughout: no exclamation
# marks, no winking, the joke turns only in the last three words, when the
# complaint becomes an action and the reviewer cancels the subscription.
REVIEW = (
    "One star. Sleep takes eight hours every night, gives nothing back, "
    "and still leaves me tired in the morning. Cancelling my subscription."
)

MAX_CHARS = 160


def build_review() -> str:
    """Return the review, refusing to ship one that breaks the gate."""
    text = REVIEW.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"review must be 1-{MAX_CHARS} characters, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("review must be a single line")
    return text


def main() -> int:
    text = build_review()
    out_dir = os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exactly the review text, no trailing newline: the gate counts
    # characters, so nothing extra may ride along in the file.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
