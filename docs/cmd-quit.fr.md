# QUIT

**`QUIT`**`"Passwort"`

Dies bewirkt, dass die Partei sich auflöst und nicht mehr mitspielt. Zur Sicherheit muss das Passwort der Partei angeben werden. Auch dieser Befehl muss einer Einheit gegeben werden.

Alle Gegenstände inklusive Silber der sterbenden Partei werden an befreundete Einheiten übergeben, die in derselben Region stehen wie Einheiten der sterbenden Partei. Sind mehrere in der Region, wird nach der Anzahl Personen in der Region aufgeteilt. Als befreundet gilt hier nur, wem ein [HELP SILBER] gesetzt wurde, wo also seitens der ausscheidenden Partei bereits Vertrauen herrschte. Die Empfängerpartei muss HELP GIVE auf die sterbende Partei gesetzt haben. Die Gegenstände gehen an die jeweils erste Einheit der Partei in der Region. Sollte sich keine befreundete Einheit in einer Region befinden, gehen alle Gegenstände an die Bauern. Die Personen der Partei werden immer an die Bauern übergeben (Ausnahmen gelten bei [Orks], [Dämonen], Monstern).

**`QUIT`**` "Passwort" PARTEI `*`Partei-nr`*

Es besteht auch die Möglichkeit mit dem QUIT Befehl zwei Parteien der gleichen Rasse zu fusionieren. Dazu dient die zweite Variante `QUIT "Passwort" PARTEI`*`Partei-nr`*, wobei die Parteinummer der anderen Partei angegeben werden muss.

Voraussetzungen für die Fusion sind:

1. Auflösende Partei und Zielpartei müssen derselben Rasse angehören.
2. Die Empfängerpartei muss die Einheit, welche den QUIT-Befehl gibt, kontaktieren.
3. Die Empfängerpartei muss dafür natürlich in derselben Region sein wie die Einheit, welche den QUIT-Befehl gibt.
4. Beide Parteien müssen mindestens 50 Runden alt sein.

Ist eine der Voraussetzungen nicht erfüllt, wird der QUIT-Befehl nicht ausgeführt und es erscheint eine Fehlermeldung.

Durch die Fusion werden sämtliche Einheiten, welche die Rasse der Partei haben, an die angegebene Partei übergeben und die Partei anschließend gelöscht. Einheiten, welche nicht der Parteirasse angehören, wie beispielsweise Migranten, magische Kreaturen oder Vertraute, werden gelöscht.

Hat die Zielpartei weniger als die maximal zulässige Anzahl an Einheiten mit mengenbegrenzten Talenten (wie Alchemie und Magie), so werden diese zufällig übergeben. Einheiten mit mengenbegrenzten Talenten, die nicht mehr übergeben werden können, werden gelöscht. Wer dies genau steuern will, sollte die nicht erwünschten Einheiten spätestens in der QUIT-Woche das entsprechende Talent vergessen lassen.

Magier werden nur dann übergeben, wenn beide Parteien das gleiche Magiegebiet haben. Vertraute werden gelöscht, da sie nicht der Parteirasse angehören. Helden werden durch die Übergabe degradiert.

Das Einheitenlimit kann durch die Parteifusion überschritten werden. Dann kann die Zielpartei aber keine neuen Einheiten erzeugen, bis sie wieder unter dem Limit liegt. Es können auch dann keine neuen Temp-Einheiten erzeugt werden, wenn am Ende der Runde das Einheitenlimit unter der Grenze liegen würde! Es ist also besser, im Vorfeld dafür Sorge zu tragen, dass die fusionierte Partei den aktuellen Grenzwert einhält.

**ACHTUNG** Wird der Befehl falsch gegeben, kann es zu einem Stirb ohne Übergabe kommen. Wenn dein Passwort *geheim* lautet und du mit der Partei (enno) fusionieren möchtest, lautet der Befehl dazu:

     QUIT "geheim" PARTEI enno

<!-- From [https://wiki.eressea.de/index.php?title=QUIT&oldid=16825] -->

[HELP SILBER]: ./cmd-help.md

[Orks]: ./races.md#orcs
[Dämonen]: ./races.md#demons
