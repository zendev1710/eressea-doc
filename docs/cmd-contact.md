---
# cSpell:locale en
alias: cmd-contact
---
# CONTACT

**`CONTACT`**` UNIT `*`unit-id`*  
**`CONTACT`**` PARTEI `*`faction-id`*  
**`CONTACT`**` `*`unit-id`*  

You are normally not allowed to give anything to units of foreign factions unless you are allied with that faction.
To allow this to a limited extent, there is the `CONTACT` order.
In this round -and only in this round- the commanding unit behaves towards the named unit as if it were allied with it (see also under [[cmd-help]]), i.e. it accepts items, silver and people from it.
Non-allied factions can also enter castles and ships, recruit people and extract resources in this way.
`CONTACT UNIT` allows this to be done by a single unit, while `CONTACT FACTION` allows all units of the faction in question in a region.
The `CONTACT unit-id` order is allowed for historical reasons, but should be passed `CONTACT UNIT unit-id` be replaced.

**Examples:**

```text
    PARTEI ff "FooBar"
        UNIT a
        GIVE x 1000 Silver ; Tribut!
        [...]

    PARTEI 300 "BarFoo"
        UNIT x
        CONTACT UNIT a ; erlaube Zahlung.
```

Unit a can give unit x the 1000 silver.
If x is the only guarding unit in the region, a is also allowed to recruit and collect taxes.
Unit b of faction ff is not allowed to do any of this.
For this, unit x would have to receive the `CONTACT FACTION ff` order give.

Unit x and unit y of one faction guard the region.
In order for unit a to recruit, x and y must both `CONTACT UNIT a` or `CONTACT PARTEI ff` orders.

## Differences to HELP

`CONTACT` has a similar function to [[cmd-help|`HELP GIVE + HELP GUARD`]], but it's not 100% the same.

- `CONTACT` is required for some things that `HELP GIVE` or `HELP GUARD` does not cover, such as [[cmd-give|`GIVE MEN`]] and some spells
- `HELP` closes `HELP SILVER, HELP COMBAT` and `HELP PARTEITARNUNG` A
- `CONTACT` applies only to the current round and only to the unit issuing the order
- `HELP`is permanent and applies to all units of my faction or group (and all units of the other faction)

<!-- From [https://wiki.eressea.de/index.php?title=CONTACT&oldid=13303] -->

