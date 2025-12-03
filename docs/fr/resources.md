# Ressources

Les matières premières peuvent être obtenues directement à partir des réserves des [Régions] sans aucun autre ingrédient. Les ressources sont toutefois limitées et ne se régénèrent que lentement, voire pas du tout. La compétence requise est indiquée dans le tableau de la section [objets].

## Exploitation des ressources

Lors de l'exploitation des ressources, il est important considérer que les unités en [garde] empêchent l'exploitation, si les factions en garde n'ont ni [`HELP GUARD`]` ni `[`HELP ALL`][`HELP GUARD`]` avec votre faction ou donné l'ordre `[`CONTACT`]` avec l'unité ou la faction qui exploite. Ceci ne s'applique pas si la faction en garde ne voit pas le producteur, par exemple parce qu'il est `[`camouflé`]`.`

` `

### Ressources minières

Le fer, la pierre, le laen et, dans les régions particulièrement anciennes, parfois même l'adamantium, peuvent être extraits des montagnes, des glaciers et parfois d'autres types de régions. Le laen et l'adamantium nécessitent une mine et une compétence en Mining particulièrement élevée. Ces ressources peuvent être difficiles à extraire. Dans votre rapport vous pouvez le savoir suivant le nombre après le "/". Par exemple, si le rapport indique « 20 iron/4 », cela signifie que 20 fers avec un niveau de compétence 4 peuvent encore être extraits. Une fois ceux-ci extraits, les mineurs auront besoin d'être niveau 5 pour extraire du fer de la couche suivante (5). En général, les quantités pouvant être extraites augmentent à chaque nouvelle couche. L'extraction nécessite les compétences Mining ou Quarrying selon la ressource.

### Ressources Forestières

Le développement de la végétation d'Eressea est déterminé par les saisons. Dès que les premiers rayons du soleil frappent le sol au printemps, les graines cachées dans le sol germent et les pousses d'arbres de l'année dernière se transforment en arbres adultes. S'il n'y a pas assez de soleil (pas d'espace de travail libre), les graines restent dormantes dans le sol. Pendant les mois d'été et d'automne, les arbres matures jettent leurs graines, qui peuvent être ramassées avec l'ordre [`MAKE`]`seed ou mallorn seed` et la compétence [Herbalism] de niveau minimun 3 ou 4 puis replanté ailleurs avec l'ordre [`PLANT`]`seed ou mallorn seed` (niveau minimum de 6 ou 7).

Si du bois ou du mallorn est abattu, la forêt se rétrécit et ne se reconstitue que très lentement. Tant qu'il y a suffisamment de bois, il peut être abattu en n'importe quelle quantité. Il en va de même pour le mallorn, un bois "magique" que l'on ne trouve que dans quelques régions. Le mallorn se reproduit certes comme le bois, mais les graines de mallorn ne poussent que dans les régions qui s'y prêtent. Dans les régions à Mallorn, la commande "MAKE wood" permet également d'abattre du bois à la place du Mallorn. Le nombre d'arbres de Mallorn est alors réduit d'autant que si l'on avait abattu des Mallorns. Compétences : forestry, herbalism

### Autres ressources

Les chevaux peuvent également être capturés à volonté avec l'ordre [`MAKE horse`][`MAKE`]. Sans aide, seuls les chevaux sauvages se reproduisent. Il est toutefois possible de faire naître d'autres chevaux dans une [Stable]. Les chevaux sauvages aiment l'espace et la liberté, c'est pourquoi certains d'entre eux migrent vers les régions voisines lorsque les chevaux y sont moins nombreux. Compétence : taming

Expérience de jeu : SoltharDie maximale Anzahl Pferde in einer Region entspricht der Anzahl der [Arbeitsplätze] / 10. In einer relativ leeren Region vermehren sie sich mit ca. 4%. Je näher sie dem Limit kommen, desto langsamer das Wachstum. Am schnellsten geht es bei ungefähr halben Besatz. In einer Ebene gibt es bei 25 Pferden jede Runde ein neues. Bei 500 Pferden kommen 10 pro Runde hinzu. Ab 1000 Pferden tut sich nichts mehr.

[Arbeitsplätze]: ./world.md "Welt"

On peut également récolter des plantes pour concocter des potions. Il y a au maximum une espèce de plante dans chaque région. Voir la [Liste des Plantes]. Compétences : Herbalism, Alchemy

## Voir aussi

- [Production]
- [Objets]
- [Routes]
- [Bâtiments]

|              |          |
|--------------|----------|
| Weiterlesen: | [objets] |

[objets]: ./items.md "Waren"

<!-- From [https://wiki.eressea.de/index.php?title=Rohstoffe/fr&oldid=16659] -->

[Régions]: ./world.md "Welt"
[garde]: ./cmd-guard.md "GUARD"
[`HELP GUARD`]: ./cmd-help.md "HELP"
[`CONTACT`]: ./cmd-contact.md "CONTACT"
[`camouflé`]: ./camouflage.md "Tarnung"
[`MAKE`]: ./cmd-make.md "MAKE"
[Herbalism]: ./skills-list.md "Liste des compétences"
[`PLANT`]: ./cmd-plant.md "PLANT"
[Stable]: ./buildings-others.md#pferdezucht "Pferdezucht"
[Liste des Plantes]: ./herbs.md#kräuterliste "Plantes"
[Production]: ./production.md "Produktion"
[Routes]: ./roads.md "Straßen"
[Bâtiments]: ./buildings.md "Gebäude"
