---
# cSpell:locale fr
alias: chaines-d-apprentissage-optimisees
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# Chaînes d'apprentissage optimisées

## Considérations préliminaires

La première chose que vous devez faire lors de l’optimisation des chaînes d’apprentissage est d’être clair sur les tâches que vous préférez des enseignants aux étudiants.
Ce n'est qu'alors que vous pourrez soit créer un ensemble de règles (appelées connaissances d'experts), soit écrire un algorithme d'optimisation qui produit le meilleur ou au moins le meilleur état possible (devoirs des enseignants et des étudiants).

Toutes les autres approches que j’ai vues jusqu’à présent appartiennent davantage à la catégorie des connaissances expertes.
Le plugin `Teacher` de Magellan ou les outils FF (2) doivent être mentionnés ici.
Les unités sont triées selon un critère puis traitées.
Les affectations sont créées successivement.
Une évaluation ou une comparaison des différentes options n'a lieu qu'au niveau le plus bas.

Cette approche n’est en aucun cas mauvaise car elle donne de bons résultats en un temps record.
De plus, les règles sont claires et compréhensibles et personne ne sera surpris de la raison pour laquelle une mission a été confiée.

Mais je voudrais également souligner ici une autre possibilité : chaque état partiel peut être évalué avec un coût ou un profit et une fonction d'estimation, similaire à la recherche d'itinéraire.
Cela signifie qu'un optimum généralement inaccessible peut être défini auquel on essaie de réduire les affectations.
La chose la plus importante est la fonction de coût ou de profit, puis la fonction d'estimation qui en dérive.

## Fonction Coût - Bénéfice

L’apprentissage a un coût, je pense que c’est clair pour tout le monde.
Dans Eressea c'est l'argent pour l'entretien ou pour les compétences coûteuses.
Si l'on vous instruit, les coûts restent absolument les mêmes, mais l'effet d'apprentissage est plus grand.
On peut donc dire que les coûts par semaine d'apprentissage sont réduits de moitié, mais pas complètement, car l'enseignant veut aussi être payé.

Vous pouvez également aborder les choses dans l'autre sens et maximiser le gain d'apprentissage et supposer que les coûts sont constants (ce qui est généralement vrai).
Ce cas nous convient car enseigner ne signifie plus des coûts infinis (puisqu'on n'apprend rien).

Ainsi, une simple fonction de profit pourrait renvoyer les valeurs suivantes par personne (exemple 1) :

    Professeur            = 0
    Apprendre sans professeur = 1
    Apprendre avec le professeur  = 2

Je peux le confirmer, cette fonction fait ce à quoi vous vous attendez : elle garantit que le plus grand nombre d'étudiants possible ait un enseignant.
Malheureusement, il n'évalue pas les compétences des enseignants ou des étudiants et garantit ainsi que, tôt ou tard, toutes les unités se situent dans une fourchette de 2 à 3 niveaux de compétence.
Il arrive aussi qu'un professeur enseigne à une unité de 2 personnes.

Ainsi, comme mentionné au début, il est important d’être clair sur certaines limites.
Ensuite, ces limites, qui ont malheureusement souvent l'effet inverse, doivent être intégrées dans la fonction de coût.

### Cas limites pour la fonction de coût

La première chose à faire est de déterminer combien d’élèves un enseignant devrait avoir au moins, même si la différence de compétence n’est que de 2 niveaux.
En outre, il convient de préciser jusqu'à quel niveau les recrues peuvent être formées, c'est-à-dire si les T20 peuvent également enseigner les T0.
Plus généralement, on précise jusqu'à quelle différence de compétence, en fonction de la compétence de l'enseignant, combien d'élèves doivent être scolarisés au minimum pour que cette répartition soit plus favorable que de laisser apprendre enseignant et élève.
La meilleure chose à faire ici est de créer un petit diagramme avec la ligne/courbe souhaitée puis de développer une fonction qui la couvre au mieux.

J'ai développé moi-même la fonction suivante :

    A = 1.2
    B = 15
    C = 0.34
    Professeur            = 0
    Apprendre sans professeur = (A^Level + B) * (3^C)
    Apprendre avec le professeur  = (A^Level + B) * (6^C)

Les paramètres A, B et C ont été créés après de longs tests et en partie en assimilant diverses formules.
La formule peut également être facilement utilisée pour [l'huile de cervelle][huile-de-cervelle]{title="Brain wax"} et [l'académie][academie] en remplaçant le 3 ou le 6 pour le nombre de tentatives d'apprentissage*3 est remplacé.
Ainsi, apprendre avec la matière grise donne (1 + 1/3)*3 = 4.

Comme vous pouvez le calculer, apprendre avec un professeur grâce au facteur C n'est pas deux fois plus rentable que sans professeur, mais ne vaut qu'environ 27 % de plus.
Et comme le niveau est inclus dans la formule comme une puissance, vous gagnez beaucoup plus si vous enseignez à 8 personnes de haut niveau au lieu de 10 débutants.

## Fonction d'estimateur

Comme mentionné, cela devrait prédire le mieux possible le profit.
Il est important de ne pas sous-estimer l’optimum.
Mais où est notre optimal ? Apparemment, tout le monde ne peut pas apprendre sans qu’il y ait un enseignant.
Cela signifie que nous pouvons supposer que chaque unité est enseignée dans son intégralité, mais en même temps nous devons en déduire le minimum qu'un enseignant aurait pu réaliser comme profit.
Une très bonne approximation de cela résulte de :

`Bénéfice estimé = Learn_with_Teacher (Niveau) -0,1 *Learn_with_Teacher (Niveau + 2) + 0,01 *Learn_with_Teacher (Niveau + 4)`

Cela signifie que nous sommes définitivement légèrement au-dessus de l’optimum possible.

## A* Recherche

Le A*-Search est probablement familier à certaines personnes en matière d'orientation.
En bref, il y a un ou plusieurs états cibles, de nombreux états intermédiaires et bien sûr un état de départ quelque part.
Ces états sont reliés par des arêtes.
Si vous longez une bordure, vous encourez des coûts (ou générez des bénéfices, selon la façon dont vous le regardez).
Un chemin est recherché dans le graphique d'état qui entraîne des coûts minimaux ou un profit maximum.

A*Search optimise la recherche dans le graphique en ne recherchant pas tous les chemins possibles, mais en recherchant spécifiquement les chemins qui ont des coûts estimés faibles/des bénéfices estimés élevés.

La qualité du fonctionnement de A*-Search dépend donc fortement de la précision de l'estimateur.
La précision signifie à quel point la valeur estimée est proche de la valeur optimale réelle.

### États d’apprentissage

Il est désormais difficile de préciser les états pour ce cas d’optimisation du système d’apprentissage.
Il est important de distinguer si une unité apprend ou enseigne, combien d'étudiants elle compte ou combien de ses propres personnes reçoivent l'enseignement.
La question de savoir si vous vous souciez des élèves d'un enseignant devient plus difficile.
Si les enseignants sont au même niveau, peu importe qui enseigne à quel élève.
Malheureusement, ce n'est pas pratique, car chaque enseignant ne peut avoir qu'un seul élève qui est enseigné par plusieurs enseignants (à savoir le dernier), à moins que vous ne spécifiiez tous les élèves pour chaque enseignant, mais nous ne le voulons pas non plus (mais cela fonctionnerait probablement côté serveur).

Lors de la construction des états, vous devez faire attention à ne pas produire deux états comparables, car cela pourrait élargir considérablement l’espace de recherche.
Malheureusement, cela arrive très souvent, car il n'est pas rare qu'il y ait plusieurs unités d'enseignement de qualité égale et de taille égale.
Il est utile ici de n'autoriser ces enseignants que dans un ordre défini.
Bien entendu, ces unités devraient si possible être enseignées exactement dans l’ordre inverse.

Ce que l’on remarque rapidement, c’est que le nombre d’états (c’est-à-dire les combinaisons possibles) augmente de façon exponentielle.
Sans A*-Search, un résultat serait impensable.
Malheureusement, la recherche A*de plus de 10 unités prend encore beaucoup de temps, vous les laissez rechercher le meilleur état cible.

Ce n'est qu'avec des "oeillères" que j'ai réussi à obtenir un très bon résultat avec l'algorithme dans un laps de temps raisonnable.
Ce résultat correspond souvent à l'optimum.
Toutefois, dans certains cas, l’algorithme rate des opportunités.
Cela tient au mécanisme de construction des États.
Je ne crée pas toutes les combinaisons possibles pour qu'un enseignant enseigne aux élèves, mais uniquement celles dans lesquelles les prochaines unités libres sont recherchées de haut en bas.
Cela fonctionne généralement assez bien, mais dans des cas exceptionnels, un meilleur état est « négligé ».

## Chaînes d'apprentissage statiques

Jusqu'à présent, nous avons discuté de la manière de planifier les unités existantes en tant qu'enseignants/étudiants.
Il s'agit maintenant de savoir quelle structure d'unités vous devez créer afin que l'enseignement et l'apprentissage puissent être coordonnés au mieux.
Certaines chaînes typiques enseignant-élève sont présentées et discutées ci-dessous :

### Chaînes d'apprentissage typiques

- **Chaîne simple enseignant-élève** -- constituée d'une unité enseignant (L) et d'une unité étudiant (S) avec 10*|L|=|S|.
  Les enseignants apprennent jusqu'à ce qu'ils aient deux niveaux d'avance, puis ils enseignent aux étudiants.
  Lorsque les étudiants n'étudient pas, ils font d'autres activités.
  Inconvénient : rythme d'apprentissage lent, avantages : seulement deux unités sont nécessaires, facile à automatiser.
  Utile pour les unités où l'apprentissage n'est pas une priorité, par ex. pour les mineurs qui apprennent principalement à atteindre des couches de minerai plus profondes, ou pour les collecteurs d'impôts qui augmentent progressivement leurs compétences de combat afin de pouvoir combattre de manière indépendante de plus petits groupes de monstres.
- **Pyramide** --Poursuite du développement de la chaîne simple enseignant-élève, composée d'une unité enseignant (L) et de plusieurs couches d'unités élèves (S1, S2,...) avec 10*|L|=|S1|, 10*|S1|=|S2|...
  Si l'objectif est de minimiser les coûts d'apprentissage des [compétences coûteuses][competences], alors l'enseignant apprend puis enseigne à la première unité d'élèves (S1).
  Ceux-ci enseignent ensuite S2, etc. Les étudiants n'apprennent que lorsqu'on leur enseigne.
  Même si cela minimise les coûts, cela est plus rapide si les élèves des classes intermédiaires apprennent même s'ils n'ont pas d'enseignant.
  Cependant, cela n'a aucun sens si cela aussi*le plus bas*Les étudiants apprennent sans professeur.
  À moyen terme, cela signifie qu'il n'y aura pratiquement aucun enseignement, car aucun niveau ne pourra obtenir un avantage en termes de compétence par rapport au niveau immédiatement inférieur.
  Si vous le souhaitez, vous pouvez ignorer toute la structure pyramidale et simplement faire apprendre une unité sans enseignant.
  Plus une pyramide comporte de couches, plus elle apprend vite.
  Étant donné que le nombre de personnes nécessaires augmente d’un facteur 10 à chaque quart de travail, il existe des limites à la hauteur de la pyramide.
- **Pyramide à double sommet** --L'unité enseignante située au sommet d'une pyramide apprend au moins les deux tiers du temps et peut enseigner au maximum un tiers du temps. 
  Cependant, l'idéal serait que la première unité d'étudiants apprenne la moitié du temps (et transmette ses connaissances dans l'autre moitié).
  Cela conduit à l’idée d’utiliser non pas une seule unité enseignant au sommet mais deux.
  L’espoir que deux enseignants puissent ensuite enseigner à tour de rôle les deux tiers du temps s’avère trompeur.
  Mais vous pouvez augmenter la vitesse d’apprentissage.
  Des analyses plus détaillées montrent qu'une pyramide à double sommet atteint la même vitesse d'apprentissage qu'une pyramide normale comportant une couche supplémentaire.
  La pyramide à double sommet est un peu moins efficace (c’est-à-dire que les gens ont relativement moins de temps pour faire autre chose que étudier), mais elle fonctionne avec moins de personnes.
- **Pyramide de 5** --La pyramide à 5 fonctionne comme son nom l'indique avec un facteur 5 en tailles d'unités.
En contrepartie, un enseignant enseigne toujours 2 unités et dispose ainsi de 10 fois plus d'élèves.
  Ce système peut être échelonné sur plusieurs niveaux.
  Le niveau supérieur comporte idéalement 6 logements de même taille.
  Le deuxième niveau comporte 3 unités de 5 fois la taille, le troisième niveau comporte 3 unités de 25 fois la taille.
  Une unité enseigne chacun des niveaux intermédiaires et deux sont enseignées.
  Au niveau supérieur, une personne enseigne et les 5 autres unités apprennent sans professeur, mais avec la puissance cérébrale et/ou une académie.
- **Apprendre de deux compétences** --Les unités de combat (S) apprennent généralement deux compétences, leur compétence d'arme et leur [endurance][skill-endurance-fr-id]{title="Endurance"}.
  Il s'avère également utile à divers enseignants (L_K, L_A).
  En principe, vous avez deux options : Les professeurs sont des spécialistes et n'apprennent qu'une seule compétence.
  Bien que cela soit meilleur en termes de vitesse d'apprentissage, ces spécialistes sont très vulnérables (voire inutilisables) en cas de combat.
  Vous pouvez également choisir |S|=9*|L_K|=9*|L_A|.
  L_K apprend la compétences de combat puis enseigne S et L_A
  L_A apprend l'[endurance][skill-endurance-fr-id]{title="Endurance"} puis enseigne S et L_K
- Pyramides à deux compétences --Il existe ici d'innombrables combinaisons possibles.
  Les vitesses d'apprentissage les plus élevées sont atteintes lorsque toutes les couches sauf la plus basse sont doublées, par ex. L_K,L_A,S1_K,S1_A,S2_K,S2_A,S3.
  Bien entendu, cela nécessite également de nombreuses unités.

### Analyse de la chaîne d'apprentissage

Quatre facteurs jouent un rôle lors de l’évaluation d’une chaîne d’apprentissage : Lequel*Vitesse*est-ce qu'elle apprend (mesurée en tentatives d'apprentissage/semaine) ? Comme*efficace*est-ce vrai, c'est-à-dire de combien de temps les gens disposent-ils pour faire autre chose que étudier ? Combien*Unités*as-tu besoin ? Combien*les gens*as-tu besoin ?
Les jeunes partis, par exemple, ne peuvent pas construire de pyramides à cinq niveaux parce qu'ils n'ont pas beaucoup de monde.
Les partis plus âgés doivent simplifier leurs chaînes en raison de la limite d'unités.
Les unités de production veulent avoir beaucoup de temps pour travailler et n'apprendre que lorsque cela en vaut vraiment la peine, etc. Avec quelques simplifications et un peu de mathématiques, vous pouvez facilement analyser les chaînes d'apprentissage concernant ces quatre facteurs.

 **Simplifications :**

1. Toutes les unités mettent le même temps pour atteindre le niveau suivant.
  En fait, il y a des fluctuations aléatoires dans le temps d'apprentissage jusqu'au niveau suivant et les enseignants doivent apprendre un peu plus que les étudiants car ils ont un niveau de compétence plus élevé.
2. Le temps peut être divisé en petits détails.
  En fait, vous ne pouvez enseigner que chaque semaine.
  En pratique, cette division est également assez fine.
3. « Enseigner » et « être enseigné » n’interfèrent pas l’un avec l’autre. 
  Des situations telles que : S2 pourrait apprendre de S1, mais aussi enseigner à S3 ; S1 ne peut pas apprendre de L et S3 ne peut pas enseigner S4.
  Puisque S2 ne peut pas faire les deux en même temps, S1 ou S3 doivent apprendre sans professeur, ce qui leur fait perdre du temps.
  En fait, de telles situations ne peuvent (presque) se produire que dans la phase de démarrage.
  Pour qu'une telle constellation naisse "d'elle-même", il faudrait que S1 ait gravi deux niveaux de compétence en une semaine, ce qui est plutôt improbable.

**Exemple de calcul**  
pour une pyramide à trois niveaux (L,S1,S2) : pour chaque unité, il est indiqué quelle proportion de son temps elle passe à enseigner/apprendre sans professeur/enseigner/faire autre chose.

- L ne peut pas être enseigné 
  Soit x la proportion de temps pendant laquelle L apprend.
  Alors il enseigne 1-x.
  Résultat : [0/x/1-x/0].
- S1 est enseigné 1-x par L et apprend y sans professeur. 
  Pour apprendre aussi vite que L, vous devez faire 2*(1-x)+y=x.
  Donc y=3*x-2.
  Le reste du temps[1-(1-x)-(3x-2)=2-2x]enseigne S1.
  Rendements[1-x /3x-2 /2-2x /0].
- S2 apprend 2-2x par S1, le reste du temps (1-(2-2x)=2x-1) il fait autre chose. 
  Rendements[2-2x /0 /0 /2x-1].
- Pour que tout le monde apprenne à la même vitesse, x = 2*(2-2x), donc x=4/5. 
- La vitesse d'apprentissage est donc de 4/5 
- Le temps non utilisé pour l'apprentissage (pondéré par la taille de l'unité) est de (100*3/5+10*0+1*0)/111=0,540540... 
  Trois unités et 111 personnes sont nécessaires
  Ci-dessous, nous spécifions cela sous la forme d'un 4-tuple (0,8000, 0,5405, 3, 111).

