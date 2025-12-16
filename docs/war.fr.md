---
alias: guerre
---
# Guerre

Les conflits sont inévitables dans Eressea. Il y aura des disputes pour l'argent, pour les régions, pour les droits de taxes, pour les routes commerciales et ainsi de suite. C'est pourquoi il faut toujours chercher des amis et des alliés, car "les amis vont et viennent, les ennemis se multiplient".

## Les camps dans une bataille

L'ordre [[cmd-attack]] permet de lancer l'attaque contre l'adversaire. Les ordres `ATTACK` sont exécutés dans un ordre aléatoire. Lors d'une attaque, les unités de tous les camps se rassemblent dans la région et se battent entre elles individuellement (personne par personne). Une bataille dure au maximum six tours : cinq tours de combat réguliers et éventuellement encore le tour 0 (zéro), le [tour de tactique].

Le camp attaquant est constitué de toutes les unités qui ont donné des ordres `ATTACK` contre une ou plusieurs unités des défenseurs.

Le camp des défenseurs est composé des unités qui ont été attaquées, sur qui l'adversaire a donc donné l'ordre `ATTACK`*`unité-id`*, et de toutes les unités de la faction agressée qui sont prêtes à combattre (donc celles en [[cmd-combat]]`,`[`COMBAT AGGRESSIVE`][`COMBAT`]`,`[`COMBAT REAR`][`COMBAT`] ou [`COMBAT DEFENSIVE`][`COMBAT`]). De plus, toutes les unités prêtes au combat des factions alliées aux factions attaquées, c'est-à-dire celles qui ont mis [`HELP COMBAT`] avec la faction attaquée, apportent leur aide.

Il y a donc différentes raisons pour lesquelles une unité participe au combat. Celles-ci sont classées par ordre de priorité :

1. L'unité prête à combattre attaque une autre unité. Dans ce cas, elle participe au combat dans tous les cas.
2. L'unité est attaquée par une autre unité. Elle rejoint alors les [Lignes de combat] en fonction de son statut de combat.
3. Une unité dont la faction est attaquée. L'unité participe alors au combat si elle n'a pas mis `COMBAT NOT` ou `COMBAT FLEE`. Dans ce dernier cas, elle n'a pas l'idée de [fuir] puisqu'elle n'est pas directement menacée.
4. Une unité d'une faction alliée (donc une faction à laquelle on a mis `HELP COMBAT`) est attaquée par quelqu'un. L'unité participe alors au combat, à moins qu'elle n'ait mis `COMBAT NOT` ou `COMBAT FLEE`. Encore une fois, une unité avec `COMBAT FLEE` ne s'enfuira pas [fuir], car elle n'est pas exposée à une menace directe.

Les alliés n'aident donc automatiquement que les défenseurs et *seulement si le défenseur n'a pas lui-même attaqué*. Les attaqués se défendent avec toutes les unités de la faction, à moins que celles-ci ne se tiennent explicitement à l'écart du combat. Pour l'attaquant, le statut de combat n'a pas d'importance : à part pour les défenseurs, seules les unités qui ont donné un ordre [[cmd-attack]] sont engagées dans le combat. Cependant, les unités qui ont mis [`COMBAT NOT`][`COMBAT`] ou [`COMBAT FLEE`][`COMBAT`] ne peuvent pas attaquer.

Ainsi, pour attaquer conjointement un ennemi, chaque faction attaquante doit attaquer au moins une unité de l'ennemi. Pour se défendre ensemble contre des assaillants, il suffit que les factions qui se défendent s'entraident (HELP).

En théorie, toute personne à laquelle [`HELP COMBAT`] a été attribuée est considérée comme alliée, et qui n'a attaqué personne à qui [`HELP COMBAT`] a été également attribuée.

**Exemple 1:** A aide B et C. C attaque B, c'est pourquoi A intervient dans la bataille : B est allié. La faction C n'est pas considérée comme alliée parce qu'elle attaque un allié.  
Qui se bat contre qui maintenant ?  
Je me bats contre mes ennemis. Mes ennemis sont des factions qui m'attaquent, que j'attaque, ou qui attaquent un allié (selon la définition que je viens de donner).

**Exemple 2:** A aide B et C. B et C s'attaquent mutuellement. Dans ce cas, A n'aide ni B ni C, car aucun d'entre eux n'est considéré comme allié et aucun n'est un ennemi de A.

**Exemple 3:** A attaque B et C. Si B et C ne sont pas alliés, ils s'entraident quand même contre A, car A est un ennemi commun. Ainsi, si B a encore des troupes de front et que C n'a plus que des archers, les troupes de B se placent devant C pour le protéger. Exception : si B et C sont ennemis, parce que par exemple B combat un allié supplémentaire D de C, alors ils ne s'aident pas entre eux, même pas contre A.

