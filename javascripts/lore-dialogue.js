document$.subscribe(() => {
  const blocks = document.querySelectorAll("div.lore-dialogue");
  const lang = document.documentElement.lang || "fr";

  const rules = {
    fr: { open: "« ", close: " »", dash: "— ", italic: true },
    en: { open: "“", close: "”", dash: "", italic: false },
    de: { open: "„", close: "“", dash: "", italic: false }
  };

  const R = rules[lang] || rules.fr;

  function normalizeEllipses(text) {
    return text.replace(/\.{3,}/g, "…");
  }

  function renderSpeech(s) {
    const dash = s.isRep ? R.dash : "";
    const spoken = R.italic
      ? `<span class="rep-part">${s.spoken}</span>`
      : s.spoken;

    let incise = "";
    if (s.incise) {
      const trimmed = s.incise.trim();
      if (trimmed.startsWith(",")) {
        incise = ` <span class="nar-part">${trimmed}</span>`;
      } else if (/^[A-Za-zÀ-ÿ]/.test(trimmed)) {
        incise = `, <span class="nar-part">${trimmed}</span>`;
      } else {
        incise = ` <span class="nar-part">${trimmed}</span>`;
      }
    }

    return `<p class="${s.isRep ? "rep" : "mono"}">${dash}${R.open}${spoken}${R.close}${incise}</p>`;
  }

  blocks.forEach(block => {
    const lines = block.innerHTML.trim().split("\n").map(l => l.trim());
    const htmlParts = [];

    let speechOpen = false;
    let speechBuffer = "";
    let speechIsRep = false;

    lines.forEach(line => {
      if (line === "") {
        if (speechOpen) {
          speechBuffer += "<br>";
        } else {
          htmlParts.push(`<p class="blank-line"></p>`);
        }
        return;
      }

      // Si on est déjà dans une prise de parole multi-ligne
      if (speechOpen) {
        const closingIndex = line.indexOf('"');

        if (closingIndex === -1) {
          speechBuffer += "<br>" + line;
          return;
        }

        speechBuffer += "<br>" + line.slice(0, closingIndex);
        const incise = line.slice(closingIndex + 1).trim();

        const parsed = {
          spoken: normalizeEllipses(speechBuffer.trim()),
          incise,
          isRep: speechIsRep
        };

        htmlParts.push(renderSpeech(parsed));

        speechOpen = false;
        speechBuffer = "";
        speechIsRep = false;
        return;
      }

      // Pas en multi-ligne : on regarde si la ligne commence par une prise de parole
      const isRep = line.startsWith("—");
      const raw = isRep ? line.replace(/^—\s*/, "") : line;
      const startsWithQuote = raw.startsWith('"');

      if (startsWithQuote) {
        // Est-ce que la ligne contient aussi un guillemet fermant ?
        const secondQuoteIndex = raw.indexOf('"', 1);

        if (secondQuoteIndex !== -1) {
          // Cas simple : tout est sur une seule ligne
          const m = raw.match(/^"\s*([^"]*)"\s*(.*)$/);
          if (m) {
            const parsed = {
              spoken: normalizeEllipses(m[1].trim()),
              incise: m[2].trim(),
              isRep
            };
            htmlParts.push(renderSpeech(parsed));
            return;
          }
        } else {
          // Pas de guillemet fermant → début de multi-ligne
          speechOpen = true;
          speechIsRep = isRep;
          speechBuffer = raw.slice(1); // après le " ouvrant
          return;
        }
      }

      // Sinon : narration
      htmlParts.push(`<p class="nar">${line}</p>`);
    });

    // Post-traitement : ajouter lignes vides autour des dialogues
    const finalParts = [];
    for (let i = 0; i < htmlParts.length; i++) {
      const curr = htmlParts[i];
      const prev = htmlParts[i - 1];
      const next = htmlParts[i + 1];

      const isRep = curr.includes('class="rep"') || curr.includes('class="mono"');
      const isNar = curr.includes('class="nar"');

      // Ajouter espace AVANT une réplique si précédée de narration
      if (isRep && prev && prev.includes('class="nar"')) {
        if (!prev.includes('blank-line')) {
          finalParts.push('<p class="blank-line"></p>');
        }
      }

      finalParts.push(curr);

      // Ajouter espace APRÈS une réplique si suivie de narration
      if (isRep && next && next.includes('class="nar"')) {
        if (!next.includes('blank-line')) {
          finalParts.push('<p class="blank-line"></p>');
        }
      }
    }

    block.innerHTML = htmlParts.join("");
  });
});
