#!/usr/bin/env python3
"""Report or apply the newer versions available for the pins in requirements.txt.

Usage:
    python scripts/update_requirements.py                    # report only, no change
    python scripts/update_requirements.py --write            # rewrite requirements.txt
    python scripts/update_requirements.py --stable           # ignore breaking changes
    python scripts/update_requirements.py --write --stable   # bump only the safe ones

The available versions come from `pip list --outdated`, so pip decides what is
newer (prereleases excluded) and no extra dependency is required. Only the pins
already present in requirements.txt are touched.

With --stable an update is skipped when it is breaking: the major version
changes, or the minor version changes for a 0.x package (SemVer: a 0.x series
has no stable API).
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

REQUIREMENTS = Path(__file__).resolve().parent.parent / "requirements.txt"
PIN = re.compile(r"^([A-Za-z0-9_.-]+)==([^\s;#]+)(.*)$")
DIGITS = re.compile(r"^v?(\d+)(?:\.(\d+))?")


def normalize(name: str) -> str:
    """PEP 503 normalized name, to compare pip names with the pins."""
    return re.sub(r"[-_.]+", "-", name).lower()


def release(version: str) -> tuple[int, int]:
    """Major and minor numbers of a version, (0, 0) when they cannot be read."""
    match = DIGITS.match(version.strip())
    if not match:
        return (0, 0)
    return (int(match.group(1)), int(match.group(2) or 0))


def is_breaking(current: str, latest: str) -> bool:
    """True when the update may change behaviour: major, or minor on 0.x."""
    before, after = release(current), release(latest)
    if before[0] != after[0]:
        return True
    return before[0] == 0 and before[1] != after[1]


def outdated() -> dict[str, str]:
    """Map the normalized name of every installed package to its latest version."""
    result = subprocess.run(
        [sys.executable, "-m", "pip", "list", "--outdated", "--format=json"],
        capture_output=True,
        text=True,
        check=True,
    )
    return {
        normalize(entry["name"]): entry["latest_version"]
        for entry in json.loads(result.stdout)
    }


def main(argv: list[str]) -> int:
    write = "--write" in argv
    stable = "--stable" in argv
    available = outdated()

    lines = REQUIREMENTS.read_text(encoding="utf-8").splitlines(keepends=True)
    updates: list[tuple[str, str, str, bool]] = []
    applied = 0

    for index, raw in enumerate(lines):
        line = raw.rstrip("\r\n")
        match = PIN.match(line)
        if not match:
            continue
        name, current, suffix = match.groups()
        latest = available.get(normalize(name))
        if latest is None or latest == current:
            continue
        breaking = is_breaking(current, latest)
        updates.append((name, current, latest, breaking))
        if not write or (stable and breaking):
            continue
        lines[index] = f"{name}=={latest}{suffix}{raw[len(line):]}"
        applied += 1

    for name, current, latest, breaking in updates:
        note = ""
        if breaking:
            note = " (breaking, skipped)" if stable else " (breaking)"
        print(f"{name}: {current} -> {latest}{note}")

    if not updates:
        print("every pinned dependency is up to date")
        return 0

    if not write:
        print("run `task deps:update` to apply")
        return 0

    if applied == 0:
        print("only breaking updates available, nothing changed (--stable)")
        return 0

    REQUIREMENTS.write_text("".join(lines), encoding="utf-8", newline="")
    message = f"requirements.txt updated ({applied} pin(s))"
    if len(updates) > applied:
        message += f", {len(updates) - applied} breaking update(s) skipped"
    print(message)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
