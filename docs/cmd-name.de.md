---
# cSpell:locale de
alias: bef-benenne
---
# BENENNE

**`BENENNE`` ``EINHEIT "`*`name`*`"`**  
**`BENENNE`` ``FREMDE EINHEIT <einheit-nr> "<name>"`  
**`BENENNE`` ``PARTEI "<name>"`**  
**`BENENNE`` ``FREMDE PARTEI <partei-nr> "<name>"`**  
**`BENENNE`` ``GEBÄUDE "<name>"`**  
**`BENENNE`` ``FREMDES GEBÄUDE <gebäude-nr> "<name>"`**  
**`BENENNE`` ``SCHIFF "<name>"`**  
**`BENENNE`` ``FREMDES SCHIFF <schiff-nr> "<name>"`**  
**`BENENNE`` ``REGION "<name>"`**  
**`BENENNE`` ``GRUPPE "<name>"`**  

Benenne das aufgeführte Objekt neu. Schiffe und Gebäude können nur umbenannt werden, wenn die Einheit auch das Kommando über das Gebäude oder das Schiff hat - sie muss also die erste Einheit unter dem Gebäude oder dem Schiff in der Auswertung sein.  
Eine Region kann nur vom Burgherr der mächtigsten Burg einer Region umbenannt werden.  
Gruppen können nur von Gruppenmitgliedern umbenannt werden und der neue Gruppenname darf nicht bereits vorhanden sein.

Der neue Name kann bis zu 127 Zeichen lang sein.  
Längere Beschreibungen fügt man mit dem Befehl [`BESCHREIBE`][bef-beschreibe] an.  

Durch den Zusatz `FREMDE` (bzw. `FREMDES`) und der Angabe der Nummer kann man Einheiten, Schiffe und sogar Gebäude (nicht nur Burgen) anderer Parteien benennen, sofern diese noch keinen Namen haben (Einheiten also als "Einheit abc" benannt sind).  
Man kann sogar eine fremde Partei benennen, sofern diese älter als zehn Runden ist.

Auch das Benennen der Partei muss von einer Einheit ausgeführt werden.

```text
ERESSEA 7 "sieben"
    BENENNE PARTEI "Falsch" ; kein Effekt
    EINHEIT 89
        BENENNE PARTEI "Richtig"
```

<!-- From [https://wiki.eressea.de/index.php?title=BENENNE&oldid=16968] -->

[bef-beschreibe]: [[bef-beschreibe]]
