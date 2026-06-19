---
# cSpell:locale fr
alias: cmd-carry-fr
---

# CARRY

*`RIDE` est un ordre [long][ordres-courts-et-longs].*  
*`CARRY` est un ordre court, mais cela n'a bien sûr de sens que si l'unité exécute un  ordre (long) de mouvement.*  

**`RIDE`**` `*`unit-id`*  
**`CARRY`**` `*`unit-id`*  

Avec l'ordre `RIDE`, une unité rejoint une unité de transport et peut en être séparée si elle reçoit l'ordre `CARRY` donné pour l’unité itinérante.  
Avec cet ordre, il est possible de voyager à cheval ou en charrette même sans compétence d'équitation.  
La condition préalable à cela est bien entendu que l'unité de transport dispose de suffisamment de capacité libre pour charger les unités mobiles et leurs objets.  

```text
PARTEI 125:
    UNIT 311
        RIDE 456 ; je veux aller avec toi
        CONTACT 456
    [...]
      
PARTEI 300:
    UNIT 777
        RIDE 456 ; je veux aller avec toi
      
PARTEI 300:
    UNIT 456
        CARRY 311 ; je laisse l'unité 311 m'accompagner
        CARRY 777 ; et l'unité 777 est également prise
        CONTACT 311
```

Règles restrictives :

- **lorsqu'ils [nagent][nager]**, les [Aquariens][aquariens]{title="Aquarians"} ne peuvent pas transporter d'autres peuples, ni emmener de chevaux ni des chars avec eux
- les [Insectes][insectes]{title="Insects"} peuvent être transportés grâce à l'ordre `CARRY`, mais ne peuvent pas être emmenés dans ou à travers un glacier

## Voir aussi

- [Déplacements][deplacements]
- [`MOVE`][cmd-move-fr]
- [`ROUTE`][cmd-route-fr]

<!-- From [https://wiki.eressea.de/index.php?title=RIDE&oldid=16721] -->

[cmd-move-fr]: [[cmd-move-fr]]
[cmd-route-fr]: [[cmd-route-fr]]
