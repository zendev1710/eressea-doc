---
# cSpell:locale de
alias: hinweise
---

# Hinweise

## Anmeldung

Unter dem folgenden [diesen Link] kann man sich wieder für Eressea anmelden, bzw. für kommende Partien Eressea vormerken lassen.

## Fehler im Spiel

Ein so großes und komplexes Programm wie Eressea beinhaltet unausweichlich Fehler.  
Das Design-Team versucht, diese Fehler schnellstmöglich zu finden und zu beheben, trotzdem werden Fehler auftauchen.

**Wer damit nicht leben kann, sollte Eressea nicht spielen!**

Es ist nicht möglich, für einen einzelnen Spielenden eine Runde nochmals auszuwerten.  
Eine neue Auswertung wird nur dann gemacht, wenn der Fehler viele Parteien schwerwiegend betraf.

Ebenso ist es nicht immer möglich, durch Fehler aufgetretene Verluste u.ä. auszugleichen bzw. zu ersetzen, besonders dann nicht, wenn Personen oder Gegenstände wie Schiffe oder Gebäude verloren gingen.

Es liegt alleine im Ermessen der Spielleitung, betroffenen Spielern Ersatz, z.B. in Form von Silber, zu geben.  
Gerade kleinere Fehler betreffen oftmals viele Parteien, so dass es sich im Großen und Ganzen von alleine ausgleicht.

Alle Spielenden sind angehalten, auftretende Fehler der Spielleitung zu melden, auch und besonders dann, wenn sie davon Vorteile haben.  
Dazu eignet sich am best ein [Bugreport][bugreport] auf [Mantis] mit dem betreffenden Ausschnitt des Reports und einer Erklärung.

## Bugreport

Eressea ist nicht fehlerfrei, doch es hat sehr wenige Fehler.  
Wenn man meint, einen Fehler gefunden zu haben, gehe man wie folgt vor:

1. Überprüfe nochmal genau, ob der Fehler im Programm liegt. Manchmal hat man einfach eine Kleinigkeit übersehen.
2. Lies die Mails in der Liste "E-Announce", die Bugreports in Mantis oder den Kanal \#general im [Discord]: manchmal wurde der Fehler schon gefunden, und deine Meldung wäre überflüssig.
3. Überlege dir, wie es wohl zu dem Fehler kam. Stelle alles notwendige dafür zusammen. Starte einen neuen Bureport in [Mantis]. Er sollte folgendes enthalten:
    1. Deine Parteinummer
    2. Nummern der betroffenen Einheiten, Schiffe oder anderer Objekte
    3. Meldungen aus dem Report, welche für das Ereignis relevant sind
    4. Namen und Regions-IDs der Regionen, in denen es passiert ist
    5. relevante Ausschnitte aus dem aktuellen und ggf. älteren Reports
    6. Ausschnitte aus den Befehlsdateien
    7. Server-Version in welcher der Fehler aufgetreten ist
    8. eine Beschreibung, die alle notwendigen Informationen enthält um den Fehler zu verstehen und nachzuvollziehen, einschließlich
    9. der Ausgangslage
    10. was du erwartet hättest
    11. was wirklich passiert ist
    12. Bitte hänge nicht deinen ganzen Report an, wenn du nicht danach gefragt wirst! Bugreports sind im Allgemeinen öffentlich.
    13. Wenn du deinen Report oder Informationen schicken musst, die deine Mitspieler nicht haben sollten, füge dem Report eine Notiz hinzu und markiere sie als "privat".

Bitte nicht gleich ungeduldig werden, wenn nicht sofort eine Antwort kommt.  
Wenn du schnell eine Antwort brauchst, stelle eine Frage im [Discord].

Behobene Bugs werden in der Regel nicht mehr sofort in die aktuelle Serverversion eingespielt, wenn es sich nicht um gravierende Fehler handelt.  
Der neue Code wird zunächst getestet und dann einmal im Quartal nach vorheriger Ankündigung ausgerollt.  
Dies dient der Stabilität der Auswertung.  
Wenn ein Bug in Mantis also als "behoben" markiert wurde, bedeutet es *nicht* automatisch, dass der Fehler in der nächsten Auswertung nicht mehr vorkommt.

## Schummeln

**Schummeln** führt zum Ausschluss aus dem Spiel.

Schummeln verdirbt anderen Spielern und oft auch einem selber den Spielspaß.  
Konkret werden unter anderem die folgenden Punkte als Schummelversuch angesehen:

### Doppelspiel

