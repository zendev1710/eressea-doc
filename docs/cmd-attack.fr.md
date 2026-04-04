---
# cSpell:locale fr
alias: cmd-attack-fr
---
<!-- disable MD052 because of mkdocs autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# `ATTACK`

**ATTACK**&nbps;&lt;unit-id&gt; [^1]  

Ordre pseudo-long [^1].  

Cet ordre déclenche l'attaque de l'unité spécifiée présente dans la région de l'attaquant.  
Un ordre `ATTACK` doit être donné pour chaque unité à attaquer.  

Les unités qui ne [[cmd-combat|combattent]] ni à l'avant (`COMBAT` ou `COMBAT AGGRESSIVE`) ni à l'arrière (`COMBAT REAR` ou `COMBAT DEFENSIVE`) ne peuvent pas attaquer.  

Au cours des premières semaines, une faction est [[puppy-protection|immunisée]] contre les attaques.  

## Voir aussi

- [[guerre|La guerre]]
- Ordre [[cmd-combat]]

[^1]: `ATTACK` est un [ordre pseudo-long][ordres-courts-et-longs] : c'est un ordre court dans le sens où plusieurs ordres  `ATTACK` peuvent être donnés;
c'est un ordre long parce qu'il exclut d'autres ordres longs si un combat « long » se produit effectivement.
Le moment où un combat « long » se produit est expliqué dans la section [fin de la bataille][fin-du-combat].

<!-- From [https://wiki.eressea.de/index.php?title=ATTACK&oldid=16719] -->
