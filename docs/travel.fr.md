---
# cSpell:locale fr
alias: deplacements
---
# Déplacements

Il existe plusieurs façons de se déplacer : à pied, à cheval, ou en bateau sur les océans.  
Parfois vous pouvez même voler ou nager.  

Pour toutes ces variantes, il faut utiliser l'ordre [[cmd-move]] ou [[cmd-route]].

## Voyage : par terre ou par mer

À chaque tour, il est possible de parcourir une région par voie terrestre.  
Si une unité a suffisamment de chevaux et qu'elle a la compétence *[riding]* (équitation), elle peut se déplacer d'une région supplémentaire.  
Si les régions contiguës sont reliées par des routes, les unités peuvent se déplacer jusqu'à 2 régions à pied et 3 régions à cheval.  

Le déplacement n'est possible que dans les six directions suivantes : nord-est (NE), nord-ouest (NW), est (E), ouest (W), sud-est (SE) et sud-ouest (SW).  
Il n'est pas possible de se déplacer directement vers le nord ou le sud.  

Avec l'ordre [[cmd-carry]]` `*`ID-du-passager`* les unités peuvent transporter d'autres unités pendant leur déplacement.  
L'unité qui doit être transportée doit donner l'ordre [[cmd-ride]]` `*`ID-du-transporteur`* (c'est un ordre long).  
Grâce à cet ordre, il est par exemple possible de transporter des unités sans la compétence *riding* sur des chevaux et dans des chariots.  
Pour cela, l'unité qui transporte doit bien sûr avoir une capacité de transport suffisante pour les passagers et leurs possessions.  

Par contre, avec [[cmd-follow]]` UNIT `*`ID-unité-suivie`* ou `FOLLOW SHIP`*`ID-bateau-suivi`* c'est comme si l'unité avait elle-même donné un ordre [[cmd-move]], si l'unité suivie (ou le bateau) a un ordre de déplacement.  
L'unité qui suit doit porter son propre poids.  

Les unités en déplacement peuvent être stoppées par des unités en garde dans une région (voir [[cmd-guard]]).  

Si une unité ou un bateau est trop lourdement chargé, il ne peut pas se déplacer.  
Pour cela, le poids total de l'unité à transporter, y compris les marchandises et les *silvers* qu'elle transporte, est comparé à sa capacité de transport.  
Le tableau dans le chapitre [[objets]] référence le poids des marchandises.

<!-- TODO: renseigner les informations de poids pour la catapulte -->

Poids et capacité de transport.

| Transporteur | Poids | Capacité |
|--------------|------:|---------:|
| Troll        |    20 |     10,8 |
| Gobelin      |     6 |      4,4 |
| Autres races |    10 |      5,4 |
| Cheval       |    50 |       20 |
| Chariot      |    40 |      100 |
| Catapulte    |     ? |        ? |
| Barque       |    -- |       50 |
| Chaloupe     |    -- |      500 |
| Drakkar      |    -- |     1000 |
| Caravelle    |    -- |     3000 |
| Trirème      |    -- |     2000 |
| Galion       |    -- |    20000 |

## Routes

La construction de [[routes]] permet d'augmenter d'une région la vitesse de déplacement.
Pour cela, toutes les régions traversées doivent avoir un réseau routier complet. Ainsi, si l'on veut se rendre à pied à l'est en deux régions en une semaine, la région de départ a besoin d'une route complète vers l'est, la région intermédiaire d'une route complète vers l'est et d'une route complète vers l'ouest et la région d'arrivée d'une route complète vers l'ouest.

## Chevaux et chariots

La **vitesse de déplacement** à pied sans [[routes|route]] est de 1 région par tour;
avec une route, c'est 2.
À cheval, on peut se déplacer de 2 régions sans route, de 3 régions avec des routes.
Un niveau de compétence par 2 chevaux est nécessaire pour monter.
L'unité monte automatiquement si elle a assez de niveaux en *riding* pour tous les chevaux possédés et si l'unité n'est pas surchargée. Si l'unité est trop lourdement chargée pour monter à cheval, mais pas trop lourdement chargée pour se déplacer à pied, l'unité se déplace d'une seule région (sans route). On considère qu'elle mène les chevaux par la bride.

Les **chevaux** ont une capacité de 20 kg/WU.

Les **chariots** (*« cart »*) ont une capacité de 100 kg/WU.
Pour cela, ils doivent être tirés par 2 chevaux (par chariot).
Mais les chariots peuvent aussi être transportés comme fret, par exemple sur un bateau ou si l'unité n'a pas assez de chevaux avec elle ; ils ont un poids de 40 kg.

Quatre trolls peuvent également tirer un chariot sans chevaux, mais seulement sur une région. Seuls les trolls peuvent utiliser des chariots sans chevaux.

**À pied**, chaque personne (même sans compétence *riding*) peut mener un cheval sur une région. De plus, chaque personne peut mener quatre chevaux par niveau de compétence en Équitation (une personne avec Équitation 1 peut donc conduire 5 chevaux au total). Si les trolls transportent à la fois des chevaux et des chariots, ce sont les chevaux qui tirent les chariots en priorité.

**À cheval**, chaque personne peut avoir deux chevaux par niveau en *riding*. Il convient de noter que le poids des cavaliers doit être déduit de la capacité de l'attelage.

Si elle a trop de chevaux, l'unité ne peut plus se déplacer.

Si une unité comprend plusieurs chevaux et chariots, leur capacité de transport est simplement additionnée. Par exemple, on peut transporter 7 pierres sur 3 chariots, alors qu'on ne peut transporter qu'une seule pierre sur un seul chariot.

**Exemples** (nous supposons ici qu'il n'y a pas de routes)

- Une unité de 4 personnes avec *riding* 1 peut transporter au maximum 20 chevaux (4 chevaux de toute façon, plus 4 \* 4 chevaux grâce à *riding* 1) à pied. Si elle n'a pas plus de 8 chevaux avec elle et qu'elle n'est pas trop lourde, elle peut se déplacer de deux cases.
- Si la même unité n'emporte que 8 chevaux et 2 chariots, elle a une capacité à cheval de 320GE (2 \* 100GE pour les chariots + 8 \* 20GE pour les chevaux − 4 \* 10GE pour les cavaliers). Les exceptions à cette règle sont les races avec un poids différent, où le poids réel du cavalier est bien sûr déduit.
- Une unité de 5 nains sans compétence *riding* peut mener 5 chevaux sur une région en transportant 127GE (5,4GE par nain et 20GE par cheval).
- Si la même unité a en plus 3 chariots, elle peut transporter 287GE d'autres marchandises (5,4GE par nain, 20GE par cheval et 2 \* 100GE pour les chariots tractés moins 40GE pour le chariot qui doit être transporté, car 5 chevaux ne suffisent que pour 2 chariots).
- Une unité de 4 trolls sans compétence *riding* et sans chevaux peut tirer un chariot sur une région (deux régions avec des routes) et transporter 143,2GE (10,8GE par troll et 100GE sur le chariot).
- Une unité de 4 trolls sans compétence *riding* peut mener 4 chevaux et 3 chariots (deux derrière les chevaux et un derrière les 4 trolls) sur une région, transportant 423,2GE (10,8GE par troll, 300GE sur le chariot et 20GE sur chacun des 4 chevaux).
- Une unité de 4 trolls avec *riding* 1 avec 4 chevaux et deux chariots peut se déplacer d'une région avec 323,2GE (10,8GE par troll, 20GE par cheval et 100GE par chariot) ou se déplacer de deux régions avec 200GE (20GE par cheval, 100GE par chariot moins 80GE pour les 4 trolls).
- Une unité avec *riding* 1, un chariot et deux chevaux peut déplacer 130 épées sur deux régions (le cavalier pèse 10 et doit être déduit de la capacité lorsqu'il est assis sur le chariot). Une unité avec *riding* 1 et 4 personnes pourrait déplacer 20 chevaux et 10 chariots sur une région et 8 chevaux et quatre chariots sur deux régions.
- Si un chariot vide avec deux chevaux doit être transporté sur un bateau, le bateau doit avoir pour cela une capacité libre de 140GE (40GE pour le chariot et 2 \* 50GE pour les chevaux).

## Voir aussi

- [[bateaux]]
- [[routes]]

Poursuivre la lecture : [[naviguer]].

[riding]: ./skills-list.fr.md#equitation

<!-- From [https://wiki.eressea.de/index.php?title=Reisen/fr&oldid=16636] -->
