---
# cSpell:locale fr
alias: production-optimisee
---
# Production optimisée

Par optimisation de la production, j'entends principalement l'utilisation économique des unités,  
C'est-à-dire J'ai un groupe d'unités dans une région avec la même tâche et je dois produire une quantité définie (argent, commerce, objets, bateaux et bâtiments).

Il est relativement clair qu’il s’agit du problème du sac à dos.  
Le but ici est de surcharger le moins possible le sac à dos, c'est-à-dire d'attribuer les unités de manière à ce que le moins de personnes possible ne fasse rien.  
En principe, il est également envisageable de fixer une limite minimale d'utilisation (pour la dernière unité attribuée).

Lors du chargement d'un sac à dos, il est important de charger autant de poids que possible dans l'espace/poids limité.  
Dans notre cas, le rapport espace/poids est la quantité à produire.  
Nous n'avons aucune valeur, mais nous avons des coûts, et ils sont par ex. plus une unité est bonne, plus elle est basse.

Le problème du sac à dos peut être assez bien résolu en utilisant les points optimaux de Pareto (états intermédiaires) pour des objets individuels très différents que vous emballez dans le sac à dos.  
Malheureusement, à Eressea, nous avons souvent affaire à un grand nombre d'unités tout aussi bien entraînées.  
c'est-à-dire que les coûts par personne sont les mêmes, seule la taille peut être différente.  
Cependant, cela signifie qu’un certain nombre d’États sont sur la même ligne, c’est-à-dire qu’il n’est guère possible d’en éliminer un seul.

Alors, comment procéder en gros :

1. Trier les unités existantes par coût par personne (le moins en premier), puis par nombre de personnes (le plus en premier)
2. Création récursive d'états
    1. Attention à n'attribuer les mêmes unités (coût et taille) que dans un ordre défini (c'est à dire si la première du groupe n'est pas là, n'essayez pas la seconde)
    2. Supprimez les états qui entraînent >= coûts avec <= quantité de production (points non optimaux de Pareto)
    3. Vérifier la condition supplémentaire d'utilisation minimale pour la dernière unité et/ou éventuellement la plus petite unité
3. Parmi tous les États cibles, choisissez celui avec la production la plus élevée et, si nécessaire, les coûts les plus bas

Une méthode qui calcule le résultat de l’optimisation n’a besoin que d’une liste des unités, de leurs coûts et de leur quantité de production.  
Si nécessaire, des conditions supplémentaires sont données à la méthode.  
Une telle liste d'unités peut être créée relativement rapidement, quelle que soit la cible réelle, et dotée des attributs nécessaires.  
Appliqué à la production, le problème du sac à dos peut être mis en œuvre assez facilement de manière généralisée.

<!-- From [https://wiki.eressea.de/index.php?title=Optimierung\_Produktion&oldid=2469] -->
