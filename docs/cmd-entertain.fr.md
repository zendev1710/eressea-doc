---
# cSpell:locale fr
alias: cmd-entertain-fr
---
<!-- disable MD052 because of mkdocs autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# `ENTERTAIN`

**`ENTERTAIN`**`[`*`Amount`*`]`  

L'unité passera le tour à divertir les paysans.  

Vous pouvez gagner jusqu'à 20 Silver par personne et par niveau de compétence en [divertissement][divertissement]{title="Entertainment"}.  
Mais les agriculteurs ne dépensent que 5 % de leur argent en divertissement.
Si plus d'unités tentent d'entretenir les agriculteurs que ce que ces derniers peuvent payer, l'argent sera réparti entre toutes les unités d'entretien.  
Si vous spécifiez un montant, l'unité gagnera au maximum ce montant.  

Supposons que les agriculteurs d'une région possèdent 1 200 Silver.
Les artistes pourront alors gagner un maximum de 1200 ÷ 20 = 60 Silver.  

Considérons maintenant deux unités : A a 1 personne avec un niveau 1 en divertissement, et B a 2 personnes avec un niveau 2 en divertissement.  
A pourrait gagner 1×1×20=20 Silver, B pourrait gagner 2×2×20=80 Silver; total 100 Silver.  

Puisque seulement 60 Silver sont disponibles, ceux-ci seront divisés en proportion d'environ 20 / 80.  
Ainsi, l’unité A reçoit environ 1/5 et l’unité B environ 4/5 de l’argent disponible.  
Cela fait environ 12 Silver pour A et 48 Silver pour B.  

Les unités à bord d'un bateau présent dans une région gardée ne peuvent ni [[cmd-work|travailler]] ni divertir (voir [[cmd-guard]] et [[cmd-help]]).

La limite de collecte des impôts d'une région indique la quantité totale d'argent qui peut être retirée aux agriculteurs (hors [commerce][le-commerce]) sans qu'ils partent.  
Il est aussi élevé que le surplus de revenu des agriculteurs.

## Voir aussi

- [[argent]]

<!-- From [https://wiki.eressea.de/index.php?title=ENTERTAIN&oldid=16748] -->
