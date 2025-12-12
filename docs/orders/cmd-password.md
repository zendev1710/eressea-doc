---
alias:
	name: 
	text: 
---
# PASSWORD

**`PASSWORD`**`["neues-passwort"]`

Dies setzt das Passwort neu. Man muß es von der nächsten Befehlsdatei an immer mit dem Befehl [`ERESSEA`] zusammen verwenden. Erlaubt sind im Passwort nur Buchstaben und Ziffern. Enthält es unzulässige Zeichen, so werden diese durch zufällige erlaubte zeichen ersetzt. `PASSWORD` ohne Parameter setzt ein zufällig erzeugtes Passwort.

Am Anfang wird jeder Partei ein zufälliges Passwort zugeordnet.

Beispiel:

    ; in der zweiten Woche des Monats Herdfeuer
    ERESSEA 11 "AltesPasswort"
      PASSWORD "Falsch" ; kein Effekt
       UNIT 75
         PASSWORD "MoftZga" ; das gilt ab nächster Runde!
         [...]
        
        
    ; in der letzten Woche des Monats Herdfeuer
    ERESSEA 11 "MoftZga"
      [...]

Vorsicht:

- Das Passwort ist die einzige Stelle in der Befehlsdatei, bei der Groß- und Kleinschreibung berücksichtigt wird.
- Das Passwort muss von einer Einheit gesetzt werden.
- Für die jeweilige Befehlsdatei gilt immer das Passwort, welches auch im letzten Zug galt, oder dasjenige, welches im letzten Zug neu gesetzt wurde. Das Passwort vom letzten Zug gilt auch dann noch, wenn für den jetzigen Zug mehrere Befehlsdateien eingeschickt wurden, in denen unterschiedliche Passwörter gesetzt wurden.
- Das Passwort wurde nur dann erfolgreich neu gesetzt, wenn auch die entsprechende Meldung in der Auswertung stand: `Das Passwort wurde auf "blabla" geändert`.

<!-- From [https://wiki.eressea.de/index.php?title=PASSWORD&oldid=6276] -->

[`ERESSEA`]: ./cmd-eressea.md "ERESSEA"
