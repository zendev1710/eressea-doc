---
# cSpell:locale fr
alias: cmd-sort-fr
---
<!-- disable MD052 because of mkdocs autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# SORT

**`SORT`**` BEFORE `*`unit-id`*  
**`SORT`**` AFTER `*`unit-id`*  

Cet ordre modifie l'ordre de tes unités **dans le rapport** et l'[évaluation des ordres][orders].  
Cela permet, par exemple, d'afficher les *élèves* (unités exécutant l'ordre `LEARN`) et les *enseignants* (unités exécutant l'ordre `TEACH`) les uns en dessous des autres.  

!!! info
    L'ordre de tri des unités [a un impact][echapper-a-la-mort-par-famine] en cas de famine.

Les limitations suivantes s'appliquent :

- *`unit-id`* doit être une unité distincte de celle qui exécute l'ordre
- Les deux unités concernées par l'ordre doivent se trouver soit dans le même bâtiment ou bateau, soit toutes deux à l'extérieur
- Il est impossible de placer une unité devant le propriétaire d'un bâtiment ou le capitaine d'un bateau. Utilisez l'ordre [`GIVE`*`unit-id`*`COMMAND`][cmd-give] à cet effet
- Le propriétaire d'un bâtiment ou le capitaine d'un bateau ne peut pas utiliser cet ordre

Le tri s'effectue en toute fin du tour, après les déplacements.  
Ainsi, les unités entrées dans une région par [[cmd-move]] ou [[cmd-ride]] peuvent être triées immédiatement.  
