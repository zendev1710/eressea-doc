---
# cSpell:locale fr
alias: cmd-spy-fr
---
<!-- disable MD052 because of mkdocs autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# SPY

*Ordre [long][ordres-courts-et-longs]*.

**`SPY`**` `*`unit-id`*

L'espionnage vous permet d'espionner les unités d'une autre faction.  
La compétence d'espionnage de l'espion est comparée à la [compétence de discrétion][discretion]{title="Stealth"} de l'unité cible.  

La probabilité de base d'une tentative d'espionnage réussie est de 10 %.  
Pour chaque niveau de compétence où la compétence d'espionnage dépasse la compétence de furtivité de la victime, cela augmente de 5 %.  

Si la tentative d'espionnage réussit, l'espion apprend le statut de combat, les objets en possession de l'unité, les compétences ainsi que la véritable affiliation à une faction.  

L'affiliation à une faction ne peut être déterminée que si la compétence d'espionnage est supérieure d'au moins 6 niveaux à la compétence de furtivité de l'unité ciblée.  
Toutes les autres informations peuvent être déterminées avec un simple succès.  

Ensuite, quel que soit le succès, un dé est lancé pour voir si la tentative d'espionnage a été remarquée.  
La probabilité que cela se produise est calculée ainsi :

`(100 - SpySpy x 5 + (Perception Sacrifice x 2) %`

## Expérience de jeu (Ralf D.)

Les espions sont toujours des unités composées d'une seule personne, car apparemment, une tentative d'espionnage n'est **PAS** effectuée par personne dans l'unité d'espionnage, mais une seule fois pour l'ensemble de l'unité.  
Comme toutes les activités qui dépendent des probabilités, vous pouvez également augmenter le succès de l'espionnage en espionnant la même unité cible avec de nombreuses unités individuelles.  

### Exemple

Les espions avec Espionnage à 10 espionnent une unité de combat avec Furtivité 1.  

- 1 unité a une chance de 10 % + (10 -1) * 5 % = 55 % d'espionner l'unité cible
- 5 unités ont donc une chance de 100 % - (100 % - 55 %)^5 = 98,2 %

Ce qui suit est également intéressant (toujours contre le camouflage 1 de l'unité cible) :

- 5 unités avec Espionnage 2 ont également 55 % de chances de succès
- 8 unités avec Espionnage 1 ont 57 % de chances de succès
- 22 unités avec Espionnage 1 ont 90 % de chances de succès

Les considérations de coût sont alors intéressantes :

- 1 unité d'espionnage 10 -> 55 tours (sans professeur) -> 5500 Silver + autres formations et recrutement
- 5 unités d'espionnage 2 -> 3 tours*5 personnes -> 1500 Silver + ...
- 8 unités d'espionnage 1 -> 1 round*8 personnes -> 800 Silver + ...

### Conclusion

Des compétences élevées en espionnage ne valent la peine que si la ou les unités ont également reçu une autre formation, ou si vous ne pouvez pas diviser les unités en raison du nombre limité d'unités, même dans les situations dans lesquelles vous avez besoin d'espionnage.  

En guise de contre-mesure, une formation de base en camouflage aide à lutter contre de nombreux mauvais espions.  
Cependant, il faut toujours déployer plus d’efforts pour le camouflage que les espions pour l’espionnage.  

Il est clair que les tentatives d'espionnage impliquant de nombreuses unités malveillantes seront détectées avec une certitude de presque 100 %.  

!!! warning "Attention"
    Si les mécanismes de jeu sont modifiés de manière à ce que l'unité cible ne calcule une limite aléatoire qu'une fois par tour, alors le même résultat s'applique à tous les espions de même qualité, ce qui rend cette considération incorrecte.  
    Actuellement, les résultats sont différents pour des espions de même nature.

<!-- From [https://wiki.eressea.de/index.php?title=SPY&oldid=16733] -->
