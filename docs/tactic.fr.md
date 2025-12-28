---
# cSpell:locale fr, en
alias: tactique
---
# Tactique

Avant la bataille, le meilleur tacticien de toutes les unités participantes est désigné. Le camp ayant le meilleur tacticien gagne ce que l'on appelle le "tour du tacticien" : par une manœuvre habile, il attire l'ennemi dans une embuscade et ses alliés peuvent frapper par surprise avant le premier tour de combat avec une certaine chance, sans que l'ennemi puisse aussi attaquer pendant ce tour. Si deux tacticiens ou plus de différents camps sont aussi bons l'un que l'autre, ils peuvent tous frapper lors du tour de tacticien. La chance de porter ce coup est de 10% pour chaque point de compétence entre le meilleur tacticien de son camp et le meilleur tacticien du camp adverse, bonus ou malus inclus. A partir d'une différence de compétence de 10, tous les alliés frappent une fois. Pour le rechargement, le tour du tacticien compte également, une arbalète qui a tiré pendant le tour du tacticien tire donc une deuxième fois au tour 3 au lieu du tour 4. Le tour de tactique permet également une tentative de fuite supplémentaire.

## Bonus de tactique en fonction de la situation

Un tacticien qui [combat] au premier rang reçoit un bonus de +1 à sa compétence de tactics. S'il se trouve en 3e ou 4e ligne, sa compétence est réduite de 1.

La compétence Tactics bénéficie également de quelques bonus raciaux qui dépendent du terrain :

| Race   | Terrain           | Bonus/Malus |
|--------|-------------------|:-----------:|
| Elf    | Forest            | +2          |
| Dwarf  | Mountain, Glacier | +1          |
| Insect | Swamps, Desert    | +1          |
|        | Mountain, Glacier | -1          |

Les insectes reçoivent également un bonus supplémentaire à la compétence Tactics lorsqu'ils apparaissent en masse.
Un tacticien insecte reçoit un bonus de log10(nombre de combattants dans son armée)-1 pour la tactique.
Cela peut aussi donner un malus si le nombre de combattants est très faible !

Important : seuls les combattants de l'armée comptent réellement. Il faut donc éviter de faire des groupes différents. Les troupes des alliés ne comptent pas.

| Nombre de combattants | 1-9 | 10-99 | 100-999 | 1000-9999 | 10000-99999 | 100000-999999 |
|-----------------------|:---:|:-----:|:-------:|:---------:|:-----------:|:-------------:|
| Bonus                 | -1  |   0   |   +1    |    +2     |     +3      |      +4       |
| Bonus                 | -1  |   0   |   +1    |    +2     |     +3      |      +4       |

## Inspiration

Afin d'introduire un peu "d'inspiration" et de chance, chaque tacticien reçoit un bonus aléatoire qui commence à 0 et peut devenir très important, avec une probabilité de plus en plus faible au fur et à mesure que le bonus augmente.
Si une unité de tacticiens est composée de plusieurs personnes, le dé est lancé une fois pour chaque personne.

| Probabilité | Bonus | Autre      |
|------------:|:-----:|------------|
|         40% |  +0   |            |
|         30% |  +1   |            |
|         20% |  +2   |            |
|          7% |  +3   |            |
|          3% |  +3   | roll again |

Il en résulte, selon le nombre de tacticiens, les bonus d'inspiration moyens suivants :

|                     |      |      |      |      |      |      |      |
|---------------------|------|------|------|------|------|------|------|
| Number of tactician | 1    | 3    | 12   | 44   | 129  | 410  | 1480 |
| Average Bonus       | 1,03 | 1,96 | 3,05 | 4,03 | 5,03 | 6,03 | 7,03 |

Cela signifie que 12 tacticiens de niveau X atteignent en moyenne le même niveau qu'un tacticien de niveau X+2. On peut donc (aussi) remplacer le manque de niveau des tacticiens par la masse, mais cela devient relativement vite très cher.

## Voir aussi

- [de la guerre]

<!-- From [https://wiki.eressea.de/index.php?title=Taktik/fr&oldid=13466] -->

[combat]: ./cmd-combat.md
[de la guerre]: ./war-tables.md#die-taktikerrunde
