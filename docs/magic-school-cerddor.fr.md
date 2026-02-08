---
# cSpell:locale fr
alias: sorts-cerddor
---
# Sorts Cerddor

Les sorts de l'École de magie **Cerddor** sont décrits ci-dessous par ordre de niveau croissant.  

*Note : Dans les descriptions ci-dessous N représente le niveau spécifié sur les ordres [[cmd-cast]] ou [[cmd-combatspell]] lancés.*

## Niveau 1

### Chant apaisant

<!-- cspell:disable -->
*Appeasing Song (EN), Friedenslied (DE)*.
<!-- cspell:enable -->

:   Cette chanson apprivoise même l'orque le plus sauvage et le rend paisible et doux.  
    Toute idée de nuire au chanteur disparaîtra.  
    Le mage peut se déplacer sans encombre dans une région voisine.

| Composants | Niv. |  Type  | Rang | B | D |
|:----------:|:----:|:------:|:----:|:-:|:-:|
|   2 aura   |  1   | Pré-c. |  5   |   |   |

`COMBATSPELL [LEVEL n] "Appeasing Song"`  

### Jonglerie

<!-- cspell:disable -->
*Jugglery (EN), Gaukeleien (DE)*.
<!-- cspell:enable -->

:   Les mages Cerddor sont les principaux jongleurs parmi les mages, ils aiment divertir les gens et être le centre d'attention.  
    Même les débutants apprennent les petits trucs et tours de magie qui peuvent être utilisés pour attirer et séduire les gens et leur faire ouvrir très grand leur portefeuille,  
    et à la fin de la semaine, le jongleur aura gagné 50 silver par niveau.

| Composants | Niv. |  Type  | Rang |              B               | D |
|:----------:|:----:|:------:|:----:|:----------------------------:|:-:|
|   N aura   |  1   | Normal |  5   | :material-check:{ .success } |   |

`CAST [LEVEL n] Jugglery`  

## Niveau 2

### Chant de générosité

<!-- cspell:disable -->
*Song of Generosity (EN), Hohes Lied der Gaukelei (DE)*.
<!-- cspell:enable -->

:   Cette chanson joyeuse se répandra comme une rumeur dans toute la région et mettra le monde entier dans une ambiance de fête.  
    Les tavernes et les théâtres seront partout pleins et même les mendiants seront nourris.

| Composants | Niv. |  Type  | Rang |              B               |              D               |
|:----------:|:----:|:------:|:----:|:----------------------------:|:----------------------------:|
| 2 x N aura |  2   | Normal |  5   | :material-check:{ .success } | :material-check:{ .success } |

`CAST [REGION x y] [LEVEL n] "Song of Generosity"`  

### Chant de guérison

<!-- cspell:disable -->
*Song of Healing (EN), Lied der Heilung (DE)*.
<!-- cspell:enable -->

:   Il n'y a pas que le médecin qui peut aider les blessés au combat.  
    Les bardes connaissent diverses chansons qui soutiennent les pouvoirs d'auto-guérison du corps.  
    Ce chant peut refermer des blessures, réparer des os brisés et régénérer même des membres sectionnés.

| Composants | Niv. |  Type   | Rang | B | D |
|:----------:|:----:|:-------:|:----:|:-:|:-:|
|   N aura   |  2   | Post-c. |  5   |   |   |

`COMBATSPELL [LEVEL n] "Song of Healing"`  

## Niveau 3

### Chant de terreur

<!-- cspell:disable -->
*Song of Terror (EN), Gesang der Furcht (DE)*.
<!-- cspell:enable -->

:   Une chanson très puissante issue des traditions des chats qui pénètre profondément dans le cœur des ennemis et leur prive de courage et d'espoir.  
    La peur les fera trembler et la panique dominera leurs pensées.  
    Pleins de peur, ils tenteront d’échapper aux chants horribles et de s’enfuir.

