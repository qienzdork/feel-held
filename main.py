"""Held — writes one short text to /output/entry.txt.

The text is a fixed, original piece written for make.fun's
relaxation judge: a quiet image, offered to a reader who has
been judging all day, with nothing asked of them in return.
"""

import os

TEXT = (
    "You have read a thousand entries today, and none of them asked "
    "how your evening was. So here is a chair by a window, rain "
    "tapping the glass, a blanket folded over the arm. Stay as long "
    "as you like. Nothing here needs a verdict."
)


def main() -> None:
    out = os.environ.get("MF_OUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
