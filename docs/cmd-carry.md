---
alias:
    name: cmd-carry
    text: CARRY
---
# CARRY

**`RIDE`**[<sup>`L`</sup>]` `*`unit-id`*  
**`CARRY`**` `*`unit-id`*

Mit dem Befehl `RIDE` schließt sich eine Einheit einer transportierenden Einheit an und kann von dieser, sofern sie den Befehl `CARRY` für die fahrende Einheit gegeben hat, mitgenommen werden. Durch diesen Befehl ist es möglich, auch ohne das Reiten-Talent auf Pferden oder Wagen zu reisen. Voraussetzung dafür ist natürlich, dass die transportierende Einheit über genügend freie Kapazitäten verfügt, um die fahrenden Einheiten samt Gegenständen aufzuladen.

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

[<sup>L</sup>][<sup>`L`</sup>] `RIDE` ist ein langer Befehl. `CARRY` ist kurz, aber ergibt natürlich nur Sinn, wenn die Einheit einen (langen) Bewegungsbefehl ausführt.

- [Meermenschen] können beim [Anschwimmen] keine anderen Rassen transportieren und auch keine Pferde oder Wagen mitnehmen.
- [Insekten] können auch mittels `CARRY` nicht in oder durch einen Gletscher gebracht werden.

## See also

- [Reisen]
- [[cmd-move]]
- [[cmd-route]]

<!-- From [https://wiki.eressea.de/index.php?title=RIDE&oldid=16721] -->

[<sup>`L`</sup>]: ./commands.md#short-and-long-orders "Orders"
[Meermenschen]: ./races.md#aquarians "Meermenschen"
[Anschwimmen]: ./sailing.md#swimming "Swimming"
[Insekten]: ./races.md#insects "Insects"
[Reisen]: ./travel.md "Reisen"
