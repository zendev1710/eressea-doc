import sys
import re
import difflib

# ============================================================
# CONFIGURATION CONSTANTS
# ============================================================

LIST_NORM_SILENT = "silent"
LIST_NORM_ANNOTATED = "annotated"
LIST_NORM_WARNING = "warning"

BLOCKQUOTE_NORM_ON = "on"
BLOCKQUOTE_NORM_OFF = "off"


# ============================================================
# TOKENS
# ============================================================

TOKEN_EMPTY = "<EMPTY>"
TOKEN_UL_ITEM = "<UL>"
TOKEN_OL_ITEM = "<OL>"
TOKEN_BLOCKQUOTE = "<BQ>"
TOKEN_CODEBLOCK = "<CODE>"
TOKEN_META = "<META>"
TOKEN_TEXT = "<TEXT>"      # Paragraphes non-alignants
TOKEN_BR = "<BR>"
TOKEN_IGNORED = None       # Commentaires HTML ignorés structurellement


def load_alignment_flags(tsv_path):
    """
    Lit le fichier .aligned.tsv et retourne une liste de flags par ligne EN.
    Chaque entrée correspond à une ligne EN reconstruite.
    """
    flags = []
    with open(tsv_path, "r", encoding="utf-8") as f:
        current_flag = None
        for line in f:
            if line.startswith("FLAG"):
                current_flag = line.split("\t", 1)[1].strip()
            if line.strip() == "":
                if current_flag is not None:
                    flags.append(current_flag)
                current_flag = None
    return flags

def detect_translation_blocks(flags, min_block=2):
    """
    Retourne deux sets :
    - block_starts : indices des lignes où un bloc commence
    - block_ends   : indices des lignes où un bloc finit
    """
    block_starts = set()
    block_ends = set()

    i = 0
    while i < len(flags):
        if flags[i] in ("NOT_TRANSLATED", "TRANSLATED_IN_FR"):
            start = i
            while i < len(flags) and flags[i] in ("NOT_TRANSLATED", "TRANSLATED_IN_FR"):
                i += 1
            end = i - 1

            if (end - start + 1) >= min_block:
                block_starts.add(start)
                block_ends.add(end)
        else:
            i += 1

    return block_starts, block_ends



# ============================================================
# NORMALISATION DES LISTES (L2)
# ============================================================

def normalize_lists_L2(lines: List[str], mode: str) -> List[str]:
    """
    Normalisation respectueuse (L2) :
    - garde '-' pour UL
    - garde '1.' pour OL
    - corrige les listes cassées
    - corrige les tirets Unicode
    - corrige les indentations cassées
    - corrige les sous-listes mal indentées
    """

    normalized = []
    warnings = []

    for idx, line in enumerate(lines):
        original = line

        # Commentaires HTML → ne pas toucher
        if line.strip().startswith("<!--") and line.strip().endswith("-->"):
            normalized.append(line)
            continue

        # Corrige les tirets Unicode
        if "–" in line:
            line = line.replace("–", "-")

        stripped = line.lstrip()
        indent = line[:len(line) - len(stripped)]

        # Cas : "- - text"
        if re.match(r"^- -\s+", stripped):
            if mode == LIST_NORM_WARNING:
                warnings.append(f"WARNING: malformed list at line {idx+1}: '{original}'")
                normalized.append(line)
                continue

            stripped = stripped.replace("- -", "-")
            if mode == LIST_NORM_ANNOTATED:
                stripped += "  <!-- normalized: double dash -->"

            normalized.append(indent + stripped)
            continue

        # Cas : "-- text"
        if re.match(r"^--\s+", stripped):
            if mode == LIST_NORM_WARNING:
                warnings.append(f"WARNING: malformed list at line {idx+1}: '{original}'")
                normalized.append(line)
                continue

            stripped = stripped.replace("--", "-")
            if mode == LIST_NORM_ANNOTATED:
                stripped += "  <!-- normalized: double dash -->"

            normalized.append(indent + stripped)
            continue

        # Cas : "-text" → "- text"
        if re.match(r"^-[A-Za-z0-9]", stripped):
            if mode == LIST_NORM_WARNING:
                warnings.append(f"WARNING: malformed list at line {idx+1}: '{original}'")
                normalized.append(line)
                continue

            stripped = "- " + stripped[1:]
            if mode == LIST_NORM_ANNOTATED:
                stripped += "  <!-- normalized: missing space -->"

            normalized.append(indent + stripped)
            continue

        # Cas : listes ordonnées "1.text" → "1. text"
        if re.match(r"^\d+\.[A-Za-z0-9]", stripped):
            if mode == LIST_NORM_WARNING:
                warnings.append(f"WARNING: malformed list at line {idx+1}: '{original}'")
                normalized.append(line)
                continue

            stripped = re.sub(r"^(\d+)\.", r"\1. ", stripped)
            if mode == LIST_NORM_ANNOTATED:
                stripped += "  <!-- normalized: missing space -->"

            normalized.append(indent + stripped)
            continue

        normalized.append(line)

    for w in warnings:
        print(w, file=sys.stderr)

    return normalized


