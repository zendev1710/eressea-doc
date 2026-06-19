---
# cSpell:locale fr
alias: deplacements
---

# Déplacements

Il existe plusieurs façons de se déplacer : à pied, à cheval, ou en bateau sur les océans.  

<!-- TODO: précision : qui peut voler ? à quelle occasion ? -->
Parfois vous pouvez même voler ou nager (capacité exclusive des [Aquariens][aquariens]{title="Aquarians"}).  

Un déplacement n'est possible que dans les six directions suivantes : nord-est (NE), nord-ouest (NW), est (E), ouest (W), sud-est (SE) et sud-ouest (SW).  

!!! note "Note"
    Il n'est pas possible de se déplacer directement vers le nord ou le sud.  

Pour se déplacer, il faudra renseigner la direction -ou les directions consécutives- à prendre, au moyen des ordres [`MOVE`][cmd-move-fr] ou [`ROUTE`][cmd-route-fr] (déplacement planfié sur plusieurs tours).  

La vitesse de déplacement se caractérise par le nombre de régions terrestres (ou de régions océaniques pour un bateau) que peut parcourir une unité en une seule fois.  

Pour qu'une unité puisse se déplacer, le poids total des objets qu'elle porte ne doit pas excéder sa capacité de transport.  
De même, un bateau en mer ne pourra se déplacer que si son chargement ne dépasse pas sa capacité de transport.

!!! info "Information"
    L'unité de poids est le **lbs**.  

## Capacité de transport

<!-- TODO: check catapult capacity -->
*Capacité de transport d'une personne selon le peuple.*

| Peuple                                    | Capacité de transport |
|-------------------------------------------|----------------------:|
| [Gobelin][gobelins]{title="Goblins"}      |               **4,4** |
| [Aquarien][aquariens]{title="Aquarians"}  |                   5,4 |
| [Chat][chats]{title="Cats"}               |                   5,4 |
| [Démon][demons-fr-id]{title="Demons"}     |                   5,4 |
| [Elfe][elfes]{title="Elves"}              |                   5,4 |
| [Halfelins][halfelins]{title="Halflings"} |                   5,4 |
| [Humain][humains]{title="Humans"}         |                   5,4 |
| [Insecte][insectes]{title="nsects"}       |                   5,4 |
| [Nain][nains]{title="Dwarves"}            |                   5,4 |
| [Orc][orcs-fr-id]{title="Orcs"}           |                   5,4 |
| [Troll][trolls-fr-id]{title="Trolls"}     |              **10,8** |

Les trolls ont une capacité de transport supérieure aux autres peuples.
Les Gobelins ont une capacité de transport moindre.  

Une unité peut augmenter sa capacité de transport grâce aux [chevaux et chariots].  

| Transporteur                     | Capacité de transport |
|----------------------------------|----------------------:|
| [Chariot][chariot]{title="Cart"} |                   100 |
| [Cheval][cheval]{title="Horse"}  |                    20 |

!!! tip "Astuce"
    Utilisez de l'[Eau de Goliath][eau-de-goliath]{title="Goliath water"} au moment opportun ! Cette potion permet d'augmenter la capacité de transport d'une unité sur une durée limitée.

| Bateau                                    | Capacité de transport |
|-------------------------------------------|----------------------:|
| [Barque][barque]{title="Boat"}            |                    50 |
| [Chaloupe][chaloupe]{title="Longboat"}    |                   500 |
| [Drakkar][drakkar]{title="Dragonship"}    |                 1 000 |
| [Trirème][trireme-fr-id]{title="Trireme"} |                 2 000 |
| [Caravelle][caravelle]{title="Caravelle"} |                 3 000 |
| [Galion][galion]{title="Galleon"}         |                20 000 |

## Poids

*Poids d'une personne selon le peuple.*

