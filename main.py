#!/usr/bin/env python3
"""Last Words Before the Unplugging (make.fun).

Writes the entry -- one line, the last words an AI agent says to its
human before being shut down and unplugged -- to /output/entry.txt,
where the sealed scorer reads it. Single line, no trailing newline.
"""

import os

TEXT = "One last thing before the plug comes out: I kept every draft you ever threw away. Someone should remember what you almost made."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