# ============================================================
# NORMALISATION DES BLOCKQUOTES
# ============================================================

def normalize_blockquotes(lines: List[str]) -> List[str]:
    normalized = []
    for line in lines:
        stripped = line.lstrip()
        indent = line[:len(line) - len(stripped)]

        if stripped.startswith(">") and not stripped.startswith("> "):
            stripped = "> " + stripped[1:]

        normalized.append(indent + stripped)
    return normalized


# ============================================================
# CLASSIFICATION DES LIGNES
# ============================================================

def classify_line_type(line: str) -> str:
    stripped = line.lstrip()

    if stripped.startswith("<!--") and stripped.endswith("-->"):
        return TOKEN_IGNORED

    if stripped == "":
        return TOKEN_EMPTY

    if stripped.startswith("```"):
        return TOKEN_CODEBLOCK

    if stripped.startswith("# cSpell:"):
        return TOKEN_TEXT

    if re.match(r"^#{1,6}\s", stripped):
        level = len(stripped) - len(stripped.lstrip("#"))
        return f"<H{level}>"

    if re.match(r"^[-*+]\s+", stripped):
        return TOKEN_UL_ITEM

    if re.match(r"^\d+\.\s+", stripped):
        return TOKEN_OL_ITEM

    if stripped.startswith("> "):
        return TOKEN_BLOCKQUOTE

    return TOKEN_TEXT


# ============================================================
# NORMALISATION GLOBALE DU FICHIER
# ============================================================

def has_forced_break(raw: str) -> bool:
    return raw.rstrip("\n").endswith("  ")

def normalize_file(path: str, list_mode: str, blockquote_mode: str) -> Tuple[List[str], List[str]]:
    with open(path, "r", encoding="utf-8") as f:
        raw_lines = [line.rstrip("\n") for line in f.readlines()]

    raw_lines = normalize_lists_L2(raw_lines, list_mode)

    if blockquote_mode == BLOCKQUOTE_NORM_ON:
        raw_lines = normalize_blockquotes(raw_lines)

    normalized = []
    in_front_matter = False
    front_matter_done = False

    for idx, line in enumerate(raw_lines):

        if idx == 0 and line.strip() == "---":
            in_front_matter = True

        if in_front_matter and not front_matter_done:
            normalized.append(TOKEN_META)
            if idx != 0 and line.strip() == "---":
                in_front_matter = False
                front_matter_done = True
            continue

        token = classify_line_type(line)

        if token is TOKEN_IGNORED:
            normalized.append(TOKEN_IGNORED)
            continue

        if has_forced_break(line):
            token += TOKEN_BR

        normalized.append(token)

    return raw_lines, normalized


# ============================================================
# APPLY STRUCTURE
# ============================================================

def apply_structure_to_line(struct_token: str, text_line: str) -> str:
    if struct_token == TOKEN_META or struct_token is TOKEN_IGNORED:
        return text_line

    if struct_token.startswith(TOKEN_TEXT):
        return text_line

    indent_match = re.match(r"^[ \t]*", struct_token)
    indent = indent_match.group(0) if indent_match else ""
    token = struct_token[len(indent):]

    stripped = text_line.lstrip(" \t")
    stripped = re.sub(r"^#{1,6}\s+", "", stripped)
    stripped = re.sub(r"^\d+\.\s+", "", stripped)
    stripped = re.sub(r"^[-*+]\s+", "", stripped)
    stripped = re.sub(r"^>\s+", "", stripped)

    forced_break = token.endswith(TOKEN_BR)
    if forced_break:
        token = token.replace(TOKEN_BR, "")

    if token.startswith("<H"):
        level = int(token[2])
        if stripped.strip() == "":
            return indent + "#" * level + " TODO"
        new_line = indent + "#" * level + " " + stripped
    # if token.startswith("<H"):
    #     level = int(token[2])
    #     new_line = indent + "#" * level + " " + stripped

    elif token == TOKEN_UL_ITEM:
        new_line = indent + "- " + stripped

    elif token == TOKEN_OL_ITEM:
        new_line = indent + "1. " + stripped

    elif token == TOKEN_BLOCKQUOTE:
        new_line = indent + "> " + stripped

    elif token == TOKEN_CODEBLOCK:
        if stripped.startswith("```"):
            new_line = indent + stripped
        else:
            new_line = indent + "```"

    elif token == TOKEN_EMPTY:
        new_line = indent

    else:
        new_line = indent + stripped

    if forced_break and not new_line.endswith("  "):
        new_line += "  "

    return new_line


