---
# cSpell:locale en
alias:
    name: cmd-name
    text: NAME
---
# NAME

    NAME UNIT "name"
    NAME FREMDE UNIT unit-id "name"
    NAME PARTEI "name"
    NAME FREMDE PARTEI faction-id "name"
    NAME GEBÄUDE "name"
    NAME FREMDES GEBÄUDE building-id "name"
    NAME SCHIFF "name"
    NAME FREMDES SCHIFF ship-id "name"
    NAME REGION "name"
    NAME GROUP "name"

Benenne das aufgeführte Objekt neu. Schiffe und Gebäude können nur umbenannt werden, wenn die Einheit auch das Kommando über das Gebäude oder das Schiff hat - sie muss also die erste Einheit unter dem Gebäude oder dem Schiff in der Auswertung sein. Eine Region kann nur vom Burgherr der mächtigsten Burg einer Region umbenannt werden. Gruppen können nur von Gruppenmitgliedern umbenannt werden und der neue Gruppenname darf nicht bereits vorhanden sein.

Der neue Name kann bis zu 127 Zeichen lang sein. Längere Beschreibungen fügt man mit dem Befehl [[cmd-describe]] an.

Durch den Zusatz `FREMDE` (bzw. `FREMDES`) und der Angabe der Nummer kann man Einheiten, Schiffe und sogar Gebäude (nicht nur Burgen) anderer Parteien benennen, sofern diese noch keinen Namen haben (Einheiten also als "Einheit abc" benannt sind). Man kann sogar eine fremde Partei benennen, sofern diese älter als zehn Runden ist.

Auch das Benennen der Partei muss von einer Einheit ausgeführt werden.

    ERESSEA 7 "sieben"
       NAME PARTEI "Falsch" ; kein Effekt
       UNIT 89
          NAME PARTEI "Richtig"

<!-- From [https://wiki.eressea.de/index.php?title=NAME&oldid=16968] -->

[`DESCRIBE`]: ./cmd-describe.md
