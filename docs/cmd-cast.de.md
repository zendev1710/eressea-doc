---
# cSpell:locale de
alias: bef-zaubere
---

# ZAUBERE

*[kurzer befehl][kurze-und-lange-befehle][^1]*.  

**`ZAUBERE`**` [REGION `*`x`*` `*`y`*`] [STUFE`*`nr`*`] "`*`Zauberspruch`*`" [`*`parameter`*`] ...`  

Mit diesem Befehl wird eine Magiereinheit versuchen, den genannten Zauberspruch zu zaubern.

!!! warning "Achtung"
    Die Modifikatoren REGION und STUFE sind nicht für jeden Zauber zutreffend.

REGION kann nur bei [Fernzaubern][fernzauber] verwendet werden und STUFE macht nur bei Zaubersprüchen mit variablen [Kosten][komponenten] Sinn.
Manche Zauber haben noch weitere Parameter.

Die Anwendung der Zauber ist zum einen im Kapitel [Magie][magie-de-id] genauer erklärt, zum anderen ist sie bei der Zauberbeschreibung selbst zu finden.
Diese erhält man, wenn man den Zauber neu erhält und kann ihn sich mit [`ZEIGE ALLE ZAUBER`][bef-zeige] nochmal anzeigen lassen.

Kampfzauber können nicht einfach so gezaubert werden.
Will man diese gegen eine Einheit verwenden, muß man den [`KAMPFZAUBER`][bef-kampfzauber] setzen und dann eine Einheit [attackieren][bef-attackiere] oder attackiert werden.
Dies kann allerdings zu größeren Schlachten führen!

[^1]: ZAUBERE ist zwar kein langer Befehl, er schließt aber weitere lange Befehle aus. Man kann aber weitere Zauber sprechen.

<!-- From [https://wiki.eressea.de/index.php?title=ZAUBERE&oldid=16737] -->

[bef-attackiere]: [[bef-attackiere]]
[bef-kampfzauber]: [[bef-kampfzauber]]
[bef-zeige]: [[bef-zeige]]