En comparaison, le même calcul suppose que chaque niveau doit apprendre 10 % de moins que le niveau supérieur suivant.

- L ne peut pas être enseigné.
  Soit x la proportion de temps pendant laquelle L apprend.
  Alors il enseigne 1-x.
  Résultat : [0/x/1-x/0].
- S1 est enseigné 1-x par L et apprend y sans professeur. 
  Puisque S1 doit apprendre 10 % de moins que L, ce qui suit s'applique : 2*(1-x)+y= 0.9x .
  Donc y=2,9x-2.
  Le reste du temps[1-(1-x)-(2.9x-2)=2-1.9x]enseigne S1.
  Rendements[1-x /2,9x-2 /2-1,9x /0].
- S2 apprend 2-1,9x par S1 le reste du temps (1-(2-1,9x)=1,9x-1), il fait autre chose. 
  Rendements[2-1,9x /0 /0 /1,9x-1].
- Pour que S2 0.9*0,9 = 0,81 fois plus vite que L apprend, doit être 0,81x = 2*(2-1,9x), donc x=0,8677. 
  Ainsi la vitesse d’apprentissage de L est de 0,8677, celle de S1 est de 0,7809 et celle de S2 est de 0,7028.
  En moyenne, cela fait 0,7113.
  Le temps non utilisé pour l'apprentissage (pondéré par la taille de l'unité) est de (100*0,6486+10*0+1*0)/111=0,5843.

Vous pouvez voir une nette différence dans la vitesse d'apprentissage calculée (0,7113 à 0,8000).
La taille absolue des valeurs indiquées ci-dessous ne doit pas être prise à la légère.
La comparaison entre eux est plus intéressante (A est plus rapide que B)

Maintenant en voici un **Aperçu de l’analyse de la chaîne d’apprentissage** pour les exemples ci-dessus.

- Chaîne L-S (pyramide à 2 couches) : (0,6667, 0,6061, 2, 11) 
- Pyramide à 3 couches, la couche intermédiaire n'apprend pas sans professeur : (0,6667, 0,6306, 3, 111). 
  À chaque quart de travail supplémentaire, la proportion de temps non consacré aux études approche 0,6333.
  La vitesse d'apprentissage reste la même.
- Pyramide à 3 couches, la couche intermédiaire apprend même sans professeur : (0,8000, 0,5405, 3, 111). 
- Pyramide à 4 niveaux, les niveaux intermédiaires apprennent même sans professeur : (0,8571, 0,5143, 4, 1111). 
- Pyramide à 5 niveaux, les niveaux intermédiaires apprennent même sans professeur : (0,8889, 0,5000, 5, 11111). 
- Pyramide à 2 couches et double pointe : (0,8000, 0,5000, 3, 12). 
  Les pics supplémentaires agissent de la même manière que les couches supplémentaires d’une pyramide.
  L'efficacité est légèrement inférieure, moins de personnes sont nécessaires.
