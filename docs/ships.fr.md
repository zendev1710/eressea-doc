---
# cSpell:locale fr
alias: bateaux
---
# Bateaux

<!-- translated from german to french -->

Les bateaux sont construits avec l'ordre [[cmd-make|**`MAKE`**&#91;*`niveaux`*&#93;*`type de bateau`*]].  
Les bateaux existants, inachevés ou endommagés sont construits avec **`MAKE`**&#91;*`niveaux`*&#91;&nbsp;`SHIP`&nbsp;&#91;`*`id-bateau`*&#93;.  

Pour cela, il te faut du bois. Plus le bateau est complexe, plus il est difficile à construire et à commander.
Ceci est résumé dans le tableau ci-dessous.  

Pour commencer à construire un bateau, poursuivre sa construction ou le réparer, l'unité a besoin du niveau requis en compétence de construction navale.  
Le tableau indique la quantité de bois nécessaire pour construire un bateau.  
Une unité peut utiliser, par tour, le nombre de bois suivant : `niveau de compétence X nombre personnes / compétence min`.  

Un bateau rst défini par son identifiant, utilisé dans les ordres.  

Exemple :

```text
Fierté des Sept Vents (18), Drakkar, (254/500). Ce magnifique

    bateau était le premier que la famille de marchands Plötzbogen
    a construit. Le capitaine Gorm se tient sur le pont arrière et donne
    des ordres aux marins. Il a tout sous contrôle.
```

Pour tes propres bateaux, la charge et la capacité sont indiquées après le type de bateau (ici 254 unités de poids sur 500 possibles).

Dans le rapport, les unités qui se trouvent sur le bateau suivent la description du bateau.

La première unité est le capitaine et a le commandement du bateau.
Elle détermine quelles autres unités sont autorisées à monter à bord du bateau.
Elle peut [[cmd-name|renommer]] ou [[cmd-describe|décrire]] le bateau et elle compte également comme équipage.

Contrairement aux bâtiments, les bateaux ne peuvent pas être agrandis.
Donc, si vous avez commencé à construire un Drakkar, vous ne pouvez pas le transformer en caravelle plus tard.

Les bateaux nouvellement construits ne sont situés sur aucune côte et peuvent donc partir vers n'importe quelle région océanique voisine.

## Types de bateau

### Barque

<!-- cspell:disable -->
*Boat (EN), Boot (DE).*
<!-- cspell:enable -->

### Chaloupe

<!-- cspell:disable -->
*Longboat (EN), Langboot (DE).*
<!-- cspell:enable -->

### Drakkar

<!-- cspell:disable -->
*Dragonship (EN), Drachenschiff (DE).*
<!-- cspell:enable -->

### Caravelle

<!-- cspell:disable -->
*Caravel (EN), Karavelle (DE).*
<!-- cspell:enable -->

### Trirème

<!-- cspell:disable -->
*Trireme (EN), Trireme (DE).*
<!-- cspell:enable -->

### Galion

<!-- cspell:disable -->
*Galleon (EN), Galeone (DE).*
<!-- cspell:enable -->

### Bateaux - Tableau de synthèse

Bateaux - Type, portée, capacité, compétence de [voile] nécessaire, niveau de compétence de construction navale nécessaire, bois nécessaire.

| Type      | Portée | Capacité | Capitaine/Équipage | Niv. construction |  Bois |
|-----------|:------:|---------:|-------------------:|:-----------------:|------:|
| Barque    |   2    |       50 |                1/2 |         1         |     5 |
| Chaloupe  |   3    |      500 |               1/10 |         1         |    50 |
| Drakkar   | 5[^1]  |    1 000 |               2/50 |         2         |   100 |
| Caravelle |   5    |    3 000 |               3/30 |         3         |   250 |
| Trirème   |   7    |    2 000 |              4/120 |         4         |   200 |
| Galion    |   5    |   20 000 |          5/250[^2] |         5         | 2 000 |

[^1]: la vitesse du drakkar dépend de la compétence en voile du capitaine.  
[^2]: pour un galion, le calcul de la compétence totale en voile ne prend en compte que les unités de niveau 2 ou plus.  

Vitesse du drakkar en fonction du niveau en compétence de voile du capitaine.

| Capitaine | 2 | 6 | 18 | 54 | 162 |
|-----------|---|---|----|----|:---:|
| Portée    | 5 | 6 | 7  | 8  |  9  |

