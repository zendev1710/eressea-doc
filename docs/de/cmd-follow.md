# FOLGE

**`FOLGE`**[<sup>`(l)`</sup>]` EINHEIT `*`einheit-nr`*  
**`FOLGE`**[<sup>`(l)`</sup>]` SCHIFF `*`schiff-nr`*`[`*`Geschwindigkeit`*`]`

Hiermit kann man Einheiten bzw. Schiffen folgen.

Mit `FOLGE EINHEIT`*`einheit-nr`* wird die eigene Einheit die angegebene Einheit "beobachten" und dieser folgen, wenn sie sich bewegt. Wenn die verfolgte Einheit allerdings schneller als die folgende Einheit ist, entkommt sie der Verfolgung. Die Verfolger folgen der verfolgten Einheit so weit wie möglich. Einheiten, die per Schiff reisen, können nicht mit `FOLGE EINHEIT` verfolgt werden. Ebensowenig können Kapitäne hiermit ihr Schiff bewegen. Stattdessen würden sie ihr Schiff verlassen und der Einheit zu Fuß folgen, wenn möglich.

[<sup>(l)</sup>][<sup>`(l)`</sup>] Hat die verfolgte Einheit keinen Bewegungsbefehl gesetzt (dazu zählen `NACH, ROUTE, FAHRE, FOLGE`, aber nicht `PIRATERIE`), kann die verfolgende Einheit ihren langen Befehl ausführen.

Mit `FOLGE SCHIFF`*`schiff-nr`* können Schiffe verfolgt werden, welche in der aktuellen oder der vorigen Runde die Region durchquert haben. Hat der Kapitän den Befehl `FOLGE SCHIFF`*`schiffnummer`* gegeben, wird das Schiff dann dem Kurs des angegebenen Schiffes folgen, bis es - wenn das eigene Schiff schnell genug ist - eingeholt wurde. Ist der optionale Parameter *Geschwindigkeit* angegeben, wird das verfolgende Schiff maximal so viele Regionen weit segeln.

Achtung, nicht gefolgt werden kann Schiffen, die selber `FOLGE SCHIFF` oder `PIRATERIE` als Befehl haben.

[<sup>(l)</sup>][<sup>`(l)`</sup>] `FOLGE SCHIFF` ist genau wie `FOLGE EINHEIT` nur dann ein langer Befehl, wenn das Ziel einen Bewegungsbefehl hat, und ersetzt dann alle anderen langen Befehle.

`FOLGE` hält nur in der Runde an, in welcher der Befehle gegeben wird. Soll der Befehl länger andauern, muss ihm ein `@` vorgestellt werden.

    EINHEIT 87b6
      @FOLGE EINHEIT hz7
      UNTERHALTE

Einheit 87b6 wird nun Einheit hz7 beobachten und ihr folgen, wenn sie sich bewegt. Ansonsten wird sie mit Unterhaltung Geld verdienen. Durch das `@` bleiben beide Befehle erhalten.

Spielererfahrung: Solthar Es ist möglich, mit einer Einheit A einer Einheit B zu folgen, die ihrerseits einer dritten Einheit C folgt. Das hat jedoch zur Folge, dass A keinen langen Befehl mehr ausführt, denn der Server nimmt zu diesem Zeitpunkt an, dass Einheit B sich ebenfalls bewegt, unabhängig davon, ob Einheit C sich ebenfalls bewegt.

Es ist nicht möglich, sinnvoll mehrere FOLGE-Befehle zu geben. Es wird immer nur der erste ausgeführt.

## Siehe auch

- [Reisen]
- [NACH]
- [ROUTE]
- [FAHRE]
- [TRANSPORTIERE]
- [PIRATERIE]

<!-- From [https://wiki.eressea.de/index.php?title=FOLGE&oldid=16723] -->

  [<sup>`(l)`</sup>]: ./commands.md#kurzlang "Befehl"
  [Reisen]: ./travel.md "Reisen"
  [NACH]: ./cmd-move.md "NACH"
  [ROUTE]: ./cmd-route.md "ROUTE"
  [FAHRE]: ./cmd-ride.md "FAHRE"
  [TRANSPORTIERE]: ./cmd-carry.md "TRANSPORTIERE"
  [PIRATERIE]: ./cmd-piracy.md "PIRATERIE"
