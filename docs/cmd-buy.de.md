---
# cSpell:locale de
alias: bef-kaufe
---

# KAUFE

*`KAUFE` ist wie [`VERKAUFE`][bef-verkaufe] ein ["pseudolanger" Befehl][kurze-und-lange-befehle].*

**`KAUFE`**` `*`anzahl`*` `*`luxusgut`*  

Wenn die Einheit das Talent [Handeln][handel] hat, wird sie versuchen, die genannte Anzahl Luxusgüter zu kaufen.
Dies geht nur, wenn sich in der Region erstens ein Handelsposten oder ein größerer Burgtyp befindet, in dessen Nähe der Markt abgehalten werden kann, und zweitens das Produkt überhaupt in der Region produziert wird.
Um etwas zu kaufen, ist kein Kontakt zum Burgherren notwendig; trotzdem ist es natürlich diplomatischer, vorher zu fragen...

Man kann insgesamt Talentstufe(Handeln) \* 10 Luxusgüter umsetzen, allerdings keine anderen langen Befehle geben.
KAUFE-Order haben Priorität vor Verkäufen.

`KAUFE`-Befehle werden also generell vor `VERKAUFE` ausgeführt, man kann also nicht den Verdienst aus Verkäufen direkt in der selben Runde für neue Einkäufe benutzen.
Auch bedeutet das, dass Einheiten ohne genügend Talent für die Ausführung aller `KAUFE`- und `VERKAUFE`-Befehle zuerst so viel wie möglich kaufen und gegebenenfalls keine Talentpunkte fürs Verkaufen übrig sind.

Beispiel:

```text
EINHEIT hndl;     Marktschreier [1, $1000]
    ; Handel 3 [180]
    VERKAUFE 15 Juwelen
    VERKAUFE 15 Öl
    KAUFE 10 Weihrauch
```

Dieser Händler wird 10 Weihrauch kaufen und insgesamt 20 Juwelen und Öl verkaufen.
Also zufällig zwischen 5 und 15 pro Handelsware, so er sie hat.

Im Normalreport taucht immer nur ein Befehl auf.
Dies ist aber nur, damit nicht eine große Liste von Befehlen dort steht.
Im Computerreport und der [Zugvorlage][befehl] sind alle `KAUFE`- und `VERKAUFE`-Befehle aufgeführt.

## Siehe auch

- [Handel][handel]
- [`VERKAUFE`][bef-verkaufe]

<!-- From [https://wiki.eressea.de/index.php?title=KAUFE&oldid=16746] -->

[bef-verkaufe]: [[bef-verkaufe]]
