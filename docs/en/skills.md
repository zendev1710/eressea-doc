# Compétences

Les compétences sont un élément essentiel qui définit une [unité] dans Eressea. Toutes les personnes d'une unité ont les mêmes compétences. Elles doivent d'abord les apprendre. Pour être précis, avec l'ordre [`LEARN`], une unité peut faire une tentative par tour pour gagner un nouveau niveau.

Certaines compétences s'améliorent également en les utilisant. Si l'unité utilise la compétence, il y a 1/3 de chances qu'elle gagne de l'expérience (2/3 de chances qu'elle n'en gagne pas). Donc en exerçant une compétence une unité progresse à environ 1/3 de la vitesse d'apprentissage (de LEARN). Les compétences qui ne s'améliorent *pas* en les exerçant sont toutes les compétences d'armes, endurance, perception, tactics et taxation.

Dans la plupart des cas, la valeur de compétence affichée dans le rapport est à celle à utiliser. Elle inclut les bonus raciaux, régionaux et des éléments comme la famine ou la magie, qui modifient la valeur de la compétence. Mais parfois, la valeur de compétence "brute" sans bonus est également nécessaire, notamment pour calculer les coûts d'apprentissage de la magie et les temps d'apprentissage.

## Apprendre des compétences

Atteindre un nouveau niveau de compétence devient de plus en plus difficile à chaque niveau. En moyenne, la progression vers un nouveau niveau de compétence avec la commande [`LEARN`] prend environ un nombre de semaines égal au niveau de compétence visé, sans tenir compte des modifications apportées par la [race] ou le terrain. Le temps d'apprentissage minimal est d'1 semaine. La durée maximale d'apprentissage ne dépasse pas (2 x nouveau niveau − 1). Les valeurs extrêmes sont moins fréquentes que la valeur moyenne. Ainsi, passer du niveau 3 au niveau 4 peut prendre jusqu'à 7 semaines, mais prendra en moyenne 4 semaines. Il faut en moyenne deux semaines à un [nain] pour passer du niveau 3 au niveau 4 dans la compétence Mining, car les nains ont un modificateur de +2 pour cette compétence (4-2=2).

**Beispiele:** Das Aufsteigen von Stufe 3 nach Stufe 4 dauert im Schnitt 4 Wochen, jedoch manchmal nur eine Woche und manchmal bis zu 7 Wochen. Eine [Zwergeneinheit][nain] mit Bergbau 3 im Report hat "roh" eigentlich Stufe 1, da Zwerge auf Bergbau einen Modifikator von +2 haben. Sie benötigt für den Aufstieg im Talent Bergbau von Stufe 3 nach Stufe 4 im Schnitt zwei Wochen.

Pour réduire le temps nécessaire à l'apprentissage d'une compétence, une seconde unité, plus expérimentée que la première, peut [enseigner] la compétence. Cette unité doit avoir au moins 2 niveaux de plus que l'élève dans la compétence. L'unité élève apprend deux fois plus vite que si elle apprenait sans professeur. L'unité enseignante, elle, n'en tire aucune expérience. Un apprentissage dans une [académie] permet d'apprendre en plus rapidement.

Un enseignant peut avoir jusqu'à 10 élèves. Une unité enseignante peut contenir autant de personnes que souhaité. Si l'"unité d'élèves" a trop de personnes, cela sera pris en compte dans les chances d'apprentissage. Une unité peut enseigner à plusieurs unités, de même qu'une unité d'élèves peut apprendre de plusieurs unités de professeurs, chaque élève ne pouvant bien sûr tirer bénéfice que d'un seul enseignement.

**Beispiel:**

Einheit l1; 1 Person, Ausdauer 3

      TEACH s1
      Einheit l2; 1 Person, Hiebwaffen 3, Ausdauer 3
      TEACH s1 s2
      Einheit s1; 15 Personen, Ausdauer 1
      LEARN Ausdauer
      Einheit s2; 10 Personen, Hiebwaffen 1
      LEARN Hiebwaffen

