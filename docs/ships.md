---
# cSpell:locale en
alias: ships
---
# Ships

<!-- translated from german to english -->

Ships are built using the command [[cmd-make|**`MAKE`**`[`*`levels`*`]`*`ship type`*]].  
Existing, unfinished, or damaged ships can be further built using **`MAKE`**`[`*`levels`*`] SHIP [`*`ship-id`*`]`.  

Wood is needed for this. The more complex the ship, the harder it is to build and command.
This is summarized in the table below.  

To start building a ship or to continue building or repairing one, the unit needs at least the specified shipbuilding skill.  
The table shows how much wood is required to build a ship.  
A unit can use per round this number of woods : `skill level X people / minimum skill`.

A ship also has an id that is used in orders. Here is an example of a ship:

```text
Pride of the Seven Winds (18), Longboat, (254/500). This beautiful

    ship was the first to be built by the Plötzbogen merchant family
    used. Captain Gorm stands on the quarterdeck and gives orders
    Orders to the sailors. He has everything completely under control.
```

For your own ships, the ship type indicates the load and capacity (here 254 weight units out of 500 possible).

In the report, the units that are on the ship are indented under the ship.

The first unit is a captain and has command of the ship.
The captain determines which other units are allowed to board the ship.
He may [[cmd-name|rename]] or [[cmd-describe|describe]] the ship, and also counts as crew.

Unlike buildings, ships cannot be expanded.
So once you start building a longboat, you won't be able to convert it into a caravel later.

Newly built ships are not located on any coast and can therefore sail to any neighboring ocean region.

Ships - type, range, capacity, needed sailing skill for captain/crew, needed building skill, needed wood.

| Type       | Range | Capacity | Captain/Crew | Building skill | Wood |
|------------|------:|---------:|-------------:|---------------:|-----:|
| Boot       |     2 |       50 |          1/2 |              1 |    5 |
| Longboat   |     3 |      500 |         1/10 |              1 |   50 |
| Dragonship |    5* |     1000 |         2/50 |              2 |  100 |
| Caravel    |     5 |     3000 |         3/30 |              3 |  250 |
| Trireme    |     7 |     2000 |        4/120 |              4 |  200 |
| Galleon    |     5 |    20000 |      5/250** |              5 | 2000 |

\* Dragonship speed depends on captain sailing skill.  
\*\* Only units from level 2 in sails are taken into account for the overall skill of the galleon.  

Dragon ship speed.

| Captain | 2 | 6 | 18 | 54 | 162 |
|---------|---|---|----|----|-----|
| Range   | 5 | 6 | 7  | 8  | 9   |

## Convoy

De la même manière que l'on peut avoir plusieurs personnes dans une unité, les convois sont composés de plusieurs bateaux du même type, par exemple

```text
Karavelle (2seh), 73 Karavellen, (12776/85410), 61% damaged.
```

Pour cela, on remet à l'unité propriétaire d'un bateau un ou plusieurs bateaux du même type avec l'ordre GIVE capt 1 SHIP. L'unité recevante devient le commandant d'un convoi. L'unité remettante et l'unité réceptrice doivent appartenir à la même faction, HELP ALL ou CONTACT ne suffisent pas. L'unité propriétaire d'un convoi commande tous ses bateaux ensemble et doit pour cela avoir le niveau de compétence minimum pour le type de bateau et une personne par bateau. Le talent total de l'équipage doit également être un multiple correspondant au nombre de bateaux. La portée correspond à celle du type de bateau, les dégâts maximums et la charge utile augmentent en fonction du nombre de bateaux.

Exemple : un convoi de 3 caravelles nécessite un capitaine d'au moins 3 personnes avec Sailing T3 et un équipage avec 90 niveaux de compétence au total. Comme précédemment, elles ont une portée de 5 cases, mais une capacité de 9000 kg. La configuration suivante, par exemple, est donc autorisée et en état de naviguer :

```text
Caravel (2seh), 3 Caravels, (9000/9000).
    * Kapitänsteam (k29), 3 Humans, Skill: Sailing 3.
    * Besatzung (2ztf), 9 Humans, Skill: Sailing 9.
    * Horde (770L), 888 Humans.
```

Comme on peut le voir, il est donc possible de déplacer de grandes unités dans un convoi sans les répartir sur des bateaux individuels. Pour le reste, les convois se comportent comme un bateau normal. Par exemple, le convoi entier part à la dérive ensemble, subit des dégâts dans son ensemble et le commandement peut être transféré.

Les "boats" sont exclus de cette règle et les bateaux d'un convoi doivent être du même type, il n'est donc pas permis, par exemple, de mélanger des trirèmes et des caravelles.

Les bateaux endommagés ou incomplets peuvent également être transférés, leur état se répercute alors proportionnellement sur le convoi. Si un bateau avec 8% de dommages est remis à un convoi de 3 bateaux, le convoi se compose ensuite de 4 bateaux avec 2% de dommages. Si un seul bateau en construction est remis, tout le convoi est ensuite en construction et ne peut naviguer qu'une fois terminé. Un bateau achevé à 50% (en construction) et un bateau achevé donne deux bateaux achevés à 75% (en construction).

Le même ordre permet également de détacher des bateaux d'un convoi. Les bateaux ou les convois de l'unité donneuse et de l'unité réceptrice doivent se trouver sur la même côte ou sur l'océan. L'unité réceptrice doit soit être capitaine d'un bateau — dans ce cas, le bateau est ajouté à son convoi — soit être sur le même bateau que l'unité donneuse, soit ne pas être dans un bateau ou dans un bâtiment.

On peut aussi donner des bateaux aux paysans : GIVE 0 2 SHIP crée un nouveau convoi avec 2 bateaux, sur lequel il n'y a personne. A terre, un commandant de convoi ne peut pas remettre tous ses bateaux aux paysans, il doit toujours en garder au moins un.

Si, après le transfert, l'unité transférée n'a plus de bateaux, toutes les unités qui l'accompagnaient auparavant passent automatiquement sur les bateaux de l'unité de destination.

Les convois ne peuvent pas être enchantés, les bateaux enchantés ne peuvent pas être transférés et aucun bateau ne peut être transféré aux propriétaires de bateaux enchantés.

Expérience de jeu : Solthar Eine leere Einheit kann nichts übergeben. Deshalb ist bei folgenden Befehlen die Reihenfolge wichtig:

```text
GIVE 123 1 SHIP
GIVE 123 ALL MEN
```

## Voir aussi

- [[travel]]
- [[cmd-give]]

Continue reading: [[buildings]].

<!-- From [https://wiki.eressea.de/index.php?title=Schiff/fr&oldid=16676] -->