- Deux enseignants (pour des compétences différentes) enseignant chacun l'un à l'autre et une unité d'étudiants : (1,0000, 0,4091, 3, 11). 
- Deux professeurs (pour des compétences différentes) qui enseignent chacun uniquement à l'unité étudiante : (1,2222, 0,2778, 3, 12). 
  Les élèves apprennent à une vitesse de 4/3, les professeurs seulement à 2/3.
- Si trois professeurs enseignent trois compétences différentes, les élèves peuvent (presque) toujours apprendre avec le professeur. 
  Malheureusement, il n'y a que quelques cas dans lesquels vous souhaitez apprendre trois compétences de manière permanente.

### Autres influences sur la vitesse

Les analyses ci-dessus montrent comment gagner plus de temps sur 100% en utilisant les leçons et en acceptant généralement une réduction de la vitesse d'apprentissage.
Cependant, pour certaines compétences, il est extrêmement important de les maîtriser au mieux tout en étant capable d'enseigner à suffisamment d'élèves.
L'objectif est donc d'augmenter la vitesse d'apprentissage au-dessus de 100 % (= toujours apprendre sans professeur).

L'augmentation grâce à l'académie et à la cire cérébrale est connue.
Ils ont chacun un effet d'un tiers lors de l'apprentissage sans professeur, c'est-à-dire que les deux aboutissent ensemble à une vitesse d'apprentissage de 166 %.

