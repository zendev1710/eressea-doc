---
alias:
    name: cmd-buy
    text: BUY
---
# BUY

**`BUY`**[<sup>`(l)`</sup>]` `*`anzahl`*` `*`luxusgut`*

Wenn die Einheit das Talent [Handeln] hat, wird sie versuchen, die genannte Anzahl Luxusgüter zu kaufen. Dies geht nur, wenn sich in der Region erstens ein Handelsposten oder ein größerer Burgtyp befindet, in dessen Nähe der Markt abgehalten werden kann, und zweitens das Produkt überhaupt in der Region produziert wird. Um etwas zu kaufen, ist kein Kontakt zum Burgherren notwendig; trotzdem ist es natürlich diplomatischer, vorher zu fragen ...

[<sup>(l)</sup>][<sup>`(l)`</sup>] `BUY` ist wie [`SELL`] ein ["pseudolanger" Befehl]. Man kann insgesamt Talentstufe(Handeln) \* 10 Luxusgüter umsetzen, allerdings keine anderen langen Befehle geben. BUY-Order haben Priorität vor Verkäufen. `BUY`-Befehle werden also generell vor `SELL` ausgeführt, man kann also nicht den Verdienst aus Verkäufen direkt in der selben Runde für neue Einkäufe benutzen. Auch bedeutet das, dass Einheiten ohne genügend Talent für die Ausführung aller `BUY`- und `SELL`-Befehle zuerst so viel wie möglich kaufen und gegebenenfalls keine Talentpunkte fürs Verkaufen übrig sind.

Beispiel:

     UNIT hndl;     Marktschreier [1, $1000]
       ; Handel 3 [180]
       SELL 15 Juwelen
       SELL 15 Öl
       BUY 10 Weihrauch

Dieser Händler wird 10 Weihrauch kaufen und insgesamt 20 Juwelen und Öl verkaufen. Also zufällig zwischen 5 und 15 pro Handelsware, so er sie hat.

Im Normalreport taucht immer nur ein Befehl auf. Dies ist aber nur, damit nicht eine große Liste von Befehlen dort steht. Im Computerreport und der [Zugvorlage]["pseudolanger" Befehl] sind alle `BUY`- und `SELL`-Befehle aufgeführt.

## See also

- [Handel][Handeln]
- [SELL][`SELL`]

<!-- From [https://wiki.eressea.de/index.php?title=BUY&oldid=16746] -->

[<sup>`(l)`</sup>]: ./commands.md#short-and-long-orders "Orders"
[Handeln]: ./silver.md#trade "Trade"
[`SELL`]: ./cmd-sell.md "SELL"
["pseudolanger" Befehl]: ./commands.md "Orders"
