---
# cSpell:locale fr
alias: magie
---
# Magie

La magie est un moyen mystique et puissant de changer et de créer des choses et peut affaiblir l'ennemi ou renforcer les alliés dans la [[guerre]].

## L'étude de la magie

Chaque faction doit choisir l'une des cinq [[ecoles-de-magie]] parmi [[sorts-illaun|Illaun]], [[sorts-tybied|Tybied]], [[sorts-gwyrrd|Gwyrrd]], [[sorts-cerddor|Cerddor]] ou [[sorts-draig|Draig]].  

L'École de Magie de la faction est déterminée par la toute première unité qui apprend la magie dans la faction.
Cela se fait à l'aide de l'ordre [[cmd-learn|`LEARN MAGIC "<école de magie>"`]].  
En conséquence, l'ordre est maintenant simplement appelé `LEARN MAGIC <école de magie>"` et tous les mages d'une [[factions|faction]] apprennent alors automatiquement l'École de Magie choisie par la faction.  
Il est cependant possible de passer l'ordre `LEARN MAGIC "<école de magie>"` pour plusieurs unités si vous ne savez pas quelle unité viendra en premier.  

!!! note
    Une fois qu’une École de Magie a été choisie, **elle ne peut plus être modifiée**.
    Cette décision doit donc être mûrement réfléchie !

Il peut y avoir un **maximum de 5 unités de mages par faction**;
Seules les factions **elfes** sont autorisées à avoir **6 mages**.  
Les unités de mages ne peuvent être composées que d’une seule personne.
Vous ne pouvez pas remettre des personnes, même à des unités `TEMP` vides.  

L'apprentissage de la magie coûte `50 + 25 * (1 + Niveau) * Niveau` Silver par personne et par tour.  

Coûts d'apprentissage.

| Niveau suivant | 1   | 2   | 3   | 4   | 5   | 6    | 7    | 8    | 9    | 10   | 11   | 12   | 13   | 14   | 15   | ... | 20    | ... | 30    | ... | 40    |
|----------------|-----|-----|-----|-----|-----|------|------|------|------|------|------|------|------|------|------|-----|-------|-----|-------|-----|-------|
| Coût           | 100 | 200 | 350 | 550 | 800 | 1100 | 1450 | 1850 | 2300 | 2800 | 3350 | 3950 | 4600 | 5300 | 6050 | ... | 10550 | ... | 23300 | ... | 41050 |

Ainsi, un mage non formé paie 100 Silver pour ses premiers apprentissages;
S’il est déjà au niveau 5 en magie, il doit payer 1 100 Silver par semaine d’apprentissage.  

