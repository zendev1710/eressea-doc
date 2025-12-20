#!/usr/bin/env python3
import subprocess
import sys
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

PIPELINE_SCRIPT = "./translate_pipeline.sh"

class TranslationGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pipeline de traduction Markdown")
        self.geometry("600x300")

        self.src_file = tk.StringVar()
        self.tgt_file = tk.StringVar()
        self.src_lang = tk.StringVar(value="de")
        self.tgt_lang = tk.StringVar(value="fr")

        self.create_widgets()

    def create_widgets(self):
        pad = {"padx": 10, "pady": 5}

        # Source
        tk.Label(self, text="Fichier source (original):").grid(row=0, column=0, sticky="w", **pad)
        tk.Entry(self, textvariable=self.src_file, width=50).grid(row=0, column=1, **pad)
        tk.Button(self, text="Parcourir", command=self.browse_src).grid(row=0, column=2, **pad)

        # Cible
        tk.Label(self, text="Fichier cible (traduction):").grid(row=1, column=0, sticky="w", **pad)
        tk.Entry(self, textvariable=self.tgt_file, width=50).grid(row=1, column=1, **pad)
        tk.Button(self, text="Parcourir", command=self.browse_tgt).grid(row=1, column=2, **pad)

        # Langues
        tk.Label(self, text="Langue source:").grid(row=2, column=0, sticky="w", **pad)
        src_cb = ttk.Combobox(self, textvariable=self.src_lang, values=["de", "fr", "en"], width=5, state="readonly")
        src_cb.grid(row=2, column=1, sticky="w", **pad)

        tk.Label(self, text="Langue cible:").grid(row=3, column=0, sticky="w", **pad)
        tgt_cb = ttk.Combobox(self, textvariable=self.tgt_lang, values=["de", "fr", "en"], width=5, state="readonly")
        tgt_cb.grid(row=3, column=1, sticky="w", **pad)

        # Bouton lancer
        tk.Button(self, text="Lancer le pipeline", command=self.run_pipeline).grid(row=4, column=0, columnspan=3, pady=20)

        # Log
        self.log = tk.Text(self, height=6)
        self.log.grid(row=5, column=0, columnspan=3, sticky="nsew", **pad)
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def browse_src(self):
        path = filedialog.askopenfilename(filetypes=[("Markdown", "*.md"), ("Tous", "*.*")])
        if path:
            self.src_file.set(path)

    def browse_tgt(self):
        path = filedialog.askopenfilename(filetypes=[("Markdown", "*.md"), ("Tous", "*.*")])
        if path:
            self.tgt_file.set(path)

    def run_pipeline(self):
        src = self.src_file.get()
        tgt = self.tgt_file.get()
        s_lang = self.src_lang.get()
        t_lang = self.tgt_lang.get()

        if not src or not tgt:
            messagebox.showerror("Erreur", "Veuillez sélectionner un fichier source et un fichier cible.")
            return

        cmd = [PIPELINE_SCRIPT, src, tgt, s_lang, t_lang]
        self.log.insert("end", f"> {' '.join(cmd)}\n")
        self.log.see("end")

        try:
            proc = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
            )
            for line in proc.stdout:
                self.log.insert("end", line)
                self.log.see("end")
                self.update_idletasks()
            proc.wait()
            if proc.returncode == 0:
                messagebox.showinfo("Terminé", "Pipeline exécuté avec succès.\nVoir alignment.txt.")
            else:
                messagebox.showerror("Erreur", f"Le pipeline a échoué (code {proc.returncode}).")
        except FileNotFoundError:
            messagebox.showerror("Erreur", f"Script introuvable : {PIPELINE_SCRIPT}")

if __name__ == "__main__":
    app = TranslationGUI()
    app.mainloop()
