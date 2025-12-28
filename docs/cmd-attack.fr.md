---
# cSpell:locale fr, en
alias: cmd-attack-fr
---
# ATTACK

**`ATTACK`**[<sup>`(l)`</sup>]` `*`unit-id`*  

Cet ordre attaque l'unité affectée dans la région actuelle.
Un ordre doit être donné pour chaque unité à attaquer.

[<sup>(L)</sup>][<sup>`(l)`</sup>] L'ordre `ATTACK` est un ordre pseudo-long.
C'est un ordre court dans le sens où plusieurs ordres  `ATTACK` peuvent être effectués.
C'est un ordre long parce qu'il exclut d'autres ordres longs si un combat « long » se produit effectivement.
Le moment où un combat « long » se produit est expliqué sous [fin de la bataille].

Les unités qui ne [[cmd-combat|combattent]] ni à l'avant (`COMBAT` ou `COMBAT AGGRESSIVE`) ni à l'arrière (`COMBAT REAR` ou `COMBAT DEFENSIVE`) ne peuvent pas attaquer.

Au cours des premières semaines, votre faction est [[puppy-protection|immunisée]] contre les attaques.

## Voir aussi

- [[guerre]]
- [[cmd-combat]]

<!-- From [https://wiki.eressea.de/index.php?title=ATTACK&oldid=16719] -->

[<sup>`(l)`</sup>]: ./commands.md#ordres-courts-et-longs
[fin de la bataille]: ./war.md#fin-du-combat
