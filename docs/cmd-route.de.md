---
# cSpell:locale de
alias: bef-route
---
# ROUTE

**`ROUTE`**[<sup>`L`</sup>]` `*`himmelsrichtung`*`[`*`himmelsrichtung`*`...]`  

Mit diesem Befehl bewegt sich die Einheit genauso wie mit dem Befehl [[bef-nach]] durch die Welt von Eressea.

Mit dem `ROUTE`-Befehl kann jedoch eine Bewegungskette erstellen, so dass eine Einheit immer zwischen zwei oder mehr Punkten pendelt oder eine lange Route abarbeitet bis sie am Ziel ist. Alle Bewegungen, die abgearbeitet wurden, werden wieder hinten an den `ROUTE`-Befehl angehängt.

Um eine Bewegung vorzeitig abzubrechen (z.B. bei Schiffen, die nicht so weit segeln sollen, wie sie können), kann man ein `PAUSE` (kann `P` abgekürzt werden) einfügen. Hat eine Einheit ihre Bewegung vollendet und als nächstes kommt ein `PAUSE`, so wird dies mit hinten angehängt, obwohl die Einheit bereits stoppt. Zwei aufeinanderfolgende `PAUSE` Befehle sorgen hingegen dafür, dass die Einheit stoppt und sich ohne Zutun des Spielers nicht mehr weiter bewegt.

Ein Reiter kommt mit Straßen drei Regionen weit. Er bekommt folgenden `ROUTE`-Befehl:

     ROUTE NO Osten Pause Osten Osten SO Westen Westen Pause SW Westen NW

Nächste Runde sieht der Befehl so aus:

     ROUTE Osten Osten SO Westen Westen Pause SW Westen NW NO Osten Pause

Und in der Runde darauf:

     ROUTE Westen Westen Pause SW Westen NW NO Osten Pause Osten Osten SO

Und in der Runde darauf:

     ROUTE SW Westen NW NO Osten Pause Osten Osten SO Westen Westen Pause

Und schließlich wieder wie am Anfang.

## Siehe auch

- [Reisen]
- [[bef-nach]][[bef-nach]]
- [[bef-folge]]

<!-- From [https://wiki.eressea.de/index.php?title=ROUTE&oldid=16732] -->

[<sup>`L`</sup>]: ./commands.md#kurzlang "Befehl"
[bef-nach]: ./cmd-move.md "NACH"
[Reisen]: ./travel.md "Reisen"
[bef-folge]: ./cmd-follow.md "FOLGE"
