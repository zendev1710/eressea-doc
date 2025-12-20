#!/usr/bin/env python3
import sys
import re

def normalize_strict(lines):
    out = []
    prev_blank = False
    in_code = False

    for raw in lines:
        line = raw.rstrip("\n")

        # Detect fenced code blocks
        if line.strip().startswith("```"):
            out.append(line.rstrip())
            in_code = not in_code
            prev_blank = False
            continue

        # Inside code block → do nothing
        if in_code:
            out.append(line)
            prev_blank = False
            continue

        # Remove trailing spaces (except forced break)
        if line.endswith("  "):
            line = line.rstrip(" ") + "  "
        else:
            line = line.rstrip(" ")

        # Convert tabs to 4 spaces
        line = line.replace("\t", "    ")

        stripped = line.lstrip()
        indent = line[:len(line) - len(stripped)]

        # Normalize headings
        if stripped.startswith("#"):
            hashes = len(stripped) - len(stripped.lstrip("#"))
            title = stripped[hashes:].lstrip()
            line = indent + "#" * hashes + " " + title

        # Normalize unordered lists
        if re.match(r"^[-*+]\s+", stripped):
            content = stripped[2:]
            line = indent + "- " + content

        # Normalize ordered lists
        if re.match(r"^\d+\.\s+", stripped):
            content = re.sub(r"^\d+\.\s+", "", stripped)
            line = indent + "1. " + content

        # Collapse multiple blank lines
        if stripped == "":
            if prev_blank:
                continue
            out.append("")
            prev_blank = True
            continue

        out.append(line)
        prev_blank = False

    return out


if __name__ == "__main__":
    lines = [l.rstrip("\n") for l in sys.stdin]
    for l in normalize_strict(lines):
        print(l)
