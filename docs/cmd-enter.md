---
# cSpell:locale en
alias:
    name: cmd-enter
    text: ENTER
---
# ENTER

**`ENTER`**` BURG `*`building-id`*  
**`ENTER`**` SCHIFF `*`ship-id`*

Betritt das angegebene [Gebäude] oder [Schiff]. Die Einheit mit dem [Kommando] über das Gebäude oder Schiff muss den Zutritt erlauben. Das tut sie, wenn sie zur eigenen Partei gehört, [[cmd-help]] GUARD für die eigene Partei gesetzt hat oder in dieser Runde den [[cmd-contact]] Befehl für die Einheit gibt. Anderenfalls wird der Zutritt verweigert.

Ein ENTER impliziert [[cmd-leave]], wenn die Einheit sich auf einem Schiff oder in einem Gebäude befindet.

**[E3A — Das Dritte Zeitalter]**

Ein Ausnahme sind Gebäudebesitzer. Diese müssen entweder ein explizites [[cmd-leave]] setzen, oder [[cmd-give]] KOMMANDO verwenden.

ENTER hat immer Vorrang vor [[cmd-leave]], wenn beide Befehle gegeben werden.

Es ist durchaus möglich, auf hoher See von einem Schiff auf ein anderes zu wechseln.

Spielererfahrung: Solthar Um in E3 ein Gebäude zu verlassen und gleichzeitig das Kommando weiterzugeben, kann man Folgendes machen:

```
 LEAVE
 ENTER BURG b2
 GIVE u2 KOMMANDO
```

<!-- From [https://wiki.eressea.de/index.php?title=ENTER&oldid=7174] -->

[Gebäude]: ./buildings.md
[Schiff]: ./ships.md
[Kommando]: ./buildings.md#units-and-buildings
[HELP]: ./cmd-help.md
[CONTACT]: ./cmd-contact.md
[LEAVE]: ./cmd-leave.md
[E3A — Das Dritte Zeitalter]: ./the-third-age.md
[GIVE]: ./cmd-give.md
