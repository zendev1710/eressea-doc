---
# cSpell:locale fr, en
alias: cmd-combat-fr
---
# COMBAT

**`COMBAT`**`FRONT`  
**`COMBAT`**`AGGRESSIVE`  
**`COMBAT`**`REAR`  
**`COMBAT`**`DEFENSIVE`  
**`COMBAT`**`NOT`  
**`COMBAT`**`FLEE`  
**`COMBAT`**`HELP [NOT]`

Mit diesem Befehl wird die Reaktion einer Einheit im Falle eines Kampfes bestimmt (siehe im Kapitel [Vom Kriege] auch den Abschnitt [Kampfreihen]).

## `COMBAT AGGRESSIVE`

Im Kampf steht die Einheit an der Front und wird nie fliehen, sondern bis zum Tode kämpfen.
Dies verwendet man mit Vorteil, wenn es wirklich auf das letzte bisschen Offensivkraft ankommt.

## `COMBAT FRONT`

Im Kampf steht die Einheit an der Front.
Sie wird versuchen zu fliehen, wenn sie weniger oder gleich 20% ihrer Trefferpunkte hat.
Dies verwendet man mit Vorteil für gute Schwertkämpfer.
Kann auch mit `COMBAT` gesetzt werden.

## `COMBAT REAR`

Die Einheit kämpft in der zweiten Reihe.
Ist die Front aufgerieben, werden diese Einheiten trotzdem in den Nahkampf hineingezogen! Dies verwendet man mit Vorteil für Schützen.
Die Einheit versucht zu fliehen, wenn sie weniger oder gleich 20% ihrer Trefferpunkte hat.

## `COMBAT DEFENSIVE`

Wie `COMBAT REAR`, aber die Einheit wird schon fliehen, wenn sie noch 90% ihrer Trefferpunkte hat.
Dies verwendet man mit Vorteil für Magier.

## `COMBAT NOT`

Die Einheit kämpft nur noch dann mit, wenn sie selber das Ziel eines feindlichen [[cmd-attack]]-Befehls ist.
Dies setzt man mit Vorteil für Einheiten ein, die sich aus dem Kampf heraushalten, aber nicht fliehen sollen, weil sie z.B.
ein Gebäude besetzt halten sollen.
Die Einheit versucht zu fliehen, wenn sie noch 90% ihrer Trefferpunkte hat.

## `COMBAT FLEE`

Wird eine fluchtbereite Einheit in einen Kampf verwickelt, versucht sie vor jeder Kampfrunde zu fliehen.
Für weitere Informationen über das "Fluchtverhalten", siehe den Abschnitt [Flucht] im Kapitel Kampf.
Diesen Kampfstatus setzt man mit Vorteil für fast alle "Zivilisten" ein.
Flieht aus einer Einheit auch nur eine Person erfolgreich aus einem Kampf, verlässt diese automatisch Gebäude oder an Land liegende Schiffe, in denen sie sich befindet.
Es gilt daher abzuwägen, ob dieser Status für Gebäudeinsassen sinnvoll ist.
Einheiten mit diesem Kampfstatus können auch nicht [[cmd-attack]][`ATTACK`]N oder [[cmd-guard]].
Setzt eine bewachende Einheit COMBAT FLEE, wird das Bewachen sofort aufgehoben, mit entsprechenden Konsequenzen.
Einheiten mit dem Kampfstatus können sich nach dem Kampf noch bewegen (mit [[cmd-move]], [[cmd-route]], [[cmd-follow]]).

!!! warning "Attention"
    Einheiten mit COMBAT FLEE oder COMBAT NOT, kämpfen, falls sie attackiert werden und die ersten beiden Reihen überrannt.
    Das heißt, Magier zaubern auch.
    Prä- und Postkampfzauber werden (derzeit) selbst dann gezaubert, wenn die ersten Reihen nicht überrannt werden.
    Soll dies verhindert werden, kann man die [Kampfzauber] deaktivieren.

Katapulte zu bedienen ist eine Aufgabe, die viel Vorbereitung erfordert, daher werden Einheiten mit dem Kampfstatus COMBAT NOT und COMBAT FLEE keine Munition verschießen, aber zu anderen Waffen greifen, so sie welche dabei haben und beherrschen.

!!! warning "Attention"
    Personen mit niedrigen Trefferpunkten, die nicht `COMBAT FLEE` gesetzt haben, fliehen erst dann, wenn sie im Kampf auch einen Treffer abbekommen haben.
    Dabei zählen auch Treffer, deren Schadenspunkte vollständig von der Rüstung aufgehalten wurden und fehlgeschlagene Trefferversuche.
    Personen mit `COMBAT FLEE` fliehen natürlich schon vorher.

## `COMBAT HELP`

Einer Einheit mit `COMBAT HELP NOT` wird im Kampf nicht geholfen, weder von Einheiten der eigenen Partei noch von Verbündeten.
Wird eine solche Einheit attackiert, werden keine anderen Einheiten in den Kampf gezogen.
Dies gilt natürlich nur, wenn nicht zusätzlich andere Einheiten ohne einen solchen Status attackiert werden.

Die eigene Partei ist immer dann involviert, wenn sie angreift, oder wenn sie oder eine Partei, der sie hilft, angegriffen wird.
Weitere Details unter [[cmd-help]] und in den Kapiteln [Kampf][Vom Kriege] und [[alliances|allianz]].

<!-- From [https://wiki.eressea.de/index.php?title=COMBAT&oldid=7216] -->

[Vom Kriege]: ./war.md
[Kampfreihen]: ./war.md#schlacht
[`ATTACK`]: ./cmd-attack.md
[Flucht]: ./war.md#die-flucht
[Kampfzauber]: ./cmd-combatspell.md
