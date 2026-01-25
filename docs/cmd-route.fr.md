---
# cSpell:locale fr
alias: cmd-route-fr
---
# `ROUTE`

*Ordre [long].*  

**`ROUTE`**` `*`himmelsrichtung`*`[`*`himmelsrichtung`*`...]`  

Avec cet ordre, l'unité se déplace dans le monde d'Eressea de la même manière qu'avec l'ordre [[cmd-move]].  

Cependant, avec l'odre `ROUTE`, il est possible de planifier une séquence de déplacements, de sorte qu'une unité se déplace toujours de la même façon entre deux points (ou plus), ou effectue un long trajet jusqu'à ce qu'elle atteigne sa destination.  
Tous les déplacements traités sont renvoyés en fin d'ordre `ROUTE`.  

Pour annuler prématurément un déplacement (par exemple pour des navires qui ne sont pas censés naviguer aussi loin qu'ils le pourraient), vous pouvez utiliser une instruction `PAUSE` (abrégé : `P`).  
Une fois qu'une unité a terminé son déplacement, vient ensuite un `PAUSE`, qui est ajouté à la fin de l'ordre, même si l'unité est déjà à l'arrêt.  
Deux instructions `PAUSE` consécutives, quant à elles, garantissent que l'unité s'arrête et ne bouge plus sans l'intervention du joueur.  

Un cavalier peut parcourir trois régions par la route. Il passe l'ordre `ROUTE` suivant :

```text
ROUTE NE East Pause East East SE West West Pause SW West NW
```

Au prochain tour, l'ordre ressemble à ceci :

```text
ROUTE East East SE West West Pause SW West NW NE East Pause
```

Et au tour suivant :

```text
ROUTE West West Pause SW West NW NE East Pause East East SE
```

Et encore au tour suivant :

```text
ROUTE SW West NW NE East Pause East East SE West West Pause
```

Et finalement, l'ordre devient identique à l'ordre initial.

## Voir aussi

- [[travel]]
- [[cmd-move]]
- [[cmd-follow]]

<!-- From [https://wiki.eressea.de/index.php?title=ROUTE&oldid=16732] -->

[long]: ./commands.md#ordres-courts-et-longs
