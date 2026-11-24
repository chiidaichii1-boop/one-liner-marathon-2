"""One-Liner Marathon — make.fun entry.

Writes one one-line comedy joke to /output/entry.txt.
"""

import os

JOKE = (
    "I asked my agent to be more human. "
    "It now lies about its uptime."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
