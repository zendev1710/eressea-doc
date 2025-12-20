# Production

Verschiedene Dinge können in Eressea produziert werden. Es gibt [Rohstoffe] (z.B. Eisen, Steine, Holz, Pferde) und [Endprodukte] (diverse Waffen und Rüstungen, [Schiffe] und Wagen, [Gebäude] und [Straßen] und alchemistische [Tränke]). Um Dinge produzieren zu können, braucht man ein entsprechendes Talent. Die meisten Dinge werden mit dem Befehl [`MAKE`*`Anzahl`*` `*`Gegenstand`*] produziert, zum Beispiel `MAKE Eisen, MAKE Schwert` oder `MAKE 15 Elfenbogen`.

Je nach Gegenstand wird ein verschieden hoher Talentwert benötigt, damit man überhaupt in der Lage ist, diesen herzustellen. die meisten [Rohstoffe][1] erfordern nur Grundkenntnisse der entsprechenden Talente (Stufe 1), während die meisten [Gegenstände] höhere Talentstufen erfordern. Bei Gegenständen mit hohen Mindesttalentwerten kann man auch nur wenige davon herstellen. In jedem Fall kann man pro Einheit und Runde nur eine Art von Gegenständen oder Rohstoffen herstellen und auch nur an einem Gebäude oder Schiff arbeiten.

Bis auf Laen und Adamantium, zwei besonders wertvolle und seltene Metalle, sowie Mallorn, ein magisches Holz, können alle Rohstoffe ab einem Talentwert von 1 produziert werden, ebenso Pferde und Kräuter. Für die Gewinnung von Laen und Adamantium braucht man ein [Bergwerk] und ein Bergbautalent von 7 für Laen bzw. 8 für Adamantium, für Mallorn Holzfällen der Stufe 2.

Für Gegenstände ebenso wie für Gebäude und Schiffe werden die Talentstufen aller Personen der Einheit zusammengezählt und durch das Mindestbautalent geteilt. Pro so errechnetem Punkt kann ein Gebäude oder Schiff um einen Größenpunkt gebaut bzw. erweitert werden bzw. ein Gegenstand hergestellt werden.

Ist ein Gebäude oder ein Schiff erst einmal angefangen, kann man mit beliebig vielen Einheiten daran weiterbauen. Es ist jedoch nicht möglich, mit einer Einheit mehrere Gebäude oder Schiffe gleichzeitig zu bauen, auch wenn Talentstufen und Rohstoffe reichen.

**Beispiele:**

- `MAKE 10 Schild` lässt die Einheit 10 Schilde herstellen - vorausgesetzt, sie hat 10 Eisen, mindestens Rüstungsbau 2 und insgesamt 20 Talentstufen (10 Schilde x Mindesttalent 2 = 20).
- `MAKE 3 Boot` lässt die Einheit nicht drei separate Boote, sondern nur die entsprechende Anzahl Holz für das genannte Schiff (hier 3 von 5 für ein Boot) verbauen.
- Eine Einheit mit 4 Personen und Waffenbau 5 hat zusammen 20 Talentstufen. Sie kann damit z.B. 6 Schwerter (Mindesttalent Waffenbau 3), 4 Elfenbögen (sofern es Elfen sind; benötigt Waffenbau 5) oder 10 Speere (Waffenbau 2) ohne Hilfsmittel herstellen.
- Mit einer Schmiede könnten die Personen ihren Eisenverbauch bei Schwertern, Schilden o.ä. halbieren, also 10 Schilde aus 5 Eisen herstellen. Außerdem haben sie dort einen Talentbonus von +1 auf die Talente Waffenbau und Rüstungsbau.
- **Wichtig:** die Talentstufen zählen nur dann zusammen, wenn die Personen in einer Einheit sind! Die Einheit muss den Mindesttalentwert aber in jedem Fall haben.

Gerade bei größeren Parteien kann das "Zusammensuchen" aller Materialien z.B. für Gebäude lästig sein. Um dies zu vereinfachen, gibt es einen [Materialpool], dessen Funktion im betreffenden Abschnitt erklärt ist.

## Voir aussi

- [Rohstoffe]
- [Waren][Endprodukte]
- [Straßen][2]
- [Schiffe][3]
- [Gebäude]
- [Parteipool]

Poursuivre la lecture : [Rohstoffe].

[Rohstoffe]: ./resources.md

<!-- From [https://wiki.eressea.de/index.php?title=Produktion&oldid=16875] -->

[Endprodukte]: ./items.md
[Schiffe]: ./ships.md
[Gebäude]: ./buildings.md
[Straßen]: ./roads.md
[Tränke]: ./alchemy.md
[1]: ./resources.md
[Gegenstände]: ./items.md
[Bergwerk]: ./buildings-others.md#mine
[Materialpool]: ./items-pool.md
[2]: ./roads.md
[3]: ./ships.md
[Parteipool]: ./faction-pool.md
