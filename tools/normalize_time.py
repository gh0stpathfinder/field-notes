#!/usr/bin/env python3
"""Normalize ISO-8601 timestamps to UTC."""

from datetime import datetime, timezone
import sys

for raw in sys.argv[1:]:
    parsed = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    print(parsed.astimezone(timezone.utc).isoformat().replace("+00:00", "Z"))
