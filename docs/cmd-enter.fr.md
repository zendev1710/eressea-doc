---
# cSpell:locale fr, en
alias: cmd-enter-fr
---
# ENTER

**`ENTER`**` BUILDING `*`building-id`*  
**`ENTER`**` SHIP `*`ship-id`*  

Permet d'entrer dans le [[bâtiments|bâtiment]] ou le [[navires|navire]] spécifié.  

L'unité qui [contrôle] le bâtiment ou le navire doit autoriser l'accès.  
L'entrée réussit si l'unité propriétaire appartient à une autre faction mais a défini [[cmd-help|`HELP GUARD`]] pour la faction demandant l'entrée, ou si elle donne l'ordre [[cmd-contact]] pour l'unité requérante au même tour de jeu.  
Dans le cas contraire, l'accès sera refusé.

Un ordre `ENTER` nécessite au préalable un ordre [[cmd-leave]] si l'unité requérante est déjà sur un navire ou dans un bâtiment.

<!-- From [https://wiki.eressea.de/index.php?title=ENTER&oldid=7174] -->

[contrôle]: ./buildings.md#unites-et-batiments
