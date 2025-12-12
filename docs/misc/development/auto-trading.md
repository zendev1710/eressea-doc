---
alias:
	name: auto-trading
	text: Automated trading
---
# Automatisierung Handel

Handel hat ja nur einen Zweck: Maximierung des Silberertrages. Damit ist das Grosse Ziel schonmal sehr einfach definiert.

Das zu optimierende Problem ist also die Maximierung des Gewinns zwischen Einkauf und Verkauf. Nebenbedingung ist der Transport der Waren, wobei diese Nebenbedingung sehr schnell sehr kompliziert werden kann.

## Handelsertragmaximierung

Meist gilt in der Welt von Eressea, dass die Regionen einer Insel jeweils eine von 2 Handelswaren zum Kauf anbieten. Damit ist inselintern die optimale Kaufmenge der Handelswaren relativ leicht zu bestimmen, da wir wissen, welche Menge wir zu welchem Preis maximal absetzen können. So lange es noch eine Spanne zwischen Ein- und Verkauf gibt, kaufen wir ein. Üblicherweise wird man also für den eigenbedarf der Inseln zum 1-3 fachen des Grundpreises einkaufen, halt in dem Mengenverhältnis in dem die beiden Luxuswaren angeboten werden. Aus Gründen der Einheitenminimierung mag man auch auf Regionen mit einem sehr geringen Handelsvolumen verzichten, diese sind dann also aus der Rechnung auzuschliessen.

Der Bedarf an externen Luxuswaren lässt sich oft noch einfacher bestimmen. Er liegt grob bei Bauernzahl der Insel geteilt durch 100. Allerdings wird man diesen Bedarf selten decken, da Schiffe meist wichtigere Dinge zu tun haben.

Die Problemstellung hier ist also eher langweilig, bzw. nicht als Problem zu bezeichnen. Erst beim Transport müssen tatsächlich "Entscheidungen" gefällt werden.

## Wichtige Nebenbedingung: Transport

Bleiben wir erstmal bei dem einfachen Fall zweier Handelswaren und schauen uns nun den Transport an. Da wir nicht beliebig viele Transporteinheiten handhaben können - im Gegenteil, diese Anzahl gilt es zu minimieren (Einheitenlimit) - können wir also kaum alle Bedarfe jede Woche "Just in Time" liefern. Wir schaffen also mehr als für eine Woche nötig auf einmal in eine Region.

Die Ansätze um den optimalen Lagerzustand und Transportmenge zu bestimmen sind nun so unterschiedlich wie ähnlich. Letztendlich versucht man immer mindestens die aktuell benötigte Menge zu liefern, aber gleichzeitig den Transport auszulasten.

Ein Ansatz ist dabei das Prioritätenmodell: In die Priorität kann dabei sowohl der Verkaufspreis als auch die Zeit bis zu der die Waren benötigt werden einfliessen. Da im Lauf der Zeit alle Verkaufspreise einer Ware den gleichen Wert erreichen kann man sich also auf die Zeit beschränken.

Weist man nun die Transporte der Priorität entsprechend zu, kann bei ausreichender Anzahl Transporten und Kapazität der Transporte immer ein Mindestbestand garantiert werden.

Je cleverer man nun die Transporte steuert, desto weniger Leerfahrten und damit weniger Transporte und Transportkapazität braucht man. Es gilt also möglichst wenige und möglichst kurze Transporte durchzuführen. Leider ist die Optimierung dieses Problems komplex, d.h. mit zunehmender Zahl Regionen und vor allem sehr unterschiedlichen Bauernzahlen und bestimmten Inseltopologien wächst ndie Zahl der Möglichen Lieferroutenkombinationen exponentiell an. Es lohnt hier vermutlich nicht die optimale kombination zu ermitteln (meist läuft es auf ein durchsuchen aller sinnvollen Kombinationen hinaus). Stattdessen versucht man nur eine gute Kombination zu finden. Das kann über diverse Regeln oder eine "zielgerichtete Suche" erfolgen.

Regeln wären z.b.:

- Suche zu einer Zielregion einen Transport in einer nahen Ausgangsregion.
- Ein Transport muss eine Füllung von min. x% erreichen

Eine zielgerichtete Suche, kann Zustände erzeugen, die ein Teilergebnis darstellen und davon ausgehend die vielversprechendsten Folgezustände expandieren. Da natürlich nicht nur auf den ersten Blick gute Teilergebnisse am Ende einen nahezu optimalen Endzustand erzeugen können, bedarf es einer Bewertung. Diese Bewertung muss wiederum Wissen und Schätzung unterschiedlich stark bewerten um auch bei Milliarden von möglichen Zuständen in angemessener Zeit einen nahezu optimalen Zielzustand zu erreichen. Ebenso sollen natürlich Zustände die definitiv kein gutes Ergebnis erzeugen von vorherein eliminiert werden.

<!-- From [https://wiki.eressea.de/index.php?title=Automatisierung\_Handel&oldid=2482] -->
