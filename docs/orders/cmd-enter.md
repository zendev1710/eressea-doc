---
alias:
	name: cmd-enter
	text: ENTER
---
# ENTER

**`ENTER`**` BURG `*`gebäude-nr`*  
**`ENTER`**` SCHIFF `*`schiff-nr`*

Betritt das angegebene [Gebäude] oder [Schiff]. Die Einheit mit dem [Kommando] über das Gebäude oder Schiff muss den Zutritt erlauben. Das tut sie, wenn sie zur eigenen Partei gehört, [HELP] GUARD für die eigene Partei gesetzt hat oder in dieser Runde den [CONTACT] Befehl für die Einheit gibt. Anderenfalls wird der Zutritt verweigert.

Ein ENTER impliziert [LEAVE], wenn die Einheit sich auf einem Schiff oder in einem Gebäude befindet.

**[E3A — Das Dritte Zeitalter]**

Ein Ausnahme sind Gebäudebesitzer. Diese müssen entweder ein explizites [LEAVE] setzen, oder [GIVE] KOMMANDO verwenden.

ENTER hat immer Vorrang vor [LEAVE], wenn beide Befehle gegeben werden.

Es ist durchaus möglich, auf hoher See von einem Schiff auf ein anderes zu wechseln.

Spielererfahrung: Solthar Um in E3 ein Gebäude zu verlassen und gleichzeitig das Kommando weiterzugeben, kann man Folgendes machen:

```
 LEAVE
 ENTER BURG b2
 GIVE u2 KOMMANDO
```

<!-- From [https://wiki.eressea.de/index.php?title=ENTER&oldid=7174] -->

[Gebäude]: ./buildings.md "Gebäude"
[Schiff]: ./ships.md "Schiff"
[Kommando]: ./buildings.md#units-and-buildings "Gebäude"
[HELP]: ./cmd-help.md "HELP"
[CONTACT]: ./cmd-contact.md "CONTACT"
[LEAVE]: ./cmd-leave.md "LEAVE"
[E3A — Das Dritte Zeitalter]: ./the-third-age.md "Das dritte Zeitalter"
[GIVE]: ./cmd-give.md "GIVE"