!!! warning "Attention"
    Le coût d'apprentissage fait toujours référence au niveau appris avant que les bonus ou pénalités raciales ne soient appliqués.
    Ainsi un elfe paie 100 et non 200 Silver pour sa première tentative d'apprentissage qui l'amène à T2.
    Un gobelin avec son -1 paie 200 Silver pour la deuxième tentative d'apprentissage même s'il est encore au niveau 0 (le système l'évalue comme T1 -1 = 0).

!!! info "message à destination des mains"
    Vous avez -2 en compétence magique.
    Une unité qui apparaît avec Magie à 0 peut en réalité être en T1 ou T2.
    Dans ce dernier cas, cependant, les coûts d’apprentissage s’élèvent à 350 Silver!
    Il n’y a aucun moyen de savoir lequel des deux est vrai. Il vaut donc mieux planifier un peu plus généreusement.

Apprendre dans une **[académie]** coûte **deux fois plus cher**.

Seuls les mages de la même école de magie que le professeur peuvent être formés.
Un mage Draig ne peut donc pas enseigner à un mage Illaun.  

Si une unité de mage n'a pas assez d'argent pour apprendre, elle n'apprendra que proportionnellement à la quantité d'argent qu'elle peut payer chaque semaine.
<!-- TODO: clarify this not understable sentences -->
La magie peut également, via [Special:MyLanguage/Talente|Application (CAST)].
Peu importe que l'unité lance un ou plusieurs sorts par tour.
Bien entendu, l’apprentissage par l’application ne coûte pas d’argent.

## Dictons

À chaque niveau que l'unité gagne en magie, elle peut acquérir de nouveaux sorts.  
Il y a actuellement un sort dans chaque niveau, dans des cas exceptionnels plusieurs voire aucun.  
Une fois que vous avez atteint un nouveau niveau, les paroles sont décrites dans l'évaluation.  
Si vous avez oublié la description, vous pouvez la faire afficher à nouveau à l'aide de l'ordre [[cmd-show]].

```text
                                     Wunderdoktor

    Beschreibung:
      Wenn einem der Alchemist nicht weiterhelfen kann, geht man zu dem gelehrten
      Tybiedmagier. Seine Tränke und Tinkturen helfen gegen alles, was man sonst
      nicht bekommen kann. Ob nun die kryptische Formel unter dem Holzschuh des
      untreuen Ehemannes wirklich geholfen hat - nun, der des Lesens nicht
      mächtige Bauer wird es nie wissen. Dem Magier hilft es auf jeden Fall...
      beim Füllen seines Geldbeutels. 50 Silber pro Stufe lassen sich so in einer
      Woche verdienen.
    Art: Normaler Zauber
    Stufe: 1
    Rang: 5
    Komponenten:
    -   1 Aura  * Stufe
    Modifikationen: Schiffszauber
    Syntax:
      CAST [LEVEL n] Wunderdoktor

```

ou alors

```text

                        Erschaffe einen Ring der Unsichtbarkeit

    Beschreibung:
      Mit diesem Spruch kann der Zauberer einen Ring der Unsichtbarkeit
      erschaffen. Der Träger des Ringes wird für alle Einheiten anderer Parteien
      unsichtbar, egal wie gut ihre Wahrnehmung auch sein mag. In einer
      unsichtbaren Einheit muss jede Person einen Ring tragen.
    Art: Normaler Zauber
    Stufe: 6
    Rang: 5
    Komponenten:
    - 50 Aura
    - 3000 Silber
    - 1 permanente Aura
    Modifikationen: Schiffszauber
    Syntax:
      CAST 'Erschaffe einen Ring der Unsichtbarkeit'
```

### Types de sort

Il existe des sorts normaux, des sorts de pré-combat, des sorts de combat et des sorts d'après-combat.

Les sorts normaux sont lancés à l'aide de la commande [[cmd-cast]].  
Leur effet se produit soit immédiatement (voir [[sequence-des-ordres]]) soit parfois plus tard, par exemple au début du tour suivant.  

Les trois types de sorts de combat ne peuvent jamais être lancés en utilisant `CAST`.  
Au lieu de cela, ils sont lancés lorsque l’unité est activement engagée dans un combat.  
Les trois types peuvent être définis avec l'ordre [[cmd-combatspell|`COMBATSPELL LEVEL n "<sort>"`]].  
Vous pouvez supprimer un sort de combat spécifique avec l'ordre `COMBATSPELL "<sort>" NOT`, ou supprimer tous les sorts de combat définis, avec [[cmd-combatspell|`COMBATSPELL NOT`]].  
Les sorts de combat fonctionnent un peu comme les ordres [`COMBAT`], c'est-à-dire qu'une fois définis, ils restent enregistrés.  
Une unité peut avoir au maximum un sort de pré-combat, un sort de combat et un sort de post-combat.  
Par exemple, si l'unité possède déjà un sort de pré-combat et qu'elle lance un nouveau sort de pré-combat, l'ancien est remplacé par le nouveau.

```text
                        Song of Fear

Description:
    A very powerful song from the traditions of cats that runs deep within
    penetrates the hearts of enemies and robs them of courage and hope. Fear will
    making her tremble and panic take over her thoughts. Become full of fear
    They try to escape the horrible songs and flee.
Art: Combat spells
Level: 3
Rank: 5
Components:
    -   1 Aura  * Level
Modifiers:
Syntax:
    COMBATSPELL [LEVEL n] 'Song of Fear'
```
<!-- TODO check if below is what german text meant -->
Si un mage active des sorts de combat, ceux-ci sont automatiquement lancés dès qu'il participe au combat : soit en donnant l'ordre `ATTACK` lui-même, soit en étant entraîné dans la bataille par une attaque ciblant son camp (voir [Les camps dans une bataille]).  
Cela peut également se produire même s'il est au statut de combat `COMBAT NOT` ou `FLEE`, dès lors qu'il est explicitement attaqué avec l'ordre [[cmd-attack]] !

Un sort de pré-combat ou de post-combat est lancé une fois avant ou après le début du combat.  
Un sort de combat normal une fois par round de combat, à condition que l'unité ait encore suffisamment d'aura (voir [aura]) et qu'elle soit encore en vie.

### Aura

L'aura est le pouvoir magique que les mages utilisent pour accomplir leur magie.  
L'aura est consommée en lançant des sorts et se régénère au fil du temps.  
Un mage peut absorber une quantité maximale d’aura, déterminée par son niveau de compétence en magie.  

Les déttails pour chaque unité de mage sont présents dans le rapport, mais, en règle générale, le maximum d'aura absorbée est d'au maximum *niveau magie* puissance 2, et en moyenne environ *niveau de magie* de l'aura est régénérée par semaine.  
Mais cela peut varier entre presque rien et le niveau en magie.  
Les races magiques régénèrent l'aura plus rapidement, les races non magiques beaucoup plus lentement.  

L'aura maximale n'est pas immuable.

D'une part, il existe un sort qui permet à une unité de transférer de l'aura à une autre.  
Cela permet à l'unité cible de recevoir temporairement plus d'aura qu'elle ne peut normalement en absorber.  
Cela lui permet de lancer des sorts qui coûtent plus que son aura maximale.  
Cependant, l’aura excédentaire est à nouveau perdue à la fin d’un tour.  

D'autre part, il existe des sorts (et éventuellement d'autres choses) qui coûtent une aura permanente aux mages, comme "Créer un anneau d'invisibilité".  
Cela signifie que l'unité peut alors stocker moins d'aura maximale.  
Il s’agit généralement de sorts ou d’artefacts magiques très puissants qui provoquent des effets permanents.

