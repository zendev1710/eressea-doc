---
alias:
	name: 
	text: 
---
# LEARN AUTO

**`LEARN AUTO`**` `*`talent`*

Durch den Befehl versucht der Server, das [Lernen] und [Lehren] in einer Region für alle Einheiten einer Partei mit diesem Befehl für dieses Talent zu automatisieren. Eine Mischung von TEACH und LEARN AUTO ist allerdings nicht möglich.

Wenn in einer Region mehrere Einheiten den Befehl LEARN AUTO &lt;Talent&gt; geben, z.B. LEARN AUTO Segeln, dann sucht der Server aus diesen Einheiten selber diejenigen heraus, die lehren müssen, damit der Rest die maximale Lernausbeute bekommt. Wie beim einfachen TEACH lernt jede Person, die dadurch einen Lehrer bekommt, doppelt so schnell.

Es ist nicht notwendig, Einheiten zu zerteilen. Wenn z.B. einen Einheit mit 10 Personen auf T7 und eine mit 10 Personen auf T5 beide LEARN AUTO befohlen haben, dann lehrt eine Person der T7 Einheit die zehn aus der T5 Einheit, die übrigen neun lernen normal. Mit den einfachen Befehlen hätte man dafür die Einheit aufteilen müssen, was sehr lästig werden kann.

Dieser Effekt greift auch bei weniger als 10 Schülern. Eine Person welche mittels LEARN AUTO 6 Schüler lehrt, erhält hat eine 4/10 Chance eine Woche zu lernen. Können keine Schüler zugewiesen werden, lernt die Einheit normal.

LEARN AUTO funktioniert nicht bei teuren Talenten und nicht in Kombination mit TEACH: Andere Einheiten, die gewöhnliche LEARN- und TEACH-Befehle benutzen, werden nicht an der automatischen Zuweisung von Lehrern beteiligt. Einheiten, die LEARN AUTO benutzen, können nicht durch TEACH gelehrt werden.

Es kann trotzdem sinnvoll sein, TEACH und LEARN AUTO parallel für verschiedene Einheiten zu nutzen. Die Vorteile von TEACH./cmd-learn.md sind:

- Einheiten mit teuren Talenten können gelehrt werden.
- Eine Einheit kann Einheiten in unterschiedlichen Talenten lehren.
- Lehrende und Lernende müssen nicht zur selben Partei gehören.
- Einheiten, die nicht lehren dürfen (zum Beispiel die meisten Vertrauten), können trotzdem gelehrt werden.

Die Vorteile von LEARN AUTO sind:

- Es ist weniger Kleinarbeit und kann eher auch mal über mehrere Wochen "in Ruhe gelassen werden".
- Einheiten, die nicht voll als Lehrer genutzt werden, nutzen die Restkapazität um selber zu lernen.

Spielererfahrung: XolgrimEin Block für LEARN AUTO besteht pro Region und Talent aus maximal 128 Einheiten. Setzen mehr Einheiten einer Partei in einer Region den Befehl, wird ein zweiter Block gebildet, der unabhängig vom ersten eine Lehre/Lern-Kette aufbaut.

<!-- From [https://wiki.eressea.de/index.php?title=LEARN\_AUTO&oldid=15393] -->

[Lernen]: ./cmd-learn.md "LEARN"
[Lehren]: ./cmd-teach.md "TEACH"
