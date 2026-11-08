---
# cSpell:locale fr
alias: cmd-enter-fr
---

# `ENTER`

**`ENTER`**` BUILDING `*`building-id`*  
**`ENTER`**` SHIP `*`ship-id`*  

Permet d'entrer dans le [bâtiment][batiments-id] ou le [bateau][bateaux-id] spécifié.  

L'unité qui [contrôle][unites-et-batiments] le bâtiment ou le bateau doit autoriser l'accès.  
L'entrée réussit si l'unité propriétaire appartient à une autre faction mais a défini [`HELP GUARD`][cmd-help-fr] pour la faction demandant l'entrée, ou si elle donne l'ordre [`CONTACT`][cmd-contact-fr] pour l'unité requérante au même tour de jeu.  
Dans le cas contraire, l'accès sera refusé.

Un ordre `ENTER` nécessite au préalable un ordre [`LEAVE`][cmd-leave-fr] si l'unité requérante est déjà sur un bateau ou dans un bâtiment.

<!-- From [https://wiki.eressea.de/index.php?title=ENTER&oldid=7174] -->

[cmd-contact-fr]: [[cmd-contact-fr]]
[cmd-help-fr]: [[cmd-help-fr]]
[cmd-leave-fr]: [[cmd-leave-fr]]
