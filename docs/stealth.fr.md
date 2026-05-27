---
# cSpell:locale fr
alias: discretion
---
<!-- disable some rules due to of autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# Discrétion

La compétence de [discrétion][camuflage]{title="Stealth"} permet de se camoufler aux yeux des autres unités.  
Une unité est toujours visible lorsqu'elle [[cmd-guard|garde]] une région, se trouve sur un bateau ou dans un bâtiment.  

## Contre-mesures

Les unités camouflées peuvent être découvertes grâce à la compétence **[Perception][perception]**.  
Si le plus haut niveau en perception de ta faction dans la région est inférieur au niveau en Discrétion d'une unité étrangère, l'unité camouflée n'apparaît pas dans le rapport - elle devient invisible.  
Si le niveau de perception et le niveau de Discrétion sont égaux, l'unité camouflée apparaît dans le rapport.  
C'est la situation de départ lorsque l'on commence la partie, car toutes les nouvelles unités sont T0 en Discrétion et Perception.  

## Contrecarrer la garde

Les unités camouflées avec succès ne sont pas soumises aux conséquences de [[cmd-guard]].  
Elles peuvent faire de l'entertain, collecter des impôts, extraire des ressources ou recruter des paysans.  

## Augmenter les chances de fuite

La chance de fuite standard d'une unité en [combat][la-fuite] est de 25 % (50 % pour les halflings).  
À chaque niveau de stealth, les chances de fuite de l'unité augmentent de 5 %.  
Qu'une unité sache ou non monter à cheval, en posséder un augmente ses chances de fuite d'un de ses membres de 10 % **une seule fois**;
5 chevaux n'apportent donc **PAS** +50 % à une personne, mais seulement +10 %.  
Les chances de fuite maximales sont de 75 % (90 % pour les halflings).  

## Vol de Silver

Les unités dissimulées peuvent voler des Silver à d'autres unités en utilisant l'ordre [[cmd-steal]].  
Ici aussi, la perception la plus élevée de la faction volée dans la région compte.  
Par niveau de différence de compétence, chaque personne qui vole vole 50 Silver.  
Dans ce cas, le vol se fait **toujours** dans la totalité de la réserve d'argent de la faction dans la région.  
La faction volée reçoit un message indiquant qu'elle a été volée, mais pas par qui.  
Si le niveau de stealth est seulement égal au niveau de perception, le vol échoue et la faction volée reçoit un rapport anonyme sur la tentative.  
Si le niveau de stealth est trop bas, la faction qui devait être volée reçoit un message avec le nom des voleurs.  

Les gobelins, s'ils ont appris stealth jusqu'au niveau 4 au moins, volent toujours au moins 50 Silver, même si leur niveau de stealth est inférieur à celui de perception.  
Un tel vol se remarque bien sûr et n'a donc de sens que dans certaines circonstances.  
On entend dire que les armées gobelines ont déjà porté un coup décisif à leurs adversaires en les privant de nourriture.  

Si l'on s'attend à être volé avec succès, la seule solution est d'apporter de l'argent dans la région concernée, car même les revenus provenant des divertissements, de la collecte des impôts, du travail et du commerce peuvent être volés (tous mes types de revenus).  

Le vol constitue de temps en temps un moyen efficace de faire tomber des espions qui sont eux-mêmes bien camouflés, car ils ont de grandes chances de s'échapper en cas d'attaque grâce à leur stealth élevé.

## Espionnage

Si une unité dotée de la compétence [Espionnage][espionnage] donne l'ordre [[cmd-spy|`SPY`*`ID unité`*]], sa compétence d'espionnage est comparée à la compétence de Discrétion de l'unité cible.  
La chance de base de réussir une tentative d'espionnage est de 10%.  
Pour chaque niveau d'Espionnage dépassant le niveau de Discrétion de la victime, le vol augmente de 5 %.  
Un niveau élevé en Discrétion permet donc à l'unité de rendre les tentatives d'espionnage plus difficiles.  
Pour atteindre une chance de succès de 50 %, un espion doit être de 8 niveaux supérieurs.

Si un espion est au moins T2 en Discrétion, atteindre les 8 niveaux de différence prendra nettement plus de temps en moyenne.  

Si la tentative d'espionnage réussit, l'espion apprend le statut de combat, les objets en possession de l'unité et ses compétences.  
L'appartenance à une faction peut en outre être découverte si le niveau d'espionnage est supérieur d'au moins 6 niveaux à celui de la Discrétion de l'unité.  
Un niveau de Discrétion élevé est donc utile pour réussir à se dissimuler en une autre faction.  

Ensuite, que la tentative d'espionnage ait réussi ou non, on détermine la probabilité que l'espion ait été **remarqué**.  
*E* étant le niveau d'espionnage de l'espion et *P* le niveau de perception de l'unité espionnée :

probabilité (en %) = 100 − E x 5 + P x 2

## Remarques

De nombreuses factions stockent leurs marchandises sur une unité très bien camouflée dans chaque région ([[cmd-combat|position de combat]]: `COMBAT NOT` ou `COMBAT FLEE`).  
Les objets sont ainsi protégés de nombreux dangers, tant qu'aucun observateur adverse ne les découvre.  

Outre ces utilisations passives de la dissimulation, il est bien sûr possible de partir à la recherche d'informations avec des unités furtives bien entraînées ou d'utiliser la capacité de voler.  

## Voir aussi

- [[cmd-guard]]
- [revenus][le-vol-la-methode-malhonnete]

Poursuivre la lecture : [[deplacements]].

<!-- From [https://wiki.eressea.de/index.php?title=Tarnung/fr&oldid=16974] -->
