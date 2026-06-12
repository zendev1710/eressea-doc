---
# cSpell:locale en
alias: cmd-carry
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# CARRY

*`RIDE` is a [long order][short-and-long-orders].*  
*`CARRY` is short, but of course only makes sense if the unit executes a (long) movement order.*  

**`RIDE <unit-id>`**  
**`CARRY <unit-id>`**  

With the order `RIDE` a unit joins a transporting unit and can be separated from it if it receives the order `CARRY` given for the traveling unit.  
With this order it is possible to travel on horses or carts even without the riding skill.  
The prerequisite for this is, of course, that the transporting unit has enough free capacity to charge the moving units and their objects.  

```text
PARTEI 125:
    UNIT 311
        RIDE 456 ; I want to go with you
        CONTACT 456
    [...]
  
PARTEI 300:
    UNIT 777
        RIDE 456 ; I want to go with you
  
PARTEI 300:
    UNIT 456
        CARRY 311 ; Let 311 come along for the ride
        CARRY 777 ; and 777 is also taken
        CONTACT 311
```

Restrictive rules:

- [Aquarians][aquarians] cannot transport other races when [swimming][swimming], nor can they take horses or chariots with them
- [Insects][insects] can also be transported by means of `CARRY`, but cannot be brought into or through a glacier

## See also

- [[movement]]
- [[cmd-move]]
- [[cmd-route]]

<!-- From [https://wiki.eressea.de/index.php?title=RIDE&oldid=16721] -->