**Exemple 4:** A et B attaquent C. Dans ce cas, ils s'entraident contre C (même s'ils ne sont pas alliés), puisqu'ils ont un ennemi commun.

Expérience de jeu : en fait, c'est encore un peu plus compliqué.

**Attention :** Des statuts d'aide ou des ordres d'ATTACK mal définis ont déjà donné lieu à des combats dont l'issue n'était pas celle attendue. Des alliés sont restés sans rien faire ou se sont même battus entre eux. Quelques astuces permettent d'éviter les plus grosses bourdes :

- Tu devrais régulièrement vérifier les statuts d'aide pour tous tes alliés. HELP ALL est préférable de pour tous ceux avec qui tu "pourrais" combattre. La méfiance fait souvent des dégâts à ce niveau.
- Si possible, il ne devrait y avoir qu'un seul [[cmd-group|groupe]].
- Dans ta faction, il faudrait que soit toutes les unités de combattants aient l'ordre ATTACK, soit aucune. Si seule une partie de tes unités attaque, il se peut que le reste ne participe pas au combat si un allié est attaqué.
- Il est conseillé d'attaquer toutes les unités ennemies. Tu devrais au moins attaquer une unité de chaque faction ennemie.
- Notez également que le camouflage des factions ne permet pas toujours de savoir qui appartient vraiment à quelle faction. Une autre stratégie pourrait consister à n'attaquer qu'une seule unité ennemie à la fois, en espérant que les statuts d'HELP de l'adversaire créent une certaine confusion. Nous ne jugerons pas ici si cette approche est honorable.

## Le combat

Une bataille dure cinq tours de combat, plus un éventuel tour de tactique. A chaque tour de combat, les combattants frappent dans un ordre aléatoire.

Notez que les personnes participant à un combat ( les personnes listées dans le rapport de combat c'est-à-dire attaquées ou attaquantes) ne peuvent en principe pas exécuter d'autres ordres longs. Les exceptions sont [combat en mer] et les combats dans des régions qui, *au début du combat*, sont gardées par au moins une unité de sa propre faction ou qui a mis [`HELP GUARD`][`HELP COMBAT`] avec celle du combattant. Dans ce cas, d'autres ordres longs sont possibles.

### Lignes de combat

Durant la bataille, il y a quatre lignes de combat. Celles-ci ne sont composées que des unités qui participent réellement au combat (voir ci-dessus). Pour plus d'informations sur les statuts de combat, voir [[cmd-combat]][`COMBAT`].

1. ligne: Ici se trouvent toutes les unités qui ont mis [[cmd-combat]] ou [`COMBAT AGGRESSIVE`][`COMBAT`].
2. ligne : Ici se trouvent toutes les unités qui ont mis [`COMBAT REAR`][`COMBAT`] ou [`COMBAT DEFENSIVE`][`COMBAT`].
3. ligne : Ici se trouvent toutes les unités qui ont mis [`COMBAT NOT`][`COMBAT`].
4. ligne : C'est ici que se trouvent toutes les unités qui cherchent simplement à s'échapper. Donc celles qui ont mis [`COMBAT FLEE`][`COMBAT`] et celles qui ont perdu un nombre approprié de Points de Vie (voir aussi [la fuite]).

Seules les deux premières lignes de combat participent activement au combat, c'est-à-dire qu'elles peuvent frapper, tirer et être touchées. Les unités qui ne sont pas combattantes et qui sont directement attaquées ne participent au combat que si la première ligne est débordée. Les unités en fuite tentent naturellement de s'échapper (voir [ici][la fuite]).

Les unités qui combattent en 2eme ligne ne peuvent être attaquées directement au corps à corps que lorsqu'elles arrivent en première ligne (cela peut arriver par exemple lorsque la 1re ligne est débordée, voir ci-dessous). Contre les attaques à distance adverses, elles se défendent avec leur meilleure compétence de combat.

Les sorts de combat des mages peuvent être lancés de l'arrière et de la ligne de front ; cela mis à part, ils s'armeront et se battront comme tout le monde.

### Débordement

Si une faction et ses alliés ont plus de trois fois plus de personnes en première ligne que leurs adversaires, la 1ère rangée est débordée. Toutes les unités adverses de 2e ligne sont obligées de monter en première ligne. La 3e ligne remonte alors en 2e ligne et participe au combat. S'il n'y a toujours pas assez de personnes en 1ère ligne, les lignes suivantes remontent jusqu'à ce qu'il y ait suffisamment de personnes en 1ère ligne. Cette répartition est vérifiée avant chaque tour de combat.

## Aux armes (eresséens)

Maintenant, les unités s'arment. Chaque personne d'une unité s'équipe en fonction de ses compétences d'une arme de corps à corps, d'une arme à distance et d'une armure. Elle privilégie les armes qui lui permettent d'obtenir le plus haut score en Attaque et Parade. Les mages qui ont choisi un sort de combat l'utilisent pour attaquer. Cependant, pour la défense, ils auront besoin d'une arme (et d'une compétence de combat appropriée), sinon ils seront considérés comme [non armés].

