---
# cSpell:locale de
alias: bef-nach
---

# `NACH`

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

Der Befehl hat ein besonderes Verhalten, was [Defaultbefehle][bef-default] betrifft, also Befehle, die die Einheit in der Folgewoche in der [Zugvorlage][befehl] bekommt: Der NACH-Befehl wird nicht in die Vorlage übernommen.  
Stattdessen werden die langen Befehle übernommen, die die Einheit in der letzten Woche in der Vorlage hatte.

Vorlage:

```text
LERNE Reiten
@GIB x 100 Silber
```

Eingeschickte Befehle

```text
NACH w
```

Vorlage nächste Woche:

```text
LERNE Reiten
```text

## Siehe auch

- [Reisen][reisen]
- [`ROUTE`][bef-route]
- [`FOLGE`][bef-folge]
- [`DEFAULT`][bef-default]

<!-- From [https://wiki.eressea.de/index.php?title=NACH&oldid=16729] -->

[bef-default]: [[bef-default]]
[bef-folge]: [[bef-folge]]
[bef-route]: [[bef-route]]
