---
# cSpell:locale fr, en
alias: cmd-contact-fr
---
# CONTACT

**`CONTACT`**` UNIT `*`unit-id`*  
**`CONTACT`**` PARTEI `*`faction-id`*  
**`CONTACT`**` `*`unit-id`*  

Man darf Einheiten fremder Parteien normalerweise nichts geben, ohne dass man mit dieser Partei alliiert ist. Um dies im begrenzten Maße doch zu erlauben, gibt es den `CONTACT` Befehl. In dieser Runde - und nur in dieser Runde - verhält sich die befehlende Einheit der genannten Einheit gegenüber, als wenn sie mit ihr alliiert wäre (s.a. unter [[cmd-help]]), d.h. sie nimmt Gegenstände, Silber und Personen von ihr an. Auch das Betreten von Burgen und Schiffen, das Rekrutieren von Personen und der Abbau von Ressourcen ist nicht-alliierten Parteien auf diesem Wege möglich.

`CONTACT UNIT` erlaubt dies einer einzigen Einheit, CONTACT PARTEI hingegen allen Einheiten der betreffenden Partei in einer Region. Der Befehl `CONTACT unit-id` ist aus historischen Gründen erlaubt, sollte aber durch `CONTACT UNIT unit-id` ersetzt werden.

**Beispiele:**

    PARTEI ff "FooBar"
      UNIT a
      GIVE x 1000 Silber ; Tribut!
      [...]

    PARTEI 300 "BarFoo"
      UNIT x
      CONTACT UNIT a ; erlaube Zahlung.

Einheit a darf Einheit x also die 1000 Silber übergeben. Falls x die einzige bewachende Einheit der Region ist, darf a auch rekrutieren und Steuern eintreiben. Einheit b von Partei ff darf nichts davon. Dafür müsste Einheit x den Befehl `CONTACT PARTEI ff` geben.

- Einheit x und Einheit y einer Partei bewachen die Region. Damit Einheit a rekrutieren kann, müssen x und y beide `CONTACT UNIT a` oder `CONTACT PARTEI ff` befehlen.

## Unterschiede zu HELP

`CONTACT` hat eine ähnliche Funktion wie [`HELP GIVE + HELP GUARD`][HELP], ist aber nicht 100%ig dasselbe.

- `CONTACT` ist für manche Dinge erforderlich, die `HELP GIVE` oder `HELP GUARD` nicht abdeckt, wie zum Beispiel [`GIVE PERSONEN`] und manche Zauber.
- `HELP` schließt `HELP SILBER, HELP COMBAT` und `HELP PARTEITARNUNG` ein.
- `CONTACT` gilt nur für die aktuelle Runde und nur für die befehlsgebende Einheit.
- `HELP` ist dauerhaft und für alle Einheiten meiner Partei oder Gruppe (und alle Einheiten der anderen Partei).

<!-- From [https://wiki.eressea.de/index.php?title=CONTACT&oldid=13303] -->

[HELP]: ./cmd-help.md
[`GIVE PERSONEN`]: ./cmd-give.md