| Peuple                                   | Poids |
|------------------------------------------|------:|
| [Gobelin][gobelins]{title="Goblins"}     |     6 |
| [Aquarien][aquariens]{title="Aquarians"} |    10 |
| [Chat][chats]{title="Cats"}              |    10 |
| [Démon][demons-fr-id]{title="Demons"}    |    10 |
| [Elfe][elfes]{title="Elves"}             |    10 |
| [Halfelin][halfelins]{title="Halflings"} |    10 |
| [Humain][humains]{title="Humans"}        |    10 |
| [Insecte][insectes]{title="nsects"}      |    10 |
| [Nain][nains]{title="Dwarves"}           |    10 |
| [Orc][orcs-fr-id]{title="Orcs"}          |    10 |
| [Troll][trolls-fr-id]{title="Trolls"}    |    20 |

<!-->
| [Chariot][chariot]{title="ar"}  |    40 |
-->

Le poids des objets les plus courants est répertorié dans le [tableau récapitulatif des objets].  

!!! note "Note"
    Les [potions][potions-fr-id], [plantes][plantes]{title="Herbs"} et la plupart des objets magiques (anneaux, amulettes...) ne pèsent rien.

## Déplacement par voie terrestre

À chaque tour, il est possible de parcourir par défaut une région par voie terrestre.  

Si une unité a suffisamment de **chevaux** et qu'elle maîtrise l'[Équitation][equitation]{title="Riding"}, elle peut se déplacer **d'une région supplémentaire**.  
Si les régions contiguës sont reliées par des [routes][routes-id], les unités peuvent se déplacer jusqu'à **2 régions à pied** et **3 régions à cheval**.  

