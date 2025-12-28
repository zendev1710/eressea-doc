---
# cSpell:locale de
alias: bef-default
---
# DEFAULT

**`DEFAULT`**`"`*`befehl`*`"`

`DEFAULT` ändert den [[befehl]], den eine Einheit normalerweise *in der nächsten Woche* ausführen würde:

## Zugvorlage und Defaultbefehle

Nachdem ich meine Befehle eingeschickt habe und der Server die Auswertung erstellt hat, kommen für jede Einheit bestimmte Befehle zurück.
Das sind die Defaultbefehle.
Sie werden in der nächsten Woche ausgeführt, falls du *für diese Einheit* keine Befehle einschickst.
Die Defaultbefehle bekommst du mit dem Report als Textdatei (auch Zugvorlage oder Befehlsvorlage genannt) zugeschickt, falls du sie nicht mit [[bef-option|`ZUGVORLAGE NICHT`]] abgeschaltet hast.
Außerdem sind sie im Computerreport (CR) enthalten.
Der Normalreport (NR) enthält immer nur den ersten langen Defaultbefehl. Man kann dort also nicht alle Defaultbefehle sehen.

In die Defaultbefehle einer Einheit werden normalerweise alle [langen Befehle] übernommen.
Ausgenommen davon sind `ATTACKIERE`, `FOLGE` und `NACH`.
Außerdem werden alle [kommentar-mit-schraegstrichen|`//`]-Kommentare und alle Befehle, die mit @ beginnen übernommen.
Die Schreibweise wird dabei möglicherweise standardisiert.

Eingeschickte Befehle:

```text
EINHEIT abc
; diese Woche nur 10
kAufe 10 Bals
VERKAUFE 100 Öl
// nächste Woche mehr Balsam kaufen
@GIB xyz ALLES Balsam ; Transporter
GIB abc 100 Silber
REKRUTIERE 1
```

Defaultbefehle der nächsten Woche

```text
EINHEIT abc
KAUFE 10 Bals
VERKAUFE 100 Öl
// nächste Woche mehr Balsam kaufen
@GIB xyz ALLES Balsam ; Transporter
```

Was passiert, wenn die Einheit illegalerweise mehrere lange Befehle bekommen hat (zum Beispiel LERNE und ARBEITE), ist übrigens nicht genau definiert.
Das Gleiche gilt für sonstige ungültige Befehle.

## Der Befehl DEFAULT

Der Befehl DEFAULT ändert dieses Verhalten, indem die Defaultbefehle, die vom Server zurückkommen, verändert werden.
Wenn die Einheit einen `DEFAULT`-Befehl bekommen hat, werden ihre **langen** Befehle nicht in die Vorlage übernommen.
[[kommentar-mit-schraegstrichen|Lange Kommentare]] (mit `//`) und kurze `@`-Befehle werden dagegen übernommen.
Die gegebenen Befehle werden dabei bis zu einem gewissen Grade validiert.
Ungültige Befehle werden also nicht übernommen.
Diese Prüfung hat jedoch Grenzen, es ist besser, sich nicht darauf zu verlassen.

Man kann auch kurze Befehle mit dem Befehl `DEFAULT` einfügen.

Eingeschickte Befehle:

```text
EINHEIT abc
; diese Woche nur 10
Kaufe 10 Balsam
VERKAUFE 100 Öl
// nächste Woche lernen
@GIB xyz ALLES Balsam ; Transporter
GIB abc 100 Silber
REKRUTIERE 1
DEFAULT "GIB 123 50 Silber; nicht vergessen"
DEFAULT "LERNE Handel" ; löscht KAUFE und VERKAUFE
DEFAULT "XXX" ; kein Befehl, wird nicht übernommen
```

Defaultbefehle der nächsten Woche

```text
EINHEIT abc
GIB 123 50 Silber; nicht vergessen
LERNE Handel
// nächste Woche lernen
@GIB xyz ALLES Balsam ; Transporter
```

Falls deine Defaultbefehle Anführungszeichen enthalten müssen, gibt es ein paar Wege, das derzeit zu erreichen:

```text
DEFAULT "ZAUBERE 'Erschaffe einen Ring der Unsichtbarkeit'"
DEFAULT 'ZAUBERE "Erschaffe einen Ring der Unsichtbarkeit"'
DEFAULT "BENENNE EINHEIT \"Bob's Builders\""
DEFAULT "MACHE 1 'Wasser des Lebens'"
```

## Der Befehl NACH

Der NACH-Befehl spielt eine besondere Rolle: Er wird nicht in die Vorlage übernommen.
Stattdessen werden die langen Befehle übernommen, die die Einheit in der letzten Woche in der Vorlage hatte, allerdings nur lange Befehle.

Defaultbefehle:

```text
LERNE Reiten
@GIB 0 10 Silber
// no comment
```

Eingeschickte Befehle:

```text
NACH o
```

Defaultbefehle der nächsten Woche:

```text
LERNE Reiten
```

Was passiert, wenn sowohl NACH als auch DEFAULT im Spiel ist?

Vorlage:

```text
ARBEITE
// jetzt nach westen
```

Eingeschickte Befehle:

```text
DEFAULT "LERNE Ausdauer"
// nun lernen
NACH w
```

Defaultbefehle der nächsten Woche:

```text
LERNE Ausdauer
// nun lernen
```

`DEFAULT` löscht also auch hier die *langen* Defaultbefehle (hier `ARBEITE`) und setzt sie neu.

Es ist möglich, NACH mit DEFAULT zu setzen.

Vorlage:

```text
ARBEITE
@GIB 0 1 Silber
```

Eingeschickte Befehle:

```text
DEFAULT "NACH o"
ARBEITE
@GIB 0 2 Silber
```

Defaultbefehle der nächsten Woche:

```text
NACH o
@GIB 0 2 Silber
```

Defaultbefehle der übernächsten Woche, wenn sonst keine Befehle für die Einheit eingeschickt werden:

```text
@GIB 0 2 Silber
```

Auch hier würde die Einheit also dann keinen langen Befehl ausführen.

!!! note
    Es gibt eine Obergrenze an Befehlen, die für eine Einheit gespeichert werden.
    Diese liegt derzeit bei 128 Befehlen, was für die meisten Zwecke leicht ausreichen sollte.

Spielererfahrung (Solthar):

`DEFAULT DEFAULT` ???

Ist es möglich, `DEFAULT`-Befehle zu schachteln, um für mehrere Wochen im Voraus Befehle zu machen?
Nun, so etwas wie `DEFAULT "DEFAULT 'LERNE Ausdauer'"` funktioniert anscheinend, wie man es erwarten würde, aber die Spielleitung möchte lieber keine Garantien dafür abgeben.
Bitte schicke keine Bugreports ein, falls so etwas nicht so klappt, wie du erwartet hast.
Für solche Vorhaben sind Scriptsprachen wie [[vorlage]], [[extendedcommands]] oder [[fftools2]] besser geeignet.

## Siehe auch

- [[befehl]]
- [[befehle-einschicken]]

<!-- From [https://wiki.eressea.de/index.php?title=DEFAULT&oldid=16788] -->

[langen Befehle]: ./commands.md#kurze-und-lange-befehle
