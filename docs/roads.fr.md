---
# cSpell:locale fr, en
alias: routes
---
# Routes

Les *routes* augmentent la vitesse de déplacement sur terre. Pour cela, il faut qu'il y ait une route complète entre la région de départ et la région d'arrivée. Ces routes permettent de se déplacer facilement, car elles ne s'embourbent pas en cas de pluie, ne sont pas envahies par la forêt et les rivières et les ravins sont enjambés par des ponts.

Dans chaque région, on peut construire une route vers les six points cardinaux, tant que la région de destination n'est pas un océan. Pour qu'une route soit complète, il doit y avoir une route dans la région de la direction correspondante dans la direction opposée. Par exemple, si l'on construit une route vers le nord-est dans une région, il faut aussi construire une route vers le sud-ouest dans la région voisine. Pour construire des routes, il faut un niveau minimum de 1 en Roadwork et on peut augmenter la route d'une pierre par niveau en Roadwork (et par personne dans l'unité).

Le tableau suivant indique combien de pierres sont nécessaires par direction. De plus, certaines régions sont tellement inhospitalières qu'il faut au préalable construire un [bâtiment]. Celui-ci doit fonctionner au moment de la construction, c'est-à-dire qu'il doit être terminé et que son entretien doit être payé. La route terminée fonctionne même sans que l'entretien soit payé.

**Exemple:** Pour construire une route depuis la plaine en (0,0) jusqu'à la montagne en (1,1) en passant par le marais en (1,0), tu as besoin de

- en (0,0) 50 stones pour `MAKE Road E`
- en (1,0) un dam (barrage) opérationnel pendant la construction et coûtant 1000 silver et 3 wood par tour.
- en (1,0) 75 stones pour `MAKE Road W`
- en (1,0) 75 stones pour `MAKE Road NE`
- en (1,1) 250 stones pour `MAKE Road SW`

Ensuite, une unité peut voyager à pied de (0,0) à (1,1) en un tour avec `MOVE E NE`.

Construction de routes

| Terrain      | Pierres | bâtiment       |
|--------------|--------:|----------------|
| Plain/Forest |      50 | --             |
| Highland     |     100 | --             |
| Mountain     |     250 | --             |
| Volcano      |     250 | --             |
| Swamp        |      75 | [Dam]          |
| Desert       |     100 | [Caravanserai] |
| Glacier      |     250 | [Tunnel]       |

[Dam]: ./buildings-others.md#barrage
[Caravanserai]: ./buildings-others.md#caravanserail
[Tunnel]: ./buildings-others.md#tunnel  

Poursuivre la lecture : [Bateaux].

[Bateaux]: ./ships.md

<!-- From [https://wiki.eressea.de/index.php?title=Straße/fr&oldid=15940] -->

[bâtiment]: ./buildings-others.md
