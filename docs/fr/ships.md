# Bateaux

Schiffe werden dem Befehl [**`MAKE`**`[`*`stufen`*`]`*`Schiffstyp`*][1] gebaut. Existierende, unfertige oder beschädigte Schiffe werden mit **`MAKE`**`[`*`stufen`*`] SHIP [`*`schiff-nr`*`]` weitergebaut. Dafür braucht man Holz. Je komplexer das Schiff, um so schwerer ist es zu erbauen und zu kommandieren. Dies ist in der Tabelle weiter unten zusammengefasst. Um mit dem Bau eines Schiffes zu beginnen oder an einem Schiff weiterzubauen bzw. es zu reparieren, braucht die Einheit mindestens das angegebene Schiffbautalent. In der Tabelle ist aufgeführt, wie viel Holz benötigt wird, um ein Schiff zu bauen. Eine Einheit kann pro Runde (Talentstufe \* Personen / Mindesttalent) Holz verbauen.

Auch Schiffe haben Nummern, die in Befehlen gebraucht werden. Hier ein Beispiel für ein Schiff:

Stolz der Sieben Winde (18), Langboot, (254/500). Dieses schöne

       Schiff war das erste, welches die Händlerfamilie Plötzbogen
       einsetzte.  Kapitän Gorm steht auf dem Achterdeck und erteilt
       Befehle an die Matrosen. Er hat alles voll im Griff.

Bei eigenen Schiffen steht hinter dem Schiffstyp die Beladung und die Kapazität (hier 254 Gewichtseinheiten von 500 möglichen).

Unter einem Schiff sind die Einheiten eingerückt, die sich auf dem Schiff befinden. Die erste Einheit ist Kapitänin und hat das Kommando über das Schiff. Sie bestimmt, welche anderen Einheiten das Schiff betreten dürfen. Sie darf das Schiff [umbenennen] oder [beschreiben] und sie zählt auch als Besatzung.

Im Gegensatz zu Gebäuden können Schiffe nicht erweitert werden. Wer also einmal begonnen hat, ein Langboot zu bauen, kann dies später nicht zu einer Karavelle umbauen.

Neu gebaute Schiffe liegen an keiner Küste und können deshalb in jede benachbarte Ozeanregion ablegen.

Schiffe - Reichweite, Kapazität, Talente

|               |            |           |                   |           |         |
|---------------|------------|-----------|-------------------|-----------|---------|
| Typ           | Reichweite | Kapazität | Kapitän/Besatzung | Bautalent | Bauholz |
| Boot          | 2          | 50        | 1/2               | 1         | 5       |
| Langboot      | 3          | 500       | 1/10              | 1         | 50      |
| Drachenschiff | 5\*        | 1000      | 2/50              | 2         | 100     |
| Karavelle     | 5          | 3000      | 3/30              | 3         | 250     |
| Trireme       | 7          | 2000      | 4/120             | 4         | 200     |
| Galeone       | 5          | 20000     | 5/250\*\*         | 5         | 2000    |

\* Drachenschiffgeschwindigkeit abhängig vom Kapitänstalent.

\*\* Für das Gesamttalent der Galeone werden nur Einheiten ab T2 in Segeln herangezogen

Drachenschiffgeschwindigkeit

|            |   |   |    |    |     |
|------------|---|---|----|----|-----|
| Kapitän    | 2 | 6 | 18 | 54 | 162 |
| Reichweite | 5 | 6 | 7  | 8  | 9   |

## Convoi

De la même manière que l'on peut avoir plusieurs personnes dans une unité, les convois sont composés de plusieurs bateaux du même type, par exemple

       Karavelle (2seh), 73 Karavellen, (12776/85410), 61% damaged.