**Attention:** les armes ou armures non utilisées ne sont pas automatiquement redistribuées aux unités non armées ou non équipées.

Pendant le combat, on ne change plus d'arme, sauf s'il est possible de prendre une meilleure arme à une personne de la même unité qui est déjà morte (les combattants survivants utilisent chacun les meilleurs sets d'armes disponibles).

Un combattant à distance qui soudain se retrouve en première ligne doit s'il est attaqué se saisir d'une arme de corps à corps (s'il en possède une et s'il a la compétence correspondante au moins au niveau 1), sinon il se défend [sans arme][non armés].

**Exemple :** Une unité de 20 personnes dispose de 15 épées, 10 boucliers et 5 cottes de mailles. Alors 5 personnes se battront avec une épée, un bouclier et une cotte de mailles, 5 autres avec une épée et un bouclier, 5 avec une épée seulement et les 5 derniers combattants resteront sans armes. Une unité de 10 personnes avec 10 épées et 10 haches de guerre se battra avec des épées, car elles ont un meilleur bonus, même si elles infligent probablement moins de dégâts !

## Tour du tacticien

Avant la bataille, le meilleur [Tacticien] de toutes les unités participantes est désigné. Un tacticien qui se bat en première ligne reçoit un bonus de +1 à sa compétence "tactics". S'il se trouve en 3e ou 4e ligne, son niveau est réduit de 1. Afin de laisser une part de "forme du jour" et de chance, chaque tacticien reçoit également un bonus aléatoire qui commence à 0 et qui, en théorie pure, peut devenir très important, la probabilité étant de plus en plus faible à mesure que le bonus augmente.

Le camp avec la meilleure valeur de tactique peut attaquer au tour 0 (appelé "tour du tacticien") sans que l'ennemi ne puisse attaquer. Le nombre de coups portés dépend de la différence entre la meilleure valeur de tactique du camp gagnant et celle du camp perdant : Pour chaque point de différence, chaque personne a 10 % de chances d'attaquer lors du tour du tacticien.

**Exemple:** Le camp A a une personne avec tactics 4 en première ligne. Le camp B a 10 personnes avec tactics 4 en troisième ligne. Donc, le camp A a effectivement 5 et le camp B 3. Sans le bonus aléatoire, chaque personne du camp A aurait 20% de chances d'attaquer lors du tour du tacticien. Si la personne du camp A obtient un 0 en bonus, il faut qu'au moins une personne du camp B obtienne un 2. Sinon, le camp A a le tour du tacticien. Supposons que le meilleur résultat obtenu au jet par le camp B soit un 5 (c'est peu probable, mais tout à fait possible). La différence pour le camp B est donc de (3 + 5) - (5 + 0) = 3. Chaque personne du camp B a alors 30% de chances de frapper au tour 0. Pour un groupe de 10, cela peut aller de 0 à 10 personnes, mais la moyenne est d'environ 3 attaques.

## Héros

Les héros sont des combattants particulièrement puissants. Ils doivent avoir été préalablement désignés avec l'ordre [[cmd-promote]]. Les héros peuvent attaquer 5 fois à chaque tour de combat.

Attention ! Cela ne s'applique pas aux attaques magiques ni aux arbalètes et catapultes.

Pour plus d'informations, voir [[cmd-promote]].

## Le combat entre deux personnes

Dans chaque bataille, les armées s'affrontent personne par personne, quel que soit leur nombre. La procédure est la suivante :

- L'attaque de l'attaquant et la parade du défenseur sont (au départ) aussi élevées que leur niveau de compétence en armes.
- Ajouter des bonus/malus : A l'attaque de l'attaquant et à la parade du défenseur, on ajoute les éventuels [bonus et malus][non armés].
- Si l'attaquant est un combattant à distance, la valeur de parade de son adversaire ainsi modifiée est divisée par deux.
- Les probabilités de base de toucher (BT) d'un attaquant sont de 30%.
- Soustraire les valeurs les unes des autres : Pour chaque point de différence entre l'attaque de l'attaquant et la parade du défenseur, le BT est maintenant augmenté ou diminué de 5%. La probabilité réelle de toucher se calcule donc comme suit : (Attaque(attaquant)-Parade(défenseur)) \* 5% + 30%.
- Chance du débutant : si l'attaque échoue, l'attaquant a en plus 10% de chances de transformer son attaque : Il peut frapper une deuxième fois, avec une chance de toucher augmentée de 90 à 99% (hasard). Les combattants fortement désavantagés ont ainsi la possibilité d'obtenir au moins quelques coups aléatoires.

Chaque personne attaque une fois par tour de combat (sauf les [Héros] et certains monstres).

Lorsqu'un combattant réussit à toucher son adversaire, il lui inflige des dégâts. Les différentes armes infligent des dégâts différents (points de dégâts, voir [Caractéristiques des armes]). Par ailleurs, il vaut la peine d'avoir des niveaux de compétences élevés en maîtrise des armes : si l'on a plus de niveaux de compétence que l'adversaire, les dégâts infligés lors d'un coup augmentent d'un point par différence de deux niveaux de compétence. Seuls les niveaux de compétences sont pris en compte, les bonus apportés par les chevaux, les châteaux, etc. ne comptent pas. Cela vaut aussi bien pour le combat à distance que pour le combat rapproché. En outre, il y a une certaine chance, dépendant de la différence de niveau, de recevoir un coup critique qui peut causer jusqu'à cinq fois plus de dégâts.

Si une personne a subi plus de points de dégâts qu'elle ne peut "en encaisser", elle meurt (voir [Modificateurs de compétences] les différents coups portés pendant le combat s'additionnent).

Lorsqu'un combattant porte une armure, celle-ci peut absorber une partie (voire la totalité) des points de dégâts. Cependant, l'armure rend le combattant moins mobile et augmente ses chances d'être touché (voir [ce] tableau). Contre les arbalètes, une armure n'est qu'à moitié efficace (arrondi à l'inférieur).

