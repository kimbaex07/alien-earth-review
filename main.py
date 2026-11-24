"""Alien Field Notes: The Two Day Earth Review.

Writes one line -- a review of planet Earth left by an alien tourist --
to /output/entry.txt. Pure Python standard library only.
"""

import os

ENTRY = (
    "Earth: four stars \u2014 lovely oceans, kind hosts, but the locals "
    "worship small furry gods who ignore them, knock things off tables, "
    "and demand food at 3am. Would serve again."
)


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
