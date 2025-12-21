#!/usr/bin/env python3
import re
import sys

def is_heading(line):
    return line.lstrip().startswith("#")

def is_list_item(line):
    stripped = line.lstrip()
    return (
        stripped.startswith("- ")
        or stripped.startswith("* ")
        or stripped.startswith("+ ")
        or re.match(r"^\s*\d+\.\s+", stripped)
    )

def is_blockquote(line):
    return line.lstrip().startswith(">")

def is_table_row(line):
    return "|" in line and line.strip().startswith("|")

def is_code_fence(line):
    return line.strip().startswith("```")

def extract_yaml_front_matter(lines):
    """
    Extrait le YAML front-matter si présent.
    Retourne (yaml_lines, content_lines).
    """
    if not lines or not lines[0].strip() == "---":
        return [], lines

    yaml = []
    content = []
    in_yaml = True

    for i, line in enumerate(lines):
        yaml.append(line)
        if i > 0 and line.strip() == "---":
            content = lines[i+1:]
            break

    return yaml, content

SENTENCE_END = re.compile(r"([.!?])\s+")

def split_paragraph_into_sentences(text):
    """
    Segmente un paragraphe en phrases.
    """
    parts = SENTENCE_END.split(text)
    sentences = []

    for i in range(0, len(parts), 2):
        if i+1 < len(parts):
            sentence = parts[i] + parts[i+1]
        else:
            sentence = parts[i]

        sentence = sentence.strip()
        if sentence:
            sentences.append(sentence)

    return sentences

def segment_content(lines):
    result = []
    in_codeblock = False

    for line in lines:

        # 1) Lignes vides → on les garde telles quelles
        if line.strip() == "":
            result.append("")
            continue

        # 2) Début/fin de codeblock
        if is_code_fence(line):
            in_codeblock = not in_codeblock
            result.append(line)
            continue

        # 3) Si on est dans un codeblock → ne rien segmenter
        if in_codeblock:
            result.append(line)
            continue

        # 4) Lignes structurelles → ne pas segmenter
        if (
            is_heading(line)
            or is_list_item(line)
            or is_blockquote(line)
            or is_table_row(line)
        ):
            result.append(line)
            continue

        # 5) Sinon → segmentation du paragraphe
        sentences = split_paragraph_into_sentences(line)
        for s in sentences:
            result.append(s)

    return result

def main():
    raw_lines = [line.rstrip("\n") for line in sys.stdin]

    # extraire YAML
    yaml, content = extract_yaml_front_matter(raw_lines)

    # segmenter le contenu
    segmented = segment_content(content)

    # réinsérer YAML tel quel
    for line in yaml:
        print(line)
    for line in segmented:
        print(line)

if __name__ == "__main__":
    main()