[[cmd-cast]] est un ordre pseudo-long comparable à [[cmd-attack]].  
Une unité peut donc lancer des sorts plusieurs fois par tour, mais ne peut exécuter aucun autre ordre long.  
Mais il y a un hic : les coûts d’aura des sorts augmentent.  
Le premier sort lancé par l'unité au cours d'un round coûte l'aura normale spécifiée dans le sort.  
Le deuxième coûte deux fois plus cher, le troisième quatre fois plus, le quatrième huit fois, etc.

Les sorts de combat sont traités séparément; ils n'augmentent pas le coût des sorts normaux ou d'autres sorts de combat et ne coûtent toujours que l'aura spécifiée.  
Les [sorts à distance] augmentent également le coût de lancement.  

### Niveau de lanceur de sorts

La valeur spécifiée comme "niveau" est initialement le niveau minimum auquel l'unité obtient le sort.  

Certains sorts ont des effets et des coûts fixes.  
Ils sont toujours lancés au niveau du sort et ne peuvent pas être modifiés par des paramètres.  
Cela peut toujours être important pour des choses comme la [résistance à la magie].  
Le sort **Create A Ring of Invisibility** est toujours lancé au niveau 6 et produit exactement un anneau.  

De nombreux sorts ont des effets et des coûts qui dépendent du niveau.  
Leur effet dépend du niveau auquel le sort a été lancé.  
Les détails dépendent du sort en question.
Parfois cela concerne la durée de l’effet, parfois le nombre de personnes enchantées, etc.  

Avec ces sorts variables, vous pouvez spécifier un niveau auquel le sort doit être lancé.  
Celui-ci doit être égal ou inférieur au niveau en magie de l'unité, mais il peut être supérieur ou inférieur au niveau normal du sort.  
Cela vous permet de lancer le sort à un niveau inférieur à votre propre compétence.

En utilisant un [[anneau-de-pouvoir]], une [Tour des mages] ou un [Cercle de pierres bénies], la force peut être augmentée d'un point supplémentaire.  
Ce bonus est ajouté au niveau spécifié.

Si le niveau n'est pas précisé, le sort est lancé au niveau maximum possible, c'est à dire le niveau de compétence de l'unité (les modifications comme les bonus raciaux ou les bonus spéciaux comme ceux des Insectes dans les déserts sont pris en compte).  
Une raison pour laquelle cela n'est pas toujours souhaitable est que le niveau auquel le sort est lancé affecte également la [probabilité d'erreurs].

Spécifier un niveau fonctionne également pour les sorts de combat :

