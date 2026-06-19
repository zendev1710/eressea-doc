---
# cSpell:locale fr
alias: description-des-sorts
---

# Description des sorts

## A

[](){ #acc-l-ration-id }

### Accélération

<!-- cspell:disable -->
*Acceleration (EN), Beschleunigung (DE)*.
<!-- cspell:enable -->

:   Ce sort accélère certains combattants de votre côté afin qu'ils puissent attaquer deux fois en un seul round de combat, tout au long du combat.  

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  T  | 5 x N aura |  9   | Pré-c. |  5   |        |       |

`COMBATSPELL [LEVEL n] Acceleration`  

[](){ #affaiblissement-id }

### Affaiblissement

<!-- cspell:disable -->
*Tiredness (EN), Schwere Glieder (DE)*.
<!-- cspell:enable -->

:   Ce sort de combat provoque une fatigue intense chez certains ennemis pendant le combat.  
    Les soldats tardent parfois à attaquer et se défendent mal.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  I  | 4 x N aura |  4   | Pré-c. |  5   |        |       |

`COMBATSPELL [LEVEL n] Tiredness`  

[](){ #analyse-de-la-magie-id }

### Analyse de la Magie

<!-- cspell:disable -->
*Analyze Magic (EN), Magie analysieren (DE)*.
<!-- cspell:enable -->

:   Ce sort permet au mage de tenter de détecter les enchantements d'un seul objet spécifié.  
    Il pourra se faire une idée de leur efficacité grâce à tous les sorts qui ne dépassent pas ses propres capacités.  
    Avec des sorts plus puissants, il lui faut un peu de chance pour réussir son analyse.

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  T  |   N aura   |  1   | Normal |  5   | :material-check:{ .success } |       |

`CAST [LEVEL n] "Analyze Magic" ( REGION | UNIT <unit-id> [<unit-id> ...] | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

[](){ #analyse-des-r-ves-id }

### Analyse des rêves

<!-- cspell:disable -->
*Analyse Dreams (EN), Traumbilder analysieren (DE)*.
<!-- cspell:enable -->

:   Avec ce sort, le tisserand de rêves peut tenter de détecter les enchantements d'une seule unité.  
    Il pourra se faire une idée de leur efficacité grâce à tous les sorts qui ne dépassent pas ses propres capacités.  
    Avec des sorts plus puissants, il lui faut un peu de chance pour réussir son analyse.

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  I  |  25 aura   |  5   | Normal |  5   | :material-check:{ .success } |       |

`CAST "Analyse Dreams" <unit-id>`  

[](){ #analyse-du-chant-de-la-vie-id }

### Analyse du chant de la Vie

<!-- cspell:disable -->
*Analyze Song of Life (EN), Gesang des Lebens analysieren (DE)*.
<!-- cspell:enable -->

:   Tous les êtres vivants ont leur propre chant de vie.  
    Il n’y a pas deux chansons identiques, même si toutes les chansons du même type sont similaires.  
    Chaque sort modifie ce chant d'une manière ou d'une autre et se révèle ainsi.  
    Ce chant aide à entendre les changements dans le chant de la vie d'une personne qui sont de nature magique.  
    Vous pourrez déchiffrer et démasquer tous les enchantements qui ne sont pas plus masqués que vos capacités.

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  C  |  10 aura   |  5   | Normal |  5   | :material-check:{ .success } |       |

`CAST "Analyze Song of Life" <unit-id>`  

[](){ #analyses-id }

### Analyses

<!-- cspell:disable -->
*Analysis (EN), Lied des Ortes analysieren (DE)*.
<!-- cspell:enable -->

:   Comme les êtres vivants, les bateaux, les bâtiments et même les régions ont leur propre chant, bien que beaucoup plus faible et plus difficile à entendre.  
    Et tout comme le chant de la vie d'une personne permet de savoir si elle est sous le charme, cela est également possible pour les châteaux, les bateaux ou les régions.  

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  C  | 3 x N aura |  8   | Normal |  5   | :material-check:{ .success } |       |

`CAST [LEVEL n] "Analysis" ( REGION | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

[](){ #antimagie-id }

### Antimagie

<!-- cspell:disable -->
*Antimagic (EN), Astrale Schwächezone (DE)*.
<!-- cspell:enable -->

:   Avec ce sort le mage peut créer une zone d'affaiblissement Astral, un déséquilibre local dans le champ Astral.  
    Cette zone s'efforcera de revenir à l'équilibre.  
    Pour ce faire, il supprimera une partie de la force de chaque sort lancé dans cette région et même absorbera complètement les plus faibles.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau |              D               |
|:---:|:----------:|:----:|:------:|:----:|:------:|:----------------------------:|
|  T  | 3 x N aura |  5   | Normal |  2   |        | :material-check:{ .success } |

`CAST [REGION x y] [LEVEL n] "Antimagic"`  

[](){ #apaisement-des-meutes-id }

### Apaisement des émeutes

<!-- cspell:disable -->
*Calm Riot (EN), Aufruhr beschwichtigen (DE)*.
<!-- cspell:enable -->

:   À l’aide de ce chant magique, le mage peut calmer une région en ébullition.  
    Les hordes d'agriculteurs vont se perdre et retourner dans leurs champs.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau |              D               |
|:---:|:----------:|:----:|:------:|:----:|:------:|:----------------------------:|
|  C  |  30 aura   |  15  | Normal |  5   |        | :material-check:{ .success } |

`CAST [REGION x y] "Calm Riot"`  

[](){ #apercu-sur-la-realite-id }

### Aperçu sur la réalité

<!-- cspell:disable -->
*Gaze Upon Reality (EN), Blick in die Realität (DE)*.
<!-- cspell:enable -->

:   Grâce à ce sort, le mage peut regarder du plan Astral vers le plan matériel et reconnaître avec précision les régions et les unités.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  T  |  40 aura   |  10  | Normal |  5   |        |       |

`CAST "Gaze Upon Reality"`  

[](){ #art-subtil-de-la-persuasion-id }

### Art subtil de la persuasion

<!-- cspell:disable -->
*High art of persuasion (EN), Hohe Kunst der Überzeugung (DE)*.
<!-- cspell:enable -->

<div class="lore-dialogue">
"À Weilersweide, près du port de Wythar, se trouve une petite auberge rarement visitée.
Nul ne sait que, jusqu'à il y a quelques années, cette ferme était la demeure du prédicateur itinérant Grauwolf. banni depuis.
Après avoir rallié à sa cause la quasi-totalité des paysans lors d'un de ses discours enflammés, il fut condamné pour sédition et exilé.
Il accepta de me révéler, à contrecœur, le secret de son éloquence."
</div>

Extrait de « Errants » de Firudin le Sage.

| Éc. | Composants  | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:-----------:|:----:|:------:|:----:|:------:|:-----:|
|  C  | 20 x N aura |  14  | Normal |  5   |        |       |

`CAST [LEVEL n] "High art of persuasion"`  

## B

[](){ #bannissement-des-esprits-id }

### Bannissement des Esprits

<!-- cspell:disable -->
*Banish Spirits (EN), Geister bannen (DE)*.
<!-- cspell:enable -->

:   Selon les anciens enseignements des druides, ce que les êtres ordinaires appellent magie est constitué d'esprits élémentaires.  
    Le mage les évoque et les bannit sous une forme permettant d'obtenir l'effet souhaité. Ce rituel est capable de chasser les esprits élémentaires invoqués dans ce monde afin de libérer un objet de la magie.  

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            |              D               |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:----------------------------:|
|  G  | 6 x N aura |  8   | Normal |  2   | :material-check:{ .success } | :material-check:{ .success } |

`CAST [REGION x y] [LEVEL n] "Banish Spirits" ( REGION | UNIT <unit-id> [<unit-id> ...] | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

[](){ #b-ton-de-mallorn-id }

### Bâton de Mallorn

<!-- cspell:disable -->
*Bless Mallorn Logs (EN), Segne Mallornstecken (DE)*.
<!-- cspell:enable -->

:   Ce rituel augmente plusieurs fois l'effet de la potion magique.  
    Alors qu’auparavant seul un arbre pouvait germer à partir d’un bâton, chaque branche produit désormais des racines.

| Éc. |                                                 Composants                                                  | Niv. |  Type  | Rang | Bateau |              D               |
|:---:|:-----------------------------------------------------------------------------------------------------------:|:----:|:------:|:----:|:------:|:----------------------------:|
|  G  | 6 x N aura, N [mallorns][mallorn-fr-id]{title="Mallorn"}, 1 [eau de vie][eau-de-vie]{title="Water of life"} |  4   | Normal |  5   |        | :material-check:{ .success } |

`CAST [REGION x y] [LEVEL n] "Bless Mallorn Logs"`  

[](){ #b-n-diction-de-la-terre-id }

### Bénédiction de la terre

<!-- cspell:disable -->
*Blessed Harvest (EN), Segen der Erde (DE)*.
<!-- cspell:enable -->

:   Ce rituel de récolte améliore les rendements des agriculteurs qui travaillent dans la région pour un silver de plus.  
    Plus le druide investit de puissance, plus le sort dure longtemps.

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            |              D               |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:----------------------------:|
|  G  |   N aura   |  1   | Normal |  5   | :material-check:{ .success } | :material-check:{ .success } |

`CAST [REGION x y] [LEVEL n] "Blessed Harvest"`  

[](){ #b-n-diction-du-cercle-de-pierres-id }

### Bénédiction du Cercle de Pierres

<!-- cspell:disable -->
*Bless Stone Circle (EN), Segne Steinkreis (DE)*.
<!-- cspell:enable -->

:   Ce rituel bénit un [Cercle de Pierres][cercle-de-pierres] qui doit d'abord être construit à partir de pierres et d'un peu de bois.  
    La bénédiction du druide transforme le cercle en un puissant site d'activité magique, offrant une protection contre la magie et une régénération accrue de l'aura.  
    On dit que les vierges rencontraient d'étranges créatures autour des cercles de pierres.

| Éc. |         Composants          | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:---------------------------:|:----:|:------:|:----:|:------:|:-----:|
|  G  | 350 aura, 5 aura permanents |  11  | Normal |  5   |        |       |

`CAST "Bless Stone Circle" <building-id>`  

[](){ #bouclier-a-rien-id }

### Bouclier aérien

<!-- cspell:disable -->
*Air Shield (EN), Windschild (DE)*.
<!-- cspell:enable -->

:   Invoque les esprits élémentaires du vent.  
    Invoque des rafales de vent soudaines, de petites rafales de vent et des évents qui gêneront les archers adverses.

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  G  | 2 x N aura |  4   | Pré-c. |  5   | :material-check:{ .success } |       |

`COMBATSPELL [LEVEL n] "Air Shield"`  

[](){ #bouclier-d-armure-id }

### Bouclier d'armure

<!-- cspell:disable -->
*Shield Shine (EN), Rüstschild (DE)*.
<!-- cspell:enable -->

:   Ce rituel, qui peut être lancé avant le combat, confère à vos troupes un bonus supplémentaire à leur armure.  
    Chaque coup réduit la puissance du sort, le bouclier se dissipera donc à un moment donné du combat.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  T  | 4 x N aura |  12  | Pré-c. |  2   |        |       |

`COMBATSPELL [LEVEL n] "Shield Shine"`  

[](){ #bouclier-du-poisson-id }

### Bouclier du poisson

<!-- cspell:disable -->
*Shield of the Fish (EN), Schild des Fisches (DE)*.
<!-- cspell:enable -->

:   Ce sort peut donner à l'ennemi une image légèrement différente de ses propres troupes, tout comme le poisson dans l'eau n'est pas là où il semble être.  
    De cette façon, la moitié des dégâts de chaque coup peuvent être rendus inoffensifs.  
    Mais le bouclier ne peut résister que quelques centaines de coups d’épée, après quoi il se désintègre.  
    Plus le mage est fort, plus le bouclier peut résister aux dégâts.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  T  | 4 x N aura |  8   | Pré-c. |  2   |        |       |

`COMBATSPELL [LEVEL n] "Shield of the Fish"`  

[](){ #boule-de-feu-id }

### Boule de feu

<!-- cspell:disable -->
*Fireball (EN), Feuerball (DE)*.
<!-- cspell:enable -->

:   Le sorcier lance un chaos ciblé dans les rangs ennemis. Le chaos en forme de boule blessera tous ceux qu'il touchera.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  D  |   N aura   |  2   | Combat |  5   |        |       |

`COMBATSPELL [LEVEL n] Fireball`  

[](){ #brise-mal-diction-id }

### Brise‑malédiction

<!-- cspell:disable -->
*Negate Curse (EN), Fluch brechen (DE)*.
<!-- cspell:enable -->

:   Ce sort permet au mage de dissiper spécifiquement un enchantement spécifique sur une unité, un bateau, un bâtiment ou même la région.

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            |              D               |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:----------------------------:|
|  T  | 3 x N aura |  7   | Normal |  3   | :material-check:{ .success } | :material-check:{ .success } |

`CAST [REGION x y] [LEVEL n] "Negate Curse" ( REGION | UNIT <unit-id> | SHIP <ship-id> | CASTLE <building-id> ) <spell-id>`  

## C

[](){ #changement-de-forme-id }

### Changement de forme

<!-- cspell:disable -->
*Shapeshift (EN), Gestaltwandlung (DE)*.
<!-- cspell:enable -->

:   Avec l’aide de ce rituel mystérieux, le tisserand de rêves est capable de dissimuler la véritable forme d’un groupe.  
    Pour les observateurs inexpérimentés, elle semble alors appartenir à un peuple différent.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  I  |   N aura   |  3   | Normal |  5   |        |       |

`CAST [LEVEL n] Shapeshift <unit-id> <peuple>`  

[](){ #chant-apaisant-id }

### Chant apaisant

<!-- cspell:disable -->
*Appeasing Song (EN), Friedenslied (DE)*.
<!-- cspell:enable -->

:   Cette chanson apprivoise même l'orque le plus sauvage et le rend paisible et doux.  
    Toute idée de nuire au chanteur disparaîtra.  
    Le mage peut se déplacer sans encombre dans une région voisine.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  C  |   2 aura   |  1   | Pré-c. |  5   |        |       |

`COMBATSPELL [LEVEL n] "Appeasing Song"`  

[](){ #chant-d-effroi-id }

### Chant d'effroi

<!-- cspell:disable -->
*Song of Fear (EN), Gesang der Angst (DE)*.
<!-- cspell:enable -->

:   Ce chant de guerre sème la panique sur les lignes de front ennemies et affaiblit ainsi considérablement leur force de combat.  
    La peur affaiblira leur bras d’épée et la peur paralysera leur bras de bouclier.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  C  | 5 x N aura |  8   | Pré-c. |  5   |        |       |

`COMBATSPELL [LEVEL n] "Song of Fear"`  

[](){ #chant-de-confusion-id }

### Chant de confusion

<!-- cspell:disable -->
*Song of Confusion (EN), Gesang der Verwirrung (DE)*.
<!-- cspell:enable -->

:   Ce chant magique est issu des anciens chants des chats et, utilisé avant un combat, peut apporter des avantages stratégiques décisifs.  
    Quiconque est sous l'influence de cette chanson ne prêtera pas attention à la mélodie de son environnement, son esprit deviendra confus et cédera de manière erratique à des inspirations soudaines.  
    On dit que des armées bien ordonnées ont soudainement trouvé leurs archers loin devant et leur cavalerie jouant aux cartes avec les gardes du camp (ou leur chef dormant dans le camp abandonné depuis longtemps, comme cela se serait effectivement produit lors des grandes guerres de l'Ancien Monde).

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  C  | 2 x N aura |  4   | Pré-c. |  5   |        |       |

`COMBATSPELL [LEVEL n] "Song of Confusion"`  

[](){ #chant-de-contre-id }

### Chant de contre

<!-- cspell:disable -->
*Countersong (EN), Bannlied (DE)*.
<!-- cspell:enable -->

:   Ce chant strident résonne sur tout le champ de bataille.  
    Les dissonances particulières des mélodies rendent presque impossible aux mages de se concentrer sur leurs sorts.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  C  | 5 x N aura |  5   | Pré-c. |  2   |        |       |

`COMBATSPELL [LEVEL n] Countersong`  

[](){ #chant-de-cour-id }

### Chant de cour

<!-- cspell:disable -->
*Song of Courting (EN), Gesang des Werbens (DE)*.
<!-- cspell:enable -->

:   Extrait « Des Chants des Anciens » de Firudin le Sage :  
    « Cette petite mélodie séduisante et quelques mots insinuants vainquent en un instant la méfiance des paysans.  
    Ils vous rejoindront avec enthousiasme et laisseront eux-mêmes leur maison et leur cour en ruines. »

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  C  | 2 x N aura |  4   | Normal |  5   |        |       |

`CAST [LEVEL n] "Song of Courting"`  

[](){ #chant-de-generosite-id }

### Chant de générosité

<!-- cspell:disable -->
*Song of Generosity (EN), Hohes Lied der Gaukelei (DE)*.
<!-- cspell:enable -->

:   Cette chanson joyeuse se répandra comme une rumeur dans toute la région et mettra le monde entier dans une ambiance de fête.  
    Les tavernes et les théâtres seront partout pleins et même les mendiants seront nourris.

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            |              D               |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:----------------------------:|
|  C  | 2 x N aura |  2   | Normal |  5   | :material-check:{ .success } | :material-check:{ .success } |

`CAST [REGION x y] [LEVEL n] "Song of Generosity"`  

[](){ #chant-de-gu-rison-id }

### Chant de guérison

<!-- cspell:disable -->
*Song of Healing (EN), Lied der Heilung (DE)*.
<!-- cspell:enable -->

:   Il n'y a pas que le médecin qui peut aider les blessés au combat.  
    Les bardes connaissent diverses chansons qui soutiennent les pouvoirs d'auto-guérison du corps.  
    Ce chant peut refermer des blessures, réparer des os brisés et régénérer même des membres sectionnés.

| Éc. | Composants | Niv. |  Type   | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:-------:|:----:|:------:|:-----:|
|  C  |   N aura   |  2   | Post-c. |  5   |        |       |

`COMBATSPELL [LEVEL n] "Song of Healing"`  

[](){ #chant-de-guerre-id }

### Chant de guerre

<!-- cspell:disable -->
*Song of War (EN), Kriegsgesang (DE)*.
<!-- cspell:enable -->

:   Comme beaucoup de chansons magiques, celle-ci vient également de la connaissance ancienne des chats, qui connaissent depuis toujours les puissants effets de la voix.  
    Cette chanson attise l'humeur des guerriers, les plongeant même dans une frénésie sauvage et une soif de sang.  
    Indépendamment de leur propre souffrance, ils se battront jusqu’à la mort et ne fuiront jamais.  
    Alors que leur attaque s’intensifie, ils ne prêtent que peu d’attention à eux-mêmes.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  C  | 5 x N aura |  7   | Pré-c. |  4   |        |       |

`COMBATSPELL [LEVEL n] "Song of War"`  

[](){ #chant-de-l-esprit-de-jouvence-id }

### Chant de l'esprit de jouvence

<!-- cspell:disable -->
*Song of the Youthful Spirit (EN), Gesang des wachen Geistes (DE)*.
<!-- cspell:enable -->

:   Ce chant magique, autrefois chanté avec ferveur, va se répandre dans toute la région, sauter de bouche en bouche et se faire entendre partout pendant un moment.  
    Le nombre de semaines pendant lesquelles la chanson disparaît de la mémoire de la région dépend de l'habileté du barde.  
    Jusqu'à ce que la chanson disparaisse complètement, sa magie accordera à tous les alliés du barde (`HELP GUARD`), et bien sûr à son propre peuple, un bonus unique de 15 % à la résistance naturelle à un enchantement.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau |              D               |
|:---:|:----------:|:----:|:------:|:----:|:------:|:----------------------------:|
|  C  | 2 x N aura |  10  | Normal |  2   |        | :material-check:{ .success } |

`CAST [REGION x y] [LEVEL n] "Song of the Youthful Spirit"`  

[](){ #chant-de-l-esprit-vieillissant-id }

### Chant de l'esprit vieillissant

<!-- cspell:disable -->
*Song of the Aging Spirit (EN), Gesang des schwachen Geistes (DE)*.
<!-- cspell:enable -->

:   Tissée dans l'essence magique de la région, cette chanson affaiblit une fois la résistance naturelle à un enchantement de 15 %.  
    Seuls les alliés du barde (`HELP GUARD`) sont immunisés contre l'effet de la chanson.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau |              D               |
|:---:|:----------:|:----:|:------:|:----:|:------:|:----------------------------:|
|  C  | 2 x N aura |  12  | Normal |  2   |        | :material-check:{ .success } |

`CAST [REGION x y] [LEVEL n] "Song of the Aging Spirit"`  

[](){ #chant-de-m-lancolie-id }

### Chant de mélancolie

<!-- cspell:disable -->
*Song of Melancholy (EN), Gesang der Melancholie (DE)*.
<!-- cspell:enable -->

:   Avec cette chanson, le barde répand une ambiance mélancolique et triste parmi les agriculteurs.  
    Pendant quelques semaines, ils se retireront dans leurs huttes et ne laisseront aucune argenterie dans les théâtres et les tavernes.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau |              D               |
|:---:|:----------:|:----:|:------:|:----:|:------:|:----------------------------:|
|  C  |  40 aura   |  11  | Normal |  5   |        | :material-check:{ .success } |

`CAST [REGION x y] "Song of Melancholy"`  

[](){ #chant-de-paix-id }

### Chant de paix

<!-- cspell:disable -->
*Song of Peace (EN), Gesang der Friedfertigkeit (DE)*.
<!-- cspell:enable -->

:   Ce sort puissant empêche toute attaque.  
    Personne dans toute la région n’est capable de prendre les armes contre qui que ce soit.  
    Les effets peuvent durer plusieurs semaines.

| Éc. | Composants  | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:-----------:|:----:|:------:|:----:|:------:|:-----:|
|  C  | 20 x N aura |  12  | Normal |  5   |        |       |

`CAST [LEVEL n] "Song of Peace"`  

[](){ #chant-de-s-duction-id }

### Chant de séduction

<!-- cspell:disable -->
*Song of Seduction (EN), Lied der Verführung (DE)*.
<!-- cspell:enable -->

:   Cette chanson peut être utilisée pour charmer une unité afin qu'elle donne la plupart de son argent et de ses biens au barde.  
    Cependant, elle garde toujours ce dont elle a besoin pour survivre.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  C  |  12 aura   |  6   | Normal |  5   |        |       |

`CAST "Song of Seduction" <unit-id>`  

[](){ #chant-de-servitude-id }

### Chant de servitude

<!-- cspell:disable -->
*Song of Slavery (EN), Gesang der Versklavung (DE)*.
<!-- cspell:enable -->

:   Ce puissant sort prive la victime de son libre arbitre et la soumet aux ordres du barde.  
    Pendant un certain temps, la victime se détournera complètement des siens et aura le sentiment d'appartenir à la faciton du barde.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  C  |  40 aura   |  13  | Normal |  5   |        |       |

`CAST "Song of Slavery" <unit-id>`  

[](){ #chant-de-terreur-id }

### Chant de terreur

<!-- cspell:disable -->
*Song of Terror (EN), Gesang der Furcht (DE)*.
<!-- cspell:enable -->

:   Une chanson très puissante issue des traditions des chats qui pénètre profondément dans le cœur des ennemis et leur prive de courage et d'espoir.  
    La peur les fera trembler et la panique dominera leurs pensées.  
    Pleins de peur, ils tenteront d’échapper aux chants horribles et de s’enfuir.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  C  |   N aura   |  3   | Combat |  5   |        |       |

`COMBATSPELL [LEVEL n] "Song of Terror"`  

[](){ #chant-des-h-ros-id }

### Chant des héros

<!-- cspell:disable -->
*Epic Heroes (EN), Heldengesang (DE)*.
<!-- cspell:enable -->

:   Cet ancien chant de bataille remonte le moral de vos troupes et les aide également à résister à l'aura effrayante des êtres démoniaques et morts-vivants.  
Un guerrier aussi solide ne fuira pas même dans des situations difficiles et son comportement réfléchi lui donnera de nombreux avantages en défense.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  C  | 2 x N aura |  5   | Pré-c. |  4   |        |       |

`COMBATSPELL [LEVEL n] "Epic Heroes"`  

[](){ #chaos-de-l-astral-id }

### Chaos de l'Astral

<!-- cspell:disable -->
*Astral Chaos (EN), Astrales Chaos (DE)*.
<!-- cspell:enable -->

:   Ce rituel, effectué avant la bataille, fait tourbillonner les énergies astrales sur le champ de bataille, rendant plus difficile le lancement de leurs sorts par les mages ennemis.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  D  | 6 x N aura |  9   | Pré-c. |  2   |        |       |

`COMBATSPELL [LEVEL n] "Astral Chaos"`  

[](){ #ch-teau-d-illusion-id }

### Château d'Illusion

<!-- cspell:disable -->
*Castle of Illusion (EN), Traumschlößchen (DE)*.
<!-- cspell:enable -->

:   Avec l'aide de ce sort, le tisserand de rêves peut créer l'illusion de n'importe quel bâtiment.  
    L'illusion peut être saisie, mais elle est par ailleurs non fonctionnelle et ne nécessite aucun entretien.
    Cela durera quelques semaines.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  I  |   3 aura   |  3   | Normal |  5   |        |       |

`CAST "Castle of Illusion" <building-type>`  

[](){ #chevaliers-de-l-ombre-id }

### Chevaliers de l'Ombre

<!-- cspell:disable -->
*Shadow Knights (EN), Schattenritter (DE)*.
<!-- cspell:enable -->

:   Ce sort peut donner à l'ennemi une image légèrement différente de ses propres troupes.  
    Les Chevaliers de l'Ombre n'ont aucune attaque efficace et être blessés au combat les détruira instantanément.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  I  |   N aura   |  1   | Pré-c. |  4   |        |       |

`COMBATSPELL [LEVEL n] "Shadow Knights"`  

[](){ #creer-des-golems-de-fer-id }

### Créer des [Golems de Fer][golem-de-fer]

<!-- cspell:disable -->
*Create Iron Golems (EN), Erschaffe Eisengolems (DE)*.
<!-- cspell:enable -->

:   Plus le mage investit de puissance, plus de golems peuvent être créés.  
    Chaque golem a 15 % de chances de se transformer en poussière à chaque tour.  
    Si vous donnez aux golems l'ordre `MAKE SWORD/CLAYMORE` ou `MAKE SHIELD/CHAIN​​​​MAIL/PLATEMAIL`, 4 fers sont consommés par golem et le golem se dissout.

| Éc. |                                         Composants                                         | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:------------------------------------------------------------------------------------------:|:----:|:------:|:----:|:------:|:-----:|
|  G  | 2 x N aura, N [fers][fer]{title="Iron"}, 1 [eau de vie][eau-de-vie]{title="Water of life"} |  2   | Normal |  4   |        |       |

`CAST [LEVEL n] "Create Iron Golems"`  

[](){ #creer-des-golems-de-pierre-id }

### Créer des [Golems de pierre][golem-de-pierre]

<!-- cspell:disable -->
*Create Stone Golems (EN), Erschaffe Steingolems (DE)*.
<!-- cspell:enable -->

<div class="lore-dialogue">
"Humidifiez un bloc de fine roche cristalline sans interstice avec une fiole d’eau de vie jusqu’à ce qu’elle soit complètement absorbée par la roche.
Ensuite, vous dirigez votre force vers la fine aura de vie qui se forme et formez un logement pour la force non liée."
</div>

:   Plus le mage investit de puissance, plus de golems peuvent être créés avant que l'aura ne se dissipe.  
    Chaque golem a 10 % de chances de se transformer en poussière à chaque tour.  
    Si vous donnez aux golems l'ordre `MAKE CASTLE` ou `MAKE STREET`, 4 pierres sont utilisées par golem et le golem se dissout.

| Éc. |                                            Composants                                             | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:-------------------------------------------------------------------------------------------------:|:----:|:------:|:----:|:------:|:-----:|
|  G  | 2 x N aura, N [pierres][pierre]{title="Stone"}, 1 [eau de vie][eau-de-vie]{title="Water of life"} |  1   | Normal |  4   |        |       |

`CAST [LEVEL n] "Create Stone Golems"`  

[](){ #creer-un-anneau-d-invisibilite-id }

### Créer un [anneau d'Invisibilité][anneau-d-invisibilite-id]{title="Ring of Invisibility"}

<!-- cspell:disable -->
*Create A Ring of Invisibility (EN), Erschaffe einen Ring der Unsichtbarkeit (DE)*.
<!-- cspell:enable -->

:   Avec ce sort, le sorcier peut créer un [anneau d'Invisibilité][anneau-d-invisibilite-id]{title="Ring of Invisibility"}.  
    Le porteur de l'anneau devient invisible pour toutes les unités des autres partis, quelle que soit la qualité de leur perception.  
    Dans une unité invisible, chaque personne doit porter une bague.

|  Éc.   |               Composants                | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:------:|:---------------------------------------:|:----:|:------:|:----:|:----------------------------:|:-----:|
| \*[^1] | 50 aura, 3 000 silver, 1 aura permanent |  6   | Normal |  5   | :material-check:{ .success } |       |

`CAST "Create A Ring of Invisibility"`  

[](){ #creer-un-anneau-de-pouvoir-id }

### Créer un [anneau de Pouvoir][anneau-de-pouvoir-id]{title="Ring of Power"}

<!-- cspell:disable -->
*Ring of Power (EN), Erschaffe einen Ring der Macht (DE)*.
<!-- cspell:enable -->

:   Ce rituel puissant crée un [anneau de Pouvoir][anneau-de-pouvoir-id]{title="Ring of Power"}.  
    Celui-ci augmente la puissance de tout sort lancé par son porteur, comme si le mage était supérieur d'un niveau.

| Éc. |                Composants                | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:----------------------------------------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  T  | 100 aura, 1 aura permanent, 4 000 silver |  9   | Normal |  5   | :material-check:{ .success } |       |

`CAST "Create A Ring of Power"`  

[](){ #creer-un-cristal-d-antimagie-id }

### Créer un [Cristal d'Antimagie][cristal-d-anti-magie-id]{title="Antimagic Crystal"}

<!-- cspell:disable -->
*Create An Antimagic Crystal (EN), Erschaffe Antimagiekristall (DE)*.
<!-- cspell:enable -->

:   À l'aide de ce sort, le mage draine un cristal de quartz de toutes ses énergies magiques.  
    Le cristal, une fois broyé en une fine poussière et dispersé, absorbera les énergies magiques libérées lors du lancement et réduira la puissance de tous les sorts lancés dans la région cette semaine-là.

| Éc. |      Composants       | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:---------------------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  T  | 50 aura, 3 000 silver |  7   | Normal |  5   | :material-check:{ .success } |       |

`CAST "Create An Antimagic Crystal"`  

[](){ #creer-un-dreameye-id }

### Créer un [DreamEye][dreameye]{title="DreamEye"}

<!-- cspell:disable -->
*Create a Visioneye (EN), Erschaffe ein Traumauge (DE)*.
<!-- cspell:enable -->

:   Un œil de dragon lancé avec ce sort est consommé lors de la communion, ce qui permet à l'utilisateur d'entrer et de lire les rêves d'une autre personne.  
    Pendant longtemps, une telle capacité a été considérée comme inutile jusqu'à ce que l'ancien maître de la magie de combat des Elfes des bois, Liarana Sundew de l'Académie Thall, présente une application spéciale :  
    les généraux rêvent souvent sans relâche avant les batailles majeures et révèlent leurs plans dans leurs rêves.  
    Cela peut donner à l'utilisateur un énorme avantage dans la bataille à venir.  
    Mais attention : interpréter les rêves est une affaire difficile.

| Éc. |                                Composants                                 | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:-------------------------------------------------------------------------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  I  | 1 [tête de dragon][tete-de-dragon]{title="Dragonhead"}, 5 aura permanents |  14  | Normal |  5   | :material-check:{ .success } |       |

`CAST "Create a Visioneye"`  

[](){ #creer-un-sac-a-herbes-magique-id }

### Créer un [[sac-a-herbes-magique]]

<!-- cspell:disable -->
*Create A magical Herb Pouch (EN), Erschaffe einen magischen Kräuterbeutel (DE)*.
<!-- cspell:enable -->

:   Le druide prend du cuir préparé, qu'il nettoie de tous les esprits impurs lors d'un grand rituel de purification, puis lie quelques petits esprits de l'air et de l'eau au matériau.  
    Il utilise désormais le cuir ainsi préparé pour fabriquer un petit sac qui permet de mieux conserver les herbes qui y sont stockées.

| Éc. |                                  Composants                                  | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:----------------------------------------------------------------------------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  G  | 30 aura, 1 aura permanent, 1 [eau de vie][eau-de-vie]{title="Water of life"} |  5   | Normal |  5   | :material-check:{ .success } |       |

`CAST "Create A magical Herb Pouch"`

[](){ #creer-un-sac-sans-fond-id }

### Créer un [[sac-sans-fond]]

<!-- cspell:disable -->
*Create A Bag of Holding (EN), Erschaffe einen Beutel des Negativen Gewichts (DE)*.
<!-- cspell:enable -->

:   Ce sac renferme un petit pli dimensionnel dans lequel jusqu'à 200 unités de poids peuvent être transportées sans être comptées dans le poids transporté.  
    Les chevaux et autres êtres vivants ainsi que les objets particulièrement volumineux (chars et catapultes) ne peuvent pas être transportés dans le sac.  
    Il n'est pas non plus possible de transporter un sac magique dans un autre. Le sac lui-même pèse 1 lbs.

| Éc. |               Composants                | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:---------------------------------------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  T  | 30 aura, 1 aura permanent, 5 000 silver |  10  | Normal |  5   | :material-check:{ .success } |       |

`CAST "Create A Bag of Holding"`

[](){ #creer-une-amulette-de-vision-decuplee-id }

### Créer une [amulette de vision décuplée][amulette-de-vision-decuplee-id]{title="Amulet of True Sight"}

<!-- cspell:disable -->
*Create An Amulet of True Sight (EN), Erschaffe ein Amulett des wahren Sehens (DE)*.
<!-- cspell:enable -->

:   Le sort permet à un mage de créer une [amulette de vision décuplée][amulette-de-vision-decuplee-id]{title="Amulet of True Sight"}.
    L'amulette permet au porteur de voir toutes les unités protégées par un [anneau d'Invisibilité][anneau-d-invisibilite-id]{title="Ring of Invisibility"}.  
    Cependant, les unités qui utilisent leur compétence de [discrétion][skill-discretion-id]{title="Stealth"} pour se cacher ne sont toujours pas détectées.

|  Éc.   |               Composants                | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:------:|:---------------------------------------:|:----:|:------:|:----:|:----------------------------:|:-----:|
| \*[^1] | 50 aura, 3 000 silver, 1 aura permanent |  6   | Normal |  5   | :material-check:{ .success } |       |

`CAST "Create An Amulet of True Sight"`  

[](){ #creer-une-ceinture-de-force-de-troll-id }

### Créer une [[ceinture-de-force-de-troll]]

<!-- cspell:disable -->
*Create A Belt of Troll Strength (EN), Erschaffe einen Gürtel der Trollstärke (DE)*.
<!-- cspell:enable -->

:   Cet artefact magique confère à son porteur la force d'un Troll des Cavernes adulte.  
    Sa capacité de charge est multipliée par 50 et sa force accrue et sa peau résistante aux trolls auront également un effet positif au combat.

| Éc. |        Composants         | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:-------------------------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  D  | 20 aura, 1 aura permanent |  9   | Normal |  5   | :material-check:{ .success } |       |

`CAST "Create A Belt of Troll Strength"`  

[](){ #creer-une-epee-de-flammes-id }

### Créer une [[epee-de-flammes]]

<!-- cspell:disable -->
*Create A Flaming Sword (EN), Erschaffe ein Flammenschwert (DE)*.
<!-- cspell:enable -->

<div class="lore-dialogue">
"Et alors frottez le sang d'un féroce combattant dans l'acier de la lame et commencez l'invocation des Sphères du Chaos.
Et si vous avez tout fait pour leur plaire, ils enverront l'un des leurs pour imprégner l'épée de son pouvoir..."
</div>

| Éc. |                                                           Composants                                                           | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:------------------------------------------------------------------------------------------------------------------------------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  D  | 100 aura, 1 [sang de berserker][sang-de-berserker]{title="Berserkers blood""}, 1 [épée][epee]{title="Sword"}, 1 aura permanent |  12  | Normal |  5   | :material-check:{ .success } |       |

`CAST "Create A Flaming Sword"`  

[](){ #creer-une-sphere-d-invisibilit-id }

### Créer une [Sphère d'Invisibilité][sphere-d-invisibilite-id]{title="Sphere of Invisibility"}

<!-- cspell:disable -->
*Create A Sphere of Invisibility (EN), Erschaffe eine Sphäre der Unsichtbarkeit (DE)*.
<!-- cspell:enable -->

:   Avec ce sort, le mage peut créer une [Sphère d'Invisibilité][sphere-d-invisibilite-id]{title="Sphere of Invisibility"}.  
    Celle-ci rend invisibles son porteur et quatre-vingt-dix-neuf autres personnes de la même unité.

| Éc. |                 Composants                 | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:------------------------------------------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  I  | 150 aura, 30 000 silver, 3 aura permanents |  13  | Normal |  5   | :material-check:{ .success } |       |

`CAST "Create A Sphere of Invisibility"`  

## D

[](){ #danse-de-la-pluie-id }

### Danse de la pluie

<!-- cspell:disable -->
*Rain Dance (EN), Regentanz (DE)*.
<!-- cspell:enable -->

:   Cet ancien rituel de danse invoque les forces de vie et de fertilité.  
    Les rendements des agriculteurs seront nettement meilleurs pendant plusieurs semaines.

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            |              D               |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:----------------------------:|
|  C  |   N aura   |  3   | Normal |  5   | :material-check:{ .success } | :material-check:{ .success } |

`CAST [REGION x y] [LEVEL n] Rain Dance`  

[](){ #de-beaux-r-ves-id }

### De beaux rêves

<!-- cspell:disable -->
*(EN), Schöne Träume (DE)*.
<!-- cspell:enable -->

:   Ce sort permet au Dreamweaver d'affecter le sommeil de toutes les unités alliées de la région, leur donnant un bonus dans toutes les compétences pendant un certain temps.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau |              D               |
|:---:|:----------:|:----:|:------:|:----:|:------:|:----------------------------:|
|  I  |  80 aura   |  8   | Normal |  5   |        | :material-check:{ .success } |

`CAST [REGION x y] "Schöne Träume"`  

[](){ #de-doux-r-ves-id }

### De doux rêves

<!-- cspell:disable -->
*Sweet Dreams (EN), Süße Träume (DE)*.
<!-- cspell:enable -->

:   Ce sortilège dont l'usage est strictement interdit dans la plupart des cultures déclenche chez la victime un désir incontrôlable d'amour physique.  
    Les individus concernés se précipiteront à corps perdu dans une histoire d'amour, trop aveuglés par le désir de penser à autre chose.  
    La plupart du temps, ils le regrettent quelques semaines plus tard...

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  I  | 5 x N aura |  12  | Normal |  5   |        |       |

`CAST [LEVEL n] "Sweet Dreams" <unit-id> [<unit-id> ...]`  

[](){ #d-livrance-des-r-ves-id }

### Délivrance des rêves

<!-- cspell:disable -->
*Remove Dreams (EN), Traumbilder entwirren (DE)*.
<!-- cspell:enable -->

:   Ce sort permet au tisserand de rêves de distinguer et de démêler les images oniriques naturelles et forcées d'une personne, d'un bâtiment, d'un bateau ou d'une région.

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            |              D               |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:----------------------------:|
|  I  | 6 x N aura |  8   | Normal |  2   | :material-check:{ .success } | :material-check:{ .success } |

`CAST [REGION x y] [LEVEL n] "Remove Dreams" ( REGION | UNIT <unit-id> [<unit-id> ...] | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

[](){ #d-voreur-de-magie-id }

### Dévoreur de magie

<!-- cspell:disable -->
*Destroy Magic (EN), Magiefresser (DE)*.
<!-- cspell:enable -->

:   Ce sort permet au mage de dissiper les enchantements sur une unité, un bateau, un bâtiment ou même une région.

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            |              D               |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:----------------------------:|
|  T  | 4 x N aura |  5   | Normal |  2   | :material-check:{ .success } | :material-check:{ .success } |

`CAST [REGION x y] [LEVEL n] "Destroy Magic" ( REGION | UNIT <unit-id> [<unit-id> ...] | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

[](){ #diable-de-feu-id }

### Diable de feu

<!-- cspell:disable -->
*Fire Fiend (EN), Feuerteufel (DE)*.
<!-- cspell:enable -->

:   Cette invocation élémentaire invoque un diable de feu, une créature venue des profondeurs des enfers enflammés.  
    Le diable du feu se jettera avec impatience sur les forêts de la région et les incendiera.

| Éc. |               Composants               | Niv. |  Type  | Rang | Bateau |              D               |
|:---:|:--------------------------------------:|:----:|:------:|:----:|:------:|:----------------------------:|
|  D  | 50 aura, 1 [huile][huile]{title="Oil"} |  10  | Normal |  5   |        | :material-check:{ .success } |

`CAST [REGION x y] "Fire Fiend"`  

[](){ #dirigeable-id }

### Dirigeable

<!-- cspell:disable -->
*Airship (EN), Luftschiff (DE)*.
<!-- cspell:enable -->

:   Ces runes magiques font voler un bateau ou une chaloupe pendant une semaine.  
    Cela peut alors également être utilisé pour traverser des terres.  
    Pour la couleur des runes, une encre spéciale doit être mélangée à partir d'un chou à la crème et d'un cristal de neige.

| Éc. |                     Composants                      | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:---------------------------------------------------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  T  | 10 aura, 1 [gousse], 1 [pétale de cristal de neige] |  6   | Normal |  5   | :material-check:{ .success } |       |

`CAST Airship <ship-id>`  

[](){ #dissimulation-d-aura-id }

### Dissimulation d'aura

<!-- cspell:disable -->
*Concealing Aura (EN), Schleieraura (DE)*.
<!-- cspell:enable -->

:   Ce sort masquera tout l'équipement de l'unité cible pendant un certain temps.

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  T  |   N aura   |  1   | Normal |  5   | :material-check:{ .success } |       |

`CAST [LEVEL n] "Concealing Aura" <unit-id>`  

[](){ #dissonance-du-silence-id }

### Dissonance du silence

<!-- cspell:disable -->
*Silence Dissonance (EN), Lebenslied festigen (DE)*.
<!-- cspell:enable -->

:   Chaque enchantement affecte le Chant de Vie, l'affaiblissant et le déformant.  
    Le barde expérimenté peut tenter de capturer et d’amplifier le chant de la vie et d’effacer les changements du chant.

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            |              D               |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:----------------------------:|
|  C  | 5 x N aura |  8   | Normal |  2   | :material-check:{ .success } | :material-check:{ .success } |

`CAST [REGION x y] [LEVEL n] "Silence Dissonance" ( REGION | UNIT <unit-id> [<unit-id> ...] | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

[](){ #divination-id }

### Divination

<!-- cspell:disable -->
*Divination (EN), Wahrsagen (DE)*.
<!-- cspell:enable -->

:   Nul ne sait interpréter les rêves aussi bien qu'un mage Illaun.  
    Il maîtrise également l'art de la divination, de la cartomancie et de la chiromancie.  
    Pour cela, les paysans lui versent 50 silver par niveau.

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  I  |   N aura   |  1   | Normal |  5   | :material-check:{ .success } |       |

`CAST [LEVEL n] Divination`  

[](){ #docteur-miracle-id }

### Docteur Miracle

<!-- cspell:disable -->
*Miracle Doctor (EN), Wunderdoktor (DE)*.
<!-- cspell:enable -->

:   Si l'alchimiste ne peut pas vous aider, vous vous adressez au savant mage Tybied.  
    Ses potions et teintures aident contre tout ce que vous ne pouvez pas obtenir autrement.  
    Si la formule énigmatique sous le sabot du mari infidèle a vraiment aidé, eh bien, le fermier qui ne sait pas lire ne le saura jamais.  
    Cela aide certainement le mage... à remplir son portefeuille. Vous pouvez gagner 50 silver par niveau en une semaine.

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  T  |   N aura   |  1   | Normal |  5   | :material-check:{ .success } |       |

`CAST [LEVEL n] "Miracle Doctor"`  

[](){ #doigts-de-f-e-id }

### Doigts de fée

<!-- cspell:disable -->
*Quick Fingers (EN), Miriams flinke Finger (DE)*.
<!-- cspell:enable -->

:   La célèbre barde Miriam Bhean'Meddaf était connue pour son extraordinaire talent avec la harpe.  
    On disait que ses doigts se déplaçaient si rapidement sur les cordes qu'ils étaient pratiquement méconnaissables.  
    Ce sort, assez simple à lancer dans une bague en argent, permet de décupler la dextérité et l'agilité des doigts.  
    On dit qu’elle a également exploité cela ailleurs; sa réputation de tricheuse de cartes était notoire.  
    Les artisans peuvent ainsi produire 10 fois plus, ce qui pourrait également être utile dans d'autres activités.

| Éc. |               Composants                | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:---------------------------------------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  C  | 20 aura, 1 000 silver, 1 aura permanent |  11  | Normal |  5   | :material-check:{ .success } |       |

`CAST "Quick Fingers"`  

[](){ #don-du-chaos-id }

### Don du Chaos

<!-- cspell:disable -->
*Chaos Gift (EN), Gabe des Chaos (DE)*.
<!-- cspell:enable -->

:   Le mage ouvre son esprit aux sphères du Chaos et disposera ainsi de plus de pouvoir magique pendant un certain temps.  
    Mais l’aide des Seigneurs des Sphères a un prix, et la phase de pouvoir est donc remplacée par une phase de faiblesse.

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  D  |   6 aura   |  3   | Normal |  3   | :material-check:{ .success } |       |

`CAST "Chaos Gift"`  

## E

[](){ #coute-clandestine-id }

### Écoute clandestine

<!-- cspell:disable -->
*Sound out (EN), Aushorchen (DE)*.
<!-- cspell:enable -->

:   Si l'unité succombe au sort, elle dira au mage tout ce qu'elle sait sur la région en question.  
    S’il n’y a personne de sa faction dans la région, elle n’a rien à signaler.  
    Elle ne peut également dire que ce qu'elle a pu voir elle-même.

| Éc. |     Composants     | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:------------------:|:----:|:------:|:----:|:------:|:-----:|
|  C  | 4 aura, 100 silver |  7   | Normal |  5   |        |       |

`CAST "Sound out" <unit-id> <x> <y>`  

[](){ #meutes-id }

### Émeutes

<!-- cspell:disable -->
*Riot (EN), Aufruhr verursachen (DE)*.
<!-- cspell:enable -->

:   À l’aide de ce chant magique, le mage met toute une région en ébullition.  
    Des hordes d’agriculteurs rebelles rendent toute taxation impossible, presque plus personne ne donne d’argent à des escroqueries et aucune nouvelle personne ne peut être recrutée.  
    Après quelques semaines, la foule se calme à nouveau.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau |              D               |
|:---:|:----------:|:----:|:------:|:----:|:------:|:----------------------------:|
|  C  |  40 aura   |  16  | Normal |  5   |        | :material-check:{ .success } |

`CAST [REGION x y] "Riot"`  

[](){ #endormissement-id }

### Endormissement

<!-- cspell:disable -->
*Sleep (EN), Schlaf (DE)*.
<!-- cspell:enable -->

:   Ce sort endort certains combattants ennemis.  
    Les combattants endormis n'attaquent pas et ont des défenses plus faibles, mais ils se réveillent dès qu'ils sont touchés au combat.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  I  |   N aura   |  7   | Combat |  5   |        |       |

`COMBATSPELL [LEVEL n] Sleep`  

[](){ #esprits-du-gardien-de-l-astral-id }

### Esprits du Gardien de l'Astral

<!-- cspell:disable -->
*Astral Guardian Spirits (EN), Astralschutzgeister (DE)*.
<!-- cspell:enable -->

:   Ce rituel invoque des esprits élémentaires de magie et les envoie dans les rangs des mages ennemis.  
    Ces derniers auront bien plus de mal à lancer des sorts pendant toute la durée du combat.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  G  | 5 x N aura |  5   | Pré-c. |  2   |        |       |

`COMBATSPELL [LEVEL n] "Astral Guardian Spirits"`  

[](){ #tirement-du-temps-id }

### Étirement du temps

<!-- cspell:disable -->
*Double Time (EN), Zeitdehnung (DE)*.
<!-- cspell:enable -->

:   Cette application pratique des connaissances théoriques sur l’espace et le temps permet de modifier l’écoulement du temps pour certaines personnes.  
    Les personnes ainsi modifiées obtiennent deux fois plus de points de mouvement et deux fois plus d'attaques par round pendant quelques semaines.

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  T  | 5 x N aura |  11  | Normal |  5   | :material-check:{ .success } |       |

`CAST [LEVEL n] "Double Time" <unit-id> [<unit-id> ...]`  

[](){ #veil-des-ents-id }

### Éveil des [Ents][ents-fr-id]

<!-- cspell:disable -->
*Awakening of the Ents (EN), Erwecke Ents (DE)*.
<!-- cspell:enable -->

:   Avec l'aide de ce sort, le druide réveille les Ents endormis dans les forêts de la région de leur sommeil éternel.  
    Les créatures sauvages des arbres le rejoindront et l’assisteront, mais après un certain temps, elles retomberont dans le sommeil.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  G  | 6 x N aura |  10  | Normal |  5   |        |       |

`CAST [LEVEL n] "Awakening of the Ents"`  

## F

[](){ #folie-de-la-guerre-id }

### Folie de la guerre

<!-- cspell:disable -->
*Madness of War (EN), Wahnsinn des Krieges (DE)*.
<!-- cspell:enable -->

:   Devant les soldats ennemis, le mage noir sacrifie les dix pions dans un rituel sanglant et cruel et invoque ainsi les esprits de la folie sur les troupes ennemies.  
    Ils réagiront confusément au combat et seront incapables de suivre les ordres de leurs officiers.

| Éc. |       Composants       | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------------------:|:----:|:------:|:----:|:------:|:-----:|
|  D  | 3 x N aura, 10 paysans |  8   | Pré-c. |  5   |        |       |

`COMBATSPELL [LEVEL n] "Madness of War"`  

[](){ #force-impie-id }

### Force impie

<!-- cspell:disable -->
*Unholy Strength (EN), Unheilige Kraft (DE)*.
<!-- cspell:enable -->

:   Ce rituel n’est transmis aux adeptes des académies obscures qu’à voix basse, car c’est l’un des plus sombres jamais écrits.  
    En invoquant des démons impies, le pouvoir des morts-vivants est amplifié et ils se transforment en monstres morts-vivants d'une grande puissance.

| Éc. |         Composants         | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:--------------------------:|:----:|:------:|:----:|:------:|:-----:|
|  D  | 10 x N aura, 5 x N paysans |  14  | Normal |  5   |        |       |

`CAST [LEVEL n] "Unholy Strength" <unit-id> [<unit-id> ...]`  

[](){ #fuite-de-l-astral-id }

### Fuite de l'Astral

<!-- cspell:disable -->
*Astral Leak (EN), Astraler Riss (DE)*.
<!-- cspell:enable -->

:   Avec ce sombre rituel, le mage noir peut provoquer une rupture dans le tissu magique, qui arrachera tout pouvoir magique de la région.  
    Toutes les personnes douées pour la magie dans la région perdront une grande partie de leur aura.

| Éc. |          Composants           | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:-----------------------------:|:----:|:------:|:----:|:------:|:-----:|
|  D  | 35 aura, 1 [[sang-de-dragon]] |  9   | Normal |  3   |        |       |

`CAST "Astral Leak"`  

## G

[](){ #gardien-de-la-montagne-id }

### Gardien de la Montagne

<!-- cspell:disable -->
*Mountain Guardian (EN), Bergwächter (DE)*.
<!-- cspell:enable -->

:   Crée un esprit gardien qui empêche l'exploitation du fer et des métaux dans les glaciers et les montagnes par des factions non alliées (`HELP GUARD`) tant qu'il garde la région.  
    Le [Gardien de la Montagne][garde-des-montagnes]{title="Mountain Guard"} est lié au lieu de l'invocation.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau |              D               |
|:---:|:----------:|:----:|:------:|:----:|:------:|:----------------------------:|
|  G  | 3 x N aura |  3   | Normal |  5   |        | :material-check:{ .success } |

`CAST [REGION x y] [LEVEL n] Mountain Guardian`  

[](){ #grande-s-cheresse-id }

### Grande sécheresse

<!-- cspell:disable -->
*Great Drought (EN), Tor in die Ebene der Hitze (DE)*.
<!-- cspell:enable -->

:   Ce rituel puissant ouvre une porte vers le plan élémentaire de la chaleur.  
    Une grande sécheresse s'annonce dans le pays.  
    Les agriculteurs, les animaux et les plantes de la région luttent pour leur survie, mais seulement la moitié de tous les êtres vivants peuvent survivre à une telle sécheresse.  
    La région pourrait être affectée par les conséquences d’une telle sécheresse pendant des années.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau |              D               |
|:---:|:----------:|:----:|:------:|:----:|:------:|:----------------------------:|
|  G  |  800 aura  |  17  | Normal |  5   |        | :material-check:{ .success } |

`CAST [REGION x y] "Great Drought"`  

[](){ #gr-le-id }

### Grêle

<!-- cspell:disable -->
*Hail (EN), Hagel (DE)*.
<!-- cspell:enable -->

:   Au combat, le mage fait appel aux esprits élémentaires du froid et les lie à lui-même.  
    Il peut alors leur ordonner d'attaquer l'ennemi avec des grêlons et des morceaux de glace.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  G  |   N aura   |  3   | Combat |  5   |        |       |

`COMBATSPELL [LEVEL n] Hail`  

[](){ #gu-rison-du-b-tail-id }

### Guérison du bétail

<!-- cspell:disable -->
*Cattle Healing (EN), Viehheilung (DE)*.
<!-- cspell:enable -->

:   Les compétences d'élevage et de guérison des mages Gwyrrd sont très recherchées par les agriculteurs.  
    Leurs services sont souvent très demandés, notamment sur les marchés.  
    Certaines personnes peuvent également utiliser leur compétence pour vendre un animal à un meilleur prix.  
    Le mage peut gagner 50 silver par niveau.

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  G  |   N aura   |  1   | Normal |  5   | :material-check:{ .success } |       |

`CAST [LEVEL n] "Cattle Healing"`  

[](){ #gu-rison-id }

### Guérison

<!-- cspell:disable -->
*Heal (EN), Heilung (DE)*.
<!-- cspell:enable -->

:   Il n'y a pas que le médecin qui peut aider les blessés au combat.  
    Les druides sont capables de refermer les blessures, de réparer les os brisés et de régénérer même les membres sectionnés en invoquant les esprits élémentaires de la vie.

| Éc. | Composants | Niv. |  Type   | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:-------:|:----:|:------:|:-----:|
|  G  |   N aura   |  5   | Post-c. |  5   |        |       |

`COMBATSPELL [LEVEL n] Heal`  

[](){ #gueule-de-bois-id }

### Gueule de bois

<!-- cspell:disable -->
*Hangover (EN), Schaler Wein (DE)*.
<!-- cspell:enable -->

:   Enregistrement de la conférence de Selen Ard'Ragorn à Bar'Glingal :  
    « On dit que ce dicton trouve son origine dans les tavernes des rues de l'Ouest, mais il pourrait tout aussi bien provenir de n'importe quel autre quartier peu recommandable.  
    Son ingrédient le plus important est un tonneau du pire vin; plus l'essence est bon marché et malsaine, plus elle est puissante.  
    L'art de distiller ce vin jusqu'à son essence pure, bien plus exigeant qu'un simple mélange de recettes d'alchimiste,  
    et de le lier et de le conserver de telle manière qu'il ne s'évapore pas immédiatement comme c'est sa nature, oui, c'est quelque chose que seul un maître du Cerddor peut accomplir.  
    Vous possédez désormais une fiole contenant un reflet rouge rubis – enfin, pas liquide, mais pas vraiment de brume non plus – appelons-le simplement un élixir.  
    Mais ce n’est pas là le véritable défi; comme son effet se dissipe rapidement, il faut le glisser discrètement dans la boisson de la victime au bout de quelques jours.  
    Vous, maîtres de la tromperie et de la séduction, voici votre chance de véritablement démontrer votre art.  
    Mais attention, ne goûtez pas vous-même l'élixir de manière imprudente, car celui qui l'a goûté ne pourra jamais renoncer au vin et en boira sûrement pendant une semaine entière.  
    Cependant, le véritable danger inhérent à l’élixir n’est pas la tentation de boire, mais plutôt le fait que l’ivresse soit suivie aussi sûrement que le jour après la nuit d’un mal de tête vraiment terrible.  
    Et il aura presque certainement oublié certaines de ses meilleures capacités pendant quelques jours, voire deux semaines d'études.  
    Un dernier mot d'avertissement : cela prend beaucoup de temps, et si vous souhaitez lancer d'autres sorts dans la même semaine, ils seront plus difficiles pour vous. »

| Éc. |                                Composants                                | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:------------------------------------------------------------------------:|:----:|:------:|:----:|:------:|:-----:|
|  C  | 28 aura, 3 [racines de nœud][racine-de-nud]{title="Knotroot"}, 50 silver |  7   | Normal |  5   |        |       |

`CAST Hangover <unit-id>`  

## H

[](){ #h-ros-morts-vivants-id }

### Héros morts‑vivants

<!-- cspell:disable -->
*Undead Heroes (EN), Untote Helden (DE)*.
<!-- cspell:enable -->

:   Ce rituel lie les âmes déjà en fuite de certaines victimes de la bataille à leurs cadavres, les ressuscitant à la vie des morts-vivants.  
    Qu’ils aient déjà combattu du côté de l’ennemi ou du leur n’a aucune importance pour le rituel.  

| Éc. | Composants | Niv. |  Type   | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:-------:|:----:|:------:|:-----:|
|  D  |   N aura   |  9   | Post-c. |  5   |        |       |

`COMBATSPELL [LEVEL n] "Undead Heroes"`  

[](){ #horreurs-indicibles-id }

### Horreurs indicibles

<!-- cspell:disable -->
*Unspeakable Horrors (EN), Grauen der Schlacht (DE)*.
<!-- cspell:enable -->

:   Avant le combat, le tisserand de rêves évoque des illusions terrifiantes qui font paniquer de nombreux adversaires.  
    Les personnes touchées tenteront d’échapper aux mirages.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  I  |   N aura   |  2   | Pré-c. |  5   |        |       |

`COMBATSPELL [LEVEL n] "Unspeakable Horrors"`  

[](){ #hurlement-des-loups-id }

### Hurlement des Loups

<!-- cspell:disable -->
*Timber Wolves (EN), Wolfsgeheul (DE)*.
<!-- cspell:enable -->

:   Au cours de leur vie dans la nature, de nombreux druides se lient d'amitié avec les plus anciens amis des grands peuples.  
    Ils apprennent à invoquer plusieurs de leurs amis pour les aider au combat avec un seul appel hurlant.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  G  | 2 x N aura |  7   | Pré-c. |  5   |        |       |

`COMBATSPELL [LEVEL n] "Timber Wolves"`  

[](){ #hymne-du-partage-d-aura-id }

### Hymne du partage d'aura

<!-- cspell:disable -->
*Hymn of Aura Sharing (EN), Gesang des Auratransfers (DE)*.
<!-- cspell:enable -->

:   Avec l'aide de ce sort, le mage peut transférer sa propre aura dans un rapport de 2:1 à un autre mage de la même École de Magie.

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  C  |   2 aura   |  5   | Normal |  1   | :material-check:{ .success } |       |

`CAST "Hymn of Aura Sharing" <unit-id> <Aura>`  

## I

[](){ #impr-cation-id }

### Imprécation

<!-- cspell:disable -->
*Hex (EN), Verwünschung (DE)*.
<!-- cspell:enable -->

:   La cible du mage est frappée par une malédiction inoffensive.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  D  |   N aura   |  1   | Normal |  5   |        |       |

`CAST [LEVEL n] Hex <unit-id>`  

[](){ #insomnie-id }

### Insomnie

<!-- cspell:disable -->
*Insomnia (EN), Schlechter Schlaf (DE)*.
<!-- cspell:enable -->

:   Ce sort provoque de l'insomnie et de l'agitation dans la zone touchée pendant quelques semaines.  
    Les personnes concernées ont beaucoup plus de mal à apprendre.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau |              D               |
|:---:|:----------:|:----:|:------:|:----:|:------:|:----------------------------:|
|  I  |  18 aura   |  6   | Normal |  5   |        | :material-check:{ .success } |

`CAST [REGION x y] Insomnia`  

[](){ #intrusion-mentale-id }

### Intrusion mentale

<!-- cspell:disable -->
*Mind Probe (EN), Traumdeuten (DE)*.
<!-- cspell:enable -->

:   Grâce à ce sort, le tisserand de rêves pénètre dans les pensées et le monde onirique de sa victime et peut ainsi espionner ses secrets les plus intimes.  
    Ses capacités, ses possessions et son affiliation à un parti ne seront plus incertaines.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  I  |  20 aura   |  7   | Normal |  5   |        |       |

`CAST "Mind Probe" <unit-id>`  

[](){ #invocation-de-l-astral-id }

### Invocation de l'Astral

<!-- cspell:disable -->
*Astral Call (EN), Astraler Ruf (DE)*.
<!-- cspell:enable -->

:   Un mage qui se trouve dans le plan Astral peut utiliser ce sort pour lui amener d'autres unités.  
    Le mage peut (niveau 3)*Envoyer 15 lbs par la porte brièvement créée.  
    Si le mage est suffisamment expérimenté pour lancer le sort aux niveaux 13 ou plus, il peut forcer d'autres unités à passer à l'autre niveau, même contre leur gré.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  T  | 2 x N aura |  6   | Normal |  7   |        |       |

`CAST [LEVEL n] "Astral Call" <x> <y> <unit-id> [<unit-id> ...]`  

[](){ #invocation-d-un-l-mentaire-d-eau-id }

### Invocation d'un Élémentaire d'Eau

<!-- cspell:disable -->
*Summon Water Elemental (EN), Beschwörung eines Wasserelementares (DE)*.
<!-- cspell:enable -->

:   Avec ce rituel, le mage force les esprits élémentaires de l'eau à son service et les amène à transporter plus rapidement le bateau spécifié sur l'eau.  
    De plus, le bateau n’est pas affecté par des vents ou des courants défavorables.

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  G  |   N aura   |  4   | Normal |  5   | :material-check:{ .success } |       |

`CAST [LEVEL n] "Summon Water Elemental" <ship-id>`  

[](){ #invocation-d-un-l-mentaire-de-feu-id }

### Invocation d'un Élémentaire de Feu

<!-- cspell:disable -->
*Summon Fire Elemental (EN), Hitzeelementar (DE)*.
<!-- cspell:enable -->

:   Ce rituel invoque des élémentaires de chaleur en colère.  
    Une sécheresse ravage le pays. Les arbres se fanent, les animaux meurent et les récoltes échouent.  
    Il n’y a pratiquement pas de travail dans l’agriculture pour les journaliers.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau |              D               |
|:---:|:----------:|:----:|:------:|:----:|:------:|:----------------------------:|
|  G  |  600 aura  |  13  | Normal |  5   |        | :material-check:{ .success } |

`CAST [REGION x y] Summon Fire Elemental`  

[](){ #invocation-d-un-l-mentaire-de-terre-id }

### Invocation d'un Élémentaire de Terre

<!-- cspell:disable -->
*Summon Earth Elemental (EN), Beschwöre einen Erdelementar (DE)*.
<!-- cspell:enable -->

:   Avec ce rituel, le druide invoque un esprit élémentaire de la terre et le fait trembler la terre.  
    Ce tremblement de terre endommagera tous les bâtiments de la région.

| Éc. |                 Composants                  | Niv. |  Type  | Rang | Bateau |              D               |
|:---:|:-------------------------------------------:|:----:|:------:|:----:|:------:|:----------------------------:|
|  G  | 25 aura, 2 [laen][laen-fr-id]{title="Laen"} |  7   | Normal |  5   |        | :material-check:{ .success } |

`CAST [REGION x y] "Summon Earth Elemental"`  

[](){ #invocation-de-la-realite-id }

### Invocation de la Réalité

<!-- cspell:disable -->
*Call of Reality (EN), Ruf der Realität (DE)*.
<!-- cspell:enable -->

:   Un mage qui se trouve dans le monde matériel peut utiliser ce sort pour invoquer des unités du monde Astral adjacent.  
    Si le mage est suffisamment expérimenté pour lancer le sort à des niveaux de 13 ou plus, il peut forcer d'autres unités à entrer dans le monde matériel contre leur gré.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  T  | 2 x N aura |  6   | Normal |  7   |        |       |

`CAST [LEVEL n] "Call of Reality" <unit-id> [<unit-id> ...]`  

[](){ #invocation-des-d-mons-de-l-ombre-id }

### Invocation des Démons de l'Ombre

<!-- cspell:disable -->
*Summon Shadowdemons (EN), Beschwöre Schattendämonen (DE)*.
<!-- cspell:enable -->

:   À l’aide de rituels sombres, le mage invoque des démons depuis la sphère des ombres.  
    Ces créatures redoutées peuvent se déplacer de manière presque invisible parmi les vivants, mais leur aura sombre peut être ressentie par tout le monde.  
    Les démons de l’ombre sont des adversaires redoutés au combat.  
    Ils sont difficiles à toucher et drainent la puissance de leur adversaire.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  D  | 3 x N aura |  8   | Normal |  5   |        |       |

`CAST [LEVEL n] "Summon Shadowdemons"`  

[](){ #invocation-des-l-mentaires-des-temp-tes-id }

### Invocation des Élémentaires des Tempêtes

<!-- cspell:disable -->
*Summon Storm Elemental (EN), Beschwöre einen Sturmelementar (DE)*.
<!-- cspell:enable -->

:   L'invocation des esprits élémentaires des tempêtes est un rituel ancien.  
    Le druide bannit les élémentaires dans les voiles des bateaux, où ils aident à transporter le bateau sur les vagues à grande vitesse.  
    Plus le druide investit de puissance dans le sort, plus le nombre d'esprits élémentaires pouvant être bannis est grand.  
    Un esprit élémentaire est requis pour chaque vaisseau.

| Éc. | Composants | Niv. |  Type  | Rang |              Bateau              | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:--------------------------------:|:-----:|
|  G  | 6 x N aura |  6   | Normal |  5   | :material-check:{ .success }[^3] |       |

`CAST [LEVEL n] "Summon Storm Elemental" <ship-id> [<ship-id> ...]`  

[](){ #invocation-des-ma-tres-de-l-ombre-id }

### Invocation des Maîtres de l'Ombre

<!-- cspell:disable -->
*Summon Shadowmasters (EN), Beschwöre Schattenmeister (DE)*.
<!-- cspell:enable -->

:   À l’aide de rituels sombres, le mage invoque des démons depuis la sphère des ombres.  
    Ces créatures redoutées peuvent se déplacer de manière presque invisible parmi les vivants, mais leur aura sombre peut être ressentie par tout le monde.  
    Au combat, les maîtres de l’ombre sont des adversaires redoutés.  
    Ils sont difficiles à frapper et drainent la force et la vie de leur adversaire.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  D  | 7 x N aura |  12  | Normal |  5   |        |       |

`CAST [LEVEL n] "Summon Shadowmasters"`  

[](){ #invocation-du-dragon-id }

### Invocation du dragon

<!-- cspell:disable -->
*Dragon Call (EN), Drachenruf (DE)*.
<!-- cspell:enable -->

:   Avec ce sombre rituel, le mage crée un leurre dont l'odeur est irrésistible pour les [dragons][dragons-connus].  
    Il n'a pas encore été possible de déterminer si les dragons viennent des environs ou de la Sphère du Chaos.  
    On dit que les deux se sont déjà produits.  
    L'appât dure environ 6 semaines, mais doit être placé sur un terrain adapté aux cerfs-volants.

| Éc. |                           Composants                            | Niv. |  Type  | Rang | Bateau |              D               |
|:---:|:---------------------------------------------------------------:|:----:|:------:|:----:|:------:|:----------------------------:|
|  D  | 80 aura, 1 [tête de dragon][tete-de-dragon]{title="Dragonhead"} |  11  | Normal |  5   |        | :material-check:{ .success } |

`CAST [REGION x y] "Dragon Call"`  

[](){ #invocation-du-familier-id }

### Invocation du familier

<!-- cspell:disable -->
*Summon Familiar (EN), Vertrauten rufen (DE)*.
<!-- cspell:enable -->

:   À un moment donné de ses pérégrinations, un mage expérimenté rencontrera un spécimen inhabituel d'une espèce qui rejoindra le mage.

|  Éc.   |         Composants          | Niv. |  Type  | Rang | Bateau | Dist. |
|:------:|:---------------------------:|:----:|:------:|:----:|:------:|:-----:|
| \*[^1] | 100 aura, 5 aura permanents | [^2] | Normal |  5   |        |       |

`CAST "Summon Familiar"`  

## J

[](){ #jonglerie-id }

### Jonglerie

<!-- cspell:disable -->
*Jugglery (EN), Gaukeleien (DE)*.
<!-- cspell:enable -->

:   Les mages Cerddor sont les principaux jongleurs parmi les mages, ils aiment divertir les gens et être le centre d'attention.  
    Même les débutants apprennent les petits trucs et tours de magie qui peuvent être utilisés pour attirer et séduire les gens et leur faire ouvrir très grand leur portefeuille,  
    et à la fin de la semaine, le jongleur aura gagné 50 silver par niveau.

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  C  |   N aura   |  1   | Normal |  5   | :material-check:{ .success } |       |

`CAST [LEVEL n] Jugglery`  

## L

[](){ #le-manteau-de-firun-id }

### Le manteau de Firun

<!-- cspell:disable -->
*Firun's Coat (EN), Firuns Fell (DE)*.
<!-- cspell:enable -->

:   Ce sort permet au mage de protéger comme par magie les insectes du froid paralysant des glaciers.  
    Vous pouvez entrer dans les glaciers et y agir normalement.  
    Le dicton fonctionne au niveau*10 insectes.  
    Un [Anneau de Pouvoir][anneau-de-pouvoir-id]{title="Ring of Power"} augmente le nombre d'insectes enchantables de 10 supplémentaires.

|  Éc.   | Composants | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:------:|:----------:|:----:|:------:|:----:|:----------------------------:|:-----:|
| \*[^1] | 2 x N aura |  3   | Normal |  5   | :material-check:{ .success } |       |

`CAST [LEVEL n] "Firun's Coat" <unit-id> [<unit-id> ...]`  

[](){ #lecture-des-r-ves-id }

### Lecture des rêves

<!-- cspell:disable -->
*Read Dreams (EN), Traumlesen (DE)*.
<!-- cspell:enable -->

:   Ce sort permet au Dreamweaver d'entrer dans les rêves d'une unité pour obtenir un rapport sur les environs.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau |              D               |
|:---:|:----------:|:----:|:------:|:----:|:------:|:----------------------------:|
|  I  |   8 aura   |  4   | Normal |  5   |        | :material-check:{ .success } |

`CAST [REGION x y] "Read Dreams" <unit-id>`  

[](){ #liens-de-vie-id }

### Liens de Vie

<!-- cspell:disable -->
*Ties of Life (EN), Sog des Lebens (DE)*.
<!-- cspell:enable -->

:   Un druide tombé dans le monde des esprits peut utiliser ce sort pour passer au niveau supérieur x Renvoyer 5 unités de poids dans une forêt du monde matériel.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  G  | 2 x N aura |  9   | Normal |  7   |        |       |

`CAST [LEVEL n] "Ties of Life" <x> <y> <unit-id> [<unit-id> ...]`  

## M

[](){ #maelstrom-id }

### Maelstrom

<!-- cspell:disable -->
*Maelstrom (EN), Mahlstrom (DE)*.
<!-- cspell:enable -->

:   Ce rituel invoque un grand élémentaire d'eau des profondeurs de l'océan.  
    L'élémentaire crée un énorme tourbillon, un maelstrom, qui peut gravement endommager tous les bateaux qui le traversent.

| Éc. |                                       Composants                                       | Niv. |  Type  | Rang |              Bateau              | Dist. |
|:---:|:--------------------------------------------------------------------------------------:|:----:|:------:|:----:|:--------------------------------:|:-----:|
|  G  | 200 aura, 1 [tête de serpent de mer][tete-de-serpent-de-mer]{title="Sea Serpent Head"} |  15  | Normal |  5   | :material-check:{ .success }[^3] |       |

`CAST "Maelstrom"`  

[](){ #magie-du-bosquet-de-ch-ne-id }

### Magie du bosquet de chêne

<!-- cspell:disable -->
*Grove of Oak Trees (EN), Hainzauber (DE)*.
<!-- cspell:enable -->

:   Alors qu'auparavant seul un arbre pouvait germer à partir d'un bâton, chaque branche produit désormais des racines.

| Éc. |                                          Composants                                          | Niv. |  Type  | Rang | Bateau |              D               |
|:---:|:--------------------------------------------------------------------------------------------:|:----:|:------:|:----:|:------:|:----------------------------:|
|  G  | 4 x N aura, N [bois][bois]{title="Wood"},, 1 [eau de vie][eau-de-vie]{title="Water of life"} |  2   | Normal |  5   |        | :material-check:{ .success } |

`CAST [REGION x y] [LEVEL n] "Grove of Oak Trees"`  

[](){ #mal-diction-de-la-peste-id }

### Malédiction de la peste

<!-- cspell:disable -->
*Curse of Pestilence (EN), Fluch der Pestilenz (DE)*.
<!-- cspell:enable -->

:   Dans un rituel élaboré, le mage noir sacrifie quelques paysans puis distribue comme par magie les cadavres dans les puits de la région.

| Éc. |     Composants      | Niv. |  Type  | Rang | Bateau |              D               |
|:---:|:-------------------:|:----:|:------:|:----:|:------:|:----------------------------:|
|  D  | 30 aura, 50 paysans |  7   | Normal |  5   |        | :material-check:{ .success } |

`CAST [REGION x y] "Curse of Pestilence"`  

[](){ #mal-diction-du-chaos-id }

### Malédiction du Chaos

<!-- cspell:disable -->
*Chaos Curse (EN), Chaosfluch (DE)*.
<!-- cspell:enable -->

:   Cette malédiction insidieuse altère considérablement les capacités magiques de la victime.  
    Une zone magique de chaos autour de la victime réduit sa capacité de concentration et rend très difficile le lancement de sorts.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  D  | 4 x N aura |  5   | Normal |  4   |        |       |

`CAST [LEVEL n] "Chaos Curse" <unit-id>`  

[](){ #mauvais-r-ves-id }

### Mauvais rêves

<!-- cspell:disable -->
*Bad Dreams (EN), Schlechte Träume (DE)*.
<!-- cspell:enable -->

:   Ce sort permet au Rêveur de perturber le sommeil de toutes les unités non alliées (`HELP GUARD`) de la région à tel point qu'elles perdent temporairement une partie de leurs souvenirs.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau |              D               |
|:---:|:----------:|:----:|:------:|:----:|:------:|:----------------------------:|
|  I  |  90 aura   |  10  | Normal |  5   |        | :material-check:{ .success } |

`CAST [REGION x y] "Bad Dreams"`  

[](){ #m-ditation-id }

### Méditation

<!-- cspell:disable -->
*Meditate (EN), Meditation (DE)*.
<!-- cspell:enable -->

:   Avec l'aide de ce sort, le mage peut transférer sa propre aura dans un rapport de 2:1 à un autre mage de la même École de Magie.

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  G  |   2 aura   |  6   | Normal |  1   | :material-check:{ .success } |       |

`CAST Meditate <unit-id> <Aura>`  

[](){ #monstres-paisibles-id }

### Monstres paisibles

<!-- cspell:disable -->
*Calm Monster (EN), Monster friedlich stimmen (DE)*.
<!-- cspell:enable -->

:   Cette chanson mélodieuse peut apprivoiser presque n'importe quel monstre intelligent.  
    Il s'abstiendra d'attaquer le mage et ne touchera pas ses compagnons.  
    Mais ne vous y trompez pas, il restera toujours une créature imprévisible.

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  C  |  15 aura   |  6   | Normal |  5   | :material-check:{ .success } |       |

`CAST "Calm Monster" <unit-id>`  

[](){ #mort-mentale-id }

### Mort mentale

<!-- cspell:disable -->
*Mental Death (EN), Tod des Geistes (DE)*.
<!-- cspell:enable -->

:   Avec ce sort, le mage attaque directement l'esprit de ses adversaires.  
    Une explosion d'énergie astrale et électrique frappe les adversaires;  
    si la résistance magique est brisée, la victime perd définitivement une partie de ses souvenirs.  
    S'il est trop souvent victime de ce sort, il peut mourir.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  I  | 2 x N aura |  11  | Pré-c. |  5   |        |       |

`COMBATSPELL [LEVEL n] "Mental Death"`  

[](){ #moulin-paroles-id }

### Moulin à paroles

<!-- cspell:disable -->
*Blabbermouth (EN), Plappermaul (DE)*.
<!-- cspell:enable -->

:   L'unité enchantée commence à babiller sans complexe, vous indiquant quelles compétences elle peut exercer, quel type d'objets elle transporte avec elle et si elle est douée en magie, même quels sorts elle peut utiliser.  
    Malheureusement, ce sort n'affecte pas la mémoire et, rétrospectivement, elle se rendra compte qu'elle en a trop dit.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  C  |  10 aura   |  4   | Normal |  5   |        |       |

`CAST Blabbermouth <unit-id>`  

[](){ #mur-de-feu-id }

### Mur de feu

<!-- cspell:disable -->
*Firewall (EN), Feuerwand (DE)*.
<!-- cspell:enable -->

:   L'assistant crée un mur de feu dans la direction spécifiée.  
    Cela fait mal à tous ceux qui le traversent.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  D  | 6 x N aura |  7   | Normal |  4   |        |       |

`CAST [LEVEL n] Firewall <direction>`  

[](){ #murs-d-eternite-id }

### Murs d'éternité

<!-- cspell:disable -->
*Eternal Walls (EN), Mauern der Ewigkeit (DE)*.
<!-- cspell:enable -->

:   Avec cette formule, le mage lie pour toujours les forces de la terre dans les murs du bâtiment.  
    Un bâtiment ainsi enchanté est protégé contre les agressions du temps et ne nécessite plus aucun entretien.

| Éc. |        Composants         | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:-------------------------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  T  | 50 aura, 1 aura permanent |  7   | Normal |  5   | :material-check:{ .success } |       |

`CAST [LEVEL n] "Eternal Walls" <building-id>`  

## N

[](){ #nuage-de-la-mort-id }

### Nuage de la Mort

<!-- cspell:disable -->
*Death Cloud (EN), Todeswolke (DE)*.
<!-- cspell:enable -->

:   Avec un sombre rituel et en sacrifiant son propre sang, le mage noir invoque un grand esprit du plan élémentaire des poisons.  
    L'esprit se manifeste sous la forme d'un nuage vert vif au-dessus de la région et nuira à tous ceux qui entreront en contact avec lui.

| Éc. |   Composants   | Niv. |  Type  | Rang | Bateau |              D               |
|:---:|:--------------:|:----:|:------:|:----:|:------:|:----------------------------:|
|  D  | 40 aura, 15 PV |  11  | Normal |  5   |        | :material-check:{ .success } |

`CAST [REGION x y] "Death Cloud"`  

## O

[](){ #onde-de-choc-id }

### Onde de choc

<!-- cspell:disable -->
*Shockwave (EN), Schockwelle (DE)*.
<!-- cspell:enable -->

:   Ce sort provoque une vague de puissance pure qui déferle sur les rangs ennemis.  
    Le choc laissera de nombreux combattants tellement hébétés qu’ils seront incapables d’attaquer pendant un bref instant.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  T  |   N aura   |  5   | Combat |  5   |        |       |

`COMBATSPELL [LEVEL n] Shockwave`  

## P

[](){ #peau-d-corce-id }

### Peau d'écorce

<!-- cspell:disable -->
*Barkskin (EN), Rindenhaut (DE)*.
<!-- cspell:enable -->

:   Ce rituel, lancé avant la bataille, confère à vos troupes un bonus d'armure supplémentaire.  
    Chaque coup réduit la puissance du sort, le bouclier finira donc par se dissiper au cours du combat.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  G  | 4 x N aura |  12  | Pré-c. |  2   |        |       |

`COMBATSPELL [LEVEL n] "Barkskin"`  

[](){ #pentagramme-id }

### Pentagramme

<!-- cspell:disable -->
*Pentagram (EN), Pentagramm (DE)*.
<!-- cspell:enable -->

:   Exactement à minuit, lorsque les pouvoirs des ténèbres sont à leur maximum, un mage noir peut également utiliser ses pouvoirs pour supprimer les enchantements.  
Pour ce faire, il dessine un pentagramme sur l'objet enchanté et commence par une invocation aux seigneurs des ténèbres.  
Les messieurs l'aideront, mais sa réussite à résoudre le sort dépend uniquement de sa propre force.

| Éc. | Composants  | Niv. |  Type  | Rang |            Bateau            |              D               |
|:---:|:-----------:|:----:|:------:|:----:|:----------------------------:|:----------------------------:|
|  D  | 10 x N aura |  10  | Normal |  2   | :material-check:{ .success } | :material-check:{ .success } |

`CAST [REGION x y] [LEVEL n] Pentagram ( REGION | UNIT <unit-id> [<unit-id> ...] | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

[](){ #perturbation-de-l-astral-id }

### Perturbation de l'Astral

<!-- cspell:disable -->
*Astral Disruption (EN), Störe Astrale Integrität (DE)*.
<!-- cspell:enable -->

:   Ce sort provoque de graves perturbations dans l'Astral.  
    Dans un rayon Astral de régions de niveau 5, tous les êtres astraux qui ne peuvent pas résister au sort sont expulsés du plan Astral.  
    Le contact Astral avec toutes les régions affectées est perturbé pendant le niveau/3 semaines.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  T  |  140 aura  |  14  | Normal |  4   |        |       |

`CAST [LEVEL n] "Astral Disruption"`  

[](){ #petit-sacrifice-de-sang-id }

### Petit sacrifice de sang

<!-- cspell:disable -->
*Lesser Sacrifice (EN), Kleines Blutopfer (DE)*.
<!-- cspell:enable -->

:   Avec ce rituel, le mage peut sacrifier une partie de son énergie vitale afin d'acquérir un pouvoir magique.  
    Les mages rituels expérimentés rapportent que le rituel, une fois lancé, est difficile à contrôler et que la quantité de pouvoir gagnée varie considérablement.  
    Ainsi est-il écrit dans le « Livre du Sang » : « Qu'Il établisse donc le signe des quatre éléments dans le cercle de la création et de la décomposition et consacre chacun d'entre eux avec une goutte de sang.  
    Alors laissez-le aller au milieu des Quatre Éternels et laissez la vie passer pour que la force puisse naître. »

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  D  |   16 PV    |  4   | Normal |  1   | :material-check:{ .success } |       |

`CAST "Lesser Sacrifice"`  

[](){ #petites-mal-dictions-id }

### Petites malédictions

<!-- cspell:disable -->
*Minor Curses (EN), Kleine Flüche (DE)*.
<!-- cspell:enable -->

:   Dans les ruelles les plus sombres, ils existent, les malédictions et les sortilèges sont faits sur commande.  
    Mais bien entendu le disciple de Draig propose aussi des contre-sorts.  
    Que le fils du voisin soit entraîné dans un sortilège d'amour ou que le rival ait des boutons et des verrues, personne n'aime admettre qu'il a eu recours à de telles mesures.  
    Pour ce service, le mage gagne 50 silver par niveau.

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  D  |   N aura   |  1   | Normal |  5   | :material-check:{ .success } |       |

`CAST [LEVEL n] "Minor Curses"`  

[](){ #pierre-de-maison-id }

### Pierre de maison

<!-- cspell:disable -->
*Homestone (EN), Heimstein (DE)*.
<!-- cspell:enable -->

:   Avec cette formule, le mage lie à jamais les forces de la terre dans les murs du château dans lequel il se trouve actuellement.  
    Les murs ainsi renforcés ne peuvent être détruits ni par magie ni par l'artillerie lourde, et l'âge les affecte également moins.  
    Le bâtiment offre également une meilleure protection contre les attaques à l’épée et à la magie.

| Éc. |        Composants         | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:-------------------------:|:----:|:------:|:----:|:------:|:-----:|
|  G  | 50 aura, 1 aura permanent |  7   | Normal |  5   |        |       |

`CAST Homestone`  

[](){ #pluie-de-rouille-id }

### Pluie de rouille

<!-- cspell:disable -->
*Rain of Rust (EN), Rostregen (DE)*.
<!-- cspell:enable -->

:   Ce rituel évoque un sombre front de tempête qui domine de façon menaçante la région.  
    La pluie magique fera rouiller tout le minerai.  
    Les armes et armures en fer deviennent ébréchées et rouillées.  
    Le pouvoir destructeur de la pluie dépend de la puissance investie par le mage.  
    Jusqu'à 10 armes de fer peuvent être affectées pour chaque niveau.  
    Un anneau de pouvoir augmente l'effet comme un niveau supplémentaire.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau |              D               |
|:---:|:----------:|:----:|:------:|:----:|:------:|:----------------------------:|
|  G  | 2 x N aura |  3   | Normal |  5   |        | :material-check:{ .success } |

`CAST [REGION x y] [LEVEL n] "Rain of Rust" <unit-id> [<unit-id> ...]`  

[](){ #portail-du-chaos-id }

### Portail du Chaos

<!-- cspell:disable -->
*Chaos Gate (EN), Chaossog (DE)*.
<!-- cspell:enable -->

:   En sacrifiant 200 paysans, le mage du chaos peut ouvrir une porte vers le monde Astral.  
    Le portail peut être utilisé la semaine suivante, il se dissout à la fin de la semaine suivante.

| Éc. |      Composants       | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:---------------------:|:----:|:------:|:----:|:------:|:-----:|
|  D  | 150 aura, 200 paysans |  14  | Normal |  5   |        |       |

`CAST "Chaos Gate"`  

[](){ #portail-puissant-et-mur-robuste-id }

### Portail puissant et Mur robuste

<!-- cspell:disable -->
*Strong Wall And Sturdy Gate (EN), Starkes Tor und feste Mauer (DE)*.
<!-- cspell:enable -->

:   Avec cette formule, au début d'un combat, le mage lie des esprits élémentaires du rocher dans les murs du bâtiment dans lequel il se trouve actuellement.  
    Le bâtiment offre alors une meilleure protection contre les attaques à l'épée et à la magie.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  G  | 2 x N aura |  8   | Pré-c. |  5   |        |       |

`COMBATSPELL [LEVEL n] "Strong Wall And Sturdy Gate"`  

[](){ #pouvoirs-des-morts-id }

### Pouvoirs des morts

<!-- cspell:disable -->
*Animate Dead (EN), Mächte des Todes (DE)*.
<!-- cspell:enable -->

:   Le mage noir doit passer des nuits à errer dans les cimetières et cimetières de la région afin de pouvoir faire revivre les cadavres déterrés.  
    Les morts-vivants seront à son service, mais les non-informés doivent savoir qu'invoquer les forces de la mort peut être une arme à double tranchant.

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            |              D               |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:----------------------------:|
|  D  | 5 x N aura |  6   | Normal |  5   | :material-check:{ .success } | :material-check:{ .success } |

`CAST [REGION x y] [LEVEL n] "Animate Dead"`  

[](){ #pr-servation-du-butin-id }

### Préservation du butin

<!-- cspell:disable -->
*Save Spoils (EN), Beute Bewahren (DE)*.
<!-- cspell:enable -->

:   Ce sort empêche certains objets qui seraient normalement détruits au combat de subir des dommages.  
    Les pertes sont réduites de 5 % par niveau du sort, jusqu'à un minimum de 25 %.

| Éc. | Composants | Niv. |  Type   | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:-------:|:----:|:------:|:-----:|
|  T  |   N aura   |  3   | Post-c. |  5   |        |       |

`COMBATSPELL [LEVEL n] "Save Spoils"`  

[](){ #protection-contre-la-magie-id }

### Protection contre la magie

<!-- cspell:disable -->
*Protection from Magic (EN), Schutz vor Magie (DE)*.
<!-- cspell:enable -->

:   Ce sort place un champ d'antimagie autour des mages ennemis, gênant considérablement leur lancement de sorts.  
    Seuls quelques-uns auront la force de pénétrer sur le terrain et d’aider leurs troupes au combat.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  T  | 3 x N aura |  2   | Pré-c. |  2   |        |       |

`COMBATSPELL [LEVEL n] "Protection from Magic"`  

## R

[](){ #racines-de-la-magie-id }

### Racines de la magie

<!-- cspell:disable -->
*Roots of Magic (EN), Wurzeln der Magie (DE)*.
<!-- cspell:enable -->

:   À l'aide de ce rituel élaboré, le druide permet à une partie de son pouvoir de circuler en permanence dans les sols et les forêts de la région.  
    Cela modifiera à jamais l’équilibre naturel de la région et, à l’avenir, seules les majornas exigeantes mais fortes prospéreront dans la région.

| Éc. |                        Composants                        | Niv. |  Type  | Rang | Bateau |              D               |
|:---:|:--------------------------------------------------------:|:----:|:------:|:----:|:------:|:----------------------------:|
|  G  | 250 aura, 10 aura permanents, 1  [[pot-of-toadslime-fr]] |  16  | Normal |  5   |        | :material-check:{ .success } |

`CAST [REGION x y] "Roots of Magic"`  

[](){ #ralliement-des-foules-id }

### Ralliement des foules

<!-- cspell:disable -->
*Mob Rule (EN), Mob aufwiegeln (DE)*.
<!-- cspell:enable -->

:   À l'aide de ce chant magique, le mage convainc les agriculteurs de la région de le rejoindre.  
    Cependant, les agriculteurs ne quitteront pas leur pays et ne céderont aucun de leurs biens.  
    Chaque semaine, certains agriculteurs abandonneront également le charme et retourneront dans leurs champs.  
    Le nombre d’agriculteurs qui rejoignent le mage dépend de la puissance de sa chanson.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  C  | 4 x N aura |  10  | Normal |  5   |        |       |

`CAST [LEVEL n] "Mob Rule"`  

[](){ #regard-du-basilic-id }

### Regard du Basilic

<!-- cspell:disable -->
*Gaze of the Basilisk (EN), Blick des Basilisken (DE)*.
<!-- cspell:enable -->

:   Ce sort de combat difficile mais efficace utilise les esprits élémentaires de pierre pour transformer un certain nombre d'ennemis en pierre pendant toute la durée de la bataille.  
    Les personnes touchées ne combattront plus, mais elles ne pourront pas non plus être blessées.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  G  |   N aura   |  8   | Combat |  5   |        |       |

`COMBATSPELL [LEVEL n] "Gaze of the Basilisk"`  

[](){ #repos-ternel-id }

### Repos éternel

<!-- cspell:disable -->
*Eternal Rest (EN), Seelenfrieden (DE)*.
<!-- cspell:enable -->

:   Ce rituel magique apaise les âmes tourmentées de ceux qui sont morts violemment, leur permettant d'entamer leur dernier voyage vers les Autres Terres.  
    Environ 50 âmes trouveront la paix par niveau de sort.  
    Le sort ne peut pas racheter les morts-vivants déjà ressuscités car leurs liens avec ce monde sont trop forts.

| Éc. |                          Composants                           | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:-------------------------------------------------------------:|:----:|:------:|:----:|:------:|:-----:|
|  I  | 3 x N aura, 1 [eau de vie][eau-de-vie]{title="Water of life"} |  2   | Normal |  5   |        |       |

`CAST [LEVEL n] "Eternal Rest"`  

[](){ #spell-resistance-a-la-magie-id }

### Résistance à la magie

<!-- cspell:disable -->
*Resist Magic (EN), Schutzzauber (DE)*.
<!-- cspell:enable -->

:   Ce sort augmente votre résistance naturelle à la magie.  
    Une unité ainsi protégée est également moins vulnérable à la magie de combat.  
    Par niveau, le pouvoir du mage est suffisant pour protéger 5 personnes.

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  T  | 5 x N aura |  3   | Normal |  2   | :material-check:{ .success } |       |

`CAST [LEVEL n] Resist Magic <unit-id> [<unit-id> ...]`  

[](){ #r-surrection-id }

### Résurrection

<!-- cspell:disable -->
*Resurrection (EN), Wiederbelebung (DE)*.
<!-- cspell:enable -->

:   Si un guerrier meurt au combat, son âme commence le long voyage vers les étoiles.  
    À l'aide d'un rituel, un tisserand de rêves peut tenter de capturer l'âme et de la restituer dans le corps du défunt.  
    Bien que le sort ne soigne pas les blessures physiques, la personne soignée survivra au combat.

| Éc. | Composants | Niv. |  Type   | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:-------:|:----:|:------:|:-----:|
|  I  |   N aura   |  5   | Post-c. |  4   |        |       |

`COMBATSPELL [LEVEL n] Resurrection`  

[](){ #r-ve-de-magie-id }

### Rêve de magie

<!-- cspell:disable -->
*Dream of Magic (EN), Traum der Magie (DE)*.
<!-- cspell:enable -->

:   Avec l'aide de ce sort, le tisserand de rêves peut transférer sa propre aura à un autre tisserand de rêves dans un rapport de 2:1.

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  I  |   2 aura   |  3   | Normal |  1   | :material-check:{ .success } |       |

`CAST "Dream of Magic" <unit-id> <Aura>`  

[](){ #r-ve-id }

### Rêve
<!-- cspell:disable -->
*Dream (EN), Traumsenden (DE)*.
<!-- cspell:enable -->

:   Le mage envoie un rêve à la cible du sort.

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  I  |   N aura   |  1   | Normal |  5   | :material-check:{ .success } |       |

`CAST [LEVEL n] Dream <unit-id>`  

[](){ #rite-d-acceptation-id }

### Rite d'acceptation

<!-- cspell:disable -->
*Rite of Acceptance (EN), Ritual der Aufnahme (DE)*.
<!-- cspell:enable -->

:   Ce rituel permet d'incorporer n'importe quelle entité, quel que soit son type, dans sa propre faction.  
    Il le prouve en [**`CONTACTANT`**][cmd-contact-fr] le mage.  
    Il sera également exclusivement occupé aux préparatifs du rituel tout au long de la semaine.  
    Le rituel échouera s’il est trop fortement lié à son ancienne faction, par exemple s’il leur doit des services en échange de son éducation coûteuse.  
    Le mage menant le rituel doit naturellement dépenser de l'aura en permanence pour assurer la liaison permanente de l'initié à sa faction.  
    Il peut accueillir une personne par niveau et par aura permanente.

| Éc. |          Composants           | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:-----------------------------:|:----:|:------:|:----:|:------:|:-----:|
|  C  | 3 x N aura, N aura permanents |  9   | Normal |  5   |        |       |

`CAST [LEVEL n] "Rite of Acceptance" <unit-id>`  

[](){ #roche-vivante-id }

### Roche vivante

<!-- cspell:disable -->
*Living Rock (EN), Belebtes Gestein (DE)*.
<!-- cspell:enable -->

:   Ce rituel énergivore utilise une boule de laen concentré pour invoquer un énorme élémentaire de terre et le bannir dans un bâtiment.  
    L'élémentaire peut alors recevoir l'ordre de transporter le bâtiment et tous ses habitants vers une région voisine.  
    La force de l'élémentaire invoqué dépend de la compétence du mage : l'élémentaire peut faire au maximum (Niveau - 12) X Déplacer des bâtiments de taille 250.  
    Le bâtiment ne sortira pas indemne de cette procédure.

| Éc. |                            Composants                             | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:-----------------------------------------------------------------:|:----:|:------:|:----:|:------:|:-----:|
|  T  | 10 x N aura, 1 aura permanent, 5 [laen][laen-fr-id]{title="Laen"} |  13  | Normal |  5   |        |       |

`CAST [LEVEL n] "Living Rock" <building-id> <direction>`  

[](){ #runes-de-protection-id }

### Runes de protection

<!-- cspell:disable -->
*Protective Runes (EN), Runen des Schutzes (DE)*.
<!-- cspell:enable -->

:   Si vous dessinez ces runes sur les murs d’un bâtiment ou sur les planches d’un bateau, il sera plus difficile de les influencer par magie.  
    Chaque rituel augmente la résistance du bâtiment ou du bateau à l'enchantement de 20 %.  
    Si plusieurs sorts de protection sont superposés, leurs effets s'additionnent, mais une protection à 100 % ne peut pas être obtenue de cette façon.  
    Le sort dure au moins trois semaines, mais selon la compétence du mage, il peut durer beaucoup plus longtemps.

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  T  |  20 aura   |  8   | Normal |  2   | :material-check:{ .success } |       |

`CAST "Protective Runes" ( SHIP <ship-id> | CASTLE <building-id> )`  

## S

[](){ #sacrifier-la-force-id }

### Sacrifier la Force

<!-- cspell:disable -->
*Sacrifice Strength (EN), Opfere Kraft (DE)*.
<!-- cspell:enable -->

:   À l'aide de ce sort, le mage peut transférer définitivement une partie de son pouvoir magique à un autre mage.  
    Il peut transférer la moitié de la puissance utilisée à un mage de la même École de Magie, et un tiers à d'autres mages.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  T  |  100 aura  |  15  | Normal |  1   |        |       |

`CAST "Sacrifice Strength" <unit-id> <Aura>`  

[](){ #soif-de-sang-id }

### Soif de sang

<!-- cspell:disable -->
*Blood Frenzy (EN), Blutrausch (DE)*.
<!-- cspell:enable -->

:   Dans ce rituel sanglant, le mage sacrifie un nouveau-né devant son armée avant le combat.  
    Les esprits du sang ainsi invoqués prendront possession des soldats et les plongeront dans une soif de sang.

| Éc. |      Composants      | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:--------------------:|:----:|:------:|:----:|:------:|:-----:|
|  D  | 5 x N aura, 1 paysan |  5   | Pré-c. |  4   |        |       |

`COMBATSPELL [LEVEL n] "Blood Frenzy"`  

[](){ #sortie-de-l-astral-id }

### Sortie de l'Astral

<!-- cspell:disable -->
*Astral Exit (EN), Astraler Ausgang (DE)*.
<!-- cspell:enable -->

:   Le mage se concentre sur la structure de la réalité et peut ainsi quitter le plan Astral.  
    Il peut globalement (Niveau-3)*Envoyer 15 lbs par la porte brièvement créée.  
    Si le mage est suffisamment expérimenté pour lancer le sort aux niveaux 11 ou plus, il peut forcer d'autres unités à passer à l'autre niveau, même contre leur gré.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  T  | 2 x N aura |  4   | Normal |  7   |        |       |

`CAST [LEVEL n] "Astral Exit" <x> <y> <unit-id> [<unit-id> ...]`  

## T

[](){ #terre-sacr-e-id }

### Terre Sacrée

<!-- cspell:disable -->
*Sacred Ground (EN), Heiliger Boden (DE)*.
<!-- cspell:enable -->

:   Ce rituel convoque divers esprits de la nature dans le sol de la région, qui le gardent désormais.  
    Dans une région aussi bénie, les morts ne quitteront plus jamais leurs tombes, et les morts-vivants apparus ailleurs les éviteront autant que possible.

| Éc. |         Composants         | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:--------------------------:|:----:|:------:|:----:|:------:|:-----:|
|  G  | 80 aura, 3 aura permanents |  9   | Normal |  5   |        |       |

`CAST "Sacred Ground"`  

[](){ #tourbillon-id }

### Tourbillon

<!-- cspell:disable -->
*Whirlwind (EN), Wirbelwind (DE)*.
<!-- cspell:enable -->

:   Cette incantation ouvre une porte vers le plan des esprits élémentaires du vent.  
    Des vents violents, voire des tempêtes, se lèvent immédiatement dans la zone autour de la porte et gênent tous les archers dans la bataille.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  G  |  15 aura   |  5   | Pré-c. |  5   |        |       |

`COMBATSPELL [LEVEL n] Whirlwind`  

[](){ #transfert-d-aura-id }

### Transfert d'aura

<!-- cspell:disable -->
*Transfer Aura (EN), Auratransfer (DE)*.
<!-- cspell:enable -->

:   À l'aide de ce sort, le mage peut transférer sa propre aura à un autre mage de la même École de Magie dans un rapport de 2:1 ou à un mage d'une autre École de Magie dans un rapport de 3:1.

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  T  |   1 aura   |  5   | Normal |  1   | :material-check:{ .success } |       |

`CAST "Transfer aura" <unit-id> <Aura>`  

[](){ #transfert-de-pouvoir-id }

### Transfert de pouvoir

<!-- cspell:disable -->
*Transfer Power (EN), Machtübertragung (DE)*.
<!-- cspell:enable -->

:   Avec l'aide de ce sort, le mage peut transférer sa propre aura dans un rapport de 2:1 à un autre mage de la même École de Magie.

| Éc. | Composants | Niv. |  Type  | Rang |            Bateau            | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:----------------------------:|:-----:|
|  D  |   2 aura   |  7   | Normal |  1   | :material-check:{ .success } |       |

`CAST "Transfer Power" <unit-id> <Aura>`  

## V

[](){ #vents-de-rouille-id }

### Vents de rouille

<!-- cspell:disable -->
*Winds of Rust (EN), Rosthauch (DE)*.
<!-- cspell:enable -->

:   Ce rituel évoque un sombre front de tempête qui domine de façon menaçante la région.  
    La pluie magique fera rouiller tout le minerai, détruisant de nombreuses armes ennemies.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  D  | 2 x N aura |  6   | Combat |  5   |        |       |

`COMBATSPELL [LEVEL n] "Winds of Rust"`  

[](){ #voie-de-l-astral-id }

### Voie de l'Astral

<!-- cspell:disable -->
*Astral Path (EN), Astraler Weg (DE)*.
<!-- cspell:enable -->

:   D'anciennes formules arcaniques permettent au mage de s'envoyer lui-même et les autres dans le plan Astral.  
    Le mage peut envoyer 15 lbs par la porte brièvement créée.  
    Si le mage est suffisamment expérimenté pour lancer le sort aux niveaux 11 ou plus, il peut forcer d'autres unités à passer à l'autre niveau, même contre leur gré.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  T  | 2 x N aura |  4   | Normal |  7   |        |       |

`CAST [LEVEL n] "Astral Path" <unit-id> [<unit-id> ...]`  

[](){ #voie-des-arbres-id }

### Voie des Arbres

<!-- cspell:disable -->
*Path of Trees (EN), Weg der Bäume (DE)*.
<!-- cspell:enable -->

:   Un grand pouvoir réside dans les endroits où la vie palpite.  
    Le druide peut collecter ce pouvoir et créer une passerelle vers le monde des êtres spirituels.  
    Le druide peut alors niveau*Envoyer 5 unités de poids à travers la porte.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau | Dist. |
|:---:|:----------:|:----:|:------:|:----:|:------:|:-----:|
|  G  | 3 x N aura |  9   | Normal |  7   |        |       |

`CAST [LEVEL n] "Path of Trees" <unit-id> [<unit-id> ...]`  

[](){ #voie-magique-id }

### Voie magique

<!-- cspell:disable -->
*Magic Path (EN), Magischer Pfad (DE)*.
<!-- cspell:enable -->

:   En accomplissant ces rituels, le mage est capable d'invoquer un puissant élémentaire de terre.  
    Tant que celle-ci sera bannie dans le sol, aucune pluie ne adoucira les sentiers et aucune rivière ne pourra détruire les ponts.  
    Cela signifie que tous les voyageurs bénéficient des mêmes avantages qui, autrement, ne seraient offerts que par un réseau routier asphalté développé.  
    Même les marécages et les glaciers peuvent être enchantés de cette façon. Plus le mage met de puissance dans le sort, plus le chemin dure longtemps.

| Éc. |                    Composants                     | Niv. |  Type  | Rang |            Bateau            |              D               |
|:---:|:-------------------------------------------------:|:----:|:------:|:----:|:----------------------------:|:----------------------------:|
|  G  | N aura, 1 [pierre][pierre]{title="Stone"}, 1 bois |  4   | Normal |  5   | :material-check:{ .success } | :material-check:{ .success } |

`CAST [REGION x y] [LEVEL n] "Magic Path"`  

[](){ #vol-d-aura-id }

### Vol d'aura

<!-- cspell:disable -->
*Steal Aura (EN), Stehle Aura (DE)*.
<!-- cspell:enable -->

:   Avec l'aide de ce sort, le mage peut retirer son aura à un autre mage contre son gré et se la fournir.

| Éc. | Composants | Niv. |  Type  | Rang | Bateau |              D               |
|:---:|:----------:|:----:|:------:|:----:|:------:|:----------------------------:|
|  T  | 2 x N aura |  6   | Normal |  3   |        | :material-check:{ .success } |

`CAST [REGION x y] [LEVEL n] "Steal Aura" <unit-id>`  

## Voir aussi

- [[list-of-spells]]

[^1]: toutes les Écoles de Magie permettent de lancer le sort
[^2]: le niveau du sort varie selon l'École de Magie. C : 9, D : 13, G : 10, I : 10, T : 12
[^3]: le sort peut être lancé **en mer**.

<!-- From [https://wiki.eressea.de/index.php?title=Zauberbeschreibungen\_E2&oldid=9278] -->

[cmd-contact-fr]: [[cmd-contact-fr]]