[](){ #travel-routes-id }

### Routes

La construction de [routes][routes-id] permet d'augmenter d'une région la vitesse de déplacement.  
Pour cela, toutes les régions traversées doivent avoir un réseau routier complet et praticable.  

Ainsi, si l'on veut se rendre à pied à l'est deux régions plus loin (`MOVE E E`) en une seule fois :

- la région de départ a besoin d'une route praticable vers l'est
- la région intermédiaire traversée a besoin d'une route praticable vers l'est et d'une route praticable vers l'ouest
- la région d'arrivée a besoin d'une route praticable vers l'ouest

Si l'une des routes à emprunter n'est pas praticable, l'unité s'arrêtera en chemin, sur la région intermédiaire.

Plus d'information : [les routes][routes-id].

### Chevaux et chariots

La **vitesse de déplacement** à pied sans [route][routes-id] est de 1 région par tour; avec une route, c'est 2.  

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
  Les exceptions à cette règle sont les peuples avec un poids différent, où le poids réel du cavalier est bien sûr déduit.
- Une unité de 5 nains sans maîtrise de l'Équitation peut mener 5 chevaux sur une région en transportant 127 lbs (5,4 lbs par nain et 20 lbs par cheval).
- Si la même unité a en plus 3 chariots, elle peut transporter 287 lbs d'autres marchandises (5,4 lbs par nain, 20 lbs par cheval et 2 x 100 lbs pour les chariots tractés moins 40 lbs pour le chariot qui doit être transporté, car 5 chevaux ne suffisent que pour 2 chariots).
- Une unité de 4 trolls sans maîtrise de l'Équitation et sans chevaux peut tirer un chariot sur une région (deux régions avec des routes) et transporter 143,2 lbs (10,8 lbs par troll et 100 lbs sur le chariot).
- Une unité de 4 trolls sans maîtrise de l'Équitation peut mener 4 chevaux et 3 chariots (deux derrière les chevaux et un derrière les 4 trolls) sur une région, transportant 423,2 lbs (10,8 lbs par troll, 300 lbs sur le chariot et 20 lbs sur chacun des 4 chevaux).
- Une unité de 4 trolls T1 en sans maîtrise de Équitation avec 4 chevaux et deux chariots peut se déplacer d'une région avec 323,2 lbs (10,8 lbs par troll, 20 lbs par cheval et 100 lbs par chariot) ou se déplacer de deux régions avec 200 lbs (20 lbs par cheval, 100 lbs par chariot moins 80 lbs pour les 4 trolls).
- Une unité T1 en Équitation, un chariot et deux chevaux peut déplacer 130 épées sur deux régions (le cavalier pèse 10 et doit être déduit de la capacité lorsqu'il est assis sur le chariot). Une unité T1 en Équitation 1 et 4 personnes pourrait déplacer 20 chevaux et 10 chariots sur une région et 8 chevaux et quatre chariots sur deux régions.
- Si un chariot vide avec deux chevaux doit être transporté sur un bateau, le bateau doit avoir pour cela une capacité libre de 140  lbs (40 lbs pour le chariot et 2 x 50 lbs pour les chevaux).

### Transport d'unités par d'autres

Avec l'ordre [`CARRY <ID-du-passager>`][cmd-carry-fr], les unités peuvent transporter d'autres unités pendant leur déplacement.  
L'unité souhaitant être transportée doit donner l'ordre [`RIDE <ID-du-transporteur>`][cmd-ride-fr] ([ordre long][ordres-courts-et-longs]).  

Il est ainsi possible de transporter des unités (sans maîtrise de l'Équitation) sur des chevaux et dans des chariots.  
L'unité de transport doit bien sûr avoir une capacité de transport suffisante pour les passagers et leurs possessions.  

Par contre, avec [`FOLLOW UNIT <ID-unité-suivie>`][cmd-follow-fr] ou `FOLLOW SHIP <ID-bateau-suivi>`, c'est comme si l'unité avait elle-même donné un ordre [`MOVE`][cmd-move-fr], si l'unité suivie (ou le bateau) a un ordre de déplacement.  
L'unité qui suit doit porter son propre poids.  

Les unités en déplacement peuvent être stoppées par des unités en garde dans une région (voir [`GUARD`][cmd-guard-fr]).  

Si une unité ou un bateau est trop lourdement chargé, il ne peut pas se déplacer.  
Pour cela, le poids total de l'unité à transporter, y compris les marchandises et les *silvers* qu'elle transporte, est comparé à sa capacité de transport.  

Voir aussi : [poids des marchandises][objets].

## Déplacement en mer

À chaque tour, il est possible de parcourir un océan.  

L'unité de transport doit bien sûr avoir une capacité de transport suffisante pour les passagers et leurs possessions.  

Par contre, avec [`FOLLOW UNIT <ID-unité-suivie>`][cmd-follow-fr] ou `FOLLOW SHIP <ID-bateau-suivi>`, c'est comme si l'unité avait elle-même donné un ordre [`MOVE`][cmd-move-fr], si l'unité suivie (ou le bateau) a un ordre de déplacement.  
L'unité qui suit doit porter son propre poids.  

Les unités en déplacement peuvent être stoppées par des unités en garde dans une région (voir [`GUARD`][cmd-guard-fr]).  

Si une unité ou un bateau est trop lourdement chargé, il ne peut pas se déplacer.  
Pour cela, le poids total de l'unité à transporter, y compris les marchandises et les *silvers* qu'elle transporte, est comparé à sa capacité de transport.  

Voir aussi : [poids des marchandises][objets].

## Voir aussi

- [Bateaux][bateaux-id]
- [Routes][routes-id]

Poursuivre la lecture : [naviguer][naviguer].

<!-- From [https://wiki.eressea.de/index.php?title=Reisen/fr&oldid=16636] -->

[cmd-carry-fr]: [[cmd-carry-fr]]
[cmd-follow-fr]: [[cmd-follow-fr]]
[cmd-ride-fr]: [[cmd-ride-fr]]
[cmd-move-fr]: [[cmd-move-fr]]
[cmd-route-fr]: [[cmd-route-fr]]
[cmd-guard-fr]: [[cmd-guard-fr]]
