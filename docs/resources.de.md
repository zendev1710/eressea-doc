---
alias: rohstoffe
---
# Rohstoffe

Rohstoffe können ohne weitere Zutaten gewonnen direkt aus den Vorräten der [Region] gewonnen werden. Die Vorkommen sind jedoch begrenzt und regenerieren sich nur langsam oder gar nicht. Das benötigte Talent geht aus der Tabelle im Abschnitt [Waren] hervor.

## Abbau von Rohstoffen

Beim Abbau aller Rohstoffe ist zu beachten, dass bewachende Einheiten den Abbau verhindern, wenn die bewachende Partei weder ` `[[bef-helfe|`HELFE BEWACHE`]] oder [[bef-helfe|`HELFE ALLES`]] zur eigenen Partei gesetzt hat oder die abbauende Einheit oder Partei [kontaktiert]. Dies gilt nicht, wenn die bewachende Einheit die Produzenten nicht sieht, beispielsweise weil diese [getarnt] sind.

### Vom Bergbau

Eisen, Steine, Laen und in besonders alten Regionen gelegentlich sogar Adamantium, kann man im Gebirge, in Gletschern und manchmal auch in anderen Regionstypen gewinnen, wobei Laen und Adamantium ein Bergwerk und einen besonders hohen Talentwert Bergbau erfordert. Jeder dieser Rohstoffe kann in einer Region unterschiedlich schwer abbaubar sein. Dies ist im Report durch die Zahlenangabe nach dem Schrägstrich erkennbar. Steht im Report beispielsweise '20 Eisen/4', so bedeutet dieses, dass noch 20 Eisen mit der Talentstufe 4 abbaubar sind. Sind diese abgebaut, benötigen die Bergleute einen höheren Talentwert, um weiteres Eisen abzubauen. Im allgemeinen werden die abbaubaren Rohstoffmengen mit steigender Schwierigkeit des Abbaus größer.

### Tief im Wald

Die Entwicklung der Vegetation Eresseas wird von den Jahreszeiten bestimmt. Sobald im Frühjahr die ersten Sonnenstrahlen auf den Waldboden treffen, treiben die im Boden verborgenen Samen aus und die Schösslinge des letzten Jahres wachsen zu ausgewachsenen Bäumen heran. Bei zu wenig Sonnenlicht (keine freien Arbeitsplätze) schlummern die Samen weiterhin im Boden. In den Sommer- und Herbstmonaten werfen die ausgewachsenen Bäume ihre Samen herab, welche mit [[bef-mache|`Samen`]] bzw. `MACHE Mallornsamen` von [Kräuterkundlern] mit einem Talent von 3 bzw. 4 oder mehr eingesammelt und mit [[bef-pflanze]]`Samen/Mallornsamen` anderswo eingepflanzt werden können (Mindesttalent von 6 bzw. 7).

Wird Holz oder Mallorn gefällt, schrumpft der Wald und erholt sich nur sehr langsam. Solange noch genug Holz vorhanden ist, kann es in beliebigen Mengen gefällt werden. Für Mallorn, ein "magisches" Holz, welches man nur in wenigen Regionen findet, gilt Gleiches. Mallorn vermehrt sich zwar wie Holz, jedoch wachsen Mallornsamen nur in den dafür geeigneten Regionen an. In Mallornregionen kann mit dem Befehl [[bef-mache]]`Holz` auch Holz anstelle von Mallorn gefällt werden. Der Bestand an Mallornbäumen wird dabei um den gleichen Betrag reduziert, als würde man Mallorn fällen.

### Und anderswo

Die in einer Region wild lebenden Pferde können von Einheiten mit dem Talent [Pferdedressur][Kräuterkundlern] mit dem Befehl [[bef-mache|`MACHE Pferd`]] gefangen werden. Wildpferde vermehren sich jede Runde. Sie sind platz- und freiheitsliebend, und so wandern einige von ihnen in Nachbarregionen ab, wenn dort weniger Pferde leben. Bereits eingefangene Pferde vermehren sich nur, wenn eine Einheit mit dem Talent [Pferdedressur][Kräuterkundlern] sie in einer [Pferdezucht] mit dem Befehl [`ZÜCHTE PFERDE`] züchtet.

Spielererfahrung: SoltharDie maximale Anzahl Pferde in einer Region entspricht der Anzahl der [Arbeitsplätze] / 10. In einer relativ leeren Region vermehren sie sich mit ca. 4%. Je näher sie dem Limit kommen, desto langsamer das Wachstum. Am schnellsten geht es bei ungefähr halben Besatz. In einer Ebene gibt es bei 25 Pferden jede Runde ein neues. Bei 500 Pferden kommen 10 pro Runde hinzu. Ab 1000 Pferden tut sich nichts mehr.

[Arbeitsplätze]: ./world.md "Welt"

Weiterhin gibt es in jeder Region maximal eine Kräuterart. Zur Zuordnung siehe die [Kräuterliste].

## Siehe auch

- [Produktion]
- [Waren]
- [Straßen]
- [Gebäude]

Weiterlesen: [Waren].

[Waren]: ./items.md "Waren"

<!-- From [https://wiki.eressea.de/index.php?title=Rohstoffe&oldid=16865] -->

[Region]: ./world.md "Welt"
[kontaktiert]: ./cmd-contact.md "KONTAKTIERE"
[getarnt]: ./camouflage.md "Tarnung"
[bef-mache]: ./cmd-make.md "MACHE"
[Kräuterkundlern]: ./skills-list.md "Liste der Talente"
[bef-pflanze]: ./cmd-plant.md "PFLANZE"
[Pferdezucht]: ./buildings-others.md#pferdezucht "Pferdezucht"
[`ZÜCHTE PFERDE`]: ./cmd-grow.md "ZÜCHTE"
[Kräuterliste]: ./herbs.md#kraeuterliste "Kräuter"
[Produktion]: ./production.md
[Straßen]: ./roads.md
[Gebäude]: ./buildings.md