```text
COMBATSPELL LEVEL 2 "Song of Fear"
```

Ceci peut être utile, par exemple, lorsque vous souhaitez conserver de l'aura pour un sort d'après-combat.

**Example:**

```text
CAST LEVEL 4 "Miracle doctor"
```

Ce sort coûtera 4 auras et rapportera 200 silver.  
Avec un Anneau de Pouvoir, cela coûte toujours 4 auras mais rapporte 250 silver.

### Composants

S'il est simplement indiqué le nombre d'aura, cela signifie que les coûts sont fixes : **Créer un Anneau d'invisibilité** coûte toujours 50 auras.  
Si les composants d'in sort indiquent par exemple `3 Aura * Level`, cela signifie que pour lancer un sort une fois, le coût de l'aura est de 3 auras multiplié par le niveau auquel le sort est lancé.  
Ainsi, **Miracle Doctor** coûte 1 aura lorsqu'il est lancé au niveau 1, et 30 auras lorsqu'il est lancé au niveau 30.  

Si le sort nécessite une aura permanente, l'aura maximale de l'unité est définitivement réduite de cette valeur.  
D'autres composants peuvent inclure des plantes, des matières premières, de l'argent, des potions ou même des objets rares ou bien des agriculteurs.  

### Magie à distance

Les sorts à distance sont lancés dans la région de l'unité de mage, mais s'appliquent dans une région différente.  
Vous pouvez alors utiliser la syntaxe suivante pour ces sorts :

```text
CAST REGION <x> <y> "<Sort>"
```

Le sort est ensuite lancé dans la région spécifiée.  
Les coordonnées X et Y font référence au [[cmd-origin]].  
Cependant, cette modification augmente le coût de tous les composants du sort de façon exponentielle.  
Le **coût** des composants matériels et de l'aura **est doublé par région de distance** entre l'emplacement de l'unité et la cible.  

Formule : 2 puissance a, où *a* est la distance entre la région cible et la région de l'unité.

À titre d’illustration :

| Distance entre régions (a) |  0 |  1 |  2 |  3 |   4 |
|----------------------------|---:|---:|---:|---:|----:|
| **Pierres** requises       |  1 |  2 |  4 |  8 |  16 |
| **Fer** requis             |  5 | 10 | 20 | 40 |  80 |
| **Bois** requis            | 10 | 20 | 40 | 80 | 160 |

Le coût de l'aura est également augmenté si une unité lance plusieurs sorts en un tour.  
La formule déterminant le coût de l'aura en fonction du nombre de sorts lancés est la suivante :

2 puissance (b-1), où b est le nombre de sorts dans ce tour, voir [ci-dessus][aura]).  

Cela ne s'applique pas aux autres composants, qui ne sont augmentés que par les sorts à distance.

Les sorts à distance et les sorts multiples combinés peuvent également augmenter les coûts en aura (CA) :

| Distance région (a) |   0    |   1    |    2    |    3    |    4    |
|---------------------|--------|--------|--------:|--------:|---------|
| 1er sort            | CA x 1 | CA x 2 |  CA x 4 |  CA x 8 | CA x 16 |
| 2ème sort           | CA x 2 | CA x 4 |  CA x 8 | CA x 16 | CA x 32 |
| 3ème sort           | CA x 4 | CA x 8 | CA x 16 | CA x 32 | CA x 64 |

Les deux modificateurs peuvent également être liés :

```text
CAST REGION <x> <y> LEVEL <niveau> "<Sort>"
```

Il est important de préciser d’abord la région, puis le niveau.

**Exemple :**

Une unité de la région (1,1) lance "Bénédiction de la Terre" au niveau 3 dans la région voisine à l'est comme premier sort du tour (a = 1 distance de champ).  
Cela coûte 2 x 3 = 6 aura.  

L'ordre à donner pour ce sort est `CAST REGION 2 1 LEVEL 3 "Blessed Harvest"`.  

### Magie en bateau et sur mer

En plus des sorts à distance, il existe également deux autres classes de sorts spéciaux.

En général, les sorts ne peuvent pas être invoqués depuis un bateau.  
Les seules exceptions sont les sorts désignés spécifiquement comme sorts de **Magie en bateau**.  

D'autres sorts, désignés spécifiquement comme sorts de **Magie en mer** marqué peuvent également lancés sur l’océan par des non-Aquariens.  

