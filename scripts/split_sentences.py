#!/usr/bin/env python3
import sys

def split_line(line):
    result = []
    current = []
    i = 0
    n = len(line)

    in_inline_code = False
    in_fenced_code = False

    while i < n:
        ch = line[i]

        # Detect fenced code blocks ```
        if line.startswith("```", i):
            in_fenced_code = not in_fenced_code
            current.append("```")
            i += 3
            continue

        # Detect inline code `
        if not in_fenced_code and ch == "`":
            in_inline_code = not in_inline_code
            current.append(ch)
            i += 1
            continue

        # If inside code (inline or fenced), copy literally
        if in_inline_code or in_fenced_code:
            current.append(ch)
            i += 1
            continue

        # Detect ellipsis ...
        if line.startswith("...", i):
            current.append("...")
            i += 3
            continue

        # Sentence-ending punctuation (Option 1)
        if ch in ".;!":
            current.append(ch)
            # End of sentence → flush
            result.append("".join(current).strip())
            current = []
            i += 1
            continue

        # Normal character
        current.append(ch)
        i += 1

    # Flush remaining text
    if current:
        result.append("".join(current).strip())

    return result


if __name__ == "__main__":
    for line in sys.stdin:
        parts = split_line(line.rstrip("\n"))
        for p in parts:
            print(p)
