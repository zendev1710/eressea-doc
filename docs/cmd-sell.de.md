---
# cSpell:locale de
alias: bef-verkaufe
---

# VERKAUFE

*`VERKAUFE` ist wie [`KAUFE`][bef-kaufe] ein ["pseudolanger" Befehl][kurze-und-lange-befehle].[^1]*

**`VERKAUFE`**` `*`anzahl`*` `*`luxusgut`*  
**`VERKAUFE`**` ALLES `*`luxusgut`*

Die im [Handeln][handel] kundige Einheit kann mit diesem Befehl Luxusgüter, in deren Besitz sie ist, an die Bauern verkaufen. Dies geht nur, wenn sich in der Region erstens ein Handelsposten oder ein größerer [Burgtyp][burgen] befindet, in dessen Nähe der Markt abgehalten werden kann, und wenn zweitens überhaupt eine Nachfrage nach dem Produkt besteht. Um etwas zu verkaufen, ist kein Kontakt zum Burgherren notwendig; trotzdem ist es natürlich diplomatischer, vorher zu fragen ...

Mit `VERKAUFE ALLES` wird soviel verkauft, wie die Nachfrage der Region ist.  
Das klappt auch, wenn in der gleichen Woche das Handelsvolumen (z.B. durch Rekrutierungen) sinkt.  
Der Befehl sollte aber nicht mehr als einer Einheit pro Region oder gar von mehreren Parteien erteilt werden: Sobald mehrere Einheiten in der Region VERKAUFE-Befehle haben, ist nicht mehr garantiert, was bei `VERKAUFE ALLES` passiert.

Im Normalreport taucht immer nur ein Befehl auf.  
Dies ist aber nur, damit nicht eine große Liste von Befehlen dort steht.  
Im Computerreport und der [Zugvorlage][befehl] sind alle `KAUFE`- und `VERKAUFE`-Befehle aufgeführt.

## Siehe auch

- [Handel][handel]
-[[bef-kaufe]]

[^1]: Man kann insgesamt Talentstufe(Handeln) \* 10 Luxusgüter verkaufen und kaufen, allerdings keine anderen langen Befehle geben. KAUFE-Order haben Priorität vor Verkäufen. `KAUFE`-Befehle werden also generell vor `VERKAUFE` ausgeführt, man kann also nicht den Verdienst aus Verkäufen direkt in der selben Runde für neue Einkäufe benutzen. Auch bedeutet das, dass Einheiten ohne genügend Talent für die Ausführung aller `KAUFE`- und `VERKAUFE`-Befehle zuerst so viel wie möglich kaufen und gegebenenfalls keine Talentpunkte fürs Verkaufen übrig sind.

<!-- From [https://wiki.eressea.de/index.php?title=VERKAUFE&oldid=16784] -->

[bef-kaufe]: [[bef-kaufe]]
