# ECheck

**ECheck** ist der Zugchecker, der auch auf dem Eressea-Server seinen Dienst tut. ECheck ist nicht perfekt und nicht vollständig. Es kann sowohl falsch negative, als auch falsch positive Meldungen geben. Wenn ECheck also keine Fehler meldet, heißt das nicht zwingend, dass die Befehle korrekt sind. Wenn ECheck Fehler meldet, heißt das nicht zwingend, dass die Befehle ungültig sind. Besonders bei Regeländerungen oder seltenen Gegenständen, weiß ECheck nicht immer sofort Bescheid. ECheck ist vielmehr als Hilfestellung gedacht, um gegebenenfalls die Befehle noch einmal zu prüfen.

ECheck kann auf verschieden Arten aufgerufen werden:

- Beim Einschicken von Befehlen wird ECheck automatisch aufgerufen und die Antwortmail vom Server enthält das Ergebnis. Hier wird nur auf Warnstufe 1 (siehe unten) geprüft.
- In Magellan. Hier kann man die Optionen beliebig einstellen. Magellan kann außerdem die "Meta-Befehle" automatisch hinzufügen. Das sind Kommentare, die ECheck helfen, zum Beispiel den Silberverbrauch zu prüfen. Es gibt aber eigentlich keinen Grund mehr, ECheck von Magellan aufzurufen, da Magellans eigene Mechanismen (Syntaxcheck und "Offene Probleme") zuverlässiger sind und mehr können.
- Auf der Kommandozeile (unter Windows Eingabeaufforderung ("cmd"), unter Linux in jedem Terminal). Dann muss man die unten aufgeführten Parameter mit angeben.

Es gibt verschiedene Warnstufen, die durch Kommandozeilenparameter gesteuert werden. Mit \`-w1\` werden nur Syntaxfehler ausgegeben. Die Stufen \`w2\` bis \`w4 geben zusätzliche Warnungen, zum Beispiel über Silberverbrauch, Lehrer oder Routen aus. Die noxxx-Parameter können außerdem bestimmte Warnungen unterdrücken. ECheck geht normalerweise davon aus, dass man deutsche Befehle für E2 eingibt. Englische Befehle kann man zum Beispiel mit dem Parameter -Len prüfen, Befehle für E3 mit -Re3.

## Aufruf

     Benutzung: ./echeck [Optionen] Befehlsdatei
     
     -Ppfad  Pfadangabe für die Zusatzdateien; das Locale de wird angehängt
     -Rgame  Zusatzdateien aus Unterverzeichnis game einlesen; Standardeinstellung: e2
     -       Verwendet stdin anstelle einer Eingabedatei.
     -b      unterdrückt Warnungen und Fehler (brief)
     -q      erwartet keine Angaben zu Personen/Silber in [] bei EINHEIT
     -rnnn   Legt Rekrutierungskosten auf nnn Silber fest
     -c      schreibt die Warnungen und Fehler in einer Compiler-ähnlichen Form
     -m      schreibt die Warnungen und Fehler für Magellan
     -e      schreibt die geprüfte Datei auf stdout, Fehler nach stderr
     -E      schreibt die geprüfte Datei auf stdout, Fehler nach stdout
     -ofile  schreibt die geprüfte Datei in die Datei 'file'
     -Ofile  schreibt Fehler in die Datei 'file'
     -h      zeigt diese kleine Hilfe an
     -hs     zeigt Liste der Schlüsselworte für tokens.txt
     -hb     zeigt Liste der Befehle für befehle.txt
     -hp     zeigt Liste der Parameter für parameter.txt
     -hr     zeigt Liste der Richtungen für richtungen.txt
     -hm     zeigt Liste der Meldungen für meldungen.txt
     -hf     zeigt Liste der Dateien, die ECheck versucht, einzulesen
     -s      verwendet stderr für Warnungen, Fehler etc., nicht stdout
     -p      verkürzt einige Ausgaben für piping
     -l      simuliert Silberpool-Funktion
     -n      zählt NameMe-Kommentare (;;) nicht als Zeile
     -noxxx  Keine xxx-Warnungen. xxx kann sein:
        ship   Einheit steuert Schiff und hat evtl. kein Kommando
        route  kein Check auf zyklisches ROUTE
        lost   Einheit verliert Silber und Gegenstände
     -w[n]   Warnungen der Stufe n (default: 4)
          1  hauptsächlich Syntaxfehler
          4  fast alle Warnungen
          5  Lehrer/Schüler
     -x      Zeilenzählung ab PARTEI statt Dateianfang
     -Lloc   Stellt Locale loc ein
     -vm.l   Mainversion.Level - für Test, ob richtige ECheck-Version
     -Q      Leise
     -C      Kompakte Ausgabe

## Siehe auch

- [Befehle einschicken]

## Externe Links und Downloads

- [Aktuelle Downloads für Windows (echeck.exe) und Linux (echeck)]
- [ECheck Sourcecode]
- [Eine veraltete ECheck-Version für Windows]

<!-- From [https://wiki.eressea.de/index.php?title=ECheck&oldid=7268] -->

[Befehle einschicken]: /Befehle_einschicken "Befehle einschicken"
[Aktuelle Downloads für Windows (echeck.exe) und Linux (echeck)]: https://www.eressea.kn-bremen.de/downloads
[ECheck Sourcecode]: https://github.com/eressea/echeck
[Eine veraltete ECheck-Version für Windows]: https://www.eressea.de/files/echeck.zip
