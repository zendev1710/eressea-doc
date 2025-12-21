#!/usr/bin/env python
import re
import sys

def extract_yaml_front_matter(lines):
    """
    Extrait le YAML front-matter si présent.
    Retourne (yaml_lines, content_lines).
    """
    if not lines or not lines[0].strip() == "---":
        return [], lines  # pas de YAML

    yaml = []
    content = []
    in_yaml = True

    for i, line in enumerate(lines):
        if in_yaml:
            yaml.append(line)
            if i > 0 and line.strip() == "---":
                in_yaml = False
        else:
            content = lines[i:]
            break

    return yaml, content


def is_list_item(line: str) -> bool:
    stripped = line.lstrip()
    return (
        stripped.startswith("- ")
        or stripped.startswith("* ")
        or stripped.startswith("+ ")
        or re.match(r"^\s*\d+\.\s+", stripped)
    )


ABBREVIATIONS = {"e.g.", "i.e.", "etc.", "vs.", "cf.", "resp.", "incl."}
FILE_EXTENSIONS = {".json", ".yaml", ".yml", ".xml", ".ini", ".cfg", ".conf",
                   ".txt", ".md", ".py", ".js", ".ts", ".html", ".css"}

URL_PATTERN = re.compile(r"https?://\S+")
CODE_INLINE_PATTERN = re.compile(r"`[^`]+`")

def ends_with_forbidden_final_dot(line: str) -> bool:
    stripped = line.strip()

    if not stripped.endswith("."):
        return False

    # plusieurs phrases → on ne touche pas
    if stripped.count(".") > 1:
        return False

    # abréviations
    for abbr in ABBREVIATIONS:
        if abbr in stripped:
            return False

    # URLs
    if URL_PATTERN.search(stripped):
        return False

    # code inline
    if CODE_INLINE_PATTERN.search(stripped):
        return False

    # parenthèse finale
    if stripped.endswith(")."):
        return False

    # fichiers
    for ext in FILE_EXTENSIONS:
        if stripped.lower().endswith(ext + "."):
            return False

    return True


def remove_final_dot_in_list_item(line: str) -> str:
    if is_list_item(line) and ends_with_forbidden_final_dot(line):
        return line.rstrip()[:-1]
    return line


def enforce_blank_line_after_heading(lines):
    """
    Ajoute toujours exactement UNE ligne vide après un titre Markdown.
    """
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]
        result.append(line)

        if line.lstrip().startswith("#"):
            # regarder la ligne suivante
            if i + 1 < len(lines):
                next_line = lines[i + 1].rstrip("\n")
                if next_line.strip() != "":
                    # insérer une ligne vide
                    result.append("")
                else:
                    # déjà une ligne vide → on force UNE seule
                    result.append("")
                    i += 1  # sauter la ligne vide existante
            else:
                # fin de fichier → ajouter une ligne vide
                result.append("")

        i += 1

    return result


def normalize_line(line: str) -> str:
    """Applique toutes les normalisations strictes."""
    line = remove_final_dot_in_list_item(line)
    return line


def normalize_content(lines):
    # 1) normalisation ligne par ligne
    normalized = [normalize_line(line) for line in lines]

    # 2) ligne vide obligatoire après les titres
    normalized = enforce_blank_line_after_heading(normalized)

    return normalized


def main():
    raw_lines = [line.rstrip("\n") for line in sys.stdin]

    # extraire YAML
    yaml, content = extract_yaml_front_matter(raw_lines)

    # normaliser contenu
    normalized = normalize_content(content)

    # réinsérer YAML tel quel
    for line in yaml:
        print(line)
    for line in normalized:
        print(line)

if __name__ == "__main__":
    main()