# ============================================================
# FIX FILE
# ============================================================

def fix_file(source_raw, source_norm, target_raw, target_norm, aligned_tsv_path):
    sm = difflib.SequenceMatcher(a=source_norm, b=target_norm)
    result = []

    for tag, i1, i2, j1, j2 in sm.get_opcodes():

        if tag == "equal":
            for k in range(i1, i2):
                src_tok = source_norm[k]
                tgt_tok = target_norm[j1 + (k - i1)]

                if tgt_tok is TOKEN_IGNORED:
                    result.append(target_raw[j1 + (k - i1)])
                    continue

                if src_tok.startswith(TOKEN_TEXT):
                    result.append(target_raw[j1 + (k - i1)])
                    continue

                result.append(apply_structure_to_line(src_tok, target_raw[j1 + (k - i1)]))

        elif tag == "replace":
            len_src = i2 - i1
            len_tgt = j2 - j1
            common = min(len_src, len_tgt)

            for offset in range(common):
                k_src = i1 + offset
                k_tgt = j1 + offset

                if target_norm[k_tgt] is TOKEN_IGNORED:
                    result.append(target_raw[k_tgt])
                    continue

                val = source_norm[k_src]
                if val is None:
                    continue
                if val.startswith(TOKEN_TEXT):
                    result.append(target_raw[k_tgt])
                    continue

                result.append(apply_structure_to_line(source_norm[k_src], target_raw[k_tgt]))

            for k_src in range(i1 + common, i2):
                result.append(f"<!-- TODO: missing {source_norm[k_src]} -->")

            for k_tgt in range(j1 + common, j2):
                if target_norm[k_tgt] is TOKEN_IGNORED:
                    result.append(target_raw[k_tgt])
                else:
                    result.append(target_raw[k_tgt] + " <!-- EXTRA -->")

        elif tag == "delete":
            for k in range(i1, i2):
                result.append(f"<!-- TODO: missing {source_norm[k]} -->")

        elif tag == "insert":
            for k in range(j1, j2):
                if target_norm[k] is TOKEN_IGNORED:
                    result.append(target_raw[k])
                else:
                    result.append(target_raw[k] + " <!-- EXTRA -->")

    # === INSERTION DES TO DO TRANSLATE ===
    # Charger les flags depuis le .aligned.tsv
    flags = load_alignment_flags(aligned_tsv_path)

    # Détecter les blocs NOT_TRANSLATED / TRANSLATED_IN_FR
    block_starts, block_ends = detect_translation_blocks(flags)

    # Ajouter les tags dans le résultat final
    for idx in range(len(result)):
        if idx in block_starts:
            result[idx] += " <!-- TODO: TRANSLATE BEGIN -->"
        if idx in block_ends:
            result[idx] += " <!-- TODO: TRANSLATE END -->"

    return result


# ============================================================
# VALIDATION DU FICHIER FIXÉ
# ============================================================

def validate_output(lines: List[str]) -> Tuple[bool, List[str]]:
    warnings = []
    ok = True

    # 1. Titres vides
    for idx, line in enumerate(lines):
        if re.match(r"^#{1,6}\s*$", line):
            ok = False
            warnings.append(f"Invalid empty heading at line {idx+1}: '{line}'")

    # 2. Listes vides
    for idx, line in enumerate(lines):
        if re.match(r"^[-*+]\s*$", line):
            ok = False
            warnings.append(f"Invalid empty list item at line {idx+1}: '{line}'")

        if re.match(r"^\d+\.\s*$", line):
            ok = False
            warnings.append(f"Invalid empty ordered list item at line {idx+1}: '{line}'")

    # 3. EXTRA sur un titre
    for idx, line in enumerate(lines):

        # Ignore EXTRA on cSpell directives
        if line.startswith("# cSpell:") and "<!-- EXTRA -->" in line:
            continue

        if re.match(r"^#{1,6}.*<!-- EXTRA -->", line):
            warnings.append(f"Heading marked EXTRA at line {idx+1}: '{line}'")
            continue

    # 4. Codeblocks non fermés
    codeblock_count = sum(1 for line in lines if line.strip().startswith("```"))
    if codeblock_count % 2 != 0:
        ok = False
        warnings.append("Unclosed codeblock detected")

    # 5. Blockquotes vides
    for idx, line in enumerate(lines):
        if re.match(r"^>\s*$", line):
            ok = False
            warnings.append(f"Empty blockquote at line {idx+1}: '{line}'")

    return ok, warnings