Ergebnis: Einheit l1 lehrt 10 Personen von Einheit s1 in Ausdauer. Einheit l2 lehrt die restlichen 5 Personen von s1 in Ausdauer und 5 Personen von Einheit s2 in Hiebwaffen. Einheit s1 wird von l1 und l2 gelehrt und lernt doppelt so schnell wie normal. Einheit s2 wird nur zur Hälfte in Ausdauer gelehrt und lernt deshalb nur 50% schneller.

Attention! Si plusieurs unités de professeurs enseignent à plusieurs unités d'élèves dans différentes compétences ou niveaux de compétence, il est possible que certains élèves n'aient pas de professeur ou ne reçoivent pas le bon professeur. Il n'est pas possible de faire autrement en raison de l'organisation interne d'Eressea. Dans ce cas, vous devez créer des « relations claires » en restructurant les unités pédagogiques. Avec l'ordre [LEARN AUTO], le serveur tente d'automatiser l'apprentissage et l'enseignement dans une région. Cependant, comme cela est dû à une simple heuristique, il n’est pas garanti qu’une chaîne d’apprentissage optimale (à long terme) soit créée.

[magie], [alchimie], [herboristerie][alchimie], [espionnage][alchimie] et [tactics] sont particulièrement difficiles et coûteux à apprendre. Apprendre l'espionnage coûte 100 Silver par personne et par tour. 200 Silver par personne et par semaine pour l'alchimie, l'herboristerie et la tactique. Apprendre la magie coûte facilement plusieurs milliers de Silver à des niveaux élevés (voir ce [tableau][magie]). L'unité qui apprend une de ces compétences doit avoir en sa possession cette somme. Le fait que l'unité reçoive ou non un enseignement n'a aucune incidence sur le coût. Si l'unité est dans une [académie][1], le coût d'apprentissage des compétences payantes est doublé.

Si l'unité en apprentissage ne dispose pas de suffisamment au moment du paiement, elle apprendra au prorata de la quantité de Silver dont elle dispose; par exemple si elle n'a que 500 Silver sur 550, ses chances d'apprendre diminueront d'environ 10%.

Dans de rares cas, une unité peut vouloir se débarrasser d'une compétence. Ceci est possible avec l'ordre [`FORGET`].

## Mélanger les compétences

Lorsque des personnes sont transférées ou recrutées dans une unité existante, les nouveaux niveaux de compétences sont calculés en fonction du nombre de semaines d'apprentissage que les deux unités ont eu. Il peut arriver que des semaines d'apprentissage soient "perdues" en raison des effets d'arrondi. Tu devrais donc éviter autant que possible de fusionner inutilement des unités.

**Exemple :** Une unité de deux personnes avec "melee" 5 recrute un paysan. Les deux personnes ont chacune étudié environ 15 semaines (à savoir 1+2+3+4+5) avant de passer au niveau 5. Les paysans n'ont pas de compétence, on ajoute donc 0. La nouvelle unité a donc environ 30 semaines d'apprentissage. Cela correspond à 3 personnes avec "melee" 4 (1+2+3+4=10 semaines par personne). La nouvelle unité est donc de niveau 4.

Pour le calcul des semaines d'apprentissage, tout comme pour l'apprentissage, ce sont les valeurs de compétences "brutes" qui comptent, auxquelles sont d'abord soustraits tous les bonus et malus tels que les bonus raciaux.

Expérience de jeu : Solthar Tatsächlich ist die Sache komplizierter. Das kannst du jedoch überspringen, wenn du diese Anleitung zum ersten Mal liest. Jedes Mal, wenn eine Einheit eine Stufe aufsteigt, wird gewürfelt, wie viele Wochen sie zum Aufstieg auf die nächste Stufe brauchen wird. Dabei ergibt sich ein Wert zwischen 1 und (2 x neue Stufe − 1). Eine Einheit kann also ein Talent zwischen (6,1) - diese Schreibweise bedeutet hier Stufe 6 und noch eine Woche bis zum Aufstieg - und (6,13) haben. Dieser Wert wird beim Mischen mit eingerechnet. Mischst du zum Beispiel eine Person mit (5,6) und eine Person mit (1,2) - beides entspricht genau dem Durchschnitt - haben sie zusammen 16 Lernwochen. Zwei Personen mit (3,4) entsprechen aber nur 12 Lernwochen. Die Differenz von zwei Wochen pro Person wird der neuen Einheit "gutgeschrieben". Sie hat deshalb (3,2) - ein bisschen besser als durchschnittlich.

