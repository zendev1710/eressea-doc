4. README clair pour ton pipeline
Voici un README que tu peux mettre dans ton repo MkDocs.

🧰 Pipeline de traduction Markdown (DE/FR/EN)
Ce projet contient un ensemble d’outils pour :

normaliser le Markdown

comparer la structure entre original et traduction

corriger automatiquement la structure

segmenter en phrases

aligner phrase par phrase

utiliser les dictionnaires cspell pour améliorer l’alignement

📦 Outils inclus
Normalisation
mdnormalize_strict.py

mdnormalize_tolerant.py

Comparaison / correction
mdstructdiff.py

Segmentation
split_sentences.py

Alignement
aligner_simple.py

aligner_advanced.py (avec heuristiques linguistiques + dictionnaires cspell)

Pipeline complet
translate_pipeline.sh

🚀 Usage
1. Lancer le pipeline complet
Code
./translate_pipeline.sh original.md traduction.md de fr
Paramètres :

original.md → fichier source

traduction.md → fichier cible

de → langue source (de|fr|en)

fr → langue cible (de|fr|en)

📄 Fichiers générés
original.md.norm.md → normalisation stricte

traduction.md.norm.md → normalisation stricte

traduction.md.fixed.md → correction structurelle

traduction.md.clean.md → normalisation tolérante

original.sentences.md → segmentation

traduction.sentences.md → segmentation

alignment.txt → alignement phrase par phrase

📚 Dictionnaires cspell
Place tes dictionnaires ici :

custom-dictionary-de.txt

custom-dictionary-fr.txt

custom-dictionary-en.txt

Ils seront automatiquement utilisés par aligner_advanced.py.

🧠 Alignement avancé
L’alignement avancé utilise :

difflib

longueur des phrases

chiffres

noms propres

mots internationaux

dictionnaires cspell

pondération selon la paire de langues

gestion des fusions/scissions