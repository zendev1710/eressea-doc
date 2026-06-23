---
# cSpell:locale fr
alias: transport-optimise
---
# Transport optimisé

## Représentant de commerce

Comme dans Eressea nous ne traitons pas seulement quelques unités mais un grand nombre d'entre elles, le problème des vendeurs ambulants se pose moins, car les transports ne vont souvent pas dans plusieurs régions en cercle, mais les demandes sont plutôt traitées en parallèle avec de nombreux transports individuels.  

## Chargement optimal

Il est logique d'utiliser le problème du sac à dos lors du chargement d'un transport de marchandises.  
Cependant, dans Eressea, vous tombez rapidement dans le piège d’essayer de charger trop d’éléments similaires.  
Les optimisations du problème du sac à dos peuvent difficilement résoudre ce problème.

Un exemple simple :

Vous devez transporter 10 pierres (60 lbs chacune) et 100 bijoux (1 lbs chacun).  
Cependant, seule une capacité de 500 lbs est disponible.  
Une pierre vaut 1 200, un bijou une valeur de 50.  
Comme les bijoux offrent plus de valeur au lbs (50 par lbs), nous chargeons d'abord tous les bijoux :

```text
Value  = 100 * 50 = 5000
Charge = 100 * 1 lbs = 100 lbs
Free   = 400 lbs
```

À 400 lbs on arrive quand même à charger 6 pierres, laissant 40 lbs libres.

```text
Value  = 5000 + 6 * 1200 = 12200
Charge = 100 lbs + 6 * 60 lbs = 460 lbs
Free   = 40 lbs
```

Alors essayons d'abord avec les pierres : 8 pierres, puis il reste encore de la place pour 20 bijoux :

```text
Value  = 20 * 50 + 8 * 1200 = 10600
```

Apparemment, ce n'était rien.
Mais peut-il y avoir une meilleure solution ? Oui, 7 pierres et 80 rubis semblent mieux utiliser la capacité :

```text
Value  = 80 * 50 + 7 * 1200 = 12400
```

La voie à suivre passe par exemple par la recherche gloutonne, c'est-à-dire la recherche dans tous les états.  
Dans ce cas, 0 à 8 pierres et 0 à 100 rubis (parfois moins) signifient environ 900 conditions à vérifier.  
Si l’on imagine maintenant un 3ème ou un 4ème produit, il devient vite évident que nous n’obtiendrons pas le résultat.  

Normalement, le moyen le plus rapide d’atteindre l’objectif consiste à passer par les états intermédiaires dits Pareto-optimaux.  
Ce que sont ces états intermédiaires peut être plus facilement expliqué dans l’autre sens.  
Les états qui ont moins de valeur qu’un autre état intermédiaire avec le même chargement ne sont pas Pareto optimaux.  
Il n’est pas nécessaire d’aller plus loin, car apparemment, seuls des états non Pareto-optimaux peuvent toujours être atteints.  

Par exemple, si vous comparez la condition « 60 rubis » avec « 1 pierre », vous constaterez que 60 rubis valent évidemment beaucoup plus avec la même charge.  
Cela ne vaut donc pas la peine d'étendre davantage "1 pierre".  
À proprement parler, vous arrivez à cette conclusion une fois que vous avez développé 24 joyaux.  

Ce type de calcul optimal est problématique car apparemment, tout nombre de rubis compris entre 0 et 100 est Pareto optimal.  
Pire encore, toute combinaison de 1 à 6 pierres de 77 à 100 rubis et de 7 pierres de 77 à 80 rubis est Pareto optimale.  
Malgré l'optimisation, nous devons étendre 100 + 6*24 + 4 = 248 états sur environ 900 états jusqu'à ce que nous puissions être sûrs de la solution que nous avons trouvée - ce qui n'est pas un bon résultat.  

Cependant, une autre optimisation est possible.  
Nous pouvons limiter les quantités de transport utilisées.  
Puisque les bijoux valent la peine tant qu'ils totalisent un nombre entier de pierres, le nombre de bijoux est compris entre 60 et 100.
Cependant, les bijoux ne peuvent jamais occuper la totalité de la capacité, c'est pourquoi un minimum de 6 pierres et un maximum de 8 peuvent être pris.
Cela réduit la recherche à 41*3 ou avec les états intermédiaires Pareto-optimaux à 41 + 24 + 4 = 69 états.

!!! warning "Attention"
    Si vous priorisez les marchandises au lieu de les évaluer, il est peu probable que ce type de paquet soit utilisé.  
    Alors ce qui suit s'applique : la priorité la plus élevée en premier...

### Paquets

Souvent, le transport des matières premières ne devient rentable que lorsque toutes les matières premières nécessaires arrivent à destination.  
L’idée est désormais d'empaqueter ces matières premières.  
Cela peut impliquer soit de les envoyer tous ou pas du tout, soit d'ajouter un bonus lorsque la taille du colis est atteinte.  
Étant donné que les matières premières d'Eressea proviennent de différentes régions, la première option entraînerait probablement une livraison nulle.  
La deuxième variante serait souhaitable, mais malheureusement elle torpille l’optimisation avec des états intermédiaires Pareto-optimaux.  
Reste la première variante limitée à un seul type d'objet.  
La question de savoir si l’effort en vaut la peine reste discutable.  

Indépendamment de cela, il est bien sûr possible et utile de noter un peu plus haut les éléments manquants pour atteindre un objectif.  

Il peut être judicieux de différencier deux ou trois types de paquets:

1. Groupes d'objets qui ne peuvent être utilisés que dans leur ensemble, par ex. niveaux individuels d'un bâtiment, plusieurs composants pour des potions ou des armes.
   Ces objets ne peuvent pas être traités individuellement à destination, c'est-à-dire que vous devez attendre que le dernier composant soit arrivé
2. Des groupes d'objets ou des sous-groupes de la catégorie supérieure sont nécessaires pour une utilisation complète dans la production hebdomadaire.
   Cependant, la production peut également être réalisée sans pleine capacité.
   Cela réduit simplement le temps pendant lequel autre chose peut être fait si nécessaire.
3. Groupes d'objets ou sous-groupes des catégories supérieures nécessaires à l'accomplissement complet d'une mission, c'est-à-dire terminer un bateau ou un bâtiment, ou équiper entièrement une unité de son équipement.
   Il peut être produit, peut-être même à pleine capacité.
   Il n’est tout simplement pas certain que tous les composants arriveront bientôt et seront terminés.

Les deux derniers groupes peuvent probablement être regroupés dans la pratique et très probablement ignorés.  
Pour le premier groupe, cependant, une prime d’accomplissement est envisageable et pourrait également être prévue.  

## Recherche multi-chemins

Lors de la planification du transport, il peut arriver qu'un transport ait déjà une certaine cargaison et donc une région cible.
Cependant, il existe encore de la capacité disponible pendant le transport qui pourrait être occupée par d'autres marchandises.
Des options simples consistent désormais à distribuer uniquement les marchandises nécessaires aux points intermédiaires de l'itinéraire.
Des techniques avancées chargent les marchandises, ce qui les rapproche un peu plus de leur objectif.

Cependant, il me semble également possible d'adapter l'itinéraire de manière à ce qu'un itinéraire soit recherché avec la même durée vers la première destination, qui mène en même temps le plus près possible, voire sur la région de la deuxième destination.  
Il est également envisageable d'optimiser l'itinéraire en le faisant passer par des « points de transbordement » afin que les marchandises destinées à la deuxième destination puissent ensuite également trouver un transport dans la région de la fourche.

Alors, comment une telle recherche multi-chemins pourrait-elle fonctionner ?  
Les tours jusqu'à l'arrivée à la destination 1 sont connus.  
Ainsi, seuls les itinéraires qui ne prennent pas plus de temps sont pris en compte.  
Cependant, vous ne le savez que lorsqu'un itinéraire a été trouvé.  
La distance minimale jusqu'à la destination 2 est le deuxième critère d'évaluation de l'itinéraire et rend le calcul de l'itinéraire un peu plus « gourmand », puisque toutes les régions qui donnent la même valeur au critère 1 sont désormais déplacées vers 2.  
La valeur doit être testée. Heureusement, la fonction d'estimation fournit également un bon service ici.  

### Objectifs équivalents

Si plusieurs destinations sont équivalentes, elles entreront bien entendu en compétition pour le prochain itinéraire à partir d'un certain point.  
En attendant, vous pouvez facilement optimiser l'itinéraire au minimum des deux itinéraires, c'est-à-dire que vous conduisez vers la région la plus proche et déchargez les marchandises pour l'autre région lorsque vous êtes le plus proche possible.  

Cependant, à mesure que de plus en plus de destinations s'ajoutent, le transport devient en réalité un « voyageur de commerce » local.  
Je n'ai pas encore examiné de plus près si et quand cela vaut réellement la peine de faire un petit tour ici.  
Mais bien sûr, il existe une telle limite.  

### Points de transbordement

Cependant, la recherche de chemins multiples peut également être beaucoup plus facile.  
Si vous définissez suffisamment de points de transbordement, vous pouvez attribuer les transports comme points intermédiaires pour les itinéraires de plus d'une semaine **toujours** se rendre aux points de transbordement, ou du moins le faire lorsqu'une limite de capacité est dépassée ou que le point de transbordement ne nécessite pas de détour.  

Le système de transport de l'ancienne CEE reconnaissait implicitement ce fait en étant organisé hiérarchiquement.  
Les points de transbordement sont des régions qui ont des régions subordonnées.  
Cependant, la hiérarchie implique souvent des détours.
Le bon fonctionnement d’un tel système dépend également de la topologie de l’île.
Les îles formant des anneaux sont particulièrement inadaptées à un système de transport strictement hiérarchique.

## Evaluation function

Divers algorithmes d'optimisation nécessitent une fonction d'évaluation pour évaluer les états intermédiaires et cibles possibles.  

Trouver une telle fonction pour les « états logistiques » n’est pas facile à première vue.  

Quoi et comment l’évaluer au mieux ?

- Satisfaire un maximum de demandes ?
- Utilisation de la capacité de transport existante ?
- Influence des priorités et des valeurs ?

Comme pour l’apprentissage, il est préférable de placer les uns à côté des autres différents choix très simples et de les différencier les uns des autres.  
Important : toutes les propriétés non mentionnées sont les mêmes.  

Règles de notation simples :

- Il est préférable d'utiliser une offre proche plutôt qu'une offre lointaine
- Il est préférable de répondre à une demande hautement prioritaire plutôt qu'à une demande peu prioritaire
- Il est préférable de répondre à une demande à partir d'une source proche plutôt que d'une source distante

Règles d'évaluation plus compliquées :

- Il vaut mieux utiliser pleinement un moyen de transport que de le faire voyager avec beaucoup d'espace vide.  
  La distinction entre « bon » et « beaucoup » est ici la question la plus complexe.  
  Des objets de même valeur mais de poids différent supposent des approches différentes selon l'environnement.  
  Si le transport ne peut pas être utilisé à pleine capacité avec l'objet léger et qu'il n'y a pas d'autres marchandises à transporter, l'objet le plus lourd est préférable.  
- Les demandes groupées (colis) doivent arriver à destination en même temps (ou le plus tôt possible)
- Il est préférable d'apporter quelque chose dans un centre de transbordement plutôt que de le laisser traîner, mais seulement si le centre de transbordement n'est pas plus éloigné et peut être atteint en une semaine.
- La priorité peut également être comprise selon deux dimensions : urgence et importance.  
  Il faut cependant pouvoir comparer deux de ces points bidimensionnels.
- Il est préférable de laisser un transport se diriger à vide vers une région ayant un besoin urgent de ravitaillement plutôt que vers une région de transbordement.  
  Mais cette dernière solution est toujours meilleure que simplement apprendre ou ne rien faire.  
- S'il n'y a pas de transport dans une source proche, qu'il y en a dans une source plus éloignée et que l'itinéraire passe par la source proche, le transport doit alors être arrêté si la source éloignée après le chargement aurait moins de marchandises que la source proche après le chargement.  
  - Exemple :
    - A a besoin de 100 pierres
    - En B, à un tour de A, il y a 1000 pierres. Il n'y a pas de transport disponible en B.
    - En C, à deux tours de A et un de B, il y a 500 pierres. Transport disponible --> Le transport doit voyager à vide de C à B si nécessaire
    - S'il y a 2000 pierres en C, les pierres sont enlevées
    - S'il y a 1050 pierres en C, 75 pierres sont prises. Après avoir chargé pour le transport, les deux sources disposent encore de 975 pierres

### Base d'évaluation de la valeur des marchandises

La base ici est une valeur de base des marchandises spécifiée par l'utilisateur pour chaque article.  
Des calculs prenant en compte l’offre et la demande mondiales sont également envisageables.  

La valeur des marchandises contient donc l’importance globale de l'objet.

La valeur des biens de base peut par exemple être exprimé en argent.  
Une marchandise pourrait par exemple utiliser la moyenne du prix d’achat et du prix de vente comme valeur.  
Il devient de plus en plus difficile d’évaluer des matières premières rares comme l’argent.  
Une surévaluation pourrait autrement conduire à ce que l'argent destiné à l'entretien ne soit pas livré parce qu'il manque une épée quelque part et que le transport emprunte donc un itinéraire différent.

#### Modification par urgence

Il est donc clair que la valeur sous-jacente doit encore être modifiée.  
L’urgence devrait pouvoir avoir un effet si fort que même les objets ayant une faible valeur de base deviennent suffisamment intéressants.  
Une fonction exponentielle ou similaire sur l'urgence a donc du sens.  

```text
f(arrondir jusqu'à nécessaire) = ?
f(0)=10000 % * Valeur sous-jacente
f(1)=1000 % * Valeur sous-jacente
f(2)=200 % * Valeur sous-jacente
f(3)=50 % * Valeur sous-jacente
f(4)=15 % * Valeur sous-jacente
f(5)=8 % * Valeur sous-jacente
f(un jour)=5 % * Valeur sous-jacente
```

Ce seraient des valeurs que j'ai en tête en ce moment et qui sont soit stockées dans une table de recherche, soit modélisées par une fonction.  
L'étendue de cette formule dépend essentiellement de la gamme d'actifs sous-jacents utilisée.  
Une épée flamboyante nécessaire à un moment donné peut avoir une valeur de base de 10 000, mais les 10 silver nécessaires de toute urgence pour l'entretien dans une autre région doivent toujours donner lieu à une valeur totale plus élevée.  
Avec la formule ci-dessus, l’épée flamboyante vaudrait 500 et les 10 silver en vaudraient 100 – trop peu pour être livrés.  
Par conséquent, les paramètres de la fonction d'urgence doivent être calculés sur la base des valeurs min et max des valeurs de base.  

Bien entendu, l’importance d’un objet peut aussi varier localement car les conditions environnementales sont différentes.  

#### Modification par suppression

Il arrive souvent qu'un produit ne puisse pas être livré directement à la demande par le fournisseur parce que les deux régions sont trop éloignées l'une de l'autre.  
Toutefois, afin d'assurer une livraison à partir d'une source la plus proche possible, il convient d'évaluer l'exécution partielle d'une demande à différents niveaux sur les différents tronçons.  

#### Évaluation des parcours à vide

Des voyages à vide peuvent être nécessaires pour ne pas se retrouver coincés dans des régions qui ne fonctionnent que comme des puits.  

Il peut y avoir deux objectifs motivés différents pour les voyages à vide :

1. En route vers les régions où il y a un besoin urgent des biens
2. En route vers les régions de transbordement – ​​il y a toujours beaucoup à transporter ici

Il peut même être judicieux de voyager à vide.

<!-- From [https://wiki.eressea.de/index.php?title=Optimierung\_Transport&oldid=2585] -->
