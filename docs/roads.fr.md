---
# cSpell:locale fr
alias: routes
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# Routes

## Utilité

Les routes permettent de se déplacer plus facilement, car entretenues, elles ne s'embourbent pas en cas de pluie, ne sont pas envahies par la forêt ni les rivières, et les ravins sont enjambés par des ponts.  

Elles augmentent la vitesse de déplacement par voie terrestre.  
Pour qu'une route soit praticable, elle doit être complètement construite.  

## Construction

Dans chaque région, on peut construire une route vers les six points cardinaux, tant que la région de destination n'est pas un océan.  
Pour qu'une route soit complète, il doit y avoir une route dans la région de la direction correspondante dans la direction opposée.  
Par exemple, si l'on construit une route vers le nord-est dans une région, il faut aussi construire une route vers le sud-ouest dans la région voisine.  
Pour construire des routes, il faut un niveau minimum de 1 en [construction de routes][construction-de-routes]{title="Roadwork"}
et on peut augmenter la route d'une pierre par niveau en construction de routes (et par personne dans l'unité).  

Le tableau suivant indique combien de pierres sont nécessaires par direction.  
De plus, certaines régions sont tellement inhospitalières qu'il faut au préalable construire un [bâtiment][bâtiments].  
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

| Terrain                                        | Pierres | Bâtiment                        |
|------------------------------------------------|--------:|---------------------------------|
| [Désert][desert-fr-id]{title="Desert"}         |     100 | [Caravansérail][caravanserail]  |
| [Forêt][foret]{title="Forest"}                 |      50 | --                              |
| [Glacier][glacier-fr-id]{title="Glacier"}      |     250 | [Tunnel][tunnel-fr-id]          |
| [Haut-plateau][haut-plateau]{title="Highland"} |     100 | --                              |
| [Marais][marais]{title="Swamp"}                |      75 | [Barrage][barrage]{title="Dam"} |
| [Montagne][montagne]{title="Mountain"}         |     250 | --                              |
| [Plaine][plaine]{title="Plain"}                |      50 | --                              |
| [Volcan][volcan]{title="Volcano"}              |     250 | --                              |

Poursuivre la lecture : [bateaux][bateaux-id].

<!-- From [https://wiki.eressea.de/index.php?title=Straße/fr&oldid=15940] -->

[bâtiments]: [[batiments-speciaux]]
