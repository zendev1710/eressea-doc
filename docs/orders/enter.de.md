---
# cSpell:locale de
alias: bef-betrete
---

# `BETRETE`

**`BETRETE`**` BURG `*`gebäude-nr`*  
**`BETRETE`**` SCHIFF `*`schiff-nr`*  

Betritt das angegebene [Gebäude][gebaude-id] oder [Schiff][schiff].  
Die Einheit mit dem [Kommando][einheiten-und-gebaude] über das Gebäude oder Schiff muss den Zutritt erlauben.  
Das tut sie, wenn sie zur eigenen Partei gehört, [`HELFE BEWACHE`][bef-helfe] für die eigene Partei gesetzt hat oder in dieser Runde den [`KONTAKTIERE`][bef-kontaktiere] Befehl für die Einheit gibt.  
Anderenfalls wird der Zutritt verweigert.

Ein BETRETE impliziert [`VERLASSE`][bef-verlasse], wenn die Einheit sich auf einem Schiff oder in einem Gebäude befindet.

<!-- TODO: exclude E3 from documentation -->
**[E3A — Das Dritte Zeitalter][das-dritte-zeitalter]**

Ein Ausnahme sind Gebäudebesitzer. Diese müssen entweder ein explizites [`VERLASSE`][bef-verlasse] setzen, oder [GIB][bef-gib] KOMMANDO verwenden.

BETRETE hat immer Vorrang vor [`VERLASSE`][bef-verlasse], wenn beide Befehle gegeben werden.

Es ist durchaus möglich, auf hoher See von einem Schiff auf ein anderes zu wechseln.

Spielererfahrung: Solthar Um in E3 ein Gebäude zu verlassen und gleichzeitig das Kommando weiterzugeben, kann man Folgendes machen:

```text
VERLASSE
BETRETE BURG b2
GIB u2 KOMMANDO
```

<!-- From [https://wiki.eressea.de/index.php?title=BETRETE&oldid=7174] -->

[bef-gib]: [[bef-gib]]
[bef-helfe]: [[bef-helfe]]
[bef-kontaktiere]: [[bef-kontaktiere]]
[bef-verlasse]: [[bef-verlasse]]