Certaines créatures ou armes peuvent également infliger des dégâts magiques. Une armure normale est inefficace contre les dégâts magiques. Seule compte la [Résistance à la magie], qui peut être augmentée par certains équipements et sorts.

Il y a également la compétence Endurance, qui permet d'endurcir son corps et de supporter plus de points de dégats avant de mourir (voir [ce tableau]).

### Combat à distance

Les armes à distance et les catapultes peuvent être utilisées efficacement en deuxième ligne. Là, elles seront protégées des combattants au corps à corps de l'adversaire par votre première ligne.

Les combattants à distance peuvent également tirer dans la deuxième ligne adverse. Ils choisissent une cible au hasard parmi tous les ennemis en première ou deuxième ligne.

Les arbalètes peuvent également transpercer les armures : Contre un tir d'arbalète, l'armure ne fait effet que pour moitié (arrondi inférieur).

Le tableau ci-dessous montre les différences entre les armes à distance. Il est très difficile d'utiliser un arc (Offensive Bonus -2), mais on peut tirer tous les rounds de combat. Les arbalètes sont beaucoup plus faciles à utiliser (OB 0), mais ne peuvent tirer qu'un round de combat sur trois. Les catapultes tirent toujours au premier tour (cela peut être le tour tactique ou le tour 1) et causent de lourds dégâts.

Contre les armes à distance, les personnes attaquées ne se défendent qu'avec la moitié de leur niveau de compétence. Cependant les unités en première ligne se défendent avec leur niveau de compétence si le combattant à distance se trouve également en première ligne.

*Attention !'* Si un combattant à distance se retrouve au premier rang (par exemple, parce qu'il a été [débordé]), il doit se défendre avec une arme de mêlée. S'il n'en possède pas ou ne peut pas l'utiliser (c'est-à-dire si la compétence correspondante est inférieure à 1), il se défend [à mains nues] !

Les catapultes nécessitent des munitions. Celles-ci peuvent être fabriquées à partir de pierres (Stone) avec l'ordre [MAKE ammunition] par maçon avec la compétence quarrying niveau 3. Elles pèsent 10 kg. Une unité de munitions correspond à une salve (6 cibles).

Ranged weapons - bonuses and time

| Weapon                        | Skill    | Offensive bonus | Reloading |
|-------------------------------|----------|-----------------|-----------|
| crossbow / mallorn crossbow   | crossbow | 0               | 2         |
| catapult                      | catapult | \-4             | 5         |
| bow / mallorn bow / elven bow | bow      | \-2             | 0         |

