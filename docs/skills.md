---
# cSpell:locale en
alias: skills
---
# Skills

Les compétences sont un élément essentiel qui définit une [[cmd-unit|unité]] dans Eressea.
Toutes les personnes d'une unité ont les mêmes compétences.
Elles doivent d'abord les apprendre.
Pour être précis, avec l'ordre [[cmd-learn]], une unité peut faire une tentative par tour pour gagner un nouveau niveau.

Certaines compétences s'améliorent également en les utilisant.
Si l'unité utilise la compétence, il y a 1/3 de chances qu'elle gagne de l'expérience (2/3 de chances qu'elle n'en gagne pas).
Donc en exerçant une compétence une unité progresse à environ 1/3 de la vitesse d'apprentissage (de LEARN).
Les compétences qui ne s'améliorent *pas* en les exerçant sont toutes les compétences d'armes, endurance, perception, tactics et taxation.

Dans la plupart des cas, la valeur de compétence affichée dans le rapport est à celle à utiliser.
Elle inclut les bonus raciaux, régionaux et des éléments comme la famine ou la magie, qui modifient la valeur de la compétence.
Mais parfois, la valeur de compétence "brute" sans bonus est également nécessaire, notamment pour calculer les coûts d'apprentissage de la magie et les temps d'apprentissage.

## Learn skills

Atteindre un nouveau niveau de compétence devient de plus en plus difficile à chaque niveau.
En moyenne, la progression vers un nouveau niveau de compétence avec la commande [[cmd-learn]] prend environ un nombre de semaines égal au niveau de compétence visé, sans tenir compte des modifications apportées par la [[races|race]] ou le terrain.
Le temps d'apprentissage minimal est d'1 semaine.
La durée maximale d'apprentissage ne dépasse pas (2 x nouveau niveau − 1).
Les valeurs extrêmes sont moins fréquentes que la valeur moyenne.
Ainsi, passer du niveau 3 au niveau 4 peut prendre jusqu'à 7 semaines, mais prendra en moyenne 4 semaines.
Il faut en moyenne deux semaines à un [nain] pour passer du niveau 3 au niveau 4 dans la compétence Mining, car les nains ont un modificateur de +2 pour cette compétence (4-2=2).

**Examples:**

Moving up from Level 3 to Level 4 takes an average of 4 weeks, but sometimes as little as a week and sometimes up to 7 weeks.
A [dwarven unit][nain] with mining 3 in the report is actually level 1 "raw", since dwarves have a modifier of +2 on mining.
It takes an average of two weeks to advance in the mining skill from level 3 to level 4.

Pour réduire le temps nécessaire à l'apprentissage d'une compétence, une seconde unité, plus expérimentée que la première, peut [[cmd-teach|enseigner]] la compétence.
Cette unité doit avoir au moins 2 niveaux de plus que l'élève dans la compétence.
L'unité élève apprend deux fois plus vite que si elle apprenait sans professeur.
L'unité enseignante, elle, n'en tire aucune expérience.
Un apprentissage dans une [académie] permet d'apprendre en plus rapidement.

Un enseignant peut avoir jusqu'à 10 élèves.
Une unité enseignante peut contenir autant de personnes que souhaité.
Si l'"unité d'élèves" a trop de personnes, cela sera pris en compte dans les chances d'apprentissage.
Une unité peut enseigner à plusieurs unités, de même qu'une unité d'élèves peut apprendre de plusieurs unités de professeurs, chaque élève ne pouvant bien sûr tirer bénéfice que d'un seul enseignement.

**Example:**
<!-- TODO: replace Slashing weapons -->
```text
Unit l1; 1 Person, Endurance 3
TEACH s1
Unit l2; 1 Person, Slashing weapons 3, Endurance 3
TEACH s1 s2
Unit s1; 15 Persons, Endurance 1
LEARN Endurance
Unit s2; 10 Persons, Slashing weapons 1
LEARN Slashing weapons
```

Result: Unit l1 teaches 10 people from unit s1 in endurance.
Unit l2 teaches the remaining 5 people from s1 in endurance and 5 people from unit s2 in cutting weapons.
Unit s1 is taught by l1 and l2 and learns twice as fast as normal.
Unit s2 is only half taught in endurance and therefore only learns 50% faster.

!!! warning "Attention"
    Si plusieurs unités de professeurs enseignent à plusieurs unités d'élèves dans différentes compétences ou niveaux de compétence, il est possible que certains élèves n'aient pas de professeur ou ne reçoivent pas le bon professeur.
    Il n'est pas possible de faire autrement en raison de l'organisation interne d'Eressea.
    Dans ce cas, vous devez créer des « relations claires » en restructurant les unités pédagogiques.
    Avec l'ordre [[cmd-learn-auto]], le serveur tente d'automatiser l'apprentissage et l'enseignement dans une région.
    Cependant, comme cela est dû à une simple heuristique, il n’est pas garanti qu’une chaîne d’apprentissage optimale (à long terme) soit créée.

