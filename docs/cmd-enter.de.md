---
# cSpell:locale de
alias: bef-betrete
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# BETRETE

**`BETRETE`**` BURG `*`gebäude-nr`*  
**`BETRETE`**` SCHIFF `*`schiff-nr`*  

Betritt das angegebene [Gebäude] oder [Schiff]. Die Einheit mit dem [Kommando][einheiten-und-gebaude] über das Gebäude oder Schiff muss den Zutritt erlauben. Das tut sie, wenn sie zur eigenen Partei gehört, [[bef-helfe]] BEWACHE für die eigene Partei gesetzt hat oder in dieser Runde den [[bef-kontaktiere]] Befehl für die Einheit gibt. Anderenfalls wird der Zutritt verweigert.

Ein BETRETE impliziert [[bef-verlasse]], wenn die Einheit sich auf einem Schiff oder in einem Gebäude befindet.

<!-- TODO: exclude E3 from documentation -->
**[E3A — Das Dritte Zeitalter]**

Ein Ausnahme sind Gebäudebesitzer. Diese müssen entweder ein explizites [[bef-verlasse]] setzen, oder [[bef-gib]] KOMMANDO verwenden.

BETRETE hat immer Vorrang vor [[bef-verlasse]], wenn beide Befehle gegeben werden.

Es ist durchaus möglich, auf hoher See von einem Schiff auf ein anderes zu wechseln.

Spielererfahrung: Solthar Um in E3 ein Gebäude zu verlassen und gleichzeitig das Kommando weiterzugeben, kann man Folgendes machen:

```text
VERLASSE
BETRETE BURG b2
GIB u2 KOMMANDO
```

<!-- From [https://wiki.eressea.de/index.php?title=BETRETE&oldid=7174] -->

[Gebäude]: ./buildings.md
[Schiff]: ./ships.md
[bef-helfe]: ./cmd-help.md
[bef-kontaktiere]: ./cmd-contact.md
[bef-verlasse]: ./cmd-leave.md
[bef-gib]: ./cmd-give.md
<!-- TODO: exclude E3 from documentation -->
[E3A — Das Dritte Zeitalter]: ./the-third-age.md
