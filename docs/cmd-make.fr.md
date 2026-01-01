---
# cSpell:locale fr, en
alias: cmd-make-fr
---
# MAKE

**`MAKE TEMP`**` `*`unit-alias-id`*`["`*`nom`*`"]`  
**`MAKE`**`[`*`niveau`*`]`*`type_batiment`*`[`*`id_batiment`*`]`  
**`MAKE`**`[`*`niveau`*`]`*`type_bateau`*  
**`MAKE`**`[`*`niveau`*`] SHIP [`*`bateau-id`*`]`  
**`MAKE`**`[`*`niveau`*`] Road`*`direction`*  
**`MAKE`**`[`*`quantité`*`] HERBS`  
**`MAKE`**`[`*`quantité`*`]`*`objet`*  

L'ordre `MAKE` est l'ordre de production général. Pour en savoir plus, voir le chapitre [[production]].

## Objets

[[items]] and [[resources|raw materials]] are created with `MAKE [`*`number`*`]`*`item`*` `. Depending on the item, a certain skill and perhaps also certain raw materials are required. Without specifying *number*, the unit will produce as many items as people, skill and possibly raw materials allow it to.

### Potions

Creating a potion is very complex and can only be done by particularly talented alchemists. Details can be found in the [[alchemy|Alchemy chapter]].

### Plantes

Herbs are produced with the `MAKE HERBS` order by units with the [herbalism] skill. For details, see the chapter on [[herbs]].

## Unités

When you create a new unit (`MAKE TEMP xy`), you assign it an alias number, because at that time you do not know yet, what the actual number will be. For all other order, you can reference the unit by this alias (including the word TEMP, for example `GIVE TEMP xy 100 silver`). When looking for a TEMP unit, your own faction is searched first, then other factions. So if you and another faction both have a unit with the ID *TEMP xy*, your own unit will always be chosen. So with a little coordination, TEMP units from other parties can also be addressed.

The alias number will be used as the new number of the unit if it is not taken. You can also assign a name to the new unit. The orders

```text
MAKE TEMP 1
    NAME UNIT "Clowns"
    NUMBER UNIT funy
```

can be shortened to :

```text
MAKE TEMP funy "Clowns"
```

A maximum of 2500 units are allowed per party. If the party has 2500 or more units, no new units can be created with `MAKE TEMP`; other units must first be deleted, e.g. by merging them. As the deletion of empty units comes at the end of the command sequence, new TEMP units can only be created in the following week.

The orders following the MAKE TEMP order are assigned to the new unit up to the END order.

However, the new unit must still have members, otherwise it will be silently deleted at the end of the round! It must therefore recruit or be given people. If the new unit is to recruit new members, it must also receive enough money to do so. If it does not receive this, the unit will not be able to recruit anyone and will be silently removed at the end of the week. If the unit receives money but does not recruit any members, it is also disbanded and the money falls to [other units of their own faction].

```text
UNIT 17;       Fighters [15,700$]
MAKE TEMP 1
   NAME UNIT "dragon riders"
   LEARN melee
END
GIVE TEMP 1 5 MEN
 
GIVE TEMP 2 100 silver
MAKE TEMP 2
   RECRUIT 1
   NAME UNIT "scouts"
   DEFAULT "LEARN perception"
   MOVE west
END
```

## Bâtiments

To erect a new building, use the order `MAKE [`*`levels`*`]`*`building_type`* (see [[buildings]]). To continue building, the order is `MAKE [levels]`*`building_type`*` `*`building_id`*. The *building type* can also be replaced by CASTLE when continuing to build, even if it is a different type of building.

Castles and many other buildings can be enlarged as much as you want. In order to build castles, the unit must have the masonry skill and stones; other buildings usually also require wood, iron, and silver in various quantities.

## Bâteaux

With `MAKE`*`ship_type`* a unit starts building a new [[ships|ship]]. This requires the shipcraft skill and wood. It can continue building with `MAKE [`*`levels`*`] SHIP`*`ship-nr`*. Ships cannot be expanded like castles; the type is determined at the start of construction. Ships can only be built up to the size specified by their type.

With buildings as well as ships you can specify with *levels* how many size points you would like to add to the ship.

- first week: `MAKE longboat`  
  A new ship is constructed and gets the number 76 from the server.
- second week: `MAKE SHIP 76`  
  Continue building the ship with the number 76.

## Routes

To make it easier to travel through a region with roads and bridges, use `MAKE ROAD`*`direction`*. To build [[roads]], the unit needs the skill [roadwork] and [[items|stones]]. In glaciers, it needs a [tunnel] beforehand, in deserts a [caravanserai] and in swamps a [dam]. One stone is used per skill point of road construction. Between 50 and 250 stones are required for each desired direction, depending on the [[terrain-types]]. Roads only work if they are complete.

Player experience: Solthar Except when erecting a new building you can exchange the type in MAKE type xyz with BURG or any other building type.

`MAKE type` or `MAKE SHIP` without further parameters is currently continuing construction on the building or ship in which the unit is currently located. **Attention:** If the unit is in a building, MAKE lighthouse does not start a new building, but continues building on the old one.

## Exemples

```text
MAKE 5 sword ; produces 5 swords (at most)
MAKE water~of~life ; produces as much of the potion as raw materials and skill allow
MAKE HERBS
LEAVE
MAKE lighthouse ; starts building a new lighthouse
MAKE lighthouse xyz ; expands the lighthouse xyz
LEAVE
MAKE CASTLE xyz ; continues building on xyz (of whatever building type)
MAKE 5 Trireme ; starts a new trireme
MAKE SHIP abc ; continues building the ship abc
MAKE ROAD SE ; continues or starts building the road towards the south-east
MAKE Trireme abc ; wrong: starts a new trireme
MAKE building xyz ; wrong: only CASTLE or building type is allowed
```

## Voir aussi

- [[production]]
- [[alchimie|Alchimie]]

<!-- From [https://wiki.eressea.de/index.php?title=MAKE/fr&oldid=16448] -->

[herbalism]: ./skills-list.md#herboristerie
[other units of their own faction]: ./factions.md#dissolution-des-unites
[roadwork]: ./skills-list.md#construction-de-routes
[tunnel]: ./buildings-others.md#tunnel
[caravanserai]: ./buildings-others.md#caravanserail
[dam]: ./buildings-others.md#barrage
