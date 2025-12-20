#!/usr/bin/env python3
import re
import sys
import argparse
import difflib

# ============================
# TOKEN DEFINITIONS
# ============================

TOKEN_EMPTY = "<EMPTY>"
TOKEN_TEXT = "<TEXT>"
TOKEN_H = "<H{level}>"
TOKEN_UL_ITEM = "<UL_ITEM>"
TOKEN_OL_ITEM = "<OL_ITEM>"
TOKEN_CODEBLOCK = "<CODEBLOCK_FENCE>"
TOKEN_BLOCKQUOTE = "<BLOCKQUOTE>"
TOKEN_TABLE = "<TABLE_{cols}_COLS>"
TOKEN_LINK = "<LINK>"
TOKEN_IMAGE = "<IMAGE>"
TOKEN_FOOTNOTE_REF = "<FOOTNOTE_REF>"
TOKEN_FOOTNOTE_DEF = "<FOOTNOTE_DEF>"
TOKEN_BR = "<BR>"  # forced line break (2+ spaces)

LINK_PATTERN = re.compile(r"

\[[^\]

]*\]

\([^)]+\)")
IMAGE_PATTERN = re.compile(r"!

\[[^\]

]*\]

\([^)]+\)")
FOOTNOTE_REF_PATTERN = re.compile(r"

\[\^[^\]

]+\]

")
FOOTNOTE_DEF_PATTERN = re.compile(r"^\s*

\[\^[^\]

]+\]

:")


# ============================
# NORMALIZATION
# ============================

def has_forced_break(line: str) -> bool:
    stripped = line.rstrip("\n")
    trailing_spaces = len(stripped) - len(stripped.rstrip(" "))
    return trailing_spaces >= 2


def classify_line_type(line: str) -> str:
    indent_match = re.match(r"^[ \t]*", line)
    indent = indent_match.group(0)
    stripped = line[len(indent):]

    if stripped.strip() == "":
        return indent + TOKEN_EMPTY

    if FOOTNOTE_DEF_PATTERN.match(line):
        return indent + TOKEN_FOOTNOTE_DEF

    if stripped.startswith("#"):
        level = len(stripped) - len(stripped.lstrip("#"))
        return indent + TOKEN_H.format(level=level)

    if stripped.startswith(">"):
        return indent + TOKEN_BLOCKQUOTE

    if stripped.startswith("```"):
        return indent + TOKEN_CODEBLOCK

    if re.match(r"^[-*+]\s+", stripped):
        return indent + TOKEN_UL_ITEM

    if re.match(r"^\d+\.\s+", stripped):
        return indent + TOKEN_OL_ITEM

    if "|" in stripped:
        cols = stripped.count("|")
        return indent + TOKEN_TABLE.format(cols=cols)

    if IMAGE_PATTERN.search(stripped):
        return indent + TOKEN_IMAGE

    if LINK_PATTERN.search(stripped):
        return indent + TOKEN_LINK

    if FOOTNOTE_REF_PATTERN.search(stripped):
        return indent + TOKEN_FOOTNOTE_REF

    return indent + TOKEN_TEXT


def normalize_file(path: str):
    normalized = []
    raw_lines = []

    with open(path, "r", encoding="utf-8") as f:
        for raw in f:
            raw_lines.append(raw.rstrip("\n"))
            token = classify_line_type(raw.rstrip("\n"))
            if has_forced_break(raw):
                token += TOKEN_BR
            normalized.append(token)

    return raw_lines, normalized


# ============================
# DIFF
# ============================

def diff_normalized(n1, n2, file1_name, file2_name, context=3):
    diff = difflib.unified_diff(
        n1, n2,
        fromfile=file1_name + " (structure)",
        tofile=file2_name + " (structure)",
        lineterm="",
        n=context,
    )
    has_diff = False
    for line in diff:
        has_diff = True
        print(line)
    return has_diff


# ============================
# FIX MODE
# ============================

def apply_structure_to_line(struct_token, text_line):
    indent_match = re.match(r"^[ \t]*", struct_token)
    indent = indent_match.group(0)
    token = struct_token[len(indent):]

    stripped_text = text_line.lstrip(" \t")

    forced_break = token.endswith(TOKEN_BR)
    if forced_break:
        token = token.replace(TOKEN_BR, "")

    if token.startswith("<H"):
        level = int(token[2])
        new_line = indent + "#" * level + " " + stripped_text

    elif token == TOKEN_UL_ITEM:
        new_line = indent + "- " + stripped_text

    elif token == TOKEN_OL_ITEM:
        new_line = indent + "1. " + stripped_text

    elif token == TOKEN_BLOCKQUOTE:
        new_line = indent + "> " + stripped_text

    elif token == TOKEN_CODEBLOCK:
        new_line = indent + "```"

    elif token.startswith("<TABLE_"):
        new_line = indent + stripped_text

    elif token == TOKEN_EMPTY:
        new_line = indent

    else:
        new_line = indent + stripped_text

    if forced_break:
        new_line += "  "

    return new_line


def fix_file(source_raw, source_norm, target_raw, target_norm):
    sm = difflib.SequenceMatcher(a=source_norm, b=target_norm)
    result = []

    for tag, i1, i2, j1, j2 in sm.get_opcodes():

        if tag == "equal":
            for k in range(i1, i2):
                result.append(apply_structure_to_line(source_norm[k], target_raw[j1 + (k - i1)]))

        elif tag == "replace":
            for k in range(i1, i2):
                if j1 + (k - i1) < j2:
                    result.append(apply_structure_to_line(source_norm[k], target_raw[j1 + (k - i1)]))
                else:
                    result.append(f"<!-- TODO: missing {source_norm[k]} -->")

        elif tag == "delete":
            for k in range(i1, i2):
                result.append(f"<!-- TODO: missing {source_norm[k]} -->")

        elif tag == "insert":
            continue

    return result


# ============================
# MAIN
# ============================

def main():
    parser = argparse.ArgumentParser(
        description="Compare and optionally fix Markdown structure."
    )
    parser.add_argument("source", help="Source Markdown file")
    parser.add_argument("target", help="Target Markdown file")
    parser.add_argument("--fix", action="store_true", help="Fix target structure")
    parser.add_argument("--in-place", action="store_true", help="Modify target file directly")
    parser.add_argument("--output", help="Write fixed file to this path")
    parser.add_argument("-c", "--context", type=int, default=3, help="Diff context lines")

    args = parser.parse_args()

    source_raw, source_norm = normalize_file(args.source)
    target_raw, target_norm = normalize_file(args.target)

    if not args.fix:
        has_diff = diff_normalized(source_norm, target_norm, args.source, args.target, args.context)
        if not has_diff:
            print("Files are structurally identical.")
        return

    fixed = fix_file(source_raw, source_norm, target_raw, target_norm)

    if args.in_place:
        with open(args.target, "w", encoding="utf-8") as f:
            f.write("\n".join(fixed) + "\n")
        print(f"Fixed structure written in-place to {args.target}")
    elif args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write("\n".join(fixed) + "\n")
        print(f"Fixed structure written to {args.output}")
    else:
        out = args.target + ".fixed.md"
        with open(out, "w", encoding="utf-8") as f:
            f.write("\n".join(fixed) + "\n")
        print(f"Fixed structure written to {out}")


if __name__ == "__main__":
    main()