Beim Mischen von (5,1) und (1,1), also Personen, die schon fast den nächsten Aufstieg geschafft haben, käme sogar (4,4) heraus. Beim Mischen von (5,11) und (1,3) ergibt sich hingegen (3,5) als neuer Wert. Es ist also nicht möglich, den Talentwert einer gemischten Einheit genau vorherzusagen. Es kann lediglich ein Minimal- und Maximalwert angegeben werden.

## Utilisations des compétences

Les compétences permettent aux unités de faire certaines choses. Parfois, c'est le niveau de compétence de l'unité qui rend possible une activité donnée. Parfois, le niveau de compétence total de l'unité joue également un rôle, c'est-à-dire le nombre de personnes \* le niveau de compétence.

Les compétences peuvent être divisées en plusieurs groupes :

### Compétences pour la production

alchemy, mining, masonry, forestry, herbalism, taming, armoursmithing, shipcraft, quarrying, roadwork, weaponsmithing, cartmaking

Il s'agit du plus grand groupe de compétences. Elles permettent de fabriquer certains objets, bâtiments, bateaux ou routes. Elles sont expliquées plus en détail dans les chapitres [production] et [alchimie][2].

### Compétences pour gagner de l'argent

Trade, taxation et entertainment sont nécessaires pour générer des Silver. Pour en savoir plus, consultez le chapitre sur [l'argent].

### Dissimulation & Co

[espionage], [stealth] et [perception] sont centrés sur la dissimulation. Elles ont leur propre chapitre.

### Pour les déplacements

Sailing et riding sont expliquées dans le chapitre sur les [déplacements]. riding est également abordé dans le chapitre des [combats].

### La magie

[magic][magie] est une compétence aux pouvoirs particulièrement puissants qui occupe tout un chapitre.

### Compétences de combat

Les compétences de maniement des armes telles que crossbow, bow, melee, catapult, polearm et unarmed, ainsi que les compétences spéciales endurance, riding et tactics sont particulièrement importantes dans les [batailles], que ce soit contre d'autres factions ou des monstres.

|-------------------|-------------------------|
| Continue reading: | [liste des compétences] |

[liste des compétences]: ./skills-list.md "Liste des compétences"

<!-- From [https://wiki.eressea.de/index.php?title=Talente/fr&oldid=16177] -->

[unité]: ./cmd-unit.mden "Einheiten"
[`LEARN`]: ./cmd-learn.md "LEARN"
[race]: ./races.md "Rassen"
[nain]: ./races.md#nains "Zwerg"
[enseigner]: ./cmd-teach.md "TEACH"
[académie]: ./buildings-others.md#akademie "Akademie"
[LEARN AUTO]: ./cmd-learn.md_AUTO "LEARN AUTO"
[magie]: ./magic.md "Magie"
[alchimie]: ./skills-list.md "Liste des compétences"
[tactics]: ./tactic.md "Taktik"
[1]: ./buildings-others.md#akademie "Andere Gebäude"
[`FORGET`]: ./cmd-forget.md "FORGET"
[production]: ./production.md "Produktion"
[2]: ./alchemy.md "Alchemie"
[l'argent]: ./silver.md "Argent"
[espionage]: ./skills-list.md#espionnage "Spionage"
[stealth]: ./camouflage.md "Tarnung"
[perception]: ./camouflage.md "Wahrnehmung"
[déplacements]: ./travel.md "Reisen"
[combats]: ./war-tables.md "Kampf"
[batailles]: ./war.md "Guerre"
