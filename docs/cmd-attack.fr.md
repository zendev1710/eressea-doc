---
# cSpell:locale fr, en
alias: cmd-attack-fr
---
# ATTACK

*ordre [pseudo-long].*  
*C'est un ordre court dans le sens où plusieurs ordres  `ATTACK` peuvent être effectués.*  
*C'est un ordre long parce qu'il exclut d'autres ordres longs si un combat « long » se produit effectivement.*  
*Le moment où un combat « long » se produit est expliqué dans la section [fin de la bataille].*

**`ATTACK`**` `*`unit-id`*  

Cet ordre déclenche l'attaque l'unité affectée dans la région actuelle.  
Un ordre doit être donné pour chaque unité à attaquer.  

Les unités qui ne [[cmd-combat|combattent]] ni à l'avant (`COMBAT` ou `COMBAT AGGRESSIVE`) ni à l'arrière (`COMBAT REAR` ou `COMBAT DEFENSIVE`) ne peuvent pas attaquer.

Au cours des premières semaines, une faction est [[puppy-protection|immunisée]] contre les attaques.

## Voir aussi

- [[guerre]]
- [[cmd-combat]]

<!-- From [https://wiki.eressea.de/index.php?title=ATTACK&oldid=16719] -->

[pseudo-long]: ./commands.md#ordres-courts-et-longs
[fin de la bataille]: ./war.md#fin-du-combat
