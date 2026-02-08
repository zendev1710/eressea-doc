---
# cSpell:locale fr
alias: ressources
---
# Ressources

Les matières premières peuvent être obtenues directement à partir des réserves des [[le-monde-d-eressea|régions]] sans aucun autre ingrédient.  
Les ressources sont toutefois limitées et ne se régénèrent que lentement, voire pas du tout.  
La compétence requise est indiquée dans le tableau de la section [objets].

## Matières premières

### Adamantium

<!-- cspell:disable -->
*Adamantium (EN), Adamantium (DE)*.
<!-- cspell:enable -->

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

Un chariot facilite le transport des unités en augmentant la [capacité de transport].

### Cheval

<!-- cspell:disable -->
*Horse (EN), Pferd (DE)*.
<!-- cspell:enable -->

| Poids | Capacité de transport |
|:-----:|:---------------------:|
|  50   |          20           |

Un cheval facilite le transport des unités en augmentant la [capacité de transport].  
Un cheval augmente également la vitesse de déplacement (d'une région supplémentaire) s'il est monté par une unité suffisamment compétente en équitation.

### Fer

<!-- cspell:disable -->
*Iron (EN), Eisen (DE)*.
<!-- cspell:enable -->

### Laen

<!-- cspell:disable -->
*Laen (EN), Laen (DE)*.
<!-- cspell:enable -->

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

Lors de l'exploitation des ressources, il est important de considérer que les unités en [[cmd-guard|garde]] empêchent l'exploitation, si les factions en garde n'ont ni [[cmd-help|`HELP GUARD`]] ni [[cmd-help|`HELP ALL`]] avec ta faction, ou donné l'ordre [[cmd-contact|`CONTACT`]] avec l'unité ou la faction qui exploite.  
Ceci ne s'applique pas si la faction en garde ne voit pas le producteur, par exemple parce qu'il est [[camouflage|camouflé]].`  

### Ressources minières

Le fer, la pierre, le laen et, dans les régions particulièrement anciennes, parfois même l'adamantium, peuvent être extraits des montagnes, des glaciers et parfois d'autres types de régions.  
Le laen et l'adamantium nécessitent une mine et une compétence en Mining particulièrement élevée.
Ces ressources peuvent être difficiles à extraire.
Dans ton rapport tu peux le savoir suivant le nombre après le "/".  
Par exemple, si le rapport indique « 20 fer/4 », cela signifie que 20 fers avec un niveau de compétence 4 peuvent encore être extraits.
Une fois ceux-ci extraits, les mineurs auront besoin d'être niveau 5 pour extraire du fer de la couche suivante (5).
En général, les quantités pouvant être extraites augmentent à chaque nouvelle couche.

Compétences concernées : [extraction minière], [extraction de pierres].

### Ressources forestières

Le développement de la végétation d'Eressea est déterminé par les saisons.  

Dès que les premiers rayons du soleil frappent le sol au printemps, les graines cachées dans le sol germent et les pousses d'arbres de l'année passée se transforment en arbres adultes.  
S'il n'y a pas assez de soleil (pas d'espace de travail libre), les graines restent dormantes dans le sol.  

Pendant les mois d'été et d'automne, les arbres matures jettent leurs graines, qui peuvent être ramassées avec l'ordre [[cmd-make|`MAKE seed` ou `MAKE mallorn seed`]] et la compétence [Herbalism] de niveau minimun 3 ou 4, puis replantées ailleurs avec l'ordre [[cmd-plant|`PLANT seed` ou `PLANT mallorn seed`]] (niveau minimum de 6 ou 7).

Si du bois ou du mallorn est abattu, la forêt se rétrécit et ne se reconstitue que très lentement.
Tant qu'il y a suffisamment de bois, il peut être abattu en n'importe quelle quantité.  
Il en va de même pour le mallorn, un bois "magique" que l'on ne trouve que dans quelques régions.  
Le mallorn se reproduit certes comme le bois, mais les graines de mallorn ne poussent que dans les régions qui s'y prêtent.  
Dans les régions à mallorn, l'ordre `MAKE wood` permet également d'abattre du bois à la place du Mallorn.  
Le nombre d'arbres de mallorn est alors réduit d'autant que si l'on avait abattu des mallorns.  

Compétences concernées : [sylviculture], [herboristerie].

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

Les chevaux peuvent également être capturés à volonté avec l'ordre [[cmd-make|`MAKE horse`]].
Sans aide, seuls les chevaux sauvages se reproduisent.
Il est toutefois possible de faire naître d'autres chevaux dans un [haras].  

Les chevaux sauvages aiment l'espace et la liberté, c'est pourquoi certains d'entre eux migrent vers les régions voisines lorsque les chevaux y sont moins nombreux.

Expérience de jeu (Solthar):

Le nombre maximal de chevaux dans une région est égal au **nombre d'[[le-monde-d-eressea|emplois]] / 10**.

Dans une plaine relativement vide, leur croissance est de 4 %.
À mesure qu’ils approchent de la limite supérieure, la croissance ralentit.  
La plupart des nouveaux chevaux naissent dans environ la moitié de la population maximale.

Dans une plaine de 25 chevaux, il y a 1 mise bas par semaine.  
Avec 500 chevaux, il y a 10 nouveaux chevaux par tour.  
Avec 1000 chevaux il n'y a plus de croissance.  

#### Plantes

<!-- cspell:disable -->
*Herbs (EN),  (DE)*.
<!-- cspell:enable -->

On peut également récolter des plantes pour concocter des potions.  
Il n'y a qu'au plus une espèce de plante dans chaque région.  

Plus d'information : [liste des plantes].

## Voir aussi

- [[production]]
- [[objets]]
- [[routes]]
- [[batiments]]

Poursuivre la lecture : [[objets]].

<!-- From [https://wiki.eressea.de/index.php?title=Rohstoffe/fr&oldid=16659] -->

[haras]: ./buildings-others.md#haras
[liste des plantes]: ./herbs.md#liste-des-plantes
[sylviculture]: ./skills-list.md#sylviculture "Forestry"
[herboristerie]: ./skills-list.md#herboristerie "Herbalism"
[extraction minière]: ./skills-list.md#extraction-miniere "Mining"
[extraction de pierres]: ./skills-list.md#extraction-de-pierres "Quarrying"

[capacité de transport]: ./travel.fr.md#capacite-de-transport