| Composants | Niv. |  Type  | Rang | B | D |
|:----------:|:----:|:------:|:----:|:-:|:-:|
|   N aura   |  3   | Combat |  5   |   |   |

`COMBATSPELL [LEVEL n] "Song of Terror"`  

### Danse de la pluie

<!-- cspell:disable -->
*Rain Dance (EN), Regentanz (DE)*.
<!-- cspell:enable -->

:   Cet ancien rituel de danse invoque les forces de vie et de fertilité.  
    Les rendements des agriculteurs seront nettement meilleurs pendant plusieurs semaines.

| Composants | Niv. |  Type  | Rang |              B               |              D               |
|:----------:|:----:|:------:|:----:|:----------------------------:|:----------------------------:|
|   N aura   |  3   | Normal |  5   | :material-check:{ .success } | :material-check:{ .success } |

`CAST [REGION x y] [LEVEL n] Rain Dance`  

## Niveau 4

### Chant de confusion

<!-- cspell:disable -->
*Song of Confusion (EN), Gesang der Verwirrung (DE)*.
<!-- cspell:enable -->

:   Ce chant magique est issu des anciens chants des chats et, utilisé avant un combat, peut apporter des avantages stratégiques décisifs.  
    Quiconque est sous l'influence de cette chanson ne prêtera pas attention à la mélodie de son environnement, son esprit deviendra confus et cédera de manière erratique à des inspirations soudaines.  
    On dit que des armées bien ordonnées ont soudainement trouvé leurs archers loin devant et leur cavalerie jouant aux cartes avec les gardes du camp (ou leur chef dormant dans le camp abandonné depuis longtemps, comme cela se serait effectivement produit lors des grandes guerres de l'Ancien Monde).

| Composants | Niv. |  Type  | Rang | B | D |
|:----------:|:----:|:------:|:----:|:-:|:-:|
| 2 x N aura |  4   | Pré-c. |  5   |   |   |

`COMBATSPELL [LEVEL n] "Song of Confusion"`  

### Chant de cour

<!-- cspell:disable -->
*Song of Courting (EN), Gesang des Werbens (DE)*.
<!-- cspell:enable -->

:   Extrait « Des Chants des Anciens » de Firudin le Sage :  
    « Cette petite mélodie séduisante et quelques mots insinuants vainquent en un instant la méfiance des paysans.  
    Ils vous rejoindront avec enthousiasme et laisseront eux-mêmes leur maison et leur cour en ruines. »

| Composants | Niv. |  Type  | Rang | B | D |
|:----------:|:----:|:------:|:----:|:-:|:-:|
| 2 x N aura |  4   | Normal |  5   |   |   |

`CAST [LEVEL n] "Song of Courting"`  

### Moulin à paroles

<!-- cspell:disable -->
*Blabbermouth (EN), Plappermaul (DE)*.
<!-- cspell:enable -->

:   L'unité enchantée commence à babiller sans complexe, vous indiquant quelles compétences elle peut exercer, quel type d'objets elle transporte avec elle et si elle est douée en magie, même quels sorts elle peut utiliser.  
    Malheureusement, ce sort n'affecte pas la mémoire et, rétrospectivement, elle se rendra compte qu'elle en a trop dit.

| Composants | Niv. |  Type  | Rang | B | D |
|:----------:|:----:|:------:|:----:|:-:|:-:|
|  10 aura   |  4   | Normal |  5   |   |   |

`CAST "Blabbermouth" <unit-id>`  

## Niveau 5

### Chant de contre

<!-- cspell:disable -->
*Countersong (EN), Bannlied (DE)*.
<!-- cspell:enable -->

:   Ce chant strident résonne sur tout le champ de bataille.  
    Les dissonances particulières des mélodies rendent presque impossible aux mages de se concentrer sur leurs sorts.

| Composants | Niv. |  Type  | Rang | B | D |
|:----------:|:----:|:------:|:----:|:-:|:-:|
| 5 x N aura |  5   | Pré-c. |  2   |   |   |

`COMBATSPELL [LEVEL n] "Countersong"`  

### Hymne du partage d'aura

<!-- cspell:disable -->
*Hymn of Aura Sharing (EN), Gesang des Auratransfers (DE)*.
<!-- cspell:enable -->

:   Avec l'aide de ce sort, le mage peut transférer sa propre aura dans un rapport de 2:1 à un autre mage de la même École de Magie.
<!-- TODO: check values below -->
| Composants | Niv. |  Type  | Rang |              B               | D |
|:----------:|:----:|:------:|:----:|:----------------------------:|:-:|
|   2 aura   |  5   | Normal |  1   | :material-check:{ .success } |   |

`CAST "Hymn of Aura Sharing" <unit-id> <Aura>`  

### Analyse du chant de la Vie

<!-- cspell:disable -->
*Analyze Song of Life (EN), Gesang des Lebens analysieren (DE)*.
<!-- cspell:enable -->

:   Tous les êtres vivants ont leur propre chant de vie.  
    Il n’y a pas deux chansons identiques, même si toutes les chansons du même type sont similaires.  
    Chaque sort modifie ce chant d'une manière ou d'une autre et se révèle ainsi.  
    Ce chant aide à entendre les changements dans le chant de la vie d'une personne qui sont de nature magique.  
    Vous pourrez déchiffrer et démasquer tous les enchantements qui ne sont pas plus masqués que vos capacités.

| Composants | Niv. |  Type  | Rang |              B               | D |
|:----------:|:----:|:------:|:----:|:----------------------------:|:-:|
|  10 aura   |  5   | Normal |  5   | :material-check:{ .success } |   |

`CAST "Analyze Song of Life" <unit-id>`  

### Chant des héros

<!-- cspell:disable -->
*Epic Heroes (EN), Heldengesang (DE)*.
<!-- cspell:enable -->

:   Cet ancien chant de bataille remonte le moral de vos troupes et les aide également à résister à l'aura effrayante des êtres démoniaques et morts-vivants.  
Un guerrier aussi solide ne fuira pas même dans des situations difficiles et son comportement réfléchi lui donnera de nombreux avantages en défense.

| Composants | Niv. |  Type  | Rang | B | D |
|:----------:|:----:|:------:|:----:|:-:|:-:|
| 2 x N aura |  5   | Pré-c. |  4   |   |   |

`COMBATSPELL [LEVEL n] "Epic Heroes"`  

## Niveau 6

### Créer une [[amulette-de-vision-decuplee]]{title="Amulet of True Sight"}

<!-- cspell:disable -->
*Create An Amulet of True Sight (EN), Erschaffe ein Amulett des wahren Sehens (DE)*.
<!-- cspell:enable -->

:   Le sort permet à un mage de créer une [amulette de vision décuplée].
    L'amulette permet au porteur de voir toutes les unités protégées par un [[anneau-d-invisibilite]].  
    Cependant, les unités qui utilisent leur compétence de [camouflage] pour se cacher ne sont toujours pas détectées.

|               Composants                | Niv. |  Type  | Rang |              B               | D |
|:---------------------------------------:|:----:|:------:|:----:|:----------------------------:|:-:|
| 50 aura, 3 000 silver, 1 aura permanent |  6   | Normal |  5   | :material-check:{ .success } |   |

`CAST "Create An Amulet of True Sight"`  

### Créer un [anneau d'Invisibilité]

<!-- cspell:disable -->
*Create A Ring of Invisibility (EN), Erschaffe einen Ring der Unsichtbarkeit (DE)*.
<!-- cspell:enable -->

:   Avec ce sort, le mage peut créer un [[anneau-d-invisibilite]].  
    Le porteur de l'anneau devient invisible pour toutes les unités des autres partis, quelle que soit la qualité de leur perception.  
    Dans une unité invisible, chaque personne doit porter une bague.  

|               Composants                | Niv. |  Type  | Rang |              B               | D |
|:---------------------------------------:|:----:|:------:|:----:|:----------------------------:|:-:|
| 50 aura, 3 000 silver, 1 aura permanent |  6   | Normal |  5   | :material-check:{ .success } |   |

`CAST "Create A Ring of Invisibility"`  

### Chant de séduction

<!-- cspell:disable -->
*Song of Seduction (EN), Lied der Verführung (DE)*.
<!-- cspell:enable -->

:   Cette chanson peut être utilisée pour charmer une unité afin qu'elle donne la plupart de son argent et de ses biens au barde.  
    Cependant, elle garde toujours ce dont elle a besoin pour survivre.

| Composants | Niv. |  Type  | Rang | B | D |
|:----------:|:----:|:------:|:----:|:-:|:-:|
|  12 aura   |  6   | Normal |  5   |   |   |

`CAST "Song of Seduction" <unit-id>`  

### Monstres paisibles

<!-- cspell:disable -->
*Calm Monster (EN), Monster friedlich stimmen (DE)*.
<!-- cspell:enable -->

:   Cette chanson mélodieuse peut apprivoiser presque n'importe quel monstre intelligent.  
    Il s'abstiendra d'attaquer le mage et ne touchera pas ses compagnons.  
    Mais ne vous y trompez pas, il restera toujours une créature imprévisible.

| Composants | Niv. |  Type  | Rang |              B               | D |
|:----------:|:----:|:------:|:----:|:----------------------------:|:-:|
|  15 aura   |  6   | Normal |  5   | :material-check:{ .success } |   |

`CAST "Calm Monster" <unit-id>`  

## Niveau 7

### Écoute clandestine

<!-- cspell:disable -->
*Sound out (EN), Aushorchen (DE)*.
<!-- cspell:enable -->

:   Si l'unité succombe au sort, elle dira au mage tout ce qu'elle sait sur la région en question.  
    S’il n’y a personne de son parti dans la région, elle n’a rien à signaler.  
    Elle ne peut également dire que ce qu'elle a pu voir elle-même.

|     Composants     | Niv. |  Type  | Rang | B | D |
|:------------------:|:----:|:------:|:----:|:-:|:-:|
| 4 aura, 100 silver |  7   | Normal |  5   |   |   |

`CAST "Sound out" <unit-id> <x> <y>`  

### Chant de guerre

<!-- cspell:disable -->
*Song of War (EN), Kriegsgesang (DE)*.
<!-- cspell:enable -->

:   Comme beaucoup de chansons magiques, celle-ci vient également de la connaissance ancienne des chats, qui connaissent depuis toujours les puissants effets de la voix.  
    Cette chanson attise l'humeur des guerriers, les plongeant même dans une frénésie sauvage et une soif de sang.  
    Indépendamment de leur propre souffrance, ils se battront jusqu’à la mort et ne fuiront jamais.  
    Alors que leur attaque s’intensifie, ils ne prêtent que peu d’attention à eux-mêmes.

| Composants | Niv. |  Type  | Rang | B | D |
|:----------:|:----:|:------:|:----:|:-:|:-:|
| 5 x N aura |  7   | Pré-c. |  4   |   |   |

`COMBATSPELL [LEVEL n] "Song of War"`  

### Gueule de bois

<!-- cspell:disable -->
*Hangover (EN), Schaler Wein (DE)*.
<!-- cspell:enable -->

<!-- TODO: trématode à nœuds ??? c'est quoi ? -->
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

|               Composants                | Niv. |  Type  | Rang | B | D |
|:---------------------------------------:|:----:|:------:|:----:|:-:|:-:|
| 28 aura, 3 [racines de nœud], 50 silver |  7   | Normal |  5   |   |   |

`CAST "Hangover" <unit-id>`  

## Niveau 8

### Chant d'effroi

<!-- cspell:disable -->
*Song of Fear (EN), Gesang der Angst (DE)*.
<!-- cspell:enable -->

:   Ce chant de guerre sème la panique sur les lignes de front ennemies et affaiblit ainsi considérablement leur force de combat.  
    La peur affaiblira leur bras d’épée et la peur paralysera leur bras de bouclier.

| Composants | Niv. |  Type  | Rang | B | D |
|:----------:|:----:|:------:|:----:|:-:|:-:|
| 5 x N aura |  8   | Pré-c. |  5   |   |   |

`COMBATSPELL [LEVEL n] "Song of Fear"`  

### Dissonance du silence

<!-- cspell:disable -->
*Silence Dissonance (EN), Lebenslied festigen (DE)*.
<!-- cspell:enable -->

:   Chaque enchantement affecte le Chant de Vie, l'affaiblissant et le déformant.  
    Le barde expérimenté peut tenter de capturer et d’amplifier le chant de la vie et d’effacer les changements du chant.

| Composants | Niv. |  Type  | Rang |              B               |              D               |
|:----------:|:----:|:------:|:----:|:----------------------------:|:----------------------------:|
| 5 x N aura |  8   | Normal |  2   | :material-check:{ .success } | :material-check:{ .success } |

`CAST [REGION x y] [LEVEL n] "Silence Dissonance" ( REGION | UNIT <unit-id> [<unit-id> ...] | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

### Analyses

<!-- cspell:disable -->
*Analysis (EN), Lied des Ortes analysieren (DE)*.
<!-- cspell:enable -->

:   Comme les êtres vivants, les bateaux, les bâtiments et même les régions ont leur propre chant, bien que beaucoup plus faible et plus difficile à entendre.  
    Et tout comme le chant de la vie d'une personne permet de savoir si elle est sous le charme, cela est également possible pour les châteaux, les bateaux ou les régions.

| Composants | Niv. |  Type  | Rang |              B               | D |
|:----------:|:----:|:------:|:----:|:----------------------------:|:-:|
| 3 x N aura |  8   | Normal |  5   | :material-check:{ .success } |   |

`CAST [LEVEL n] "Analysis" ( REGION | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

## Niveau 9

### Ritual der Aufnahme

<!-- cspell:disable -->
*(EN), Ritual der Aufnahme (DE)*.
<!-- cspell:enable -->

:   Ce rituel permet d'incorporer n'importe quelle entité, quel que soit son type, dans sa propre faction.  
    Il le prouve en [[cmd-contact|**`CONTACTANT`**]] le mage.  
    Il sera également exclusivement occupé aux préparatifs du rituel tout au long de la semaine.  
    Le rituel échouera s’il est trop fortement lié à son ancienne faction, par exemple s’il leur doit des services en échange de son éducation coûteuse.  
    Le mage menant le rituel doit naturellement dépenser de l'aura en permanence pour assurer la liaison permanente de l'initié à son groupe.  
    Il peut accueillir une personne par niveau et par aura permanente.

|          Composants           | Niv. |  Type  | Rang | B | D |
|:-----------------------------:|:----:|:------:|:----:|:-:|:-:|
| 3 x N aura, N aura permanents |  9   | Normal |  5   |   |   |

`CAST [LEVEL n] "Ritual der Aufnahme" <unit-id>`  

### Invocation du Familier

<!-- cspell:disable -->
*Summon Familiar (EN), Vertrauten rufen (DE)*.
<!-- cspell:enable -->

:   À un moment donné de ses pérégrinations, un mage expérimenté rencontrera un spécimen inhabituel d'une espèce qui rejoindra le mage.

|         Composants          | Niv. |  Type  | Rang | B | D |
|:---------------------------:|:----:|:------:|:----:|:-:|:-:|
| 100 aura, 5 aura permanents |  9   | Normal |  5   |   |   |

`CAST "Summon Familiar"`  

## Niveau 10

### Gesang des wachen Geistes

<!-- cspell:disable -->
*(EN), Gesang des wachen Geistes (DE)*.
<!-- cspell:enable -->

:   Ce chant magique, autrefois chanté avec ferveur, va se répandre dans toute la région, sauter de bouche en bouche et se faire entendre partout pendant un moment.  
    Le nombre de semaines pendant lesquelles la chanson disparaît de la mémoire de la région dépend de l'habileté du barde.  
    Jusqu'à ce que la chanson disparaisse complètement, sa magie accordera à tous les alliés du barde (`HELP GUARD`), et bien sûr à son propre peuple, un bonus unique de 15 % à la résistance naturelle à un enchantement.

| Composants | Niv. |  Type  | Rang | B |              D               |
|:----------:|:----:|:------:|:----:|:-:|:----------------------------:|
| 2 x N aura |  10  | Normal |  2   |   | :material-check:{ .success } |

`CAST [REGION x y] [LEVEL n] "Gesang des wachen Geistes"`  

### Mob aufwiegeln

<!-- cspell:disable -->
*(EN), Mob aufwiegeln (DE)*.
<!-- cspell:enable -->

:   À l'aide de ce chant magique, le mage convainc les agriculteurs de la région de le rejoindre.  
    Cependant, les agriculteurs ne quitteront pas leur pays et ne céderont aucun de leurs biens.  
    Chaque semaine, certains agriculteurs abandonneront également le charme et retourneront dans leurs champs.  
    Le nombre d’agriculteurs qui rejoignent le mage dépend de la puissance de sa chanson.

| Composants | Niv. |  Type  | Rang | B | D |
|:----------:|:----:|:------:|:----:|:-:|:-:|
| 4 x N aura |  10  | Normal |  5   |   |   |

`CAST [LEVEL n] "Mob aufwiegeln"`  

## Niveau 11

### Gesang der Melancholie

<!-- cspell:disable -->
*(EN), Gesang der Melancholie (DE)*.
<!-- cspell:enable -->

:   Avec cette chanson, le barde répand une ambiance mélancolique et triste parmi les agriculteurs.  
    Pendant quelques semaines, ils se retireront dans leurs huttes et ne laisseront aucune argenterie dans les théâtres et les tavernes.

| Composants | Niv. |  Type  | Rang | B |              D               |
|:----------:|:----:|:------:|:----:|:-:|:----------------------------:|
|  40 aura   |  11  | Normal |  5   |   | :material-check:{ .success } |

`CAST [REGION x y] "Gesang der Melancholie"`  

### Miriams flinke Finger

<!-- cspell:disable -->
*(EN), Miriams flinke Finger (DE)*.
<!-- cspell:enable -->

:   La célèbre barde Miriam Bhean'Meddaf était connue pour son extraordinaire talent avec la harpe.  
    On disait que ses doigts se déplaçaient si rapidement sur les cordes qu'ils étaient pratiquement méconnaissables.  
    Ce sort, assez simple à lancer dans une bague en argent, permet de décupler la dextérité et l'agilité des doigts.  
    On dit qu’elle a également exploité cela ailleurs ; sa réputation de tricheuse de cartes était notoire.  
    Les artisans peuvent ainsi produire dix fois plus, ce qui pourrait également être utile dans d'autres activités.

|               Composants                | Niv. |  Type  | Rang |              B               | D |
|:---------------------------------------:|:----:|:------:|:----:|:----------------------------:|:-:|
| 20 aura, 1 000 silver, 1 aura permanent |  11  | Normal |  5   | :material-check:{ .success } |   |

`CAST "Miriams flinke Finger"`  

## Niveau 12

### Gesang der Friedfertigkeit

:   Ce sort puissant empêche toute attaque.  
    Personne dans toute la région n’est capable de prendre les armes contre qui que ce soit.  
    Les effets peuvent durer plusieurs semaines.

| Composants  | Niv. |  Type  | Rang | B | D |
|:-----------:|:----:|:------:|:----:|:-:|:-:|
| 20 x N aura |  12  | Normal |  5   |   |   |

`CAST [LEVEL n] "Gesang der Friedfertigkeit"`  

### Gesang des schwachen Geistes

<!-- cspell:disable -->
*(EN), Gesang des schwachen Geistes (DE)*.
<!-- cspell:enable -->

:   Tissée dans l'essence magique de la région, cette chanson affaiblit une fois la résistance naturelle à un enchantement de 15 %.  
    Seuls les alliés du barde (`HELP GUARD`) sont immunisés contre l'effet de la chanson.

| Composants | Niv. |  Type  | Rang | B |              D               |
|:----------:|:----:|:------:|:----:|:-:|:----------------------------:|
| 2 x N aura |  12  | Normal |  2   |   | :material-check:{ .success } |

`CAST [REGION x y] [LEVEL n] "Gesang des schwachen Geistes"`  

## Niveau 13

### Gesang der Versklavung

<!-- cspell:disable -->
*(EN), Gesang der Versklavung (DE)*.
<!-- cspell:enable -->

:   Ce puissant sort prive la victime de son libre arbitre et la soumet aux ordres du barde.  
    Pendant un certain temps, la victime se détournera complètement des siens et aura le sentiment d'appartenir à la faction du barde.

| Composants | Niv. |  Type  | Rang | B | D |
|:----------:|:----:|:------:|:----:|:-:|:-:|
|  40 aura   |  13  | Normal |  5   |   |   |

`CAST "Gesang der Versklavung" <unit-id>`  

## Niveau 14

### Hohe Kunst der Überzeugung

<!-- cspell:disable -->
*(EN), Hohe Kunst der Überzeugung (DE)*.
<!-- cspell:enable -->

<div class="lore-dialogue">
"À Weilersweide, près du port de Wythar, se trouve une petite auberge rarement visitée.
Nul ne sait que, jusqu'à il y a quelques années, cette ferme était la demeure du prédicateur itinérant Grauwolf. banni depuis.
Après avoir rallié à sa cause la quasi-totalité des paysans lors d'un de ses discours enflammés, il fut condamné pour sédition et exilé.
Il accepta de me révéler, à contrecœur, le secret de son éloquence."
</di>

Extrait de « Errants » de Firudin le Sage.  

| Composants  | Niv. |  Type  | Rang | B | D |
|:-----------:|:----:|:------:|:----:|:-:|:-:|
| 20 x N aura |  14  | Normal |  5   |   |   |

`CAST [LEVEL n] "Hohe Kunst der Überzeugung"`  

## Niveau 15

### Aufruhr beschwichtigen

:   À l’aide de ce chant magique, le mage peut calmer une région en ébullition.  
    Les hordes d'agriculteurs vont se perdre et retourner dans leurs champs.

| Composants | Niv. |  Type  | Rang | B |              D               |
|:----------:|:----:|:------:|:----:|:-:|:----------------------------:|
|  30 aura   |  15  | Normal |  5   |   | :material-check:{ .success } |

`CAST [REGION x y] "Aufruhr beschwichtigen"`  

## Niveau 16

### Aufruhr verursachen

:   À l’aide de ce chant magique, le mage met toute une région en ébullition.  
    Des hordes d’agriculteurs rebelles rendent toute taxation impossible, presque plus personne ne donne d’argent à des escroqueries et aucune nouvelle personne ne peut être recrutée.  
    Après quelques semaines, la foule se calme à nouveau.

| Composants | Niv. |  Type  | Rang | B |              D               |
|:----------:|:----:|:------:|:----:|:-:|:----------------------------:|
|  40 aura   |  16  | Normal |  5   |   | :material-check:{ .success } |

`CAST [REGION x y] "Aufruhr verursachen"`  

<!-- From [https://wiki.eressea.de/index.php?title=Cerddorzauber&oldid=7018] -->

[amulette de vision décuplée]: ./amulet-of-true-sight.md "Amulet of True Sight"
[camouflage]: ./camouflage.md "Stealth"
[anneau d'Invisibilité]: ./ring-of-invisibility.md "Ring of Invisibility"
