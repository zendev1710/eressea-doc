# FOLLOW

**`FOLLOW`**` UNIT `*`unit-ID`*  
**`FOLLOW`**` SHIP `*`ship-ID`*`[`*`vitesse`*`]`

Peut être utilisé pour suivre une unité ou un bateau

Avec `FOLLOW UNIT`*`unit-id`*, votre propre unité "surveillera" l'unité spécifiée et la suivra lorsqu'elle se déplacera. Cependant, si l’unité poursuivie est plus rapide que l’unité poursuivante, elle échappe à la poursuite. Les poursuivants suivent l'unité poursuivie aussi loin que possible. Les unités voyageant par bateau ne peuvent pas être suivies avec `FOLLOW UNIT`. Les capitaines ne peuvent pas non plus l'utiliser pour déplacer leur navire. Au lieu de cela, ils abandonneraient le navire et suivraient l'unité à pied si possible.

Si l'unité poursuivie n'a pas émis d'ordre de mouvement (cela inclut `MOVE, ROUTE, RIDE, FOLLOW`, mais pas `PIRACY`), l'unité poursuivante peut exécuter son ordre long.

Avec `FOLLOW SHIP`*`ship-id`* vous pouvez suivre les navires qui ont traversé la région au cours du tour en cours ou précédent. Si le capitaine a donné l'ordre `FOLLOW SHIP`*`ship-id`*, le navire suivra alors la route du navire spécifié jusqu'à ce qu'il soit rattrapé - si votre propre navire est suffisamment rapide. Si le paramètre optionnel « Vitesse » est spécifié, le navire poursuivant naviguera au maximum dans ce nombre de régions.

Attention, vous ne pouvez pas suivre les navires qui ont comme ordre `FOLLOW SHIP` ou `PIRACY`.

`FOLLOW SHIP`, comme `FOLLOW UNIT`, n'est un ordre longu que si la cible a un ordre de déplacement et remplace ensuite toutes les autres ordres longs.

`FOLLOW` ne dure que pendant le tour au cours duquel la commande est donnée. Si la commande doit durer plus longtemps, elle doit être précédée d'un `@`.

    UNIT 87b6
      @FOLLOW UNIT hz7
      ENTERTAIN

L'unité 87b6 surveillera l'unité hz7 et la suivra dans ses mouvements. Sinon, elle gagnera de l'argent grâce au divertissement. Avec le `@` les deux commandes sont conservées.

Expérience de jeu : SoltharEs ist möglich, mit einer Einheit A einer Einheit B zu folgen, die ihrerseits einer dritten Einheit C folgt. Das hat jedoch zur Folge, dass A keinen langen Befehl mehr ausführt, denn der Server nimmt zu diesem Zeitpunkt an, dass Einheit B sich ebenfalls bewegt, unabhängig davon, ob Einheit C sich ebenfalls bewegt.

Es ist nicht möglich, sinnvoll mehrere FOLGE-Befehle zu geben. Es wird immer nur der erste ausgeführt.

## Voir aussi

- [Voyager]
- [MOVE]
- [ROUTE]
- [RIDE]
- [CARRY]
- [PIRACY]

<!-- Récupéré depuis [https://wiki.eressea.de/index.php?title=FOLGE/fr&oldid=8283] -->

[Kategorie][]:

- [Befehle/fr]

  [Voyager]: /Spezial:Meine_Sprache/Reisen "Spezial:Meine Sprache/Reisen"
  [MOVE]: /Spezial:Meine_Sprache/NACH "Spezial:Meine Sprache/NACH"
  [ROUTE]: /Spezial:Meine_Sprache/ROUTE "Spezial:Meine Sprache/ROUTE"
  [RIDE]: /Spezial:Meine_Sprache/FAHRE "Spezial:Meine Sprache/FAHRE"
  [CARRY]: /Spezial:Meine_Sprache/TRANSPORTIERE "Spezial:Meine Sprache/TRANSPORTIERE"
  [PIRACY]: /Spezial:Meine_Sprache/PIRATERIE "Spezial:Meine Sprache/PIRATERIE"
  [https://wiki.eressea.de/index.php?title=FOLGE/fr&oldid=8283]: https://wiki.eressea.de/index.php?title=FOLGE/fr&oldid=8283
  [Kategorie]: /Spezial:Kategorien "Spezial:Kategorien"
  [Befehle/fr]: /index.php?title=Kategorie:Befehle/fr&action=edit&redlink=1 "Kategorie:Befehle/fr (Seite nicht vorhanden)"
