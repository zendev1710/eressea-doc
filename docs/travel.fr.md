---
# cSpell:locale fr
alias: deplacements
---
# Déplacements

Il existe plusieurs façons de se déplacer : à pied, à cheval, ou en bateau sur les océans.  
Parfois vous pouvez même voler ou nager.  

Pour toutes ces variantes, il faut utiliser l'ordre [[cmd-move]] ou [[cmd-route]] (déplacement planfié sur plusieurs tours).  

Pour qu'une unité puisse se déplacer, le poids total des objets qu'elle porte ne doit pas excéder sa capacité de transport.  
De même, un bateau en mer ne pourra se déplacer que si son chargement ne dépasse pas sa capacité de transport.

!!! info "Information"
    L'unité de poids est le **lbs**.  

## Capacité de transport

<!-- TODO: check catapult capacity -->
*Capacité de transport d'une personne selon la race.*

| Race       | Capacité de transport |
|------------|----------------------:|
| [Gobelin]  |               **4,4** |
| [Aquarien] |                   5,4 |
| [Chat]     |                   5,4 |
| [Démon]    |                   5,4 |
| [Elfe]     |                   5,4 |
| [Halfling] |                   5,4 |
| [Humain]   |                   5,4 |
| [Insecte]  |                   5,4 |
| [Nain]     |                   5,4 |
| [Orc]      |                   5,4 |
| [Troll]    |              **10,8** |

Les trolls ont une capacité de transport supérieure. Les Gobelins ont une capacité de transport moindre.  

Une unité peut augmenter sa capacité de transport grâce aux [chevaux et chariots].  

| Transporteur | Capacité de transport |
|--------------|----------------------:|
| [Chariot]    |                   100 |
| [Cheval]     |                    20 |

!!! tip "Astuce"
    Utilisez de l'[Eau de Goliath] au moment opportun ! Cette potion permet d'augmenter la capacité de transport d'une unité sur une durée limitée.

| Bateau      | Capacité de transport |
|-------------|----------------------:|
| [Barque]    |                    50 |
| [Chaloupe]  |                   500 |
| [Drakkar]   |                 1 000 |
| [Trirème]   |                 2 000 |
| [Caravelle] |                 3 000 |
| [Galion]    |                20 000 |

## Poids

*Poids d'une personne selon la race.*

| Race       | Poids |
|------------|------:|
| [Gobelin]  |     6 |
| [Aquarien] |    10 |
| [Chat]     |    10 |
| [Démon]    |    10 |
| [Elfe]     |    10 |
| [Halfling] |    10 |
| [Humain]   |    10 |
| [Insecte]  |    10 |
| [Nain]     |    10 |
| [Orc]      |    10 |
| [Troll]    |    20 |
| [Chariot]  |    40 |

Le poids des objets les plus courants est répertorié dans le [tableau récapitulatif des objets].  

!!! note "Note"
    Les [potions], [plantes] et la plupart des objets magiques (anneaux, amulettes...) ne pèsent rien.

## Voyage : par terre ou par mer

À chaque tour, il est possible de parcourir une région par voie terrestre.  
Si une unité a suffisamment de **chevaux** et qu'elle maîtrise l'[Équitation], elle peut se déplacer **d'une région supplémentaire**.  
Si les régions contiguës sont reliées par des [[routes]], les unités peuvent se déplacer jusqu'à **2 régions à pied** et **3 régions à cheval**.  

Le déplacement n'est possible que dans les six directions suivantes : nord-est (NE), nord-ouest (NW), est (E), ouest (W), sud-est (SE) et sud-ouest (SW).  
Il n'est pas possible de se déplacer directement vers le nord ou le sud.  

Avec l'ordre [[cmd-carry|`CARRY <ID-du-passager>`]], les unités peuvent transporter d'autres unités pendant leur déplacement.  
L'unité souhaitant être transportée doit donner l'ordre [[cmd-ride|`RIDE <ID-du-transporteur>`]] ([ordre long]).  

