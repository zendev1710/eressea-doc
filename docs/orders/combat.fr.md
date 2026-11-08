---
# cSpell:locale fr
alias: cmd-combat-fr
---

# `COMBAT`

**`COMBAT [FRONT]`**  
**`COMBAT AGGRESSIVE`**  
**`COMBAT DEFENSIVE`**  
**`COMBAT FLEE`**  
**`COMBAT HELP [NOT]`**  
**`COMBAT NOT`**  
**`COMBAT REAR`**  

Cet ordre détermine la réaction d'une unité en cas de bataille (voir aussi la section [Lignes de combat][lignes-de-combat] dans le chapitre [Guerre][guerre]).  

Ensemble des statuts de combat, de la plus forte exposition au combat à la plus faible.  

| Statut                            | Ligne | Tentative de fuite | Adapté pour                        |
|:----------------------------------|:------|:-------------------|:-----------------------------------|
| [`AGGRESSIVE`][combat-aggressive] | 1ère  | Jamais             | Les combattants les moins précieux |
| [`FRONT`][combat-front]           | 1ère  | Dégâts >= 20 %     | Les bons épéistes                  |
| [`REAR`][combat-rear]             | 2ème  | Dégâts >= 20 %     | Les tireurs                        |
| [`DEFENSIVE`][combat-defensive]   | 2ème  | Dégâts >= 10 %     | Les mages                          |
| [`NOT`][combat-not]               | ---   | Dégâts >= 10 %     | Les occupants d'un bâtiment        |
| [`FLEE`][combat-flee]             | ---   | Toujours           | Les civils                         |

!!! note
    une unité **en première ligne** est dite aussi au front (ou dans la mêlée).

## `COMBAT [FRONT]`

Peut également s'écrire `COMBAT`.  

Avec cet ordre, lors d'un combat, l'unité est au front (en première ligne).  
L'unité tentera de fuir dès qu'elle aura perdu au moins 20 % de ses points de vie.  

Ceci est utilisé avec avantage pour les bons épéistes.  

## `COMBAT AGGRESSIVE`

Avec cet ordre, au combat, l'unité est au front et **ne fuira jamais**.  
Elle se battra jusqu'à la mort.  

Ceci est utilisé à son avantage lorsque la dernière puissance offensive compte vraiment.  

## `COMBAT DEFENSIVE`

Avec cet ordre, l'unité combat en deuxième ligne.  
Si le front est anéanti, ces unités seront toujours entraînées dans la mêlée (en première ligne) !  
L'unité fuira **dès qu'elle aura perdu 10 %** de ses points de vie (à la différence de `COMBAT REAR`, où l'unité fuit à 20 % de dégâts).  

Ceci est utilisé avec avantage pour les **mages**.  

## `COMBAT FLEE`

Si une unité prête à [fuir][la-fuite] est impliquée dans un combat, elle tentera de fuir avant chaque round de combat.  

<!-- TODO: find escape section and combat chapter -->
Pour plus d'informations sur le comportement de fuite, consultez la section [Échappement] du chapitre Combat.  

Ce statut de combat est mis à profit par presque tous les « civils » (sans arme ni compétence de combat).  

Si même une personne d'une unité réussit à s'échapper d'un combat, elle quitte automatiquement les bâtiments ou les bateaux terrestres dans lesquels elle se trouve.  
Il est donc important de se demander si ce statut a du sens pour les occupants d'un bâtiment ou d'un bateau.  

Les unités avec ce statut de combat ne peuvent pas non plus [attaquer][cmd-attack-fr] ni [garder][cmd-guard-fr].  
Si une unité de garde se place en `COMBAT FLEE`, la garde est immédiatement annulée, avec les conséquences correspondantes.  
Les unités avec ce statut de combat peuvent toujours se déplacer après le combat (avec [`MOVE`][cmd-move-fr], [`ROUTE`][cmd-route-fr], [`FOLLOW`][cmd-follow-fr]).  

!!! warning "Attention"
    Les unités avec `COMBAT FLEE` ou `COMBAT NOT` se battront si elles sont attaquées et que les deux premières lignes sont débordées.  
    Cela signifie que les mage font aussi de la magie.  
    Les sorts pré-combat et post-combat sont lancés même si les lignes de front ne sont pas débordées.  
    Si vous souhaitez éviter cela, vous pouvez désactiver le [statut des sorts de combat][cmd-combatspell-fr].

Faire fonctionner des catapultes est une tâche qui demande beaucoup de préparation, donc une unité ayant le statut de combat `COMBAT NOT` ou `COMBAT FLEE` ne tirera pas de munitions, mais utilisera toute autre arme si elle en possède une et sait s'en servir.

!!! warning "Attention"
    Les personnes avec **peu de points de vie** qui ne sont pas en `COMBAT FLEE` fuiront dès qu’elles auront été touchées au combat.  
    Les coups dont les points de dégâts ont été complètement stoppés par l'armure et les tentatives de coup ratées comptent également.  
    Bien entendu, les personnes ayant `COMBAT FLEE` fuient avant.

## `COMBAT NOT`

Avec cet ordre, l'unité ne participe pas au combat, à moins qu'elle soit la cible d'un ordre [d'attaque][cmd-attack-fr] ennemi.  
L'unité tentera de fuir dès qu'elle aura perdu 10 % de ses points de vie.  

Ceci est utilisé avantageusement pour les unités qui restent hors du combat mais ne sont pas censées fuir, comme par exemple les occupants d'un bâtiment.  

## `COMBAT REAR`

Avec cet ordre, l'unité combat en deuxième ligne.  
Si le front est anéanti, ces unités seront toujours entraînées dans la mêlée (en première ligne) !  

L'unité tentera de fuir dès qu'elle aura perdu 20 % de ses points de vie.  

Ceci est utilisé avec avantage pour les tireurs.  

## `COMBAT HELP [NOT]`

Avec l'ordre `COMBAT HELP NOT`, une unité **ne sera pas aidée au combat**, ni par les unités de votre propre faction ni par les alliés.  
Si une telle unité est spécifiquement attaquée, aucune autre unité ne sera engagée dans la bataille.  
Bien entendu, cela ne s'applique que si d'autres unités ne possédant pas ce statut ne sont pas également attaquées.  

Votre propre faction est toujours impliquée lorsqu'elle attaque, ou lorsqu'elle-même ou une faction qu'elle aide est attaquée.  
Plus de détails sur [`HELP`][cmd-help-fr] :

- [La guerre][guerre]
- [Les alliance][alliances-fr-id]

L'ordre `COMBAT HELP` réactive le statut qui permet à l'unité d'être aidée en cas d'attaque.

<!-- From [https://wiki.eressea.de/index.php?title=COMBAT&oldid=7216] -->

[cmd-attack-fr]: [[cmd-attack-fr]]
[cmd-combatspell-fr]: [[cmd-combatspell-fr]]
[cmd-guard-fr]: [[cmd-guard-fr]]
[cmd-move-fr]: [[cmd-move-fr]]
[cmd-route-fr]: [[cmd-route-fr]]
[cmd-follow-fr]: [[cmd-follow-fr]]
[cmd-help-fr]: [[cmd-help-fr]]
