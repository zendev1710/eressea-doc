---
alias: automatisierung-ereignissreaktion
---
# Automatisierung Ereignissreaktion

Viele Ereignisse in Eressea sind zufällig oder durch andere Spieler beeinflusst.
Um solche Ereignisse nicht zu verpassen oder besser noch gleich angemessen darauf zu reagieren, muss man natürlich erstmal festlegen welche Ereignisse man entdecken will und wie dies zu bewerkstelligen ist.

## Meldungen

Viele Ereignisse lassen sich einfach durch prüfen der Meldungen erkennen - ausgelöste magische Effekte, erscheinende Monster, Kämpfe, Hunger ...

Dabei reicht es meist nach dem Meldungtyp zu suchen und die Attribute der Meldung zu verwenden.

## Vergleichen

Alles andere lässt sich leider meist nur durch vergleichen des Zustandes mit der Ereignisbedingung prüfen.
Anwesenheit bestimmter Einheiten oder Rassen, Durchreise von unbekannten Einheiten oder Schiffen, ...

## Priorität

Prinzipiell bietet es sich an Ereignisse mit einer Priorität zu versehen um dann entsprechend der Priorität die Ereignisse abzuarbeiten.

## Reaktion

Hat man die Ereignisse priorisiert, geht es daran betroffene Einheiten zu ermitteln um diesen an ggf.
eine Reaktion auf dieses Ereignis zu ermöglichen.
Schwierig ist trotz Priorität die Reaktion auf mehrere Ereignisse, da möglicherweise durchaus auch sekundäre Ereignisse noch einen Einfluss auf die Befehle der Einheit haben können.

<!-- TODO: replace outdaed example, the current remains here until a suitable alternative example is created -->
***veraltet***: hungern verhindert lange befehle nicht mehr
Beispiel:
Eine Einheit hungert und es erscheinen Untote.
Die höhere Priorität sollte hier der Hunger haben, da dieser den langen Befehl ARBEITEN erzwingt.
Damit werden die Reaktionsmöglichkeiten auf das Untotenereignis natürlich eingeschränkt.
Ein Bewegen in die Nachbarregion ist nicht mehr möglich.
Es ist jedoch möglich den Kampfstatus zu setzen.
Je nach nachdem ob man über- oder unterlegen ist, sind hier natürlich unterschiedliche Reaktionen notwendig.

<!-- From [https://wiki.eressea.de/index.php?title=Automatisierung\_Ereignissreaktion&oldid=6434] -->
