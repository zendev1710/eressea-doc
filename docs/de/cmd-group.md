# GRUPPE

**`GRUPPE`**`["`*`name`*`"]`

Mit dem Befehl `GRUPPE` kann man die Partei in Untergruppen zerteilen, die einen andere [`HELFE`]-Status haben als der Rest der Partei. Dadurch kann man z.B. ein Söldnerheer aufstellen, das auf der Insel des Auftragsgebers ihm hilft, während der Rest der Partei es nicht tut.

Ebenso kann man für Teilnehmer eines Turnieres alle `HELFE KÄMPFE` Zuordnungen auflösen, damit man nicht in einen Zweikampf eingreift. Auch Angriffe auf Verbündete, mit einem parteigetarnten Trupp von Einheiten sind möglich, ohne das man sich durch das Lösen von `HELFE KÄMPFE` auf Parteiebene verrät. Und wer z.B. seine Wälder auch vor Verbündeten schützen will, der stellt eine Truppe von Waldwächtern auf, die niemandem `HELFE BEWACHE` geben. Für jede Gruppe kann man außerdem ein eigenes [PRÄFIX] festlegen.

Eine Einheit gibt zum Beispiel den Befehl `GRUPPE` "Freibeuter der Meere", um in eine Gruppe einzutreten. Wenn es eine Gruppe dieses Namens noch nicht gibt, wird eine angelegt, die anfangs immer den gleichen `HELFE`-Status wie die Partei hat, auch wenn die Einheit vorher in einer anderen Gruppe war. Mit `GRUPPE` ohne Namen verlässt man eine Gruppe. Verlassen alle Einheiten eine Gruppe, wird diese aufgelöst. Sterben hingegen alle Einheiten einer Gruppe, bleibt die Gruppe bestehen und kann erneut betreten werden.

Jede Einheit kann nur einer Gruppe angehören. Eine Einheit, die einen `HELFE` Befehl gibt, ändert den Status ihrer Gruppe, wenn sie einer Gruppe zugeteilt ist, oder den Status der Partei, wenn sie keiner Gruppe angehört.

In einem Kampf wird aus jeder Gruppe ein getrenntes Heer, so wie es auch schon passiert, wenn Einheiten parteigetarnt sind.

<!-- exclude E3 from documentation -->
<!--
|---------|----------------------------------------------------------------------------------|
| **E3A** | Für E3 gilt das nicht! Hier sind alle Einheiten einer Partei in dem selben Heer. |
-->

<!-- From [https://wiki.eressea.de/index.php?title=GRUPPE&oldid=6657] -->

[`HELFE`]: ./cmd-help.md "HELFE"
[PRÄFIX]: ./cmd-prefix.md "PRÄFIX"
