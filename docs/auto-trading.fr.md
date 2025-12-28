---
# cSpell:locale fr, en
alias: commerce-automatise
---
# Commerce automatisé

Trading has only one purpose: maximizing the silver yield. This means that the big goal is defined very simply.

So the problem to be optimized is maximizing the profit between purchasing and selling.
The secondary condition is the transport of the goods, although this secondary condition can quickly become very complicated.

## Trading profit maximization

In the world of Eressea, the regions of an island usually offer one of two trade goods for purchase.
This makes it relatively easy to determine the optimal purchase quantity of merchandise within the island, as we know the maximum quantity we can sell at what price.
As long as there is still a margin between buying and selling, we will buy.
Usually you will buy for your own needs on the islands at 1-3 times the basic price, just in the proportion in which the two luxury goods are offered.
For reasons of unit minimization, regions with a very low trading volume may also be avoided, so these should then be excluded from the calculation.

The need for external luxury goods is often even easier to determine.
It is roughly the number of farmers on the island divided by 100.
However, this need will rarely be met because ships usually have more important things to do.

The problem here is rather boring or cannot be described as a problem.
Only during transport do “decisions” actually have to be made.

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
