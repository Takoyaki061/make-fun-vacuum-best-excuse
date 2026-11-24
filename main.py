#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse.

Writes one one-line excuse a robot vacuum gives for missing a spot to
/output/entry.txt (1-140 characters, UTF-8). Stdlib only, deterministic.
"""

import os

EXCUSE = (
    "My lidar mapped that corner as a wall in 2019 "
    "and I have never once questioned it."
)


def main() -> None:
    # Guard the gate: /output/entry.txt must hold 1-140 chars of non-blank
    # UTF-8 text, or the entry is never judged. Fail loudly here rather
    # than shipping an invalid file.
    text = EXCUSE.strip()
    if not text or len(text) > 140:
        raise ValueError(
            "excuse must be 1-140 non-blank characters, got %d" % len(text)
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
