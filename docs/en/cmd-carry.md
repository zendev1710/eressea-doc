# FAHRE

**`FAHRE`**[<sup>`L`</sup>]` `*`einheit-nr`*  
**`TRANSPORTIERE`**` `*`einheit-nr`*

Mit dem Befehl `FAHRE` schließt sich eine Einheit einer transportierenden Einheit an und kann von dieser, sofern sie den Befehl `TRANSPORTIERE` für die fahrende Einheit gegeben hat, mitgenommen werden. Durch diesen Befehl ist es möglich, auch ohne das Reiten-Talent auf Pferden oder Wagen zu reisen. Voraussetzung dafür ist natürlich, dass die transportierende Einheit über genügend freie Kapazitäten verfügt, um die fahrenden Einheiten samt Gegenständen aufzuladen.

       Partei 125:
          EINHEIT 311
            FAHRE 456 ; ich will mitfahren
            KONTAKTIERE 456
          [...]
      
       Partei 300:
          EINHEIT 777
            FAHRE 456 ; ich will mitfahren
      
       Partei 300:
          EINHEIT 456
            TRANSPORTIERE 311 ; Lasse 311 mitfahren
            TRANSPORTIERE 777 ; und 777 wird auch mitgenommen
            KONTAKTIERE 311

[<sup>L</sup>][<sup>`L`</sup>] `FAHRE` ist ein langer Befehl. `TRANSPORTIERE` ist kurz, aber ergibt natürlich nur Sinn, wenn die Einheit einen (langen) Bewegungsbefehl ausführt.

- [Meermenschen] können beim [Anschwimmen] keine anderen Rassen transportieren und auch keine Pferde oder Wagen mitnehmen.
- [Insekten] können auch mittels `TRANSPORTIERE` nicht in oder durch einen Gletscher gebracht werden.

## Siehe auch

- [Reisen]
- [NACH]
- [ROUTE]

<!-- From [https://wiki.eressea.de/index.php?title=FAHRE&oldid=16721] -->

[<sup>`L`</sup>]: ./commands.md#kurzlang "Befehl"
[Meermenschen]: ./races.md#aquarians "Meermenschen"
[Anschwimmen]: ./sailing.md#swimming "Swimming"
[Insekten]: ./races.md#insects "Insects"
[Reisen]: ./travel.md "Reisen"
[NACH]: ./cmd-move.md "NACH"
[ROUTE]: ./cmd-route.md "ROUTE"
