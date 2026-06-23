---
# cSpell:locale de
alias: bef-transportiere
---

# `TRANSPORTIERE`

*`FAHRE` ist ein [langer Befehl][kurze-und-lange-befehle]*.  
*`TRANSPORTIERE` ist kurz, aber ergibt natürlich nur Sinn, wenn die Einheit einen (langen) Bewegungsbefehl ausführt.*

**`FAHRE`**` `*`einheit-nr`*  
**`TRANSPORTIERE`**` `*`einheit-nr`*  

Mit dem Befehl `FAHRE` schließt sich eine Einheit einer transportierenden Einheit an und kann von dieser, sofern sie den Befehl `TRANSPORTIERE` für die fahrende Einheit gegeben hat, mitgenommen werden.
Durch diesen Befehl ist es möglich, auch ohne das Reiten-Talent auf Pferden oder Wagen zu reisen.
Voraussetzung dafür ist natürlich, dass die transportierende Einheit über genügend freie Kapazitäten verfügt, um die fahrenden Einheiten samt Gegenständen aufzuladen.

```text
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
```

- [Meermenschen][meermenschen] können beim [Anschwimmen][anschwimmen] keine anderen Rassen transportieren und auch keine Pferde oder Wagen mitnehmen.
- [Insekten][insekten] können auch mittels `TRANSPORTIERE` nicht in oder durch einen Gletscher gebracht werden.

## Siehe auch

- [Reisen][reisen]
- [NACH][bef-nach]
- [`ROUTE`][bef-route]

<!-- From [https://wiki.eressea.de/index.php?title=FAHRE&oldid=16721] -->

[bef-nach]: [[bef-nach]]
[bef-route]: [[bef-route]]
