---
# cSpell:locale fr, en
alias: cmd-give-fr
---
# GIVE

**`GIVE`**` `*`ID-unité`*`HERBS`  
**`GIVE`**` `*`ID-unité`*`COMMAND`  
**`GIVE`**` `*`ID-unité`*`UNIT`  
**`GIVE`**` `*`ID-unité quantité`*`MEN`  
**`GIVE`**` `*`ID-unité quantité objet`*  
**`GIVE`**` `*`ID-unité quantité SHIP`*  
**`GIVE`**` `*`ID-unité`*`ALL MEN`  
**`GIVE`**` `*`ID-unité`*`ALL`  
**`GIVE`**` `*`ID-unité`*` ALL `*`objet`*  
**`GIVE`**` `*`ID-unité`*` EACH `*`quantité`*` `*`objet`*  
**`GIVE`**` 0 `*`quantité`*`MEN`  
**`GIVE`**` 0 `*`quantité`*`SHIP`  
**`GIVE`**` 0 `*`quantité objet`*  

L'unité transfère des objets, le commandement de bateaux ou de bâtiments, des personnes, des bateaux ou même elle-même à d'autres unités.

## Objets

Avec `GIVE` les unités peuvent donner toutes les marchandises qu'elles possèdent à d'autres unités.
La condition est que l'unité indiquée accepte des choses.
C'est le cas si elle appartient à la même faction ou à une faction alliée (`HELP GIVE`), ou si elle a donné ce tour-ci l'ordre [[cmd-contact]] pour l'unité donatrice.
Les unités de monstres et certaines unités de joueurs avec des races de monstres n'acceptent rien non plus.
Ceux qui veulent simplement se débarrasser d'objets peuvent aussi les donner aux paysans ou les jeter dans l'océan (`GIVE 0`*`quantité" "objet`*).
Les personnes, les Silver et les chevaux augmentent respectivement la réserve de paysans, de Silver et de chevaux d'une région (terrestre). Tous les autres objets disparaissent.

L'unité donatrice et l'unité réceptrice doivent bien entendu se trouver dans la même région.
Le transfert fonctionne également en haute mer, entre bateaux et de bateau à la terre ferme et inversement.

<!-- TODO: translate in french -->
Instead of a number you can also use the parameter `ALL`.
`GIVE`*`unit-id`*`ALL Swords`, for example, hand over all the swords that the unit has at the time.
`GIVE`*`unit-id`*`ALL` hands over all items, herbs, potions and silver, but not the people in the unit.
With`GIVE`*`unit-id`*`herb` all herbs that the unit has are handed over.
You give the order explicitly `GIVE`*`unit-id`*`ALL MEN`, all people are handed over and the unit is dissolved.

!!! warning "Caution"
    All items and silver that come with `GIVE` have been handed over, are automatically reserved and can no longer be passed on from the material pool!
    Also `GIVE` uses the [[items-pool]], except in the context of GIVE EVERYTHING, where the unit only gives its own, unreserved items.

The variant `GIVE xyz JE` hands over *number* items per person in the target unit.
For example, if the unit xyz has 10 people, with `GIVE xyz JE 20 Silver` order, it transfers her 200 Silver.

!!! tip
    With `@GIVE` you can set up automatic transfers.
    For example, a unit with `@GIVE abc ALL Iron` hand over all the iron to the *abc* unit every week.

    ```
    GIVE k3f 300 Silver
    ; Gives the unit k3f 300 Silver.

    GIVE 0 5 Stone
    ; Discard 5 stones.

    GIVE TEMP 3 7 MEN
    ; Gives 7 people to the newly created unit TEMP 3.
    ```

!!! Caution
    Between `MAKE TEMP` and `END` there are orders for the new unit - and it has no money.
    So the following **doesn't work**:

    ```
    MAKE TEMP 1
        GIVE TEMP 1 200 Silver  ;  Pointless!
        RECRUIT 2
        MOVE WEST
    END
    ```

    Instead, it needs to be written like this:

    ```
    GIVE TEMP 1 200 Silver
    MAKE TEMP 1
        RECRUIT 2
        MOVE WEST
    END
    ; GIVE TEMP 1 200 Silver  ;  or here!
    ```

## People and units

If you want to bring people from different units together, this is done with `GIVE`*`unit-id`*`anzahl MEN`.
**The [[skills]] are then mixed up**, and you **shouldn't forget the items**, as they may go to the farmers if the unit runs out of people.

Player experience (Solthar):

If you want to hand over people to a unit of another faction, a simple HELP GIVE is not enough;
the receiving unit must CONTACT the transferring unit.
In addition, if the receiving unit is a [migrant unit], it must not have any people at the time of transfer.
Ideally it should be an empty TEMP unit. Example:

    ```
    UNIT a; Faction X
    GIVE TEMP x ALL MEN
    UNIT b; Faction Y
    MAKE TEMP x
    CONTACT UNIT a
    END
    ```

With `GIVE`*`unit-id`*`UNIT` the complete unit with all items is given to another faciton, i.e. it switches to the faction of the recipient unit and is not added to the recipient unit!
The unit does not carry out any further orders during the turn!

## Commandement

If the unit also has a ship or building under its command - i.e. if it is the first listed unit in the ship or building - it can also pass command to another unit.
The unit in command determines which other units are allowed to enter the ship or building.

`GIVE unit COMMAND` should always be used, even if the unit with the command leaves the ship or building and the following unit is to receive the command.
The order of the units during the evaluation is not always that of the report.
New owners of a building are placed in the first position in the building at the end of the round and may therefore only benefit from the building in the following round (e.g. mining bonus).
The command cannot be given to units without people (e.g. after a battle or "empty" TEMP units).

## Convoi

With `GIVE`*`unit-id`*` `*`number`*`SHIP` the owner of a ship or convoy hands over the number of ships.
The transferring and receiving units must belong to the same faction; HELP ALL or CONTACT is not sufficient.
If the other unit also owns a ship, a [convoy] is formed.
Convoys always consist of ships of the same type.
Boats cannot form convoys and the ships must be on the same coast.

## Voir aussi

- [[cmd-reserve]]
- [[items-pool]]
- [[ships]]
- [[buildings]]

<!-- From [https://wiki.eressea.de/index.php?title=GIVE/fr&oldid=15993] -->

[migrant unit]: ./races.md#humains
[convoy]: ./ships.md#convoi
