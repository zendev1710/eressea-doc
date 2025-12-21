---
# cSpell:locale de
alias: alchemie
---
# Tränke

In der Welt von Eressea sind alchemistische Tränke nicht nur einfache Gebräue – sie sind mächtige Werkzeuge, die das Blatt wenden und das Schicksal eines Volkes stark beeinflussen können, zum Beispiel zur Unterstützung der Produktion, zur Stärkung der Truppen im Kampf oder um ein Volk besser gedeihen zu lassen.

Tränke werden mit Hilfe von [Kräutern] und anderen Zutaten gebraut und können dann von jeder Einheit benutzt werden. Um einen Trank herstellen zu können, braucht man das Talent [Alchemie]. Um die benötigten Kräuter finden zu können, braucht man das Talent [Kräuterkunde][Alchemie].

Tränke werden mit dem Befehl [[bef-mache]]`"Trank"` hergestellt. Pro Trank braucht man diverse Zutaten. Welche dies sind, erfährt man aus den Rezepten, die man mit Erlangen einer neuen Stufe im Talent Alchemie automatisch für diese Stufe bekommt. Später kann man sie sich mit dem Befehl [[bef-zeige]] anzeigen lassen. Um einen Trank herstellen zu können, muss die Stufe des Alchemisten doppelt so hoch sein wie die Stufe des Trankes. Ein Alchemist kann jede Runde Talentstufe/(2\*Trankstufe) Tränke herstellen. Ein Alchemist der Stufe 6 kann also maximal einen Trank der Stufe 3, einen der zweiten Stufe oder drei Tränke der ersten Stufe herstellen.

Tränke werden mit dem Befehl [[bef-benutze]]`[anzahl] "Trank" [einheit-nr]` angewendet. Die Einheitennummer ist dabei nur bei Dumpfbackenbrot anzugeben, da dies der einzige Trank ist, der auf andere Einheiten wirkt. Ein Trank lässt sich nicht auf mehrere Einheiten aufteilen - man kann aber nach der Trank-Benutzung eine große Einheit in mehrere kleinere Einheiten aufteilen.

Tränke können der Einheit nutzen, die sie anwendet, auf andere Einheiten wirken (Dumpfbackenbrot) oder sich auf eine Region beziehen - hier wird der Effekt in der Region erzielt, in der sich die Einheit bei Zugbeginn aufhält.

Ein Trank wirkt normalerweise für 10 Personen bzw. Gegenstände (dies ist in den Rezepten auch angegeben), und zwar in der Runde, in der er benutzt wurde. Tränke, die auf die Gegenstände einer Einheit wirken, verfallen, wenn sie nicht benutzt werden können, weil die Einheit diese Gegenstände nicht (mehr) hat. Viele Tränke wirken so, dass zu viele Personen in der Einheit nichts ausmachen, d.h. bei 12 Personen und einem Trank (wirkt für 10) betrifft die Wirkung eben nur 10 der 12 Leute. Beim "Berserkerblut" ist dies nicht möglich, da im Kampf die Beteiligten nicht als Einheit auftreten. Hier ist es notwendig, dass vor dem Kampf alle Personen der Einheit die Wirkung des Trankes haben, da er sonst nicht wirkt!

Die "Restwirkung" von Tränken verfällt nicht bei allen Tränken, so dass z.B. eine Person nach Anwendung von einem Gehirnschmalz oder Schaffenstrunk zehn Wochen von der Wirkung profitieren kann.

## Trankliste

Trankliste

| Stufe | Kürzel | Name               | Zutaten                                                                            | Beschreibung                                                                                   | Wirkung              |
|-------|--------|--------------------|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|----------------------|
| 1     | TW     | Trank der Wahrheit | Flachwurz, Fjordwuchs                                                              | Dieser Trank hat schon seit einiger Zeit keine Funktion mehr                                   | Region               |
| 1     | Sm     | Siebenmeilentee    | Blauer Baumringel, Windbeutel                                                      | 10 Leute schnell wie Pferde                                                                    | Einheit              |
| 1     | Gw     | Goliathwasser      | Gurgelkraut, Fjordwuchs                                                            | 10 Leute Tragkraft wie Pferde                                                                  | Einheit              |
| 1     | WL     | Wasser des Lebens  | Elfenlieb, Knotiger Saugwurz                                                       | macht aus 10 Holz/Mallorn 10 Schößlinge/Mallornschößlinge                                      | Region               |
| 2     | Ba     | Bauernblut         | Höhlenglimm, Fjordwuchs, Blauer Baumringel, Bauer                                  | bis zu 100 Dämonen brauchen keinen Bauern zum Fraß                                             | Einheit\*            |
| 2     | St     | Schaffenstrunk     | Alraune, Spaltwachs, Würziger Wagemut                                              | verdoppelt Produktivität von 10 Leuten (nur bei `MACHE`)                                       | Einheit              |
| 2     | Ws     | Wundsalbe          | Blauer Baumringel, Weißer Wüterich, Würziger Wagemut                               | bringt bis zu 400 Trefferpunkte zurück                                                         | Einheit              |
| 3     | Be     | Berserkerblut      | Weißer Wüterich, Alraune, Flachwurz, Sandfäule                                     | 10 Leute im Kampf Angriff +1                                                                   | Einheit              |
| 3     | Db     | Dumpfbackenbrot    | Eulenauge, Grüner Spinnerich, Höhlenglimm, Fjordwuchs                              | bei 10 Leuten: kein Lernen oder Lehrer bringt nichts oder vergessen 1 Woche des besten Talents | (fremde) Einheit\*\* |
| 3     | Gs     | Gehirnschmalz      | Wasserfinder, Steinbeißer, Windbeutel, Gurgelkraut                                 | erhöhte Lernchance für 10 Personen                                                             | Einheit              |
| 3     | Pg     | Pferdeglück        | Blauer Baumringel, Sandfäule, Kakteenschwitz, Knotiger Saugwurz                    | 50 Pferde vermehren sich bis zu vier mal                                                       | Region               |
| 3     | Nw     | Nestwärme          | Eisblume, Grüner Spinnerich, Spaltwachs, Kakteenschwitz                            | Insekten können auch im Winter rekrutieren                                                     | Region               |
| 4     | Bl     | Bauernlieb         | Alraune, Schneekristall, Steinbeißer, Blasenmorchel, Elfenlieb                     | gibt bis zu 1000 Bauern in der Region die zehnfache Chance, sich zu vermehren                  | Region               |
| 4     | EM     | Elixier der Macht  | Elfenlieb, Wasserfinder, Windbeutel, Grüner Spinnerich, Blasenmorchel, Drachenblut | gibt 10 Personen fünffache Trefferpunkte                                                       | Einheit              |
| 4     | Ht     | Heiltrank          | Gurgelkraut, Windbeutel, Eisblume, Elfenlieb, Spaltwachs                           | eine Person überlebt sonst tödlichen Schaden; pro Person nur einmal pro Woche möglich          | Einheit              |