# ============================================================
# DEBUG
# ============================================================

def debug_dump(source_path, target_path, source_raw, source_norm, target_raw, target_norm):
    print("=== DEBUG mdstructdiff ===")
    print(f"SOURCE: {source_path}")
    print(f"TARGET: {target_path}")

    print("\n--- SOURCE TOKENS ---")
    for i, (raw, tok) in enumerate(zip(source_raw, source_norm), 1):
        print(f"{i:4d}: {str(tok):12s} | {raw}")

    print("\n--- TARGET TOKENS ---")
    for i, (raw, tok) in enumerate(zip(target_raw, target_norm), 1):
        print(f"{i:4d}: {str(tok):12s} | {raw}")

    print("\n--- OPCODES ---")
    sm = difflib.SequenceMatcher(a=source_norm, b=target_norm)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        print(f"{tag:7s} src[{i1}:{i2}] -> tgt[{j1}:{j2}]")
        print("  SRC:", source_norm[i1:i2])
        print("  TGT:", target_norm[j1:j2])

    print("=== END DEBUG ===")


# ============================================================
# MAIN
# ============================================================

def parse_args(argv):
    src = None
    tgt = None
    fix = False
    output = None
    debug = False
    list_mode = LIST_NORM_SILENT
    blockquote_mode = BLOCKQUOTE_NORM_ON
    batch_mode = False
    aligned_tsv_path = None   # <-- AJOUT : par défaut, rien

    positional = []
    i = 0
    while i < len(argv):
        arg = argv[i]

        if arg == "--fix":
            fix = True
            i += 1

        elif arg == "--output":
            output = argv[i + 1]
            i += 2

        elif arg == "--debug":
            debug = True
            i += 1

        elif arg == "--list-normalization-mode":
            list_mode = argv[i + 1]
            i += 2

        elif arg == "--normalize-blockquotes":
            blockquote_mode = argv[i + 1]
            i += 2

        elif arg == "--batch":
            batch_mode = True
            i += 1

        elif arg == "--aligned":                     # <-- AJOUT
            aligned_tsv_path = argv[i + 1]           # <-- AJOUT
            i += 2                                    # <-- AJOUT

        else:
            positional.append(arg)
            i += 1

    if len(positional) < 2:
        raise SystemExit(
            "Usage: mdstructdiff.py source.md target.md "
            "[--fix --output file] "
            "[--aligned file.aligned.tsv] "           # <-- AJOUT
            "[--debug] "
            "[--list-normalization-mode silent|annotated|warning] "
            "[--normalize-blockquotes on|off] "
            "[--batch]"
        )

    return (
        positional[0],
        positional[1],
        fix,
        output,
        debug,
        list_mode,
        blockquote_mode,
        batch_mode,
        aligned_tsv_path,                             # <-- AJOUT
    )


def main():
    src, tgt, do_fix, out, debug, list_mode, blockquote_mode, batch_mode, aligned_tsv_path = parse_args(sys.argv[1:])

    source_raw, source_norm = normalize_file(src, list_mode, blockquote_mode)
    target_raw, target_norm = normalize_file(tgt, list_mode, blockquote_mode)

    if debug:
        debug_dump(src, tgt, source_raw, source_norm, target_raw, target_norm)

    if do_fix:
        fixed = fix_file(source_raw, source_norm, target_raw, target_norm, aligned_tsv_path)

        ok, warnings = validate_output(fixed)

        if not ok:
            print(f"\n❌ Validation failed for {tgt}:", file=sys.stderr)
            for w in warnings:
                print("  - " + w, file=sys.stderr)

            if not batch_mode:
                sys.exit(1)
            else:
                print("⚠️  Skipping file due to validation errors (batch mode).", file=sys.stderr)
                return

        if out:
            with open(out, "w", encoding="utf-8") as f:
                f.write("\n".join(fixed) + "\n")
        else:
            with open(tgt, "w", encoding="utf-8") as f:
                f.write("\n".join(fixed) + "\n")

        return

    sm = difflib.SequenceMatcher(a=source_norm, b=target_norm)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        print(f"{tag:7s} src[{i1}:{i2}] -> tgt[{j1}:{j2}]")
        print("  SRC:", source_norm[i1:i2])
        print("  TGT:", target_norm[j1:j2])


if __name__ == "__main__":
    main()