La colonne « Reloading » indique le temps nécessaire pour que l'arme soit à nouveau prête à tirer. Une catapulte ne peut donc être utilisée qu'une fois par combat. Une arbalète peut tirer tous les trois rounds, et un arc peut tirer à chaque round.

### Boni et Mali

Various factors can modify the chance of hitting someone (attack) or deflecting a hit (parry). All bonuses and penalties have a direct effect on the skill and are taken into account before any skill halving by ranged fighters. The damage points that a person deals are not changed by the bonuses and penalties; the unmodified skill values count here. See also [tables de combat].

Combat à mains nues (unarmed combat)  
Les personnes ne possédant pas de compétence correspondant à leur arme sont également considérées comme désarmées.

Les personnes désarmées combattent avec un score de -2.

Les combattants à distance qui entrent en combat au corps à corps et ne peuvent accéder à une arme de corps à corps (et au skill correspondant) se défendent avec un score de -2. Ils peuvent toujours attaquer avec leur arme à distance.

Les gobelins se défendent avec +/-0.

La compétence avec laquelle les orcs engagent le combat au corps à corps est déterminée par le niveau de leur meilleur skill de corps à corps -3.

Certaines races (généralement les familiers) peuvent apprendre le combat au corps à corps et ne subissent alors aucune pénalité lorsqu'ils combattent au corps à corps.

Bonus du château
Les personnes se trouvant dans un château bénéficient d'une protection supplémentaire. Les occupants du château bénéficient d'un bonus de parade, selon la taille du château, s'ils appartiennent au camp défenseur et que le château est suffisamment grand pour les accueillir. Une fortification donne +1, une tour +2, et ainsi de suite, jusqu'à la citadelle, qui donne +5. Si les occupants du château s'attaquent eux-mêmes, ils ne bénéficient d'aucun bonus de parade. Le bonus du château s'applique également aux combattants à distance !

Bonus Cavalerie
Dans les plaines, les déserts et les Highlands, les combattants en première ligne en terrain découvert peuvent utiliser un cheval. Pour monter un cheval au combat, il faut un score de Riding d'au moins 2 et un cheval. Les cavaliers bénéficient d'un bonus de +2 à l'attaque et à la parade, car ils sont plus rapides et plus agiles. Les cavaliers à l'intérieur d'un château, et bénéficiant du bonus du château, n'ont pas le bonus cavalerie si ils sont attaqués. Les trolls ne peuvent pas utiliser de chevaux au combat.

Bonus de lance  
Les porteurs de lances et de spears montés reçoivent un bonus additionnel de +1 en attaque.

Bonus de piquiers  
Les porteurs de spears et de hallebardes qui n'utilisent pas de cheval reçoivent un bonus de +1 à la parade contre les troupes montées.

