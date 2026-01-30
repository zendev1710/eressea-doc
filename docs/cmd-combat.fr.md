---
# cSpell:locale fr
alias: cmd-combat-fr
---
# `COMBAT`

**`COMBAT`**`FRONT`  
**`COMBAT`**`AGGRESSIVE`  
**`COMBAT`**`REAR`  
**`COMBAT`**`DEFENSIVE`  
**`COMBAT`**`NOT`  
**`COMBAT`**`FLEE`  
**`COMBAT`**`HELP [NOT]`  

Cet ordre détermine la réaction d'une unité en cas de bataille (voir aussi la section [Lignes de combat] dans le chapitre [[guerre]]).  

## `COMBAT AGGRESSIVE`

Au combat, l'unité est au front et ne fuira jamais, mais se battra jusqu'à la mort.  
Ceci est utilisé à son avantage lorsque la dernière puissance offensive compte vraiment.  

## `COMBAT FRONT`

Avec cet ordre, au combat, l'unité est au front.  

L'unité tentera de fuir lorsqu'elle aura perdu au moins 20% de ses points de vie.  
Ceci est utilisé avec avantage pour les bons épéistes.  
Peut également accompagné de l'ordre `COMBAT`.  

## `COMBAT REAR`

Avec cet ordre, l'unité combat en deuxième ligne.  

Si le front est anéanti, ces unités seront toujours entraînées dans la mêlée (en première ligne) !  
Ceci est utilisé avec avantage pour les tireurs.  
L'unité tentera de fuir lorsqu'elle aura perdu au moins 20% de ses points de vie.  

## `COMBAT DEFENSIV`

Comme `COMBAT REAR`, mais l'unité fuira dès qu'elle aura perdu 10% de ses points de vie.  
Ceci est utilisé avec avantage pour les magiciens.  

## `COMBAT NOT`

L'unité ne participe pas au combat, à moins qu'elle soit la cible d'un ordre [[cmd-attack|d'attaque]] ennemi.  
Ceci est utilisé avantageusement pour les unités qui restent hors du combat mais ne sont pas censées fuir, par exemple pour occuper un bâtiment.  
L'unité tentera de fuir dès qu'elle aura perdu 10% de ses points de vie.  

## `COMBAT FLEE`

Si une unité prête à [fuir] est impliquée dans un combat, elle tentera de fuir avant chaque round de combat.  
<!-- TODO: find escape section and combat chapter -->
Pour plus d'informations sur le comportement de fuite, consultez la section [Échappement] du chapitre Combat.  

Ce statut de combat est mis à profit par presque tous les « civils ».  
Si même une personne d'une unité réussit à s'échapper d'un combat, elle quitte automatiquement les bâtiments ou les bateaux terrestres dans lesquels elle se trouve.  
Il est donc important de se demander si ce statut a du sens pour les occupants d'un bâtiment ou d'un bateau.  

Les unités avec ce statut de combat ne peuvent pas non plus [[cmd-attack|attaquer]] ni [[cmd-guard|garder]].  
Si une unité de garde se place en `COMBAT FLEE`, la garde est immédiatement annulée, avec les conséquences correspondantes.  
Les unités avec ce statut de combat peuvent toujours se déplacer après le combat (avec [[cmd-move]], [[cmd-route]], [[cmd-follow]]).  

!!! warning "Attention"
    Les unités avec `COMBAT FLEE`ou`COMBAT NOT` se battront s'ils sont attaqués et que les deux premières lignes sont débordées.  
    Cela signifie que les magiciens font aussi de la magie.  
    Les sorts pré et post-combat sont (actuellement) lancés même si les lignes de front ne sont pas débordées.  
    Si vous souhaitez éviter cela, vous pouvez désactiver le [[cmd-combatspell|statut des sorts de combat]].

Faire fonctionner des catapultes est une tâche qui demande beaucoup de préparation, donc une unité ayant le statut de combat `COMBAT NOT` ou `COMBAT FLEE` ne tirera pas de munitions, mais utilisera toute autre arme si elle en possède une et sait s'en servir.

!!! warning "Attention"
    Les personnes avec **peu de points de vie** qui ne sont pas en `COMBAT FLEE` fuiront dès qu’ils auront été touchés au combat.  
    Les coups dont les points de dégâts ont été complètement stoppés par l'armure et les tentatives de coup ratées comptent également.  
    Bien entendu, les personnes ayant `COMBAT FLEE` fuient avant.

## `COMBAT HELP`

Une unité avec `COMBAT HELP NOT` ne sera pas aidée au combat, ni par les unités de votre propre faction ni par les alliés.  
Si une telle unité est spécifiquement attaquée, aucune autre unité ne sera engagée dans la bataille.  
Bien entendu, cela ne s'applique que si d'autres unités ne possédant pas ce statut ne sont pas également attaquées.  

Votre propre faction est toujours impliquée lorsqu'elle attaque, ou lorsqu'elle-même ou une faction qu'elle aide est attaquée.  
Vous trouverez plus de détails sur [[cmd-help]] et dans les chapitres [[guerre]] et [[alliances|Alliance]].

<!-- From [https://wiki.eressea.de/index.php?title=COMBAT&oldid=7216] -->

[Lignes de combat]: ./war.md#lignes-de-combat
[fuir]: ./war.md#la-fuite