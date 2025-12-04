# BETRETE

**`BETRETE`**` BURG `*`gebäude-nr`*  
**`BETRETE`**` SCHIFF `*`schiff-nr`*

Betritt das angegebene [Gebäude] oder [Schiff]. Die Einheit mit dem [Kommando] über das Gebäude oder Schiff muss den Zutritt erlauben. Das tut sie, wenn sie zur eigenen Partei gehört, [HELFE] BEWACHE für die eigene Partei gesetzt hat oder in dieser Runde den [KONTAKTIERE] Befehl für die Einheit gibt. Anderenfalls wird der Zutritt verweigert.

Ein BETRETE impliziert [VERLASSE], wenn die Einheit sich auf einem Schiff oder in einem Gebäude befindet.

**[E3A — Das Dritte Zeitalter]**

Ein Ausnahme sind Gebäudebesitzer. Diese müssen entweder ein explizites [VERLASSE] setzen, oder [GIB] KOMMANDO verwenden.

BETRETE hat immer Vorrang vor [VERLASSE], wenn beide Befehle gegeben werden.

Es ist durchaus möglich, auf hoher See von einem Schiff auf ein anderes zu wechseln.

Spielererfahrung: Solthar Um in E3 ein Gebäude zu verlassen und gleichzeitig das Kommando weiterzugeben, kann man Folgendes machen:

```
 VERLASSE
 BETRETE BURG b2
 GIB u2 KOMMANDO
```

<!-- From [https://wiki.eressea.de/index.php?title=BETRETE&oldid=7174] -->

[Gebäude]: ./buildings.md "Gebäude"
[Schiff]: ./ships.md "Schiff"
[Kommando]: ./buildings.md#einheiten-und-gebäude "Gebäude"
[HELFE]: ./cmd-help.md "HELFE"
[KONTAKTIERE]: ./cmd-contact.md "KONTAKTIERE"
[VERLASSE]: ./cmd-leave.md "VERLASSE"
[E3A — Das Dritte Zeitalter]: ./the-third-age.md "Das dritte Zeitalter"
[GIB]: ./cmd-give.md "GIB"
