---
# cSpell:locale de
alias: allianz
---
# Allianz

Allianzen bilden das Rückgrat der Welt, ob dies nun Kriegs-, Handels- oder einfach nur Friedensallianzen sind.
In Eressea gibt es einige Bereiche, in denen man anderen Parteien nicht nur "im Geiste" helfen, sondern sie auch regeltechnisch unterstützen kann, was mit dem Befehl [[bef-helfe]] geschieht.

Wenn eine Partei einer anderen hilft, bedeutet das nicht automatisch, dass die andere Partei dies auch macht.
Hier verhilft nur die Probe auf's Exempel zur Klarheit.
Dass diese Rechte nicht automatisch gewährt werden, hat seinen Grund: wäre dies nicht so, könnte man gegnerische Einheiten mit Steinen beladen, den feindlichen Elitetruppen ein paar Bauern anhängen, oder dem lokalen Burgherren seine gesamten Steuern abzweigen.

Zu den einzelnen Bereichen der Unterstützung:

## `HELFE GIB`

Die eigenen Einheiten werden alles annehmen, was alliierte Einheiten ihnen geben (Silber, Gegenstände usw.).
Dies ist quasi ein ständiges [[bef-kontaktiere]] für [[bef-gib]].

!!! warning "Achtung"
    Für die Übergabe einzelner Personen oder Einheiten an Einheiten einer anderen Partei mit dem Befehl [[bef-gib|GIB fremder-einheit anzahl PERSONEN]] muss weiterhin der [[bef-kontaktiere]]-Befehl explizit von der Empfänger-Partei benutzt werden!  
    Ebenso kann für einige Zauber ein [[bef-kontaktiere]] notwendig sein.

## `HELFE KÄMPFE`

Eigene kampfbereite Einheiten (solche mit Kampfstatus vorne und hinten) werden mit in einen [[krieg|kampf]] eingreifen, wenn die alliierte Partei angegriffen wird.

## `HELFE SILBER`

Hiermit unterstützen die eigenen Einheiten die alliierte Partei im Unterhalt, sofern sie nach dem Unterhalt für die eigenen Einheiten noch Silber übrig haben.
Reicht das Silber der alliierten Einheiten nicht zur Ernährung, werden die eigenen Einheiten mit Silber aushelfen.
Für das reine Bereitstellen von Unterhalt über HELFE SILBER ist kein HELFE GIB der Empfängerpartei notwendig.

## `HELFE BEWACHE`

Hebt die behindernden Funktionen von [[bef-bewache]] auf und dehnt die nützlichen Funktionen auf die Zielpartei aus: Normalerweise lassen bewachende Einheiten keine andere Partei [Steuern eintreiben], [rekrutieren] oder endliche [Rohstoffe] abbauen und manchmal werden fremde Einheiten bei der [Durchreise aufgehalten][[bef-bewache]].
Ist diese Hilfe gesetzt, wird den Einheiten der anderen Partei dieses gestattet und sie können ungehindert durchreisen, abbauen und rekrutieren.

Außerdem dürfen alliierte Parteien eventuell nach langen Kämpfen noch lange Befehle ausführen (siehe [Kampfende]).

Schließlich wird hiermit alliierten Parteien erlaubt, eigene Burgen und Schiffe zu [[bef-betrete|betreten]].

## `HELFE PARTEITARNUNG`

Wenn man eigene Einheiten mit [bef-tarne|TARNE PARTEI NUMMER xx] mit einer anderen Parteikennung versieht, können Parteien, denen man diesen Helfe-Status gibt, die echte Partei trotzdem erkennen.

## `HELFE ALLES`

ist die Zusammenfassung aller einzelnen Bereiche.

## siehe auch

- [[bef-helfe]]
- [[bef-bewache]]
- [[bef-kontaktiere]]

Weiterlesen: [[magie-de]].

<!-- From [https://wiki.eressea.de/index.php?title=Allianz&oldid=16179] -->

[Steuern eintreiben]: ./silver.md
[rekrutieren]: ./silver.md#rekrutieren "REKRUTIERE"
[Rohstoffe]: ./resources.md
[Kampfende]: ./war.md#das-ende "Kampfende"
