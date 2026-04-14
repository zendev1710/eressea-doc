---
# cSpell:locale fr
alias: cmd-enter-fr
---
<!-- disable MD052 because of mkdocs autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# ENTER

**`ENTER`**` BUILDING `*`building-id`*  
**`ENTER`**` SHIP `*`ship-id`*  

Permet d'entrer dans le [[batiments|bâtiment]] ou le [[bateaux|bateau]] spécifié.  

L'unité qui [contrôle][unites-et-batiments] le bâtiment ou le bateau doit autoriser l'accès.  
L'entrée réussit si l'unité propriétaire appartient à une autre faction mais a défini [[cmd-help|`HELP GUARD`]] pour la faction demandant l'entrée, ou si elle donne l'ordre [[cmd-contact]] pour l'unité requérante au même tour de jeu.  
Dans le cas contraire, l'accès sera refusé.

Un ordre `ENTER` nécessite au préalable un ordre [[cmd-leave]] si l'unité requérante est déjà sur un bateau ou dans un bâtiment.

<!-- From [https://wiki.eressea.de/index.php?title=ENTER&oldid=7174] -->