\* Wirkt auf die Einheit, aber alle Dämonen der Partei in der Region bedienen sich davon, wenn etwas übrig ist. Es reicht also, eine Einheit (pro Region) damit zu bestücken, solange sie genug Bauernblut für alle Dämonen trinkt.

\*\* Der Trank wird auf eine andere Einheit mit dem Befehl `BENUTZE Dumpfbackenbrot abcd` angewandt. Hierbei ist zu beachten: Ist das Tarnungstalent des Anwenders kleiner oder gleich Wahrnehmung + 2 des Opfers, so geht die Anwendung fehl. Im Falle dass die Anwendung schief geht, bleibt das Dumpfbackenbrot beim Anwender und er bekommt eine Fehlermeldung.

## Kräutermatrix

| Kraut             | TW | Sm | Gw | WL | Ba | St | Ws | Be | Db | Gs | Pg | Nw | Bl | EM | Ht |
|-------------------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| Flachwurz         | X  |    |    |    |    |    |    | X  |    |    |    |    |    |    |    |
| Würziger Wagemut  |    |    |    |    |    | X  | X  |    |    |    |    |    |    |    |    |
| Eulenauge         |    |    |    |    |    |    |    |    | X  |    |    |    |    |    |    |
| Grüner Spinnerich |    |    |    |    |    |    |    |    | X  |    |    | X  |    | X  |    |
| Blauer Baumringel |    | X  |    |    | X  |    | X  |    |    |    | X  |    |    |    |    |
| Elfenlieb         |    |    |    | X  |    |    |    |    |    |    |    |    | X  | X  | X  |
| Gurgelkraut       |    |    | X  |    |    |    |    |    |    | X  |    |    |    |    | X  |
| Knotiger Saugwurz |    |    |    | X  |    |    |    |    |    |    | X  |    |    |    |    |
| Blasenmorchel     |    |    |    |    |    |    |    |    |    |    |    |    | X  | X  |    |
| Wasserfinder      |    |    |    |    |    |    |    |    |    | X  |    |    |    | X  |    |
| Kakteenschwitz    |    |    |    |    |    |    |    |    |    |    | X  | X  |    |    |    |
| Sandfäule         |    |    |    |    |    |    |    | X  |    |    | X  |    |    |    |    |
| Windbeutel        |    | X  |    |    |    |    |    |    |    | X  |    |    |    | X  | X  |
| Fjordwuchs        | X  |    | X  |    | X  |    |    |    | X  |    |    |    |    |    |    |
| Alraune           |    |    |    |    |    | X  |    | X  |    |    |    |    | X  |    |    |
| Steinbeißer       |    |    |    |    |    |    |    |    |    | X  |    |    | X  |    |    |
| Spaltwachs        |    |    |    |    |    | X  |    |    |    |    |    | X  |    |    | X  |
| Höhlenglimm       |    |    |    |    | X  |    |    |    | X  |    |    |    |    |    |    |
| Eisblume          |    |    |    |    |    |    |    |    |    |    |    | X  |    |    | X  |
| Weißer Wüterich   |    |    |    |    |    |    | X  | X  |    |    |    |    |    |    |    |
| Schneekristall    |    |    |    |    |    |    |    |    |    |    |    |    | X  |    |    |

Weiterlesen: [Kräuter].

<!-- From [https://wiki.eressea.de/index.php?title=Tränke&oldid=16967] -->

[Kräuter]: ./herbs.md "Kräuter"
[Kräutern]: ./herbs.md "Kräuter"
[Alchemie]: ./skills-list.md "Liste der Talente"
[bef-mache]: ./cmd-make.md "MACHE"
[bef-zeige]: ./cmd-show.md "ZEIGE"
[bef-benutze]: ./cmd-use.md "BENUTZE"