Wer mehr als eine Partei spielt ("Doppelspiel"), erschleicht sich damit einen Vorteil gegenüber anderen Spielern mit nur einer Partei.  
Aus diesem Grund ist Doppelspiel grundsätzlich verboten.  
Mehrere Parteien zu spielen hebelt Beschränkungen wie das Einheitenlimit, die Obergrenze für Magier und Alchemisten, sowie die Rassenfertigkeiten aus.

Die Vergangenheit hat gezeigt, dass ein solches Verbot alleine nicht reicht, und aus verschiedenen Gründen doch Doppelspiel auftritt.  
Ohne Absprache mit der Spielleitung ist das, egal aus welchem Grund, trotzdem ein Grund, vom Spiel ausgeschlossen zu werden.

Ein anderer Grund ist oft, dass das Ausscheiden einer Partei zu einer starken Änderung der Kräfteverhältnisse führen würde.  
Eine Allianz, die ein wichtiges Mitglied verliert, übernimmt die Partei des Spielers, und führt sie als Zweitpartei.  
Das ist ebenfalls nicht okay, es sei denn es wurde mit der Spielleitung abgesprochen (es gibt mehrere Altparteien, bei denen es erlaubt wurde).  
Zur Linderung des Phänomens haben wir den Befehl [`STIRB`][bef-stirb] mit dem Argument PARTEI, der die Einheiten der ausscheidenden Partei an eine verbündete Partei übergibt, was die Einhaltung des Einheitenlimits und der Obergrenzen für Magier, Helden, etc.  
gewährleistet.

Mehrere Spieler, die sich einen Mail-Account teilen, können zu Eressea nicht zugelassen werden - die Gefahr des Schummelns ist hier zu groß.

Weder die Übergabe noch das Beschaffen von Passwörtern anderer Spieler ist erlaubt und das Einsenden von Befehlen für fremde Parteien ist grundsätzlich verboten.

**Nichtbeachtung dieser Regeln führt zum Ausschluss aller beteiligten Parteien.**

### Zweitpartei

Einzige Ausnahme zum generellen Verbot zum führen mehrerer Parteien: Wer wirklich nicht mit einer Partei ausgelastet ist, darf eine **zweite** Partei starten, wenn seine erste Partei mindestens 150 Runden alt ist.

Der Fairness halber muss allerdings immer offensichtlich sein, dass zwei Parteien nicht unabhängig geführt werden, und wann immer zwei Parteien ihre Befehl vom selben Spieler bekommen, müssen diese die selbe E-Mail-Adresse benutzen.  
Die eingetragene Adresse muss existieren und der Spieler innerhalb von 14 Tagen auf Mails der Spielleitung an ihre Adresse reagieren, falls es Zweifel an ihrer Echtheit gibt.

**Nichtbeachtung dieser Regeln führt zum Ausschluss aller beteiligten Parteien.**

### Urlaubsvertretung

Das Einsenden von Befehlen für fremde Parteien ist grundsätzlich verboten.  
Die einzige Ausnahme hiervon sind Urlaubsvertretungen.  
Damit diese legal sind, muss die zu vertretende Partei im [`BANNER`][bef-banner] die E-Mail-Adresse und die genaue Dauer der Vertretung angeben.  
Eine kurzzeitige Übernahme zum Zweck der "Auflösung" der Partei ist keine Urlaubsvertretung! Urlaubsvertretungen von mehr als 3 Wochen sind vorher bei der Spielleitung anzumelden.  
**Missachtung dieser Regel führt zur Löschung der Partei.**

### Ausnutzen von Fehlern im Programm

Wer einen Fehler des Programms zu seinem Vorteil ausnutzt, anstatt ihn der Spielleitung zu melden, schummelt.

### Unsoziales Verhalten auf Spieler-Ebene

Seid nett zueinander.  
Auch euer ärgster Feind im Spiel ist sicherlich ein netter Mensch und verdient es nicht, mit Werbe-Mails, "Igitt-Bildern" und anderen Dingen bombardiert zu werden.  
**Unsoziales Verhalten führt zum Ausschluss vom Spiel.**

Weiterlesen: [Anfängertipps][anfangertipps-id].

<!-- From [https://wiki.eressea.de/index.php?title=Hinweise&oldid=13366] -->

[diesen Link]: https://www.eressea.de/?page_id=186
[Mantis]: http://bugs.eressea.de/
[Discord]: https://discord.gg/KT5Fffh

[bef-banner]: [[bef-banner]]
[bef-stirb]: [[bef-stirb]]
