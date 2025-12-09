# FOLLOW

**`FOLLOW`**` UNIT `*`unit-ID`*  
**`FOLLOW`**` SHIP `*`ship-ID`*`[`*`speed`*`]`

This can be used to follow units or ships.

With `FOLLOW UNIT`*`unit-ID`* your own unit will "watch" the specified unit and follow it when it moves. However, if the pursued unit is faster than the following unit, it escapes pursuit. The pursuers follow the pursued unit as far as possible. Units traveling by ship cannot be tracked with `FOLLOW UNIT`. Nor can captains use this to move their ship. Instead, they would abandon ship and follow the unit on foot if possible.

If the pursued unit has not issued a movement order (this includes `MOVE, ROUTE, RIDE, FOLLOW`, but not `PIRACY`), the pursuing unit can execute its long order.

With `FOLLOW SHIP`*`ship-id`* you can follow ships that have crossed the region in the current or previous round. If the captain has given the command `FOLLOW SHIP`*`ship-id`*, the ship will then follow the course of the specified ship until it is overtaken - if your own ship is fast enough. If the optional parameter *Speed* is specified, the pursuing ship will sail a maximum of this many regions.

Attention, you cannot follow ships that have `FOLLOW SHIP` or `PIRACY` as their command.

`FOLLOW SHIP`, like `FOLLOW UNIT`, is only a long order if the target has a move command and then replaces all other long order.

`FOLLOW` only lasts in the round in which the order is given. If the order is to last longer, it must be preceded by a `@`.

    UNIT 87b6
      @FOLLOW UNIT hz7
      ENTERTAIN

Unit 87b6 will now watch unit hz7 and follow it as it moves. Otherwise, she will make money from entertainment. With the `@` both commands are retained.

Player experience: Solthar Es ist möglich, mit einer Einheit A einer Einheit B zu folgen, die ihrerseits einer dritten Einheit C folgt. Das hat jedoch zur Folge, dass A keinen langen Befehl mehr ausführt, denn der Server nimmt zu diesem Zeitpunkt an, dass Einheit B sich ebenfalls bewegt, unabhängig davon, ob Einheit C sich ebenfalls bewegt.

Es ist nicht möglich, sinnvoll mehrere FOLLOW-Befehle zu geben. Es wird immer nur der erste ausgeführt.

## See also

- [Travel]
- [MOVE]
- [ROUTE]
- [RIDE]
- [CARRY]
- [PIRACY]

<!-- From [https://wiki.eressea.de/index.php?title=FOLLOW/en&oldid=8282] -->

[Travel]: ./travel.md "Reisen"
[MOVE]: ./cmd-move.md "MOVE"
[ROUTE]: ./cmd-route.md "ROUTE"
[RIDE]: ./cmd-ride.md "RIDE"
[CARRY]: ./cmd-carry.md "CARRY"
[PIRACY]: ./cmd-piracy.md "PIRACY"
