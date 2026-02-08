---
# cSpell:locale fr
alias: routes
---
# Routes

## Utilité

Les routes permettent de se déplacer plus facilement, car entretenues, elles ne s'embourbent pas en cas de pluie, ne sont pas envahies par la forêt ni les rivières, et les ravins sont enjambés par des ponts.  

Elles augmentent la vitesse de déplacement par voie terrestre.  
Pour qu'une route soit praticable, elle doit être complètement construite.  

## Construction

Dans chaque région, on peut construire une route vers les six points cardinaux, tant que la région de destination n'est pas un océan.  
Pour qu'une route soit complète, il doit y avoir une route dans la région de la direction correspondante dans la direction opposée.  
Par exemple, si l'on construit une route vers le nord-est dans une région, il faut aussi construire une route vers le sud-ouest dans la région voisine.  
Pour construire des routes, il faut un niveau minimum de 1 en [construction de routes] et on peut augmenter la route d'une pierre par niveau en construction de routes (et par personne dans l'unité).  

Le tableau suivant indique combien de pierres sont nécessaires par direction.  
De plus, certaines régions sont tellement inhospitalières qu'il faut au préalable construire un [bâtiment].  
Celui-ci doit fonctionner au moment de la construction, c'est-à-dire qu'il doit être terminé et que son entretien doit être payé.  
La route terminée fonctionne même sans que l'entretien soit payé.  

**Exemple:**

Pour construire une route depuis la plaine en (0,0) jusqu'à la montagne en (1,1), en passant par le marais en (1,0), vous avez besoin de :

- en (0,0) 50 pierre pour `MAKE Road E`
- en (1,0) un [barrage] opérationnel pendant la construction et coûtant 1 000 silver et 3 bois par tour.
- en (1,0) 75 pierre pour `MAKE Road W`
- en (1,0) 75 pierre pour `MAKE Road NE`
- en (1,1) 250 pierre pour `MAKE Road SW`

Ensuite, une unité peut voyager à pied de (0,0) à (1,1) en un tour avec `MOVE E NE`.

*Construction de routes.*

| Terrain        | Pierres | Bâtiment        |
|----------------|--------:|-----------------|
| [Désert]       |     100 | [caravansérail] |
| [Forêt]        |      50 | --              |
| [Glacier]      |     250 | [tunnel]        |
| [Haut-plateau] |     100 | --              |
| [Marais]       |      75 | [barrage]       |
| [Montagne]     |     250 | --              |
| [Plaine]       |      50 | --              |
| [Volcan]       |     250 | --              |

Poursuivre la lecture : [[bateaux]].

<!-- From [https://wiki.eressea.de/index.php?title=Straße/fr&oldid=15940] -->

[caravansérail]: ./buildings-others.md#caravanserail
[Tunnel]: ./buildings-others.md#tunnel
[bâtiment]: ./buildings-others.md
[barrage]: ./buildings-others.md#barrage "Dam"
[construction de routes]: ./skills-list.md#construction-de-routes "Roadwork"

[Désert]: ./terrains.md#desert "Desert"
[Forêt]: ./terrains.md#foret "Forest"
[Glacier]: ./terrains.md#glacier "Glacier"
[Haut-plateau]: ./terrains.md#haut-plateau "Highland"
[Marais]: ./terrains.md#marais "Swamp"
[Montagne]: ./terrains.md#montagne "Mountain"
[Plaine]: ./terrains.md#plaine "Plain"
[Volcan]: ./terrains.md#volcan "Volcano"
