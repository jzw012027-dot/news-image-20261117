#!/usr/bin/env python3
"""Publish the 17 November 2026 news poster as this entry's image.

The poster itself ships in this repository as entry.png. Running
this program copies it, byte for byte, to entry.png inside the
output directory (/output, or MAKEFUN_OUTPUT_DIR when that is
set), which is the file the sealed gate and the judge then read.
"""

import os
import pathlib
import shutil

POSTER = pathlib.Path(__file__).resolve().with_name("entry.png")


def publish() -> pathlib.Path:
    out_dir = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(POSTER, target)
    print(f"published {target} ({target.stat().st_size} bytes)")
    return target


if __name__ == "__main__":
    publish()
