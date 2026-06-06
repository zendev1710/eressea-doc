---
# cSpell:locale de
alias: gebaeude
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# Gebäude

Es gibt verschiedene Gebäude in Eressea, die unterschiedliche Vorteile bieten. Außer Burgen und Monumente brauchen alle Gebäude einen laufenden Unterhalt, der die Funktion sicherstellt.

## Unterhalt

Diese Unterhaltskosten sind meistens unabhängig von der Größe des Gebäudes und müssen am Anfang der Runde vom Besitzer des Gebäudes bezahlt werden, zwischen dem [[bef-gib]]-Befehl und den langen Befehlen (siehe [Befehlsreihenfolge]). Eine Einheit kann also nicht Steuern eintreiben und dann mit dem eingetriebenen Geld den Unterhalt bezahlen. Ist zu diesem Zeitpunkt kein Geld da, funktioniert das Gebäude nicht.

Der Unterhalt ist voll fällig, sobald an dem Gebäude gebaut wird; allerdings noch nicht in der Runde, in der es mit [`MACHE`*`Gebäude`*] angefangen wird. Dies hat zur Folge, dass unterhaltspflichtige Gebäude, die in nur einer Runde fertiggestellt werden, in der Bauwoche nicht funktionieren, da zu Beginn der Woche kein Unterhalt bezahlt wurde.

Wenn das Silber knapp ist, oder man in einer Woche ein bestimmtes Gebäude nicht benutzt und den Unterhalt sparen möchte, kann die Einheit, die das Kommando über das Gebäude hat (siehe nächster Abschnitt), mit dem Befehl [`BEZAHLE NICHT`] dafür sorgen, dass der Unterhalt in dieser Runde nicht bezahlt wird. Das Gebäude hat dann in dieser Woche natürlich keine Funktion.

## Einheiten und Gebäude

Unter einem Gebäude sind die Einheiten eingerückt, die sich in dem betreffenden Gebäude befinden. Die erste Einheit hat das Kommando über das Gebäude. Sie bestimmt, welche anderen Einheiten das Gebäude betreten dürfen, und sie darf das Gebäude umbenennen und beschreiben. Die Besitzereinheit der größten Burg einer Region darf sogar die Region, über die sie herrscht, umbenennen und beschreiben.

Die Wirkung von Gebäuden (auch von Burgen) wird einheitenweise angerechnet. Einheiten, die also - auch nur teilweise - nicht mehr in die noch freie Kapazität passen, bekommen keinen Bonus durch das Gebäude - auch dann, wenn sie die einzige Einheit sind!

Sind mehrere Einheiten in einem Gebäude, werden diese der Reihe nach von oben nach unten abgefragt. Die erste zu große Einheit "sperrt" das Gebäude dann für weitere, auch dann, wenn kommende Einheiten passen würden, wenn die zu große nicht dort wäre. Der [[bef-sortiere]]-Befehl kann hier abhelfen.

## Bau und Abriss

Gebäude werden mit dem [[bef-mache]][`MACHE `*`Gebäude`*]-Befehl gebaut und erweitert. Wie bei anderen Produktionsbefehlen ist die Bauleistung von Talent (Burgenbau) und Größe der Baumeistereinheit und vom erforderlichen Mindesttalent abhängig. Eine Einheit kann pro Runde (Talentstufe x Personen / Mindesttalent) Größenpunkte bauen; du kannst also beispielsweise mit einer hinreichend guten Einheit und genug Steinen problemlos in einer Woche einen Turm bauen. Gebäude können mit dem Befehl [ZERSTÖRE] wieder abgerissen werden.

## Siehe auch

- [Burgen]
- [Andere Gebäude]
- [Produktion]
- [Ausgaben][ausgaben]
- [Zerstöre][4]

Weiterlesen: [Burgen].

[Burgen]: ./castles.md

<!-- From [https://wiki.eressea.de/index.php?title=Gebäude&oldid=16113] -->

[bef-gib]: ./cmd-give.md
[Befehlsreihenfolge]: ./commands-sequence.md
[`MACHE `*`Gebäude`*]: ./cmd-make.md
[bef-sortiere]: ./cmd-sort.md
[ZERSTÖRE]: ./cmd-destroy.md
[Andere Gebäude]: ./buildings-others.md
[Produktion]: ./production.md
[4]: ./cmd-destroy.md
[`BEZAHLE NICHT`]: ./cmd-pay-not.md