### Magie sur les gens et les objets

Certains sorts peuvent être utilisés pour influencer avec la magie des personnes et des objets.  
Il est à noter que la grande majorité des sorts à lancer sur des unités amies nécessitent que l'unité cible contacte le mage avec [[cmd-contact]].  
Les téléportations et autres enchantements peuvent être bien intentionnés, mais peuvent souvent être utilisés pour des méfaits, et avec [[cmd-contact]], la cible signale qu'elle accepte l'enchantement.  

### Rang

L'ordre des sorts normaux est déterminé par le rang du sort.  
Au cours d'un round, les sorts de rang inférieur sont toujours exécutés avant ceux de rang supérieur.  
Le rang 1 est le plus bas et le rang 9 est le plus élevé.  
La plupart des sorts ont un rang standard de 5, mais les sorts antimagiques ont presque tous un rang de 2, ils peuvent donc être lancés avant les sorts normaux.  
Les sorts de même rang sont lancés dans l'ordre spécifié lors du tour.

**Exemple :**

Soit trois sorts, appelés "Aaa", "Bee" et "Cee" :

- "Aaaa" est de rang 5 et coûte 10 auras
- "Beee" est de rang 2 et coûte 20 auras
- "Ceee" est de rang 5 et coûte 5 auras

En supposant que l'unité passe les ordres :

```text
CAST "Ceee"
CAST "Beee"
CAST "Aaaa"
```

dans cet ordre.

« Beee » est lancé en premier, car le sort est de rang 2.
C'est le premier sort de l'unité cette semaine, il coûte donc 20 auras.
Ensuite, "Ceee" est lancé, car "Aaaa" et "Ceee" ont le même rang et "Ceee" vient avant "Aaaa".
"Ceee" est le deuxième sort, il coûte donc 5*2^1=10 aura. Vient maintenant « Aaaa ».
"Aaaa" est le troisième sort, il coûte donc 10*2^2=40 aura.

## Gaffe

Il y a beaucoup de choses qui ne sont pas évidentes dans le système de magie et dans les sorts.  
En général, de nombreuses paroles contiennent des risques directs ou indirects.  
Un mage peut aussi rater un sort.

Ainsi, un sort peut tout simplement échouer, même si tous les composants sont réellement là et que l’aura d’unité est suffisante.  
Ce n'est pas un bug, un message tout à fait normal est présent dans le rapport ("The spell fails.").  
Si des composants ou une aura manquent, cela sera également mentionné dans le message.

La probabilité d'une erreur dépend de nombreux facteurs, parmi lesquels le niveau, la difficulté du sort par rapport au niveau auquel le sort est lancé par le mage, l' École de Magie, le sort, l'environnement, la cible, etc.  

Les erreurs peuvent avoir des effets secondaires extrêmement désagréables !  
Cependant, si l’unité survit à une erreur, celle-ci n’est généralement pas permanente.

Experience de jeu (Solthar) :

Un sort lancé au niveau maximum possible a environ 20 % de chances d'échec; à mi-niveau, il y a 0 % de chance.  
Pour les mages Draig, c'est 10 % de plus.
Conséquences possibles (par ordre décroissant de fréquence) :

- Le sort fonctionne, mais les sorts suivants deviennent beaucoup plus chers
- Toute aura est perdue, le sort fonctionne ou non
- Le sort ne fonctionne pas et vous devenez un [[crapaud]] pendant 2 semaines ou plus
- Le sort ne fonctionne pas et il y a un effet spécial

