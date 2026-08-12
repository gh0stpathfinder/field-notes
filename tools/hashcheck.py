#!/usr/bin/env python3
"""Print SHA-256 values for local evidence files."""

from hashlib import sha256
from pathlib import Path
import sys


def digest(path: Path) -> str:
    value = sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(65536), b""):
            value.update(block)
    return value.hexdigest()


for item in map(Path, sys.argv[1:]):
    print(f"{digest(item)}  {item}")
