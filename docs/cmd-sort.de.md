---
alias: bef-sortiere
---
# SORTIERE

**`SORTIERE`**` VOR `*`einheit-nr`*  
**`SORTIERE`**` HINTER `*`einheit-nr`*

Mit diesem Befehl ändert man die Reihenfolge, in der eigene Einheiten im Report und der [Zugvorlage] auftauchen. Dies ist nützlich, um z.B. Schüler und Lehrer direkt untereinander stehen zu haben. Folgende Einschränkungen gibt es:

- *`einheit-nr`* muß eine eigene Einheit sein.
- Man kann sich nicht in ein Gebäude oder ein Schiff rein- oder raussortieren. Beide Einheiten müssen entweder in demselben Gebäude bzw. demselben Schiff sein, oder beide außerhalb.
- Man kann sich nicht VOR einen Gebäudebesitzer oder Schiffskapitän einsortieren. Dafür nutzt man den Befehl [GIB einheit-nr KOMMANDO]
- Ein Gebäudebesitzer oder Schiffskapitän kann den Befehl gar nicht benutzen.

Die Sortierung erfolgt ganz am Ende der Runde, nach der Bewegung. Man kann also Einheiten, die mittels [[bef-nach]] oder [[bef-fahre]] in die Region gelangt sind, gleich passend einsortieren.

<!-- From [https://wiki.eressea.de/index.php?title=SORTIERE&oldid=16704] -->

[Zugvorlage]: ./commands.md "Befehl"
[GIB einheit-nr KOMMANDO]: ./cmd-give.md "GIB"
[bef-nach]: ./cmd-move.md "NACH"
[bef-fahre]: ./cmd-ride.md "FAHRE"