[[magic]], [alchemy], [herbalism], [espionage] et [[tactics]] sont particulièrement difficiles et coûteuses.
Apprendre l'espionnage coûte 100 Silver par personne et par tour.
200 Silver par personne et par semaine pour l'alchimie, l'herboristerie et la tactique.
Apprendre la magie coûte facilement plusieurs milliers de Silver à des niveaux élevés (voir [[magic|ce tableau]]).
L'unité qui apprend une de ces compétences doit avoir en sa possession cette somme.
Le fait que l'unité reçoive ou non un enseignement n'a aucune incidence sur le coût.
Si l'unité est dans une [academy], le coût d'apprentissage des compétences payantes est doublé.

Si l'unité en apprentissage ne dispose pas de suffisamment au moment du paiement, elle apprendra au prorata de la quantité de Silver dont elle dispose;
par exemple si elle n'a que 500 Silver sur 550, ses chances d'apprendre diminueront d'environ 10%.

Dans de rares cas, une unité peut vouloir se débarrasser d'une compétence.
Ceci est possible avec l'ordre [[cmd-forget]].

## Mixing skills

Lorsque des personnes sont transférées ou recrutées dans une unité existante, les nouveaux niveaux de compétences sont calculés en fonction du nombre de semaines d'apprentissage que les deux unités ont eu.
Il peut arriver que des semaines d'apprentissage soient "perdues" en raison des effets d'arrondi.
Tu devrais donc éviter autant que possible de fusionner inutilement des unités.

**Exemple :**

Une unité de deux personnes avec "melee" 5 recrute un paysan.
Les deux personnes ont chacune étudié environ 15 semaines (à savoir 1+2+3+4+5) avant de passer au niveau 5.
Les paysans n'ont pas de compétence, on ajoute donc 0.
La nouvelle unité a donc environ 30 semaines d'apprentissage.
Cela correspond à 3 personnes avec "melee" 4 (1+2+3+4=10 semaines par personne).
La nouvelle unité est donc de niveau 4.

Pour le calcul des semaines d'apprentissage, tout comme pour l'apprentissage, ce sont les valeurs de compétences "brutes" qui comptent, auxquelles sont d'abord soustraits tous les bonus et malus tels que les bonus raciaux.

Expérience de jeu (Solthar):

In fact, the matter is more complicated.
However, you can skip this if you are reading this guide for the first time.
Each time a unit advances a level, a dice is rolled to determine how many weeks it will take to advance to the next level.
This results in a value between 1 and (2 x new level − 1).
A unit can therefore have a talent between (6,1) -this notation means level 6 and still a week until promotion -and (6,13).
This value is taken into account when mixing.
For example, if you mix a person with (5.6) and a person with (1.2) -both of which correspond exactly to the average -they have a total of 16 weeks of learning.
However, two people with (3.4) only correspond to 12 weeks of learning.
The difference of two weeks per person will be “credited” to the new unit.
It therefore has (3.2) -a little better than average.

If you mix (5,1) and (1,1), i.e. people who have almost made it to the next climb, you would even get (4,4).
However, mixing (5,11) and (1,3) results in (3,5) as the new value. So it is not possible to accurately predict the talent value of a mixed unit.
Only a minimum and maximum value can be specified.

## Use of skills

Les compétences permettent aux unités de faire certaines choses.
Parfois, c'est le niveau de compétence de l'unité qui rend possible une activité donnée.
Parfois, le niveau de compétence total de l'unité joue également un rôle, c'est-à-dire le nombre de personnes \* le niveau de compétence.

Les compétences peuvent être divisées en plusieurs groupes.

### Skills for production

alchemy, mining, masonry, forestry, herbalism, taming, armoursmithing, shipcraft, quarrying, roadwork, weaponsmithing, cartmaking

Il s'agit du plus grand groupe de compétences.
Elles permettent de fabriquer certains objets, bâtiments, bateaux ou routes.
Elles sont expliquées plus en détail dans les chapitres [[production]] et [[alchemy|alchemy]].

### Skills for making money

Trade, taxation et entertainment sont nécessaires pour générer des Silver.
Pour en savoir plus, consultez le chapitre sur [[money|l'argent]].

### Concealment & Co

[espionage], [[camouflage|stealth]] et [[camouflage|perception]] sont centrés sur la dissimulation.
Elles ont leur propre chapitre.

### For travel

Sailing et riding sont expliquées dans le chapitre sur les [[travel|déplacements]].
riding est également abordé dans le chapitre des [[war-tables|combats]].

### Magic

[[magic]] est une compétence aux pouvoirs particulièrement puissants qui occupe tout un chapitre.

### Combat skills

Les compétences de maniement des armes telles que crossbow, bow, melee, catapult, polearm et unarmed, ainsi que les compétences spéciales endurance, riding et tactics sont particulièrement importantes dans les [[war|batailles]], que ce soit contre d'autres factions ou des monstres.

Continue reading: [[skills-list]].

<!-- From [https://wiki.eressea.de/index.php?title=Talente/fr&oldid=16177] -->

[alchemy]: ./skills-list.md#alchemy
[espionage]: ./skills-list.md#espionage
[herbalism]: ./skills-list.md#herbalism
[academy]: ./buildings-others.md#academy
[académie]: ./buildings-others.md#academy
[nain]: ./races.md#dwarves
