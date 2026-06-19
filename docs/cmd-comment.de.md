---
# cSpell:locale de
alias: bef-kommentar
---

# KOMMENTAR (;)

Das Semikolon ";" dient in Eressea-Befehlen der Markierung (temporärer) Kommentare. Einige dieser Kommentare werden "automatisch" eingefügt. Die Standard-[Zugvorlage][befehl] enthält zum Beispiel immer die Namen von Regionen und Einheiten, die Anzahl der Personen und deren Silbervorrat als Kommentar. Außerdem werden Kommentare auch genutzt, um dem Programm [[echeck]] bestimmte Informationen mitzuteilen, wie etwa den Lohn in einer Region.

```text
ERESSEA abcd "hier_passwort_eintragen"

; ECHECK -l -w4 -r90 -v4.01

REGION 85,-48 ; Dunkelland
; ECheck Lohn 15

EINHEIT ub2;    Handwerker [3,30$]
    LERNEN Holzfällen
    // LERNEN Schiffbau AUF T2 oder 3
```

Verwendet man das Programm [[vorlage]] zur Erzeugung einer Zugvorlage, so werden über diese Kommentare vielfältige Informationen an den Spieler übermittelt:

```text
REGION 85,-48 ; Dunkelland (Ebene, 290 Personen, 4270$ Silber)
; ECheck Lohn 15
;  . .  |Bauern:       8534 +9|Silber: 47588297 +48400|Unterhalt: 2379414 +2420|
; . E w |Rekruten:      213 +0|Pferde:     2532     -8|Gewinn:      51204   +54|
;  . .  |Pl. frei:     1466 -9|                       |                        |
;       |Gewürz:        125 +0|Juwel:       175     +0|Myrrhe:        125    +0|
;       |Öl:             75 +0|Seide:       150     +0|Weihrauch:     100    +0|
; Prod.: Balsam:     -4   +0    max. handelbar: 85
; Straße (100%) in Osten
; Regionseinnahmen:  2660 Silber
; Nahrungskosten:    2900 Silber
; Materialpool: 4270 Silber, 1 Speer

; -   -   -   -   -   -   -   -   -   -   -   -
; Auf freiem Feld:

EINHEIT ub2;  Handwerker [3,0$] flieht
; Gew: 60.00GE  Gehen: 32.40GE/32.40GE
; Holzfällen 2
    LERNEN Holzfällen
    // LERNEN Holzfällen AUF T3
```

Auch der Spieler selbst kann hinter einem Semikolon Kommentare einfügen.
Da diese Kommentare aber nicht in die Vorlage der nächsten Woche übernommen werden, sind dauerhafte Kommentare nach [`//`][bef-kommentar-mit-schraegstrichen] in der Regel sinnvoller.

Um Übertragungskapazität zu sparen, können temporäre Kommentare vor dem Versenden der Befehle entfernt werden.
Dies erledigen manche Tools wie [Magellan][magellan-de-id]oder VPP.

## Externe Links

- [Vorlage und VPP auf Gulrak.de]

<!-- From [https://wiki.eressea.de/index.php?title=;&oldid=16702] -->

[Vorlage und VPP auf Gulrak.de]: http://www.gulrak.de/eressea/tools.html

[bef-kommentar-mit-schraegstrichen]: [[bef-kommentar-mit-schraegstrichen]]
