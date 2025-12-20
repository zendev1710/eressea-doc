#!/usr/bin/env python3
from flask import Flask, render_template_string, request, redirect, url_for
import subprocess
import os

PIPELINE_SCRIPT = "./translate_pipeline.sh"

app = Flask(__name__)

HTML_FORM = """
<!doctype html>
<title>Pipeline de traduction Markdown</title>
<h1>Pipeline de traduction Markdown</h1>
<form method="post">
  <label>Fichier source (chemin absolu ou relatif):</label><br>
  <input type="text" name="src" size="80"><br><br>

  <label>Fichier cible (chemin absolu ou relatif):</label><br>
  <input type="text" name="tgt" size="80"><br><br>

  <label>Langue source:</label>
  <select name="src_lang">
    <option value="de">de</option>
    <option value="fr">fr</option>
    <option value="en">en</option>
  </select>

  <label>Langue cible:</label>
  <select name="tgt_lang">
    <option value="fr">fr</option>
    <option value="de">de</option>
    <option value="en">en</option>
  </select>

  <br><br>
  <button type="submit">Lancer le pipeline</button>
</form>

{% if output %}
<hr>
<h2>Résultat</h2>
<pre>{{ output }}</pre>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    output = None
    if request.method == "POST":
        src = request.form.get("src", "").strip()
        tgt = request.form.get("tgt", "").strip()
        src_lang = request.form.get("src_lang", "de")
        tgt_lang = request.form.get("tgt_lang", "fr")

        if not src or not tgt:
            output = "Erreur : veuillez fournir source et cible."
        elif not os.path.exists(src):
            output = f"Erreur : fichier source introuvable : {src}"
        elif not os.path.exists(tgt):
            output = f"Erreur : fichier cible introuvable : {tgt}"
        else:
            cmd = [PIPELINE_SCRIPT, src, tgt, src_lang, tgt_lang]
            try:
                result = subprocess.run(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    check=False,
                )
                output = result.stdout + f"\nCode retour : {result.returncode}"
            except FileNotFoundError:
                output = f"Erreur : script pipeline introuvable : {PIPELINE_SCRIPT}"

    return render_template_string(HTML_FORM, output=output)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
