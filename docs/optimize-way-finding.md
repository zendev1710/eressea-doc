---
# cSpell:locale en
alias:
    name: optimize-wayfinding
    text: Optimizing wayfinding
---
# Optimizing wayfinding

Die generelle Funktionsweise eine Routenberechnung dürfte vielen bekannt sein. Es werden glücklicherweise nicht alle Wege nach Rom gesucht, sondern nur solche die offenbar in die ungefähre Richtung gehen.

Die einfachste Möglichkeit (Greedy) wäre vom Startpunkt aus erstmal alle vorhandenen Wege zu gehen und sich die neuen Zwischenpunkte zu merken. Von dort aus werden wieder alle Wege gegangen. Es wird sich immer der kürzeste Weg zu einem Punkt gemerkt (Route und Entfernung). Expandiert man so immer weiter findet man irgendwann den Zielpunkt (sofern er erreichbar ist). Das man dabei dem Ziel nicht nur näher kommt, sondern sogar in die total falsche Richtung läuft bei einigen Wegen ist jedoch bei langen Routen ein extremer Nachteil, sowohl was die Abarbeitungszeit als auch den Speicherbedarf für Zwischenzustände angeht.

Die A\*-Suche hingegen hat zum Ziel, möglichst nur Zwischenpunkte zu expandieren die tatsächlich auf der richtigen Route liegen. Durch einen Kostenfunktion werden für jeden Punkt (inklusive Start und Ziel) die Kosten berechnet die **vermutlich** bis zum Ziel anfallen. Wichtig ist hierbei das vermutlich, denn wir kennen ja die Entfernung zum Ziel nicht, solange wir die Route nicht kennen. D.h. also wir schätzen die Entfernung. Auf der Landkarte ist hierbei die Luftlinie eine gute Schätzung die wir sicher nicht unterbieten werden (ohne Stargates, Wurmlöcher und dergleichen ;-)

Für Eressea und andere Spiele auf Hex-Karten kann die minimale Entfernung relativ leicht aus den Koordinaten berechnet werden.

    hx = start.x - ziel.x
    hy = start.y - ziel.y
    Distanz = max(abs(hx), abs(hy), abs(hx+hy))

Diese geschätzte Entfernung zum Ziel wir mit der bereits zurückgelegten addiert. Nach diesem Kriterium werden die noch zu expandierenden Regionen sortiert. Bei wenigen Hindernissen auf der Karte gelangt der Algorithmus so sehr schnell auch über weite Entfernungen zum Ziel.

Jedes Hindernis und jede zusätzliche Bedingung, die in die Kostenfunktion eingebaut werden sollen, lassen die Ausführung hingegen schnell wieder langsamer werden.

Magellan hat eine Funktion zur Routenfindung bereits eingebaut. Sie unterstützt neben der Entfernung auch das Entlangsegeln von Schiffen an Küsten.

Weitere Nebenbedingungen können die Sicherheit von Regionen betreffen (Seeschlangen, Gegner), die Anlanderichtung in der Zielregion oder der bevorzugte Zwischenstopp in Landregionen zum Rundenende. Gerade solche Nebenbedingungen lassen sich jedoch schwer bis gar nicht durch die Schätzfunktion berechnen, so dass das Verhalten des Algorithmus immer mehr "greedy" wird. Den die A\*-Suche mit einer Schätzfunktion die immer 0 zurückgibt entspricht der Greedy-Suche.

<!-- From [https://wiki.eressea.de/index.php?title=Optimierung\_Wegfindung&oldid=2478] -->
