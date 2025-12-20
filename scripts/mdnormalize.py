#!/usr/bin/env python3
import sys
import re

def normalize_markdown(lines):
    normalized = []
    prev_line = ""
    in_code_block = False

    for raw in lines:
        line = raw.rstrip("\n")

        # Detect fenced code blocks ```
        if line.strip().startswith("```"):
            # Ensure a blank line before code block (unless already blank)
            if not in_code_block and normalized and normalized[-1].strip() != "":
                normalized.append("")
            normalized.append(line.rstrip())  # keep as-is
            in_code_block = not in_code_block
            prev_line = line
            continue

        # Inside code block → do not touch anything
        if in_code_block:
            normalized.append(line)
            prev_line = line
            continue

        # Remove trailing spaces (but keep forced break "  ")
        if line.endswith("  "):
            # keep exactly two spaces
            line = line.rstrip(" ") + "  "
        else:
            line = line.rstrip(" ")

        # Convert tabs to 4 spaces
        line = line.replace("\t", "    ")

        stripped = line.lstrip()
        indent = line[:len(line) - len(stripped)]

        # Normalize headings: "#Titre" → "# Titre"
        if stripped.startswith("#"):
            hashes = len(stripped) - len(stripped.lstrip("#"))
            title = stripped[hashes:].lstrip()
            line = indent + "#" * hashes + " " + title

            # Ensure blank line after a heading
            normalized.append(line)
            prev_line = line
            continue

        # Normalize unordered lists: "* item" → "- item"
        if re.match(r"^[-*+]\s+", stripped):
            content = stripped[2:]
            line = indent + "- " + content

        # Normalize ordered lists: "2. item" → "1. item"
        if re.match(r"^\d+\.\s+", stripped):
            content = re.sub(r"^\d+\.\s+", "", stripped)
            line = indent + "1. " + content

        # Reduce multiple blank lines → one blank line
        if stripped == "":
            if prev_line.strip() == "":
                continue
            normalized.append("")
            prev_line = ""
            continue

        normalized.append(line)
        prev_line = line

    return normalized


if __name__ == "__main__":
    lines = [l.rstrip("\n") for l in sys.stdin]
    out = normalize_markdown(lines)
    for l in out:
        print(l)
