---
# cSpell:locale de
alias: bef-nach
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# NACH

*[Langer Befehl][kurze-und-lange-befehle].*

**`NACH`**` `*`himmelsrichtung`*`[`*`himmelsrichtung`*`]...`  

Mit dem Befehl `NACH` bewegt sich die Einheit durch die Welt von Eressea. Die Himmelsrichtungen sind in Eressea Nordosten, Nordwesten, Osten, Westen, Südosten und Südwesten. Die Koordinaten werden nicht verwendet.

| Richtung   | Abkürzungen |
|------------|-------------|
| Nordosten  | NO, Nordo   |
| Osten      | O           |
| Südosten   | SO, Südo    |
| Nordwesten | NW, Nordw   |
| Westen     | W           |
| Südwesten  | SW, Südw    |

Der Befehl hat ein besonderes Verhalten, was [Defaultbefehle] betrifft, also Befehle, die die Einheit in der Folgewoche in der [Zugvorlage][befehl] bekommt: Der NACH-Befehl wird nicht in die Vorlage übernommen. Stattdessen werden die langen Befehle übernommen, die die Einheit in der letzten Woche in der Vorlage hatte.

Vorlage:

     LERNE Reiten
     @GIB x 100 Silber

Eingeschickte Befehle

     NACH w

Vorlage nächste Woche:

     LERNE Reiten

## Siehe auch

- [Reisen][reisen]
- [[bef-route]]
- [[bef-folge]]
- [[bef-default]][Defaultbefehle]

<!-- From [https://wiki.eressea.de/index.php?title=NACH&oldid=16729] -->

[Defaultbefehle]: [[bef-default]]
[bef-folge]: [[bef-folge]]
[bef-route]: [[bef-route]]
