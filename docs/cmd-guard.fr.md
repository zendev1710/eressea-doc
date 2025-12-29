---
# cSpell:locale fr, en
alias: cmd-guard-fr
---
# GUARD

**`GUARD`**`[NOT]`

Les unités peuvent garder leur région.
Pour ce faire, elles doivent être [[arme|prêtes au combat]], équipées d'au moins une [arme] et posséder la compétence d'armement appropriée.
Les régions océaniques ne peuvent être gardées.

<!-- TODO: translate in french -->
When a faction is guarding a region, units that are not allied with it are subject to [[alliances|alliances]] ([[cmd-help|`HELP GUARD`]] or [[cmd-contact]]), the following restrictions:

- You can no longer collect taxes, mine raw materials, [trade] or recruit farmers in this region
- You can no longer collect taxes, mine resources, [trade] or recruit farmers in this region
- There is a certain probability that you will be stopped in transit
- If you are on a ship, you cannot [[cmd-work]], [[cmd-entertain]], [[cmd-attack]] or move overland immediately.
  In order to be able to carry out the actions the following week, you must first have the ship [[cmd-leave]]

If the unit is not seen, for example because it has a higher Stealth Talent than the guarding party's best Perception Talent in the region, the first two restrictions do not apply.

However, it is very possible to have conversations on land in a guarded region, even if the guard has not set HELP GUARD.
However, this is not possible if the entertainer unit is on board a ship.

If several parties give the GUARD command at the same time or one after the other, they all guard the region.
Only for parties with*everyone*guarding parties are allied, the above restrictions do not apply.

Parties with*at least one*Allied guards can continue to carry out orders (possibly with the exceptions above) for a long time despite fighting (see [End of battle]).

In the round in which the`GUARD`-Order has been given, all of these restrictions do not apply yet, because the guarding unit first has to find out where foreign units could collect silver, etc.
The guarding unit immediately becomes visible to all other units in the region, regardless of how high its stealth talent is.

With`GUARD NOT`The guard status of a unit is dissolved.
This also happens when the unit is moving.
Units with the combat status [[cmd-combat|COMBAT FLEE]] cannot guard, and units from which all survivors flee during combat also stop guarding.

When a unit travels through a region guarded by at least one non-allied faction, the chance of being stopped depends on several factors: it is increased by the number of enemy guards, the region type (it becomes more difficult in swamps, glaciers, mountains and volcanoes), the perception talent of the enemy guards, Amulets of True Seeing, and the size of the region owner's castle if they are not allied.
It is reduced by the number of allied guards and the unit's stealth skill, as well as rings of invisibility.

!!! note
    [[monsters|Monster]] faction (ii) units are generally considered armed due to their claws, teeth, claws and other extremities, even if they do not carry a visible weapon.
    This also applies to monsters magically summoned by players.

In the [[puppy-protection|first few weeks]] your faction cannot guard yet.

## Voir aussi

- [[cmd-help|`HELP GUARD`]]
- [[alliances]]
- [[cmd-contact]]

<!-- From [https://wiki.eressea.de/index.php?title=GUARD&oldid=16839] -->

[arme]: ./war-tables.md#armes-et-leurs-proprietes
[trade]: ./silver.md#commerce
[End of battle]: ./war.md#fin-du-combat