Pour cela, on remet à l'unité propriétaire d'un navire un ou plusieurs navires du même type avec l'ordre GIVE capt 1 SHIP. L'unité recevante devient le commandant d'un convoi. L'unité remettante et l'unité réceptrice doivent appartenir à la même faction, HELP ALL ou CONTACT ne suffisent pas. L'unité propriétaire d'un convoi commande tous ses navires ensemble et doit pour cela avoir le niveau de compétence minimum pour le type de navire et une personne par navire. Le talent total de l'équipage doit également être un multiple correspondant au nombre de navires. La portée correspond à celle du type de navire, les dégâts maximums et la charge utile augmentent en fonction du nombre de navires.

Exemple : un convoi de 3 caravelles nécessite un capitaine d'au moins 3 personnes avec Sailing T3 et un équipage avec 90 niveaux de compétence au total. Comme précédemment, elles ont une portée de 5 cases, mais une capacité de 9000 GE. La configuration suivante, par exemple, est donc autorisée et en état de naviguer :

     Caravel (2seh), 3 Caravels, (9000/9000).
       * Kapitänsteam (k29), 3 Humans, Skill: Sailing 3.
       * Besatzung (2ztf), 9 Humans, Skill: Sailing 9.
       * Horde (770L), 888 Humans.

Comme on peut le voir, il est donc possible de déplacer de grandes unités dans un convoi sans les répartir sur des navires individuels. Pour le reste, les convois se comportent comme un navire normal. Par exemple, le convoi entier part à la dérive ensemble, subit des dégâts dans son ensemble et le commandement peut être transféré.

Les "boats" sont exclus de cette règle et les navires d'un convoi doivent être du même type, il n'est donc pas permis, par exemple, de mélanger des trirèmes et des caravelles.

Les navires endommagés ou incomplets peuvent également être transférés, leur état se répercute alors proportionnellement sur le convoi. Si un navire avec 8% de dommages est remis à un convoi de 3 navires, le convoi se compose ensuite de 4 navires avec 2% de dommages. Si un seul navire en construction est remis, tout le convoi est ensuite en construction et ne peut naviguer qu'une fois terminé. Un navire achevé à 50% (en construction) et un navire achevé donne deux navires achevés à 75% (en construction).

La même commande permet également de détacher des navires d'un convoi. Les navires ou les convois de l'unité donneuse et de l'unité réceptrice doivent se trouver sur la même côte ou sur l'océan. L'unité réceptrice doit soit être capitaine d'un navire — dans ce cas, le navire est ajouté à son convoi — soit être sur le même navire que l'unité donneuse, soit ne pas être dans un navire ou dans un bâtiment.

On peut aussi donner des bateaux aux paysans : GIVE 0 2 SHIP crée un nouveau convoi avec 2 bateaux, sur lequel il n'y a personne. A terre, un commandant de convoi ne peut pas remettre tous ses bateaux aux paysans, il doit toujours en garder au moins un.

Si, après le transfert, l'unité transférée n'a plus de navires, toutes les unités qui l'accompagnaient auparavant passent automatiquement sur les navires de l'unité de destination.

Les convois ne peuvent pas être enchantés, les navires enchantés ne peuvent pas être transférés et aucun navire ne peut être transféré aux propriétaires de navires enchantés.

Expérience de jeu : Solthar Eine leere Einheit kann nichts übergeben. Deshalb ist bei folgenden Befehlen die Reihenfolge wichtig:

```
  GIVE 123 1 SHIP
  GIVE 123 ALLES PERSONS
```

## Voir aussi

- [naviguer]
- [GIVE]

|              |           |
|--------------|-----------|
| Weiterlesen: | [Gebäude] |

[Gebäude]: ./buildings.md "Gebäude"

<!-- From [https://wiki.eressea.de/index.php?title=Schiff/fr&oldid=16676] -->

[1]: ./cmd-make.md "MAKE"
[umbenennen]: ./cmd-name.md "NAME"
[beschreiben]: ./cmd-describe.md "DESCRIBE"
[naviguer]: ./travel.md "Schiffsreise"
[GIVE]: ./cmd-give.md "GIVE"
