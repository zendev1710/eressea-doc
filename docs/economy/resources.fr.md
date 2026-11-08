---
# cSpell:locale fr
alias: ressources
---

# Ressources

Les matières premières peuvent être obtenues directement à partir des réserves des [régions][le-monde-d-eressea-id] sans aucun autre ingrédient.  
Les ressources sont toutefois limitées et ne se régénèrent que lentement, voire pas du tout.  
La compétence requise est indiquée dans le tableau de la section [objets].

## Matières premières

[](){ #adamantium-fr-id }

### Adamantium

<!-- cspell:disable -->
*Adamantium (EN), Adamantium (DE)*.
<!-- cspell:enable -->

Expérience de jeu :

L’adamantium est encore plus rare que le [laen][laen-fr-id]{title="Laen"} !  

On en trouve à peine un par tour, si tant est qu’il y en ait dans la région.  

Ce métal précieux permet de fabriquer :

- une [armure en adamantium][armure-en-adamantium]{title="Adamantium plate"}
- une [hache en adamantium][hache-en-adamantium]{title="Adamantium axe"}

#### Liens externes

- [Adamantium sur Wikipedia]

<!-- From [https://wiki.eressea.de/index.php?title=Adamantium&oldid=6241] -->

### Bois

<!-- cspell:disable -->
*Wood (EN), Holz (DE)*.
<!-- cspell:enable -->

### Chariot

<!-- cspell:disable -->
*Cart (EN), Wagen (DE)*.
<!-- cspell:enable -->

| Poids | Capacité de transport |
|:-----:|:---------------------:|
|  40   |          100          |

Un chariot facilite le transport des unités en augmentant la [capacité de transport][capacite-de-transport].

### Cheval

<!-- cspell:disable -->
*Horse (EN), Pferd (DE)*.
<!-- cspell:enable -->

| Poids | Capacité de transport |
|:-----:|:---------------------:|
|  50   |          20           |

Un cheval facilite le transport des unités en augmentant la [capacité de transport][capacite-de-transport].  
Un cheval augmente également la vitesse de déplacement (d'une région supplémentaire) s'il est monté par une unité suffisamment compétente en équitation.

### Fer

<!-- cspell:disable -->
*Iron (EN), Eisen (DE)*.
<!-- cspell:enable -->

[](){ #laen-fr-id }

### Laen

<!-- cspell:disable -->
*Laen (EN), Laen (DE)*.
<!-- cspell:enable -->

[](){ #mallorn-fr-id }

### Mallorn

<!-- cspell:disable -->
*Mallorn (EN), Mallorn (DE)*.
<!-- cspell:enable -->

### Munition

<!-- cspell:disable -->
*Ammunition (EN), Katapultmunition (DE)*.
<!-- cspell:enable -->

### Pierre

<!-- cspell:disable -->
*Stone (EN), Stein (DE)*.
<!-- cspell:enable -->

## Exploitation des ressources

Lors de l'exploitation des ressources, il est important de considérer que les unités en [garde][cmd-guard-fr] empêchent l'exploitation, si les factions en garde n'ont ni [`HELP GUARD`][cmd-help-fr] ni [`HELP ALL`][cmd-help-fr] avec ta faction, ou donné l'ordre [`CONTACT`][cmd-contact-fr] avec l'unité ou la faction qui exploite.  
Ceci ne s'applique pas si la faction en garde ne voit pas le producteur, par exemple parce qu'il est [dissimulé][discretion].  

### Ressources minières

Le fer, la pierre, le laen et, dans les régions particulièrement anciennes, parfois même l'adamantium, peuvent être extraits des montagnes, des glaciers et parfois d'autres types de régions.  
Le laen et l'adamantium nécessitent une mine et une compétence en Mining particulièrement élevée.
Ces ressources peuvent être difficiles à extraire.
Dans ton rapport tu peux le savoir suivant le nombre après le "/".  
Par exemple, si le rapport indique « 20 fer/4 », cela signifie que 20 fers avec un niveau de compétence 4 peuvent encore être extraits.
Une fois ceux-ci extraits, les mineurs auront besoin d'être niveau 5 pour extraire du fer de la couche suivante (5).
En général, les quantités pouvant être extraites augmentent à chaque nouvelle couche.

Compétences concernées : [extraction minière][extraction-miniere]{title="Mining"}, [extraction de pierres][extraction-de-pierres]{title="Quarrying"}.

### Ressources forestières

Le développement de la végétation d'Eressea est déterminé par les saisons.  

Dès que les premiers rayons du soleil frappent le sol au printemps, les graines cachées dans le sol germent et les pousses d'arbres de l'année passée se transforment en arbres adultes.  
S'il n'y a pas assez de soleil (pas d'espace de travail libre), les graines restent dormantes dans le sol.  

Pendant les mois d'été et d'automne, les arbres matures jettent leurs graines, qui peuvent être ramassées avec l'ordre [`MAKE seed` ou `MAKE mallorn seed`][cmd-make-fr] et la compétence [Herbalism] de niveau minimun 3 ou 4, puis replantées ailleurs avec l'ordre [`PLANT seed` ou `PLANT mallorn seed`][cmd-plant-fr] (niveau minimum de 6 ou 7).

Si du bois ou du mallorn est abattu, la forêt se rétrécit et ne se reconstitue que très lentement.
Tant qu'il y a suffisamment de bois, il peut être abattu en n'importe quelle quantité.  
Il en va de même pour le mallorn, un bois "magique" que l'on ne trouve que dans quelques régions.  
Le mallorn se reproduit certes comme le bois, mais les graines de mallorn ne poussent que dans les régions qui s'y prêtent.  
Dans les régions à mallorn, l'ordre `MAKE wood` permet également d'abattre du bois à la place du Mallorn.  
Le nombre d'arbres de mallorn est alors réduit d'autant que si l'on avait abattu des mallorns.  

Compétences concernées : [sylviculture][sylviculture]{title="Forestry"}, [herboristerie][herboristerie]{title="Herbalism"}.

#### Arbres

<!-- cspell:disable -->
*Trees (EN), Bäume (DE)*.
<!-- cspell:enable -->

#### Jeunes arbres (ou pousses)

<!-- cspell:disable -->
*Saplings (EN), Schößlinge (DE)*.
<!-- cspell:enable -->

#### Arbres de mallorn

<!-- cspell:disable -->
*Mallorn Trees (EN), Mallornbäume (DE)*.
<!-- cspell:enable -->

#### Jeunes arbres de mallorn (ou pousses de mallorn)

<!-- cspell:disable -->
*Mallorn Saplings (EN), Mallornschößlinge (DE)*.
<!-- cspell:enable -->

#### Graines

<!-- cspell:disable -->
*Seeds (EN), Samen (DE)*.
<!-- cspell:enable -->

#### Graines de mallorn

<!-- cspell:disable -->
*Mallornseeds (EN), Mallornsamen (DE)*.

### Autres ressources

#### Chevaux

<!-- cspell:disable -->
*Horses (EN),  (DE)*.
<!-- cspell:enable -->

Les chevaux peuvent également être capturés à volonté avec l'ordre [`MAKE horse`][cmd-make-fr].
Sans aide, seuls les chevaux sauvages se reproduisent.
Il est toutefois possible de faire naître d'autres chevaux dans un [haras][haras].  

Les chevaux sauvages aiment l'espace et la liberté, c'est pourquoi certains d'entre eux migrent vers les régions voisines lorsque les chevaux y sont moins nombreux.

Expérience de jeu (Solthar):

Le nombre maximal de chevaux dans une région est égal au **nombre d'[emplois][le-monde-d-eressea-id] / 10**.

Dans une plaine relativement vide, leur croissance est de 4 %.
À mesure qu’ils approchent de la limite supérieure, la croissance ralentit.  
La plupart des nouveaux chevaux naissent dans environ la moitié de la population maximale.

Dans une plaine de 25 chevaux, il y a 1 mise bas par semaine.  
Avec 500 chevaux, il y a 10 nouveaux chevaux par tour.  
Avec 1000 chevaux il n'y a plus de croissance.  

[](){ #resources-plantes-id }

#### Plantes

<!-- cspell:disable -->
*Herbs (EN),  (DE)*.
<!-- cspell:enable -->

On peut également récolter des plantes pour concocter des potions.  
Il n'y a qu'au plus une espèce de plante dans chaque région.  

Plus d'information : [liste des plantes][liste-des-plantes].

## Voir aussi

- [Production][production-fr-id]
- [Objets][objets]
- [Routes][routes-id]
- [Bâtiments][batiments-id]

Poursuivre la lecture : [objets][objets].

<!-- From [https://wiki.eressea.de/index.php?title=Rohstoffe/fr&oldid=16659] -->

[Adamantium sur Wikipedia]: http://fr.wikipedia.org/wiki/Adamantium

[cmd-contact-fr]: [[cmd-contact-fr]]
[cmd-guard-fr]: [[cmd-guard-fr]]
[cmd-help-fr]: [[cmd-help-fr]]
[cmd-plant-fr]: [[cmd-plant-fr]]
[cmd-make-fr]: [[cmd-make-fr]]
