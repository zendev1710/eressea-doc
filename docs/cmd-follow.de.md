---
# cSpell:locale de
alias: bef-folge
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# FOLGE

*[Kurzer Befehl][kurze-und-lange-befehle].*  

**`FOLGE`**` EINHEIT `*`einheit-nr`*  
**`FOLGE`**` SCHIFF `*`schiff-nr`*`[`*`Geschwindigkeit`*`]`  

Hiermit kann man Einheiten bzw. Schiffen folgen.

Mit `FOLGE EINHEIT`*`einheit-nr`* wird die eigene Einheit die angegebene Einheit "beobachten" und dieser folgen, wenn sie sich bewegt.
Wenn die verfolgte Einheit allerdings schneller als die folgende Einheit ist, entkommt sie der Verfolgung.
Die Verfolger folgen der verfolgten Einheit so weit wie möglich.
Einheiten, die per Schiff reisen, können nicht mit `FOLGE EINHEIT` verfolgt werden.
Ebensowenig können Kapitäne hiermit ihr Schiff bewegen.
Stattdessen würden sie ihr Schiff verlassen und der Einheit zu Fuß folgen, wenn möglich.

Hat die verfolgte Einheit keinen Bewegungsbefehl gesetzt (dazu zählen `NACH, ROUTE, FAHRE, FOLGE`, aber nicht `PIRATERIE`), kann die verfolgende Einheit ihren langen Befehl ausführen.

Mit `FOLGE SCHIFF`*`schiff-nr`* können Schiffe verfolgt werden, welche in der aktuellen oder der vorigen Runde die Region durchquert haben.
Hat der Kapitän den Befehl `FOLGE SCHIFF`*`schiffnummer`* gegeben, wird das Schiff dann dem Kurs des angegebenen Schiffes folgen, bis es - wenn das eigene Schiff schnell genug ist - eingeholt wurde.
Ist der optionale Parameter *Geschwindigkeit* angegeben, wird das verfolgende Schiff maximal so viele Regionen weit segeln.

!!! warning "Achtung"
    nicht gefolgt werden kann Schiffen, die selber `FOLGE SCHIFF` oder `PIRATERIE` als Befehl haben.

`FOLGE SCHIFF` ist genau wie `FOLGE EINHEIT` nur dann ein langer Befehl, wenn das Ziel einen Bewegungsbefehl hat, und ersetzt dann alle anderen langen Befehle.

`FOLGE` hält nur in der Runde an, in welcher der Befehle gegeben wird.
Soll der Befehl länger andauern, muss ihm ein `@` vorgestellt werden.

```text
EINHEIT 87b6
    @FOLGE EINHEIT hz7
    UNTERHALTE
```

Einheit 87b6 wird nun Einheit hz7 beobachten und ihr folgen, wenn sie sich bewegt.
Ansonsten wird sie mit Unterhaltung Geld verdienen.
Durch das `@` bleiben beide Befehle erhalten.

Spielererfahrung: Solthar Es ist möglich, mit einer Einheit A einer Einheit B zu folgen, die ihrerseits einer dritten Einheit C folgt.
Das hat jedoch zur Folge, dass A keinen langen Befehl mehr ausführt, denn der Server nimmt zu diesem Zeitpunkt an, dass Einheit B sich ebenfalls bewegt, unabhängig davon, ob Einheit C sich ebenfalls bewegt.

Es ist nicht möglich, sinnvoll mehrere FOLGE-Befehle zu geben.
Es wird immer nur der erste ausgeführt.

## Siehe auch

- [Reisen][reisen]
- [[bef-nach]]
- [[bef-route]]
- [[bef-fahre]]
- [[bef-transportiere]]
- [[bef-piraterie]]

<!-- From [https://wiki.eressea.de/index.php?title=FOLGE&oldid=16723] -->

[bef-nach]: ./cmd-move.md
[bef-route]: ./cmd-route.md
[bef-fahre]: ./cmd-ride.md
[bef-transportiere]: ./cmd-carry.md
[bef-piraterie]: ./cmd-piracy.md
