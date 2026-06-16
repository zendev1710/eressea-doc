---
# cSpell:locale fr
alias: cmd-reserve-fr
---
# RESERVE

**`RESERVE`**` `*`number`*` `*`Item`*  
**`RESERVE`**` ALL `*`Item`*  
**`RESERVE`**` EACH `*`number`*` `*`Item`*  

Cela permet à une unité de prendre et de « sauvegarder » des objets ou de l’argent provenant d’autres unités de la région.  
Il est à noter que l'unité prend ses marchandises dans n'importe quelle unité (généralement de haut en bas selon l'ordre dans le NR), à moins que cette unité n'ait réservé cet objet (voir [[items-pool]] !).  

Avec l'ordre `RESERVE ALL`` `*`Item`*, une unité réserve tout ce qu'elle possède de l'élément spécifié.  

Avec l'ordre `RESERVE EACH`` `*`number`*` `*`Item`*, le nombre d'items spécifié est réservé **par personne**.  

```text
RESERVE EACH 100 Silver
```

Pour une unité de 10 personnes, 100 Silver sont réservés pour chaque personne, soit 1000 Silver réservés au total pour l'unité.  

## Sources d'erreur

- une unité `TEMP` ne peut pas réserver ! Les objets tout comme l'argent doivent leur être donnés en utilisant l'ordre [`GIVE`][cmd-give-fr]
- L'ordre `RESERVE` s'exéute avanr les ordres [`GIVE`][cmd-give-fr] et [`RECRUIT`][cmd-recruit-fr] dans la [[orders-sequence]]. Donc l'instruction `EACH` s'applique sur le nombre de personnes **avant** passation et recrutement
- Si les unités d'une faction réservent plus d'un objet donné que ce qui est disponible dans la région (dans la réserve d'objets) dans son ensemble, le résultat est difficile à prédire. Pour plus de détails, voir [[items-pool]]
- Si le même article est réservé plusieurs fois par une même unité, seule le dernier ordre est valable et pris en compte

## Exemples

Avec :

```text
RESERVE EACH 1 Sword
RESERVE EACH 1 Shield
GIVE depo ALL
```

Une unité peut conserver une arme et un bouclier par personne, même après une bataille perdue, et donner tout le reste (butin) à une unité de dépôt.  

Avec :

```text
@RESERVE 100 Silver
RESERVE 1 Sword
RESERVE 50 Silver
```

L'unité réservera une épée et 50 Silver.  

## Voir aussi

- [[items-pool]]
- [`GIVE`][cmd-give-fr]

<!-- From [https://wiki.eressea.de/index.php?title=RESERVE&oldid=14809] -->

[cmd-give-fr]: [[cmd-give-fr]]
[cmd-recruit-fr]: [[cmd-recruit-fr]]