Les effets spéciaux affectent principalement Gwyrrd (des Ents enragés sont créés) et Draig (des foules de paysans ou d'autres conséquences).

## Résistance à la magie

La résistance à la magie d'une unité est la capacité inhérente de chaque personne à résister à un sort lancé contre elle et la gravité avec laquelle une personne est affectée par les dégâts de magie au combat.  
La résistance à la magie d'une unité s'obtient par l'addition de :

- la résistance naturelle à la magie des [[races]]
- +5 % par niveau de compétence en magie
- *+10 % x Nombre de licornes* par personne
- Éventuellement un bonus ou un malus dû au [[liste-des-sorts|sort]] sur l'unité ou la région
- Éventuellement un bonus de [bâtiment][Cercle de pierres bénies]

Le résultat ne peut jamais être supérieur à 90 %.  

Pour certains enchantements directs, il est en outre influencé par l'expérience de l'unité.  

- 50 % + 5 % * (valeur de compétence la plus élevée de l'unité enchantée - compétence magique de l'unité qui lance)
- Jamais en dessous de 2 %, jamais au-dessus de 98 %

<!-- TODO: clarify translation -->
Au lieu de cela, les bonus supplémentaires des [armes ou armures] fonctionnent contre les sorts de combat tels que les boules de feu et les armes considérées comme magiques.  
Sinon, seules la protection magique et l’armure naturelle fonctionnent contre les dégâts de magie.  

Même la « matière inanimée » (c'est-à-dire les régions, les bateaux, les bâtiments...), a parfois une résistance magique.  
Il peut également être renforcé par certains sorts.  

**Exemples:**

La chance de base est de 0 % pour les humains, de 10 % pour les [[skills-modifiers|elfes]], et de -5 % pour les [[skills-modifiers|gobelins]].  

Une unité Mining 10 a 50 % de chances de résister à un sort comme [Malédiction du Chaos] lancé par une unité de T10 en magie.  
Si le niveau en magie est T12, les chances tombent à 40 %.  
Si l'unité cible est composée de gobelins, les chances diminuent encore à 35 %.  

Par exemple, une boule de feu qui ferait 50 dégâts (5d10 + 15) ne fait que (90 % contre un elfe équipé d'une [épée en laen][armes ou armures] * 70 %) = 63 % de cela, soit environ 31 dégâts.  

## Tour des Mages

Une [Tour de Mage] augmente la régénération de l'aura de 75 % et augmente le niveau effectif de tout sort lancé en son sein de 1, le cas échéant, en plus d'un [[anneau-de-pouvoir]] sans augmenter le coût.  
De plus, la probabilité d’un échec du sort est considérablement réduite.  

## Familiers

Les mages expérimentés rencontreront à un moment donné au cours de leurs pérégrinations un spécimen inhabituel d’une espèce qui les rejoindra.  
Le genre auquel appartient cette créature dépend principalement de l' École de Magie et de la race.  

Plus d'information sur ces créatures : les [[familiers]].  

## L'Astral

!!! note
    Vous pouvez également ignorer cette section si vous lisez les instructions pour la première fois - car il faut plusieurs semaines avant qu'un groupe puisse voyager dans l'Astral - ou si vous préférez comprendre vous-même les règles compliquées de l'Astral.

Les opinions sur ce qu'est réellement ce deuxième plan d'existence varient aussi largement que les noms qui lui sont donnés : certains l'appellent le **monde des Esprits** , d'autres le **Monde astral**, mais le terme le plus connu est **plan de l'Astral**.  
Des lois de la nature complètement différentes prévalent dans cet autre monde.  
Ce fait est peut-être la seule raison pour laquelle l'Astral est resté une application pratique de la magie : celui qui parvient à brouiller la frontière entre l'Astral et la réalité au bon moment en utilisant ses pouvoirs magiques peut obtenir de grands avantages – que ce soit en percevant les choses de l'autre côté sans être vu lui-même, ou en voyageant rapidement sur de grandes distances.

Quiconque pénètre dans l'Astral - cela n'est possible que grâce à certains [[liste-des-sorts|sorts]] - disparaît complètement du monde réel.  
Comme le monde réel, l’Astral est divisé en régions dont les points cardinaux sont connus.  
Les unités situées en un point de l'Astral apparaissent dans le rapport et sont jouées comme les autres unités.  
Vous pouvez ainsi recevoir des ordres comme [[cmd-move]] et [[cmd-attack]] et interagir avec d'autres entités de l'Astral.  
Ils ne peuvent communiquer avec le monde normal que par magie.  

Les sens des créatures du monde sont incapables de percevoir concrètement l'environnement de l'Astral.  
L'œil voit l'environnement comme une simple brume et tous les sons sont étouffés.  
De chaque point de l'Astral, jusqu'à 19 régions du monde réel peuvent être vues schématiquement, qui sont éloignées d'au plus deux régions d'une région réelle spécifique, que nous appellerons ici le « point de référence » (vert sur l'image).  
Certains sorts peuvent rendre ces schémas plus précis.  
Dans l’image d’exemple, toutes les régions pouvant être identifiées à partir d’une région sont encadrées en rouge.  
6 régions coupées en deux par la ligne rouge sont même visibles depuis deux régions astrales chacune.  

<!-- TODO: astral connection map 488X393 - should be where in the page ? -->
![Connexion de l'Astral](assets/images/astral-space-connection.jpg "onnexion de l'Astral")

Ce qui rend l'espace astral particulièrement déroutant, c'est que ces schémas ne sont pas identiques aux régions qui sont reliées à la région de l'Astral, à partir desquelles on peut accéder à la région de l'Astral et vice versa.  
Au lieu de cela, chaque point de l'Astral est connecté à une zone du monde normal, chacune comprenant 16 régions (en jaune sur l'image).  
Cette zone a la forme d'un parallélogramme avec 4 régions s'étendant chacune dans les directions est-ouest et sud-ouest-nord-est.  
Le « point de référence » en est le coin sud-ouest.  
Toutes les régions d’une telle zone mènent au même point en entrant dans l'Astral.  
Cette connexion est une condition préalable à la plupart des sorts impliquant l'Astral.  
Mais il peut aussi être perturbé, par exemple par des Cercles de pierres bénies récemment visités par un mage.  
Selon le sort utilisé, des restrictions supplémentaires peuvent s'appliquer.  

C'est pourquoi la prudence est de mise - car d'une part vous pouvez voir les schémas de régions réelles qui ne sont pas connectées à ce point dans l'Astral, mais d'autre part toutes les régions du monde réel avec lesquelles il existe une telle connexion n'apparaissent pas comme des schémas.  
Ce n'est que lorsque les voyageurs s'orienteront malgré ces différences qu'ils se rendront compte qu'ils peuvent progresser plusieurs fois plus rapidement dans l'Astral.  
Parce que chaque étape dans le monde spirituel correspond à 4 étapes dans le monde réel.

Ce n'est que grâce à la magie que la réalité peut être modifiée de telle manière que les êtres vivants entrent dans le monde des êtres spirituels.  
De plus, vous ne pouvez pas emmener de pierres, de chevaux, de chars ou de catapultes dans le monde des Esprits.  
Seulement les **Chevaux elfiques** semblent être capables de survivre en tant que montures magiques dans l'Astral.  

En général, tout le monde devrait être mis en garde contre une traversée imprudente dans l'Astral, car celui-ci est habité par des [créatures monstrueuses] qui ne peuvent être vaincus par des armes ordinaires et qui privent impitoyablement leurs victimes de leur volonté et de leur mémoire.  
Seuls ceux qui portent avec eux des armes magiques puissantes  ou sont capables de se cacher extrêmement bien des regards hostiles seront immunisés contre ces horreurs de l'Astral.  
Les autres devront compter sur leurs alliés !  

## Listes de tous les sorts

Dans les premiers jours d'Eressea, les listes exactes de sorts étaient secrètes afin que "nous puissions anticiper si et quels nouveaux sorts on recevrait en atteignant un nouveau niveau".
Eressea existe maintenant depuis si longtemps que les nouveaux joueurs seraient trop désavantagés par rapport aux joueurs confirmés si les sorts n'étaient pas connus.  
C'est pourquoi il existe désormais une [[liste-des-sorts]] et une [[description-des-sorts]].

Poursuivre la lecture : [[ecoles-de-magie]].

<!-- From [https://wiki.eressea.de/index.php?title=Magie/de&oldid=16363] -->

[aura]: #aura
[sorts à distance]: ./magic.md#magie-a-distance
[résistance à la magie]: ./magic.md#resistance-a-la-magie
[probabilité d'erreurs]: #gaffe

[Académie]: ./buildings-others.md#academie
[`COMBAT`]: ./war.md#lignes-de-combat
[Les camps dans une bataille]: ./war.md#les-camps-dans-une-bataille
[Tour de Mage]: ./buildings-others.md#tour-de-mage
[Cercle de pierres bénies]: ./buildings-others.md#cercle-de-pierres
[armes ou armures]: ./war-tables.md#resistance-a-la-magie
[Malédiction du Chaos]: ./spells-descriptions.fr.md#malediction-du-chaos
[créatures monstrueuses]: ./monsters.md#morts-vivants
