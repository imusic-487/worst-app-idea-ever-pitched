"""Worst App Idea Ever Pitched: PlantBell.

Writes one sentence (205 characters) pitching the worst, most
useless app imaginable to /output/entry.txt.
"""

import os

ENTRY = (
    "PlantBell is a $13-a-month smart doorbell for your houseplants "
    "that lets visitors ring to announce themselves to your ferns, "
    "so your plants never miss a guest they cannot hear, see, "
    "or answer the door for."
)


def main() -> None:
    # Gate, mirroring the scorer: 1-240 characters, not only whitespace.
    if not 1 <= len(ENTRY) <= 240 or not ENTRY.strip():
        raise ValueError(f"entry is {len(ENTRY)} characters, must be 1-240")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
