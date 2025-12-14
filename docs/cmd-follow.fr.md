# FOLLOW

**`FOLLOW`**` UNIT `*`unit-ID`*  
**`FOLLOW`**` SHIP `*`ship-ID`*`[`*`vitesse`*`]`

Peut être utilisé pour suivre une unité ou un bateau

Avec `FOLLOW UNIT`*`unit-id`*, votre propre unité "surveillera" l'unité spécifiée et la suivra lorsqu'elle se déplacera. Cependant, si l’unité poursuivie est plus rapide que l’unité poursuivante, elle échappe à la poursuite. Les poursuivants suivent l'unité poursuivie aussi loin que possible. Les unités voyageant par bateau ne peuvent pas être suivies avec `FOLLOW UNIT`. Les capitaines ne peuvent pas non plus l'utiliser pour déplacer leur bateau. Au lieu de cela, ils abandonneraient le bateau et suivraient l'unité à pied si possible.

Si l'unité poursuivie n'a pas émis d'ordre de mouvement (cela inclut `MOVE, ROUTE, RIDE, FOLLOW`, mais pas `PIRACY`), l'unité poursuivante peut exécuter son ordre long.

Avec `FOLLOW SHIP`*`ship-id`* vous pouvez suivre les bateaux qui ont traversé la région au cours du tour en cours ou précédent. Si le capitaine a donné l'ordre `FOLLOW SHIP`*`ship-id`*, le bateau suivra alors la route du bateau spécifié jusqu'à ce qu'il soit rattrapé - si votre propre bateau est suffisamment rapide. Si le paramètre optionnel « Vitesse » est spécifié, le bateau poursuivant naviguera au maximum dans ce nombre de régions.

Attention, vous ne pouvez pas suivre les bateaux qui ont comme ordre `FOLLOW SHIP` ou `PIRACY`.

`FOLLOW SHIP`, comme `FOLLOW UNIT`, n'est un ordre longu que si la cible a un ordre de déplacement et remplace ensuite toutes les autres ordres longs.

`FOLLOW` ne dure que pendant le tour au cours duquel la commande est donnée. Si la commande doit durer plus longtemps, elle doit être précédée d'un `@`.

    UNIT 87b6
      @FOLLOW UNIT hz7
      ENTERTAIN

L'unité 87b6 surveillera l'unité hz7 et la suivra dans ses mouvements. Sinon, elle gagnera de l'argent grâce au divertissement. Avec le `@` les deux commandes sont conservées.

Expérience de jeu : SoltharEs ist möglich, mit einer Einheit A einer Einheit B zu folgen, die ihrerseits einer dritten Einheit C folgt. Das hat jedoch zur Folge, dass A keinen langen Befehl mehr ausführt, denn der Server nimmt zu diesem Zeitpunkt an, dass Einheit B sich ebenfalls bewegt, unabhängig davon, ob Einheit C sich ebenfalls bewegt.

Es ist nicht möglich, sinnvoll mehrere FOLLOW-Befehle zu geben. Es wird immer nur der erste ausgeführt.

## Voir aussi

- [Voyager]
- [[cmd-move]]
- [[cmd-route]]
- [[cmd-ride]]
- [[cmd-carry]]
- [[cmd-piracy]]

<!-- From [https://wiki.eressea.de/index.php?title=FOLLOW/fr&oldid=8283] -->

[Voyager]: ./travel.md "Reisen"
[MOVE]: ./cmd-move.md "MOVE"
[ROUTE]: ./cmd-route.md "ROUTE"
[RIDE]: ./cmd-ride.md "RIDE"
[CARRY]: ./cmd-carry.md "CARRY"
[PIRACY]: ./cmd-piracy.md "PIRACY"