Il est ainsi possible de transporter des unités (sans maîtrise de l'Équitation) sur des chevaux et dans des chariots.  
L'unité de transport doit bien sûr avoir une capacité de transport suffisante pour les passagers et leurs possessions.  

Par contre, avec [[cmd-follow|`FOLLOW UNIT <ID-unité-suivie>`]] ou `FOLLOW SHIP <ID-bateau-suivi>`, c'est comme si l'unité avait elle-même donné un ordre [[cmd-move]], si l'unité suivie (ou le bateau) a un ordre de déplacement.  
L'unité qui suit doit porter son propre poids.  

Les unités en déplacement peuvent être stoppées par des unités en garde dans une région (voir [[cmd-guard]]).  

Si une unité ou un bateau est trop lourdement chargé, il ne peut pas se déplacer.  
Pour cela, le poids total de l'unité à transporter, y compris les marchandises et les *silvers* qu'elle transporte, est comparé à sa capacité de transport.  
Le tableau dans le chapitre [[objets]] référence le poids des marchandises.

## Routes

La construction de [[routes]] permet d'augmenter d'une région la vitesse de déplacement.  
Pour cela, toutes les régions traversées doivent avoir un réseau routier complet.  
Ainsi, si l'on veut se rendre à pied à l'est en deux régions en une semaine :

- la région de départ a besoin d'une route complète vers l'est
- la région intermédiaire a besoin d'une route complète vers l'est et d'une route complète vers l'ouest
- la région d'arrivée a besoin d'une route complète vers l'ouest

## Chevaux et chariots

La **vitesse de déplacement** à pied sans [[routes|route]] est de 1 région par tour; avec une route, c'est 2.  

À cheval, on peut se déplacer de 2 régions sans route, de 3 régions avec des routes.  

Un niveau de compétence par 2 chevaux est nécessaire pour monter.
L'unité monte automatiquement si elle a assez de niveaux en Équitation pour tous les chevaux possédés et si l'unité n'est pas surchargée.
Si l'unité est trop lourdement chargée pour monter à cheval, mais pas trop lourdement chargée pour se déplacer à pied, l'unité se déplace d'une seule région (sans route).
On considère qu'elle mène les chevaux par la bride.

Les **chevaux** ont une capacité de transport de 20 lbs.  

Les **chariots** (*« cart »*) ont une capacité de 100 lbs.
Pour cela, ils doivent être tirés par 2 chevaux (par chariot).
Mais les chariots peuvent aussi être transportés comme fret, par exemple sur un bateau ou si l'unité n'a pas assez de chevaux avec elle ; ils ont un poids de 40 lbs.

Quatre trolls peuvent également tirer un chariot sans chevaux, mais seulement sur une région. Seuls les trolls peuvent utiliser des chariots sans chevaux.

**À pied**, chaque personne (même sans maîtrise de l'Équitation) peut mener un cheval sur une région. De plus, chaque personne peut mener quatre chevaux par niveau de compétence en Équitation (une personne T1 en Équitation peut donc conduire 5 chevaux au total).
Si les trolls transportent à la fois des chevaux et des chariots, ce sont les chevaux qui tirent les chariots en priorité.

**À cheval**, chaque personne peut avoir deux chevaux par niveau en Équitation.
Il convient de noter que le poids des cavaliers doit être déduit de la capacité de l'attelage.

Si elle a trop de chevaux, l'unité ne peut plus se déplacer.

Si une unité comprend plusieurs chevaux et chariots, leur capacité de transport est simplement additionnée. Par exemple, on peut transporter 7 pierres sur 3 chariots, alors qu'on ne peut transporter qu'une seule pierre sur un seul chariot.

**Exemples** (nous supposons ici qu'il n'y a pas de routes)

- Une unité de 4 personnes T1 en Équitation peut transporter au maximum 20 chevaux (4 chevaux de toute façon, plus 4 x 4 chevaux grâce à Équitation T1) à pied. Si elle n'a pas plus de 8 chevaux avec elle et qu'elle n'est pas trop lourde, elle peut se déplacer de deux cases.
- Si la même unité n'emporte que 8 chevaux et 2 chariots, elle a une capacité à cheval de 320 lbs (2 x 100 lbs pour les chariots + 8 x 20 lbs pour les chevaux − 4 x 10 lbs pour les cavaliers).
  Les exceptions à cette règle sont les races avec un poids différent, où le poids réel du cavalier est bien sûr déduit.
- Une unité de 5 nains sans maîtrise de l'Équitation peut mener 5 chevaux sur une région en transportant 127 lbs (5,4 lbs par nain et 20 lbs par cheval).
- Si la même unité a en plus 3 chariots, elle peut transporter 287 lbs d'autres marchandises (5,4 lbs par nain, 20 lbs par cheval et 2 x 100 lbs pour les chariots tractés moins 40 lbs pour le chariot qui doit être transporté, car 5 chevaux ne suffisent que pour 2 chariots).
- Une unité de 4 trolls sans maîtrise de l'Équitation et sans chevaux peut tirer un chariot sur une région (deux régions avec des routes) et transporter 143,2 lbs (10,8 lbs par troll et 100 lbs sur le chariot).
- Une unité de 4 trolls sans maîtrise de l'Équitation peut mener 4 chevaux et 3 chariots (deux derrière les chevaux et un derrière les 4 trolls) sur une région, transportant 423,2 lbs (10,8 lbs par troll, 300 lbs sur le chariot et 20 lbs sur chacun des 4 chevaux).
- Une unité de 4 trolls T1 en sans maîtrise de Équitation avec 4 chevaux et deux chariots peut se déplacer d'une région avec 323,2 lbs (10,8 lbs par troll, 20 lbs par cheval et 100 lbs par chariot) ou se déplacer de deux régions avec 200 lbs (20 lbs par cheval, 100 lbs par chariot moins 80 lbs pour les 4 trolls).
- Une unité T1 en Équitation, un chariot et deux chevaux peut déplacer 130 épées sur deux régions (le cavalier pèse 10 et doit être déduit de la capacité lorsqu'il est assis sur le chariot). Une unité T1 en Équitation 1 et 4 personnes pourrait déplacer 20 chevaux et 10 chariots sur une région et 8 chevaux et quatre chariots sur deux régions.
- Si un chariot vide avec deux chevaux doit être transporté sur un bateau, le bateau doit avoir pour cela une capacité libre de 140  lbs (40 lbs pour le chariot et 2 x 50 lbs pour les chevaux).

## Voir aussi

- [[bateaux]]
- [[routes]]

Poursuivre la lecture : [[naviguer]].

[Équitation]: ./skills-list.md#equitation "Riding"

<!-- From [https://wiki.eressea.de/index.php?title=Reisen/fr&oldid=16636] -->

[Troll]: ./races.md#trolls "Trolls"
[Gobelin]: ./races.md#gobelins "Goblins"
[Aquarien]: ./races.md#aquariens "Aquarians"
[Chat]: ./races.md#chats "Cats"
[Démon]: ./races.md#demons "Demons"
[Elfe]: ./races.md#elfes "Elves"
[Halfling]: ./races.md#halflings "Halflings"
[Humain]: ./races.md#humains "Humans"
[Insecte]: ./races.md#insectes "Insects"
[Nain]: ./races.md#nains "Dwarves"
[Orc]: ./races.md#orcs "Orcs"

[Barque]: ./ships.md#barque "Boat"
[Chaloupe]: ./ships.md#chaloupe "Longboat"
[Drakkar]: ./ships.md#drakkar "Dragonship"
[Trirème]: ./ships.md#trireme "Trireme"
[Caravelle]: ./ships.md#caravelle "Caravelle"
[Galion]: ./ships.md#galion "Galleon"

[Chariot]: ./resources.md#chariot "Cart"
[Cheval]: ./resources.md#cheval "Horse"
[Eau de Goliath]: ./alchemy.md#eau-de-goliath "Goliath water"
[potions]: ./alchemy.md#potions "Potions"
[plantes]: ./herbs.md "Herbs"
[ordre long]: ./commands.md#ordres-courts-et-longs
