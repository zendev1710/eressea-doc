---
alias:
	name: cmd-leave
	text: LEAVE
---
# LEAVE

**`LEAVE`**

Die Einheit wird das Schiff oder das Gebäude, in dem sie sich befindet, verlassen. Wenn man die Befehle [`ENTER`] oder [`MOVE`] verwendet, verlassen die Einheiten z.T. automatisch ihre Schiffe und Gebäude. Dies funktioniert allerdings nicht immer: ist die Einheit Kapitän eines Schiffs und verwendet MOVE, wird sie versuchen in diese Richtung zu segeln, auch wenn dort Festland ist. Kapitäne müssen ihr Schiff zuerst `VERLASSEN`, alle anderen Segler können sich aber mit `MOVE` über Land bewegen und verlassen das Schiff dabei automatisch.

**[E3A — Das Dritte Zeitalter]**

Gebäudebesitzer müssen ebenfalls das Gebäude `VERLASSEN` oder das Kommando abgeben, um sich zu Bewegen oder ein anderes Gebäude oder Schiff zu betreten.

Verläßt eine Einheit ein Gebäude oder ein Schiff, über das sie das Kommando hat, fällt dieses nicht zwangsweise an die folgende Einheit des Reports. Hier sollte man mit [`GIVE einheit-nr KOMMANDO`] die Kommando-Übergabe kontrolliert vonstatten gehen lassen. Die Reihenfolge der Einheiten ist während der Auswertung nicht immer die dem Report entsprechende. Sind eigene Einheiten in dem Gebäude oder auf dem Schiff, fällt das Kommando aber diesen zu.

Befindet sich die Einheit auf einem Schiff und wird die Region von einer nicht-alliierten Partei bewacht, muss sie das Schiff erst verlassen, wenn sie bestimmte Aktionen durchführen will. Siehe hierzu Näheres unter [`GUARD`]. Auf offener See funktioniert der Verlasse-Befehl nicht. Eine Möglichkeit um Personen trotzdem über Bord springen zu lassen ist "Gib 0 \[Anzahl\] Personen". Eine andere, nur für Meermenschen bereitstehende Lösung, bei der die Personen nicht umkommen, ist das [Anschwimmen].

<!-- From [https://wiki.eressea.de/index.php?title=LEAVE&oldid=15184] -->

[`ENTER`]: ./cmd-enter.md "ENTER"
[`MOVE`]: ./cmd-move.md "MOVE"
[E3A — Das Dritte Zeitalter]: ./the-third-age.md "Das dritte Zeitalter"
[`GIVE einheit-nr KOMMANDO`]: ./cmd-give.md "GIVE"
[`GUARD`]: ./cmd-guard.md "GUARD"
[Anschwimmen]./travel.md#anschwimmen "Schiffsreise"
