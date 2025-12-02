# OPTION

**`OPTION`**` `*`option`*`[NICHT]`

Diese Optionen lassen sich ein- und ausstellen. Sie kontrollieren, wie die Auswertung genau aussieht.

- `AUSWERTUNG`: Dies ist die normale Auswertung im Klartext. Falls man nur die Computer Auswertung verwendet, kann auf die normale Auswertung verzichtet werden.

- `COMPUTER`: Diese Auswertung ist für Programme leichter zu lesen. Mit ihr kann jede Art von selber geschriebenen Programmen gespeist werden, z.B. Hilfstools oder Kartenzeichner.

- `ZIPPED`: Die Auswertung wird vor dem Versand mit zip gepackt.

- `BZIP2`: Die Auswertung wird vor dem Versand mit bzip2 gepackt.

- `STATISTIK`: Mit dieser Option wird nach jeder Region in der normalen Auswertung eine kleine Statistik angezeigt.

- `PUNKTE`: Mit dieser Option wird, frühestens ab der 13. Runde, eine Punktzahl ausgegeben, die einen kleinen Vergleich mit anderen Parteien zulässt.

- `ZUGVORLAGE`: Eine separate Datei enthält eine [Vorlage für die Befehle der nächsten Runde]. Diese kann man hiermit aus- und wieder anstellen. Wer diese nicht benötigt, weil er z.B. zur Zugerstellung ein Tool benutzt, sollte die Zugvorlage abstellen.

- `TALENTVERSCHIEBUNG`: Hiermit kann man eine kleine Anzeige im NR einschalten. Hinter dem Talent ist dann aufgeführt, wenn sich das Talent in der betreffenden Runde verändert hat.

- `ADRESSEN`: Hiermit wird die Adressliste der Parteien, die man in der Runde gesehen hat, an den Report angehängt.

## Alte Optionen

Mit der Auswertung Nummer 559 wurden die Optionen Materialpool und Silberpool als Standard gesetzt. Eine Deaktivierung ist nicht mehr möglich

`SILBERPOOL`: Normalerweise zahlen Einheiten anfallende Ausgaben "aus eigener Tasche". Mit dieser Option kann eingeschaltet werden, dass notwendiges Silber von allen Einheiten der Region gesammelt wird.

`MATERIALPOOL`: ist der [Materialpool] eingeschaltet, werden allen benötigten Gegenstände einer Einheit ähnlich wie Silber mit dem [Silberpool] bei Bedarf zusammengesammelt. Einheiten können sich mit dem Befehl [`RESERVIERE`] Gegenstände sichern und so vermeiden, dass andere Einheiten sie von ihnen nehmen und verbrauchen. Diese Option sollte wohlüberlegt benutzt werden, da man schnell unbedacht z.B. alles Holz einer Region verbaut, welches man für andere Zwecke verplant hatte, nur weil man ein `RESERVIERE` vergaß.

<!-- From [https://wiki.eressea.de/index.php?title=OPTION&oldid=16703] -->

  [Vorlage für die Befehle der nächsten Runde]: /Befehl "Befehl"
  [Materialpool]: /Materialpool "Materialpool"
  [Silberpool]: ./items-pool.md#der-silberpool "Silberpool"
  [`RESERVIERE`]: /RESERVIERE "RESERVIERE"