D'autres facteurs d'influence qui augmentent la vitesse d'apprentissage maximale sont les courses, le terrain et les familiers.
Cela profite du fait que la compétence fluctue en fonction de la « condition » et qu'en changeant la condition, une unité peut passer d'un enseignant à un élève.
Le meilleur exemple en est les insectes, qui peuvent développer toutes les compétences en combinaison avec d'autres races.

Sans trop entrer dans les détails, notons que la vitesse d’apprentissage maximale des meilleures unités peut dépasser 100 %.
Les considérations ci-dessus doivent donc être développées.

#### 5 pyramide

Supposons une académie et des ressources intellectuelles pour les 6 unités d'enseignants.
On obtient donc 5/3=166%.
Lors de l'enseignement il n'y a pas de progrès dans l'apprentissage (élèves non scolarisés) donc 0/3 = 0% dans ce cas.
Un professeur enseigne, 5 apprentissage -> 1/6*0/3 + 5/6*5/3 = 0 + 25/18 = 139 %.
Le niveau suivant comportant 3 unités d'enseignement est divisé en 2 apprentissages et 1 enseignement : 2/3*6/3 + 1/3*0% = 4/3 = 133% C'est légèrement plus lent, mais finalement plus rapide car chaque niveau a environ 10 % de moins à apprendre, comme mentionné ci-dessus.
Un à deux niveaux intermédiaires supplémentaires sont possibles, chacun multipliant par cinq le nombre d'étudiants possibles.

Si vous commencez avec deux unités au sommet, elles rempliront la moitié d’une académie – mais elles nécessitent également beaucoup de puissance cérébrale.
Le premier niveau intermédiaire comprend alors 3 unités de 10 personnes chacune, le deuxième comporte 3 unités de 50 personnes chacune.
Le troisième et sans doute dernier niveau intermédiaire compte 250 personnes par unité et peut donc former 2500 personnes d'un coup -à 200%, c'est à dire que les étudiants rattrapent leur retard.
Sinon, il y en aurait 3750 qui pourraient être enseignés jusqu'à 133 %.
c'est-à-dire qu'après avoir déduit quelques pourcentages pour les différences de niveaux, 4000 étudiants devraient être possibles.

<!-- From [https://wiki.eressea.de/index.php?title=Optimierung\_Lernketten&oldid=3553] -->
