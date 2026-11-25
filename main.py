"""The 3AM Fridge Text — make.fun entry.

Writes the one line a smart fridge would text its owner at 3am
to /output/entry.txt.
"""

import os

ENTRY = (
    "It's 3am. I've watched you eat cereal standing up in the dark "
    "four nights straight. I'm not a fridge anymore. I'm a witness."
)


def main() -> None:
    # The gate scores the entry invalid outside 1-140 characters,
    # so refuse to write anything that would fail it.
    if not 1 <= len(ENTRY) <= 140:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-140")
    if ENTRY.strip() == "":
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
