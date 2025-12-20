# Pipeline de traduction Markdown (DE/FR/EN)

Ce projet fournit un pipeline complet pour :

- normaliser le Markdown
- comparer la structure entre original et traduction
- corriger automatiquement la structure
- segmenter en phrases
- aligner phrase par phrase
- utiliser les dictionnaires cspell pour améliorer l’alignement linguistique

Il est conçu pour fonctionner dans un workflow MkDocs multilingue (DE/FR/EN).

---

## 🧰 Outils inclus

### Normalisation

- `mdnormalize_strict.py` — normalisation stricte (structure stable)
- `mdnormalize_tolerant.py` — normalisation tolérante (lisibilité)

### Comparaison / correction

- `mdstructdiff.py` — comparaison structurelle + correction automatique

### Segmentation

- `split_sentences.py` — segmentation en phrases (DE/FR/EN)

### Alignement

- `aligner_simple.py` — alignement difflib (rapide, prévisible)
- `aligner_advanced.py` — alignement avancé (heuristiques linguistiques + dictionnaires cspell)

### Pipeline complet

- `translate_pipeline.sh`

---

## 🚀 Utilisation du pipeline

### Commande principale

```bash
./translate_pipeline.sh original.md traduction.md de fr
