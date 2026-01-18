---
# cSpell:locale fr
alias: production-optimisee
---
# Production optimisée

Unter der Optimierung der Produktion verstehe ich hauptsächlich die sparsame Verwendung von Einheiten. D.h. Ich habe in einer Region eine Gruppe von Einheiten mit der gleichen Aufgabe und soll eine festgelegte Menge produzieren (Silber, Handel, Gegenstände, Schiffe und Gebäude).

Relativ eindeutig handelt es sich dabei um das sogenannte Rucksackproblem. Dabei gilt es hier eher darum den Rucksack so gering wie möglich zu überladen, d.h. die Einheiten so zuzuordnen, dass sich möglichst wenig Personen nichts tun. Prinzipiell ist es auch denkbar eine minimale Auslastungsgrenze (für die letzte zugeordnete Einheit) festzulegen.

Beim beladen eines Rucksackes zählt ja möglichst viel Wert auf den begrenzten Raum/Gewicht zu laden. Raum/Gewicht ist in unserem Fall die zu produzierende Menge. Einen Wert haben wir eher nicht, aber wir haben Kosten. Und die sind z.b. umso geringer je besser eine Einheit ausgebildet ist.

Das Rucksack-Problem kann man für einzelne sich stark unterscheidende Gegenstände die man in den Rucksack packt, recht gut über Pareto-Optimale Punkte (zwischenzustände) lösen. Leider haben wir bei Eressea oft die Situation mit sehr vielen gleich gut ausgebildeten Einheiten zu hantieren. d.h. die Kosten pro Person sind die gleichen, lediglich die Grösse mag unterschiedlich sein. Dadurch liegen aber ziemlich viele Zustände auf einer Linie, d.h. es lassen sich kaum welche eliminieren.

Wie geht man also prinzipiell vor:

1. Sortieren der vorhandenen Einheiten nach Kosten pro Person (geringste zuerst) und dann nach Anzahl Personen (meiste zuerst)
2. Rekursives Erzeugen der Zustände
    1. Achtung gleiche Einheiten (Kosten und Grösse) nur in definierter Reihenfolge zuordnen (d.h. falls die erste aus der Gruppe nicht dabei ist, die zweite nicht versuchen)
    2. Dabei entfernen von Zuständen die &gt;= Kosten bei &lt;= Produktionsmenge verursachen (Nicht Pareto-optimale Punkte)
    3. für die letzte Einheit und/oder ggf. kleinste Einheit die Nebenbedingung minimale Auslastung prüfen
3. Aus allen Zielzuständen den mit höchster Produktion und ggf. geringsten Kosten wählen

Eine Methode die uns das Ergebnis der Optimierung ausrechnet, braucht also lediglich eine Liste der Einheiten, deren Kosten und deren Produktionsmenge. Ggf. werden Methode noch Nebenbedingungen mitgegeben. Solche Einheitenliste lässt sich unabhängig vom eigentlichen Ziel relativ schnell erstellen und mit den notwendigen Attributen versehen. Das Rucksackproblem lässt sich auf die Produktion angewandt also recht leicht verallgemeinert implementieren.

<!-- From [https://wiki.eressea.de/index.php?title=Optimierung\_Produktion&oldid=2469] -->
