---
alias:
	name: cmd-sell
	text: SELL
---
# SELL

**`SELL`**[<sup>`(l)`</sup>]` `*`anzahl`*` `*`luxusgut`*  
**`SELL`**[<sup>`(l)`</sup>]` ALLES `*`luxusgut`*

Die im [Handeln] kundige Einheit kann mit diesem Befehl Luxusgüter, in deren Besitz sie ist, an die Bauern verkaufen. Dies geht nur, wenn sich in der Region erstens ein Handelsposten oder ein größerer [Burgtyp] befindet, in dessen Nähe der Markt abgehalten werden kann, und wenn zweitens überhaupt eine Nachfrage nach dem Produkt besteht. Um etwas zu verkaufen, ist kein Kontakt zum Burgherren notwendig; trotzdem ist es natürlich diplomatischer, vorher zu fragen ...

Mit `SELL ALLES` wird soviel verkauft, wie die Nachfrage der Region ist. Das klappt auch, wenn in der gleichen Woche das Handelsvolumen (z.B. durch Rekrutierungen) sinkt. Der Befehl sollte aber nicht mehr als einer Einheit pro Region oder gar von mehreren Parteien erteilt werden: Sobald mehrere Einheiten in der Region SELL-Befehle haben, ist nicht mehr garantiert, was bei `SELL ALLES` passiert.

[<sup>(l)</sup>][<sup>`(l)`</sup>] `SELL` ist wie [`BUY`] ein ["pseudolanger" Befehl]. Man kann insgesamt Talentstufe(Handeln) \* 10 Luxusgüter verkaufen und kaufen, allerdings keine anderen langen Befehle geben. BUY-Order haben Priorität vor Verkäufen. `BUY`-Befehle werden also generell vor `SELL` ausgeführt, man kann also nicht den Verdienst aus Verkäufen direkt in der selben Runde für neue Einkäufe benutzen. Auch bedeutet das, dass Einheiten ohne genügend Talent für die Ausführung aller `BUY`- und `SELL`-Befehle zuerst so viel wie möglich kaufen und gegebenenfalls keine Talentpunkte fürs Verkaufen übrig sind.

Im Normalreport taucht immer nur ein Befehl auf. Dies ist aber nur, damit nicht eine große Liste von Befehlen dort steht. Im Computerreport und der [Zugvorlage]["pseudolanger" Befehl] sind alle `BUY`- und `SELL`-Befehle aufgeführt.

## See also

- [Handel][Handeln]
- [BUY][`BUY`]

<!-- From [https://wiki.eressea.de/index.php?title=SELL&oldid=16784] -->

[<sup>`(l)`</sup>]: ./commands.md#short-and-long-orders "Orders"
[Handeln]: ./silver.md#trade "Trade"
[Burgtyp]: ./castles.md "Burgen"
[`BUY`]: ./cmd-buy.md "BUY"
["pseudolanger" Befehl]: ./commands.md "Orders"