Modificateurs d'armes  
Les [Modificateurs d'armes][Caractéristiques des armes] sont également considérés comme des bonus et des malus.

Une unité de hallebardiers a donc (en plus de tout autre bonus ou malus éventuel) un bonus de +2 à sa parade. Si elle n'est pas montée et qu'elle se bat contre un cavalier, sa valeur de parade est alors augmentée de +1.

**Exemples:**

- Basiswert des Angreifers: BT = 30%  

Angreifer mit Talent 3, Verteidiger Talent 4 -&gt; Trefferchance=25%  
Verteidiger steht in Zitadelle -&gt; Parade +5 -&gt; Trefferchance=0%  
Der Angreifer hat also nur eine Chance von 10% ("Anfängerglück"), überhaupt noch einen zweiten Versuch zu bekommen, und dann nochmal eine 90 bis 99%ige den Treffer zu landen. Insgesamt hat er also lediglich 9 bis 9,9% Chance, den Verteidiger zu treffen. Er ist ja auch (durch die Zitadelle) wirklich stark im Nachteil.

- Diesmal steht der Verteidiger nicht in der Zitadelle:  

Basiswert des Angreifers -&gt; BT = 30%  
Angreifer mit Talent 3, Verteidiger Talent 4 -&gt; Trefferchance = 25%  
Angreifer mit Pferdebonus -&gt; Attacke +2 -&gt; Trefferchance = 35%

- Eine Schwertkämpferin mit Hiebwaffen 3 gegen einen Reiter mit Reiten 1 und Stangenwaffen 2: Sie kämpft mit Attacke 3 (Talent 3) gegen Parade 2 (Talent 2, ohne Pferdebonus - der Reiter kann nicht gut genug reiten).  

Die Angreiferin hat also eine Trefferchance von 35%.

- Ein Bogenschütze mit Talent 9 greift aus der 2. Reihe eine Lanzenreiterin mit Reiten 3 und Stangenwaffen 9 an. Er attackiert mit 7 (Malus von 2 durch den Bogen) gegen eine Parade von 5 (der Paradewert wird halbiert und abgerundet: Talent 9, +2 Pferdebonus -&gt; (9+2)/2=5).  

Der Angreifer hat also eine Trefferchance von (7 - 5) \* 5% + 30% = 40%

- Eine Lanzenreiterin mit Reiten 3 und Stangenwaffen 9 greift einen Bogenschützen mit Talent 9 in der 1. Reihe an.
  - Sie attackiert mit 12 (Talent 9, +2 Pferdebonus und +1 Lanzenbonus) gegen eine Parade von -2 (Schütze ohne Waffe für den Nahkampf).  

Die Angreiferin hat eine Trefferchance von 100%; sie wird also in jedem Fall treffen...

- - Sie pariert mit ihrem vollen Paradewert (also Waffentalent + Pferdebonus = 11) gegen die Fernkampfwaffe, da der Schütze in der 1. Reihe steht, und der Schütze muss auf seinen Talentwert den Malus 2 (durch den Bogen) hinnehmen.  

Der Schütze greift also effektiv mit einer Attacke von 7 gegen die Reiterin mit einer Parade von 11 an. Er hat also eine Trefferchance von (7 - 11) \* 5% + 30% = 10%.

- Eine Speerträgerin mit Stangenwaffen 3 in einer Burg greift eine Reiterin mit Reiten 2 und Stangenwaffen 3 an.
  - Sie attackiert mit 3 (Talent 3, kein Pikenbonus bei der Attacke; kein Burgenbonus, da sie den Angriff begonnen hat) gegen 5 (Talent 3, +2 Pferdebonus, kein Lanzenbonus bei der Parade).  

Die Angreiferin hat eine Trefferchance von (3-5)\*5%+30%=20%.

- - Sie pariert mit 4 (Talent 3, kein Burgenbonus, da sie selbst angegriffen hat; +1 Pikenbonus) gegen 6 (+2 Pferdebonus und +1 Lanzenbonus).  

Die Angegriffene hat eine Trefferchance von (6 - 4) \* 5% + 30% = 40%.

- Ein Reiter mit Reiten 2 und Hiebwaffen 2 gegen einen Speerträger mit Stangenwaffen 3:
  - Er attackiert mit 4 (Talent 2, +2 Pferdebonus) gegen 4 (Talent 3 und +1 Pikenbonus).  

Der Angreifer hat also eine Trefferchance von 30%.

- - Der Speerträger schlägt zurück mit 3 gegen 4 (der Pikenbonus gilt nur bei der Parade, nicht bei der Attacke).  

Der Speerträger hat also eine Trefferchance von 25%.

- Ein Lanzenreiter mit Reiten 2 und Stangenwaffen 3 greift eine gleich gute Kollegin an. Er kämpft mit 6 (Talent 3, +2 Pferdebonus, +1 Lanzenbonus) gegen 5 (Talent 3, +2 Pferdebonus)  

Der Angreifer hat damit eine Trefferchance von 35%.

Hieraus folgt, dass man eine Burg relativ gut halten kann, dass man aber aus einer Burg heraus möglichst keine Angriffe starten sollte, denn damit verliert man seinen Bonus bei der Verteidigung. Hieraus folgt auch, dass Speerträger ein wenig wirksamer gegen berittene Truppen sind als Schwertträger.

## La fuite

Personen, die [COMBAT FLEE][`COMBAT`] gesetzt haben und [attackiert][`ATTACK`] werden, versuchen zu fliehen. Dies tun sie vor jeder Kampfrunde, es kann also sein, dass sie erst (weitere) Treffer hinnehmen müssen, bevor die Flucht gelingt.

Personen mit [[cmd-combat]][`COMBAT`] oder [`COMBAT REAR`][`COMBAT`], die nur noch 20% ihrer Trefferpunkte haben und Personen mit [`COMBAT DEFENSIVE`][`COMBAT`] oder [`COMBAT NOT`][`COMBAT`], die nur nur noch 90% ihrer Trefferpunkte haben, versuchen ebenfalls zu fliehen, aber erst, wenn sie im Kampf einen Treffer abbekommen haben. Dabei zählen auch Treffer, deren Schadenspunkte vollständig von der Rüstung aufgehalten wurden und fehlgeschlagene Trefferversuche. Das soll verhindern, dass Einheiten, die schon vor dem Kampf angeschlagen waren, fliehen, obwohl sie nicht tatsächlich in Gefahr waren.

Die Grundchance für die Flucht beträgt 25% (50% für Halblinge), dazu kommen 10%, wenn man ein Pferd hat und je 5% pro Stufe im Talent Tarnung; der Maximalwert ist aber 75% (bzw. 90% für Halblinge).

Fliehende Einheiten entziehen sich dem Kampf, verbleiben aber in sicherer Entfernung zum Kampfgeschehen in der Region. Befand sich die Einheit in einem Gebäude oder auf einem Schiff an Land, verlässt sie dieses, sobald eine Person aus der Einheit während des Kampfes geflohen ist.

**Hinweis:** Es kann deshalb sinnvoll sein, Burgen- oder Schiffsinsassen zu befehlen, ihr eigenes Schiff wieder zu betreten, was sie nach dem Kampf evtl. tun können. Zu beachten ist, dass auch das Kommando wieder an die richtige Einheit übergeben werden sollte.

Besonderheiten gelten für Einheiten mit dem Status FLEE. Diese Einheiten können sich nach dem Kampf noch bewegen, auch wenn sie sonst keinen langen Befehl ausführen dürften. Weiterhin können diese Einheiten keine Regionen bewachen. Eine durchgeführte Bewachung wird automatisch aufgelöst, wenn die Einheit den Status FLEE einnimmt. Dies geschieht zu Beginn der Runde, womit alle Effekte von [[cmd-guard]] sofort aufgelöst werden.

## Combats à bord et depuis les navires

Seeschlachten werden wie Schlachten zu Land ausgefochten: Die [Schiffe] entern sich gegenseitig und die Einheiten fallen übereinander her. Nach der Schlacht ist es den Einheiten möglich, weitere lange Befehle auszuführen.

Ist ein Schiff in eine Schlacht verwickelt, so bekommt es pro Kampfrunde 5% Schaden, wenn mindestens eine Person Schaden erleidet, die auf dem Schiff ist oder zu Beginn der Runde auf dem Schiff war. Es hilft also nicht, das Schiff vor Kampfbeginn zu verlassen. Die [Taktikrunde][Tacticien] und die erste Runde wird nicht mitgezählt, so dass es immer nur maximal 20% Schaden geben kann.

Zu größeren Schäden kann es kommen, wenn Seeschlangen in den Kampf verwickelt sind. Diese Monster haben, wie auch einige Vertraute, einen Angriff der jede Kampfrunde Strukturschaden an Schiffen verursachen kann.

Ist das Schiff nach der Schlacht unterbesetzt oder leer, treibt es ohne Kontrolle im Ozean und nimmt weiteren [Schaden].

Will man mit einem Schiff Truppen in einer feindlich [bewachten][`GUARD`] Region anlanden, so müssen diese erst das Schiff [[cmd-leave]] und können erst in der folgenden Runde den Angriff starten oder sich bewegen. Dadurch hat der Gegner die Möglichkeit, entsprechend zu reagieren.

Von Land aus kann man Schiffe an der Küste sofort angreifen. Auch reihen sich Truppen auf Schiffen normal gemäß Kampf- und [[cmd-help]][`HELP COMBAT`]-Status in die Kampfreihen ein, falls sie oder Verbündete angegriffen werden.

## Piraterie

Mit **Piraterie** hat ein Schiffskapitän die Möglichkeit, Schiffe anderer Parteien in Nachbarregionen aufzubringen.

Der Kapitän legt sich auf die Lauer nach Schiffen, die nach ihrer Bewegung in einer Nachbarregion liegen. Dort angekommen, kann die Mannschaft in der kommenden Runde ganz normal agieren. Mit Hilfe von [`FOLLOW SHIP`] könnte man zum Beispiel seine Opfer auch erstmal verfolgen. Bei der ganzen Geschichte sind einige Sachen zu beachten:

- Als Ziele werden nur Parteien erkannt, mit denen man nicht mit `HELP COMBAT` alliiert ist.
- Werden Parteinummern angegeben ([`PIRACY <parteinummer> ...`], so werden nur Kapitäne der angegebenen Parteien als Ziele erkannt.
- Der Mechanismus funktioniert auch, wenn das Piratenschiff an Land ist. Er bietet also eine effektive Möglichkeit zum Küstenschutz.
- Piraten segeln auch in Landregionen, sofern das Schiff dort landen kann. Falls es nicht landen kann, nimmt es Schaden.
- Piratenkapitäne sind dumm wie Brot. Sie können nicht einschätzen, ob ein Ziel ihnen möglicherweise überlegen ist, und werden fröhlich auch mit einem einzigen Schiff in einer feindliche Flotte von 100 Schiffen hineinfahren. Das Piratendasein hat eben seine Risiken.
- Stehen mehrere potentielle Ziele zur Auswahl, wird der Kapitän eines nach dem Zufallsprinzip aussuchen.
- Piratenflotten bleiben zusammen. Genauer gesagt: Hat bereits ein alliiertes Schiff (zu dem der Kapitän [`HELP COMBAT`][`HELP COMBAT`] gesetzt hat) aus der eigenen Region ein Opfer erkannt, so segelt unser Schiff auch in die betreffende Region, vorausgesetzt, das vom ersten Schiff erkannte Opfer ist ebenfalls ein potentielles Opfer für uns.

<!-- GERMAN SECTION TRANSLATED -->
## Fin du combat

Après la bataille, on compte les morts, et tout le matériel utilisable des unités anéanties est récupéré et distribué aux survivants.

Les unités blessées au combat restent blessées. Ceci est indiqué dans le rapport. Avec le temps, elles guérissent. Elles régénèrent généralement 5 % (certaines [races] davantage) de leurs points de vie maximum par tour, mais au moins un point par individu. Les unités mortes-vivantes ne se régénèrent pas.

Si la région où les combats ont eu lieu était [[alliances|gardée]] *au début du combat* par une unité amie ou une unité ayant activé l'ordre [`HELP GUARD`][`HELP COMBAT`] pour les forces amies, toutes les unités participant au combat (celles figurant dans le rapport de bataille) peuvent exécuter des ordres longs. Ceci est valable même si des troupes ennemies gardent également la région. Cela fonctionne aussi si tu as attaqué toi-même (c'est-à-dire si tu as donné toi-même l'ordre `ATTACK`).

Si aucune unité amie ou alliée ne gardait la région au début du combat, les unités participantes ne pourront plus exécuter d'ordres longs après le combat.

Die einzigen Ausnahmen bilden Einheiten mit dem Kampfstatus [`COMBAT FLEE`][`COMBAT`] und Einheiten auf See. Einheiten mit dem Status `COMBAT FLEE` können sich nach dem Kampf noch bewegen, wenn sie einen der folgenden Befehle gesetzt haben: [[cmd-move]]`,`[`ROUTE`]` oder `[`FOLLOW`][`FOLLOW SHIP`]. Nach Kämpfen auf See kann man stets noch lange Befehle ausführen.

## Voir aussi

- [Taktik]
- [Kriegstabellen]

Poursuivre la lecture : [[alliances]].

<!-- From [https://wiki.eressea.de/index.php?title=Krieg/fr&oldid=16966] -->

[`ATTACK`]: ./cmd-attack.md "ATTACK"
[tour de tactique]: #tour-du-tacticien
[`COMBAT`]: ./cmd-combat.md "COMBAT"
[`HELP COMBAT`]: ./cmd-help.md "HELP"
[Lignes de combat]: #lignes-de-combat "Lignes de combat"
[fuir]: #la-fuite
[combat en mer]: ./war.md#combats-a-bord-et-depuis-les-navires "Kampf auf Schiffen"
[la fuite]: ./war.md#la-fuite "Die Flucht"
[non armés]: #boni-et-mali
[Tacticien]: ./tactic.md "Taktik"
[Héros]: ./#heros "Héros"
[Caractéristiques des armes]: ./war-tables.md#waffeneigenschaften "Guerrestabellen"
[Modificateurs de compétences]: ./war-tables.md#caractéristiques-raciales "Guerrestabellen"
[ce]: ./war-tables.md#rüstung "Guerrestabellen"
[Résistance à la magie]: ./war-tables.md#magieresistenz "Guerrestabellen"
[ce tableau]: ./war-tables.md#ausdauer "Guerrestabellen"
[débordé]: #lignes-de-combat "Lignes de combat"
[à mains nues]: #boni-et-mali
[MAKE ammunition]: ./cmd-make.md "MAKE"
[tables de combat]: ./war-tables.md#kampfmodifikatoren "Guerrestabellen"
[`GUARD`]: ./cmd-guard.md "GUARD"
[Schiffe]: ./ships.md "Schiffe"
[Schaden]: ./ships.md#schiffsschaden "Schiff"
[`FOLLOW SHIP`]: ./cmd-follow.md "FOLLOW"
[`PIRACY <parteinummer> ...`]: ./cmd-piracy.md "PIRACY"
[races]: ./skills-modifiers.md "Talentmodifikatoren"
[`ROUTE`]: ./cmd-route.md "ROUTE"
[Taktik]: ./tactic.md "Taktik"
[Kriegstabellen]: ./war-tables.md "Guerrestabellen"
