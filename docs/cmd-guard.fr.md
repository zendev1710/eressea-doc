---
# cSpell:locale fr
alias: cmd-guard-fr
---

# GUARD

**`GUARD`**`[NOT]`

Les unités peuvent garder leur région.  
Pour cela, elles doivent être [armées et prêtes au combat][arme-et-pret-au-combat], c'est à dire équipées d'au moins une [arme][armes-tableau-de-synthese] et posséder la compétence de maniement de l'arme appropriée.  

!!! note
    Les régions océaniques ne peuvent être gardées.  

## Garde d'une région par une faction non alliée

Lorsqu'une faction garde une région, les unités qui ne lui sont pas alliées sont soumises aux [alliances][alliances-fr-id] ([`HELP GUARD`][cmd-help-fr] ou [`CONTACT`][cmd-contact-fr]).  
Ainsi, si tes unités sont dans cette situation (non alliées), les restrictions suivantes s'appliquent :

1. Il n'est plus possible de collecter les taxes, d'extraire des matières premières, de [faire du commerce][le-commerce] ou de recruter des agriculteurs dans cette région
2. Il y a une certaine probabilité que tes unités en mouvement soient stoppées
3. Si ton unité est sur un navire, elle ne pourra pas [travailler][cmd-work-fr], [divertir][cmd-entertain-fr], ou [attaquer][cmd-attack-fr], ni se déplacer immédiatement par voie terrestre.
  Afin de pouvoir réaliser ces actions la semaine suivante, elle devra d'abord [quitter][cmd-leave-fr] le bateau

Si l'unité n'est pas visible, parce qu'elle possède une compétence de [discrétion][skill-discretion-id]{title="Stealth"} de niveau supérieur à la meilleure compétence de perception de la faction de garde dans la région, les deux premières restrictions ne s'appliquent pas.

Dans tous les cas, il est tout à fait possible de [divertir][silver-divertissement-id]{title="Entertainment"} à terre dans une région gardée, même si le gardien n'a pas activé l'ordre `HELP GUARD`.  
Cela n'est pas possible si l'unité de divertissement se trouve à bord d'un bateau.  

Dans le tour au cours duquel l'ordre  `GUARD` a été donné, toutes ces restrictions ne s'appliquent pas encore, car l'unité de garde doit d'abord découvrir où les unités étrangères pourraient collecter de l'argent, etc.  
L'unité de garde devient immédiatement visible par toutes les autres unités de la région, quel que soit son niveau de furtivité.

## Gardes multiples dans une région

Si plusieurs factions donnent l'ordre `GUARD` en même temps ou les uns après les autres, ils gardent tous la région.
Pour les factions où **tout le monde** garde, les factions sont alliées, et les restrictions ci-dessus ne s'appliquent pas.

Les factions avec **au moins un** garde allié peuvent continuer à exécuter les ordres (éventuellement avec les exceptions ci-dessus) pendant une longue période malgré les combats (voir [Fin de bataille][fin-du-combat]).

## Dissolution de la garde

Avec `GUARD NOT`, le statut de garde d'une unité est dissous.  
Cela se produit également lorsque l'unité est en mouvement.  
Les unités avec le statut de combat [`COMBAT FLEE`][cmd-combat-fr] ne peuvent pas garder, et les unités dont tous les survivants fuient pendant le combat cessent également de garder.  

## Garde et mouvement

Lorsqu'une unité traverse une région gardée par au moins une faction non alliée, la probabilité d'être stoppée dans son mouvement dépend de plusieurs facteurs.  

La probabilité d'être stoppée augmente avec :

- le nombre de gardes ennemis
- le type de région (la probabilité est moindre dans les marais, les glaciers, les montagnes et les volcans)
- la compétence de perception des gardes ennemis
- l'utilisation d'une Amulette de Vision Décuplée
- la taille du château du propriétaire de la région s'ils n'est pas un allié

La probabilité d'être stoppée décroît avec :

- le nombre de gardes alliés
- la compétence de furtivité de l'unité en mouvement
- l'utilisation d'un [anneau d'Invisibilité][anneau-d-invisibilite-id]

## Particularités

!!! note
    Les [Monstre][monstres] (ii) sont généralement considérés comme armés en raison de leurs griffes, dents et autres extrémités, même si elles ne portent pas d'arme visible.  
    Cela s'applique également aux monstres invoqués par magie par les joueurs

Au cours des [premières semaines][puppy-protection], une faction ne peut pas encore assurer la garde.

## Voir aussi

- [`HELP GUARD`][cmd-help-fr]
- [Les alliances][alliances-fr-id]
- [`CONTACT`][cmd-contact-fr]

<!-- From [https://wiki.eressea.de/index.php?title=GUARD&oldid=16839] -->

[cmd-attack-fr]: [[cmd-attack-fr]]
[cmd-combat-fr]: [[cmd-combat-fr]]
[cmd-contact-fr]: [[cmd-contact-fr]]
[cmd-entertain-fr]: [[cmd-entertain-fr]]
[cmd-help-fr]: [[cmd-help-fr]]
[cmd-leave-fr]: [[cmd-leave-fr]]
[cmd-work-fr]: [[cmd-work-fr]]
