---
# cSpell:locale de
alias: bef-kontaktiere
---
# KONTAKTIERE

**`KONTAKTIERE`**` EINHEIT `*`einheit-nr`*  
**`KONTAKTIERE`**` PARTEI `*`partei-nr`*  
**`KONTAKTIERE`**` `*`einheit-nr`*  

Man darf Einheiten fremder Parteien normalerweise nichts geben, ohne dass man mit dieser Partei alliiert ist. Um dies im begrenzten Maße doch zu erlauben, gibt es den `KONTAKTIERE` Befehl. In dieser Runde - und nur in dieser Runde - verhält sich die befehlende Einheit der genannten Einheit gegenüber, als wenn sie mit ihr alliiert wäre (s.a. unter [[bef-helfe]]), d.h. sie nimmt Gegenstände, Silber und Personen von ihr an. Auch das Betreten von Burgen und Schiffen, das Rekrutieren von Personen und der Abbau von Ressourcen ist nicht-alliierten Parteien auf diesem Wege möglich.

`KONTAKTIERE EINHEIT` erlaubt dies einer einzigen Einheit, KONTAKTIERE PARTEI hingegen allen Einheiten der betreffenden Partei in einer Region. Der Befehl `KONTAKTIERE einheit-nr` ist aus historischen Gründen erlaubt, sollte aber durch `KONTAKTIERE EINHEIT einheit-nr` ersetzt werden.

**Beispiele:**

    PARTEI ff "FooBar"
      EINHEIT a
      GIB x 1000 Silber ; Tribut!
      [...]

    PARTEI 300 "BarFoo"
      EINHEIT x
      KONTAKTIERE EINHEIT a ; erlaube Zahlung.

Einheit a darf Einheit x also die 1000 Silber übergeben. Falls x die einzige bewachende Einheit der Region ist, darf a auch rekrutieren und Steuern eintreiben. Einheit b von Partei ff darf nichts davon. Dafür müsste Einheit x den Befehl `KONTAKTIERE PARTEI ff` geben.

- Einheit x und Einheit y einer Partei bewachen die Region. Damit Einheit a rekrutieren kann, müssen x und y beide `KONTAKTIERE EINHEIT a` oder `KONTAKTIERE PARTEI ff` befehlen.

## Unterschiede zu HELFE

`KONTAKTIERE` hat eine ähnliche Funktion wie [`HELFE GIB + HELFE BEWACHE`][[bef-helfe]], ist aber nicht 100%ig dasselbe.

- `KONTAKTIERE` ist für manche Dinge erforderlich, die `HELFE GIB` oder `HELFE BEWACHE` nicht abdeckt, wie zum Beispiel [`GIB PERSONEN`] und manche Zauber.
- `HELFE` schließt `HELFE SILBER, HELFE KÄMPFE` und `HELFE PARTEITARNUNG` ein.
- `KONTAKTIERE` gilt nur für die aktuelle Runde und nur für die befehlsgebende Einheit.
- `HELFE` ist dauerhaft und für alle Einheiten meiner Partei oder Gruppe (und alle Einheiten der anderen Partei).

<!-- From [https://wiki.eressea.de/index.php?title=KONTAKTIERE&oldid=13303] -->

[bef-helfe]: ./cmd-help.md
[`GIB PERSONEN`]: ./cmd-give.md