## Convoi

De la même manière que l'on peut avoir plusieurs personnes dans une unité, les convois sont composés de plusieurs bateaux **du même type**, par exemple :

```text
Karavelle (2seh), 73 Karavellen, (12776/85410), 61% damaged.
```

Pour cela, on remet à l'unité propriétaire d'un bateau un ou plusieurs bateaux du même type avec l'ordre `GIVE`` `*`target-captain`*` ``1 SHIP`.
L'unité cible devient le commandant d'un convoi.
Les unité sources et cibles **doivent appartenir à la même faction**, les ordres `HELP ALL` ou `CONTACT` ne suffisent pas.

L'unité propriétaire d'un convoi dirige tous ses bateaux ensemble et doit pour cela :

- Avoir le niveau de compétence requis en [voile] pour le type de bateau
- Avoir une personne par bateau

Le compétence totale de l'équipage doit également être un multiple correspondant au nombre de bateaux.  
La portée correspond à celle du type de bateau, les dégâts maximums et la charge utile augmentent en fonction du nombre de bateaux.  

Exemple.

Un convoi de 3 caravelles nécessite un capitaine d'au moins 3 personnes avec [voile] T3 et un équipage avec 90 niveaux de compétence au total.
Comme précédemment, elles ont une portée de 5 cases, mais une capacité de 9000 kg. La configuration suivante, par exemple, est donc autorisée et en état de naviguer :

```text
Caravel (2seh), 3 Caravels, (9000/9000).
    * Kapitänsteam (k29), 3 Humans, Skill: Sailing 3.
    * Besatzung (2ztf), 9 Humans, Skill: Sailing 9.
    * Horde (770L), 888 Humans.
```

Comme on peut le voir, il est possible de déplacer de grandes unités dans un convoi sans les répartir sur des bateaux individuels.  
Pour le reste, les convois se comportent comme un bateau normal.  
Par exemple, le convoi entier part à la dérive ensemble, subit des dégâts dans son ensemble et le commandement peut être transféré.  

Les [barques] sont exclus de cette règle et les bateaux d'un convoi doivent être du même type.  
Il n'est donc pas permis, par exemple, de mélanger des trirèmes et des caravelles.  

Les bateaux endommagés ou incomplets peuvent également être transférés, leur état se répercute alors proportionnellement sur le convoi.
Si un bateau avec 8% de dommages est remis à un convoi de 3 bateaux, le convoi se compose ensuite de 4 bateaux avec 2% de dommages.
Si un seul bateau en construction est remis, tout le convoi est ensuite en construction et ne peut naviguer qu'une fois terminé.
Un bateau achevé à 50% (en construction) et un bateau achevé donne deux bateaux achevés à 75% (en construction).

Le même ordre permet également de détacher des bateaux d'un convoi.  
Les bateaux ou les convois de l'unité donneuse et de l'unité réceptrice doivent se trouver sur la même côte ou sur l'océan.  
L'unité réceptrice doit soit être capitaine d'un bateau — dans ce cas, le bateau est ajouté à son convoi — soit être sur le même bateau que l'unité donneuse, soit ne pas être dans un bateau ou dans un bâtiment.  

On peut aussi donner des bateaux aux paysans : `GIVE 0 2 SHIP` crée un nouveau convoi avec 2 bateaux, sur lequel il n'y a personne.  
À terre, un commandant de convoi ne peut pas remettre tous ses bateaux aux paysans, il doit toujours en garder au moins un.  

Si, après le transfert, l'unité transférée n'a plus de bateaux, toutes les unités qui l'accompagnaient auparavant passent automatiquement sur les bateaux de l'unité de destination.  

Les convois ne peuvent pas être enchantés, les bateaux enchantés ne peuvent pas être transférés et aucun bateau ne peut être transféré aux propriétaires de bateaux enchantés.  

Expérience de jeu (Solthar) :

Une unité vide ne peut rien céder.  
C'est pourquoi l'ordre dans la séquence d'écriture des ordres suivants est importante :

```text
GIVE 123 1 SHIP
GIVE 123 ALL MEN
```

## Voir aussi

- [[deplacements]]
- [[cmd-give]]

Poursuivre la lecture : [[batiments]].

<!-- From [https://wiki.eressea.de/index.php?title=Schiff/fr&oldid=16676] -->

[barques]: #barque
[voile]: ./skills-list.md#voile "Sailing"
