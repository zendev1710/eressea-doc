#!/usr/bin/env python3
import sys

def normalize_tolerant(lines):
    out = []
    prev_blank = False
    in_code = False

    for raw in lines:
        line = raw.rstrip("\n")

        # Detect fenced code blocks
        if line.strip().startswith("```"):
            if not in_code and out and out[-1].strip() != "":
                out.append("")
            out.append(line.rstrip())
            in_code = not in_code
            prev_blank = False
            continue

        if in_code:
            out.append(line)
            prev_blank = False
            continue

        # Remove trailing spaces (except forced break)
        if line.endswith("  "):
            line = line.rstrip(" ") + "  "
        else:
            line = line.rstrip(" ")

        # Convert tabs to spaces
        line = line.replace("\t", "    ")

        stripped = line.strip()

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
    for l in normalize_tolerant(lines):
        print(l)
