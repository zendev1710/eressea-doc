---
# cSpell:locale en
alias: cmd-guard
---
# GUARD

**`GUARD`**`[NOT]`

Units can guard their region.
To do so, the unit must be [[armed]] with at least one [weapon] and possess the appropriate weapon skill.

!!! note
    Ocean regions cannot be guarded.

When a faction is guarding a region, units that are not allied with it are subject to [[alliances|alliances]] ([[cmd-help|`HELP GUARD`]] or [[cmd-contact]]), with the following restrictions:

1. You can no longer collect taxes, mine raw materials, [trade] or recruit farmers in this region
2. There is a certain probability that you will be stopped in transit
3. If you are on a ship, you cannot [[cmd-work]], [[cmd-entertain]], [[cmd-attack]] or move overland immediately.
   In order to be able to carry out the actions the following week, you must first [[cmd-leave]] the ship

If the unit is not seen, for example because it has a higher Stealth skill than the guarding faction's best Perception skill in the region, the first two restrictions do not apply.

However, it is very possible to [entertain] on land in a guarded region, even if the guard has not set `HELP GUARD`.  
This is not possible if the entertainer unit is on board a ship.  

If several factions give the `GUARD` order at the same time or one after the other, they all guard the region.  
For factions with **everyone** guarding, factions are allied, and the above restrictions do not apply.  

Factions with **at least one** allied guard can continue to carry out orders (possibly with the exceptions above) for a long time despite fighting (see [End of battle]).

In the round in which the `GUARD` order has been given, all of these restrictions do not apply yet, because the guarding unit first has to find out where foreign units could collect silver, etc.  
The guarding unit immediately becomes visible to all other units in the region, regardless of how high its stealth skill is.

With `GUARD NOT` the guard status of a unit is dissolved.  
This also happens when the unit is moving.  
Units with the combat status [[cmd-combat|COMBAT FLEE]] cannot guard, and units from which all survivors flee during combat also stop guarding.  

When a unit travels through a region guarded by at least one non-allied faction, the chance of being stopped depends on several factors.

It is increased by :

- the number of enemy guards
- the region type (it becomes more difficult in swamps, glaciers, mountains and volcanoes)
- the perception skill of the enemy guards
- the use of an Amulets of True Seeing
- the size of the region owner's castle if he is not an ally

It is reduced by :

- the number of allied guards
- the moving unit's stealth skill
- the use of a [[ring-of-invisibility]]

!!! note
    [[monsters|Monster]] faction (ii) units are generally considered armed due to their claws, teeth and other extremities, even if they do not carry a visible weapon.  
    This also applies to monsters magically summoned by players.

In the [[puppy-protection|first few weeks]] a faction cannot guard yet.

## See also

- [[cmd-help|`HELP GUARD`]]
- [[alliances]]
- [[cmd-contact]]

<!-- From [https://wiki.eressea.de/index.php?title=GUARD&oldid=16839] -->

[weapon]: ./war-tables.md#weapons-summary-table
[trade]: ./silver.md#trade
[End of battle]: ./war.md#the-end
[entertain]: ./skills-list.md#entertainment
