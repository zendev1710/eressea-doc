---
# cSpell:locale fr, en
alias: ressources
---
# Ressources

Les matières premières peuvent être obtenues directement à partir des réserves des [[le-monde-d-eressea|régions]] sans aucun autre ingrédient.
Les ressources sont toutefois limitées et ne se régénèrent que lentement, voire pas du tout.
La compétence requise est indiquée dans le tableau de la section [objets].

## Exploitation des ressources

Lors de l'exploitation des ressources, il est important de considérer que les unités en [[cmd-guard|garde]] empêchent l'exploitation, si les factions en garde n'ont ni [[cmd-help|`HELP GUARD`]] ni [[cmd-help|`HELP ALL`]] avec ta faction, ou donné l'ordre [[cmd-contact|`CONTACT`]] avec l'unité ou la faction qui exploite.
Ceci ne s'applique pas si la faction en garde ne voit pas le producteur, par exemple parce qu'il est `[`camouflé`]`.`

` `

### Ressources minières

Le fer, la pierre, le laen et, dans les régions particulièrement anciennes, parfois même l'adamantium, peuvent être extraits des montagnes, des glaciers et parfois d'autres types de régions.
Le laen et l'adamantium nécessitent une mine et une compétence en Mining particulièrement élevée.
Ces ressources peuvent être difficiles à extraire.
Dans ton rapport tu peux le savoir suivant le nombre après le "/".
Par exemple, si le rapport indique « 20 iron/4 », cela signifie que 20 fers avec un niveau de compétence 4 peuvent encore être extraits.
Une fois ceux-ci extraits, les mineurs auront besoin d'être niveau 5 pour extraire du fer de la couche suivante (5).
En général, les quantités pouvant être extraites augmentent à chaque nouvelle couche.

Compétences : l'extraction nécessite les compétences Mining ou Quarrying selon la ressource.

### Ressources forestières

Le développement de la végétation d'Eressea est déterminé par les saisons.
Dès que les premiers rayons du soleil frappent le sol au printemps, les graines cachées dans le sol germent et les pousses d'arbres de l'année dernière se transforment en arbres adultes.
S'il n'y a pas assez de soleil (pas d'espace de travail libre), les graines restent dormantes dans le sol.
Pendant les mois d'été et d'automne, les arbres matures jettent leurs graines, qui peuvent être ramassées avec l'ordre [[cmd-make]]`seed ou mallorn seed` et la compétence [Herbalism] de niveau minimun 3 ou 4 puis replanté ailleurs avec l'ordre [[cmd-plant]]`seed ou mallorn seed` (niveau minimum de 6 ou 7).

Si du bois ou du mallorn est abattu, la forêt se rétrécit et ne se reconstitue que très lentement.
Tant qu'il y a suffisamment de bois, il peut être abattu en n'importe quelle quantité.
Il en va de même pour le mallorn, un bois "magique" que l'on ne trouve que dans quelques régions.
Le mallorn se reproduit certes comme le bois, mais les graines de mallorn ne poussent que dans les régions qui s'y prêtent.
Dans les régions à Mallorn, la commande "MAKE wood" permet également d'abattre du bois à la place du Mallorn.
Le nombre d'arbres de Mallorn est alors réduit d'autant que si l'on avait abattu des Mallorns.  

Compétences : forestry, herbalism

### Autres ressources

Les chevaux peuvent également être capturés à volonté avec l'ordre [[cmd-make|`MAKE horse`]].
Sans aide, seuls les chevaux sauvages se reproduisent.
Il est toutefois possible de faire naître d'autres chevaux dans une [Stable].
Les chevaux sauvages aiment l'espace et la liberté, c'est pourquoi certains d'entre eux migrent vers les régions voisines lorsque les chevaux y sont moins nombreux.

Expérience de jeu (Solthar):

The maximal amount of horses in a region equals the number of [[world|jobs]] / 10.

In a relatively empty plain they grow at a rate of 4%.
As they approach the upper limit, growth slows down.
The most new horses are born at about half the maximal population.
In a plain with 25 horses, there is 1 birth per week.
With 500 horses there are 10 new horses per round.
At 1000 horses there is no more growth.

On peut également récolter des plantes pour concocter des potions.
Il y a au maximum une espèce de plante dans chaque région.
Voir la [liste des plantes].

## Voir aussi

- [[production]]
- [[objets]]
- [[routes]]
- [[batiments]]

Poursuivre la lecture : [[objets]].

<!-- From [https://wiki.eressea.de/index.php?title=Rohstoffe/fr&oldid=16659] -->

[Herbalism]: ./skills-list.md#herboristerie
[Stable]: ./buildings-others.md#haras
[liste des plantes]: ./herbs.md#liste-des-plantes
