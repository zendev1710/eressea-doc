---
# cSpell:locale fr, en
alias: cmd-carry-fr
---
# CARRY

**`RIDE`**[<sup>`L`</sup>]` `*`unit-id`*  
**`CARRY`**` `*`unit-id`*  

With the order `RIDE` a unit joins a transporting unit and can be separated from it if it receives the order `CARRY` given for the traveling unit.
With this order it is possible to travel on horses or carts even without the riding skill.
The prerequisite for this is, of course, that the transporting unit has enough free capacity to charge the moving units and their objects.

```text
    Partei 125:
        UNIT 311
            RIDE 456 ; ich will mitfahren
            CONTACT 456
        [...]
      
    Partei 300:
        UNIT 777
            RIDE 456 ; ich will mitfahren
      
    Partei 300:
        UNIT 456
            CARRY 311 ; Lasse 311 mitfahren
            CARRY 777 ; und 777 wird auch mitgenommen
            CONTACT 311
```

[<sup>L</sup>][<sup>`L`</sup>] `RIDE` is a long order. `CARRY` is short, but of course only makes sense if the unit executes a (long) movement order.

- [Aquarians] cannot transport other races when [swimming], nor can they take horses or chariots with them
- [Insects] can also be found by means of `CARRY` not be brought into or through a glacier

## Voir aussi

- [[travel]]
- [[cmd-move]]
- [[cmd-route]]

<!-- From [https://wiki.eressea.de/index.php?title=RIDE&oldid=16721] -->

[<sup>`L`</sup>]: ./commands.md#ordres-courts-et-longs
[Aquarians]: ./races.md#aquariens
[swimming]: ./sailing.md#nager
[Insects]: ./races.md#insectes
