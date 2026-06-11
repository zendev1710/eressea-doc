---
# cSpell:locale de
alias: rohstoffe
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD042 MD052 -->
# Natürliche Ressourcen

Rohstoffe können ohne weitere Zutaten gewonnen direkt aus den Vorräten der [Region][welt] gewonnen werden.
Die Vorkommen sind jedoch begrenzt und regenerieren sich nur langsam oder gar nicht.
Das benötigte Talent geht aus der Tabelle im Abschnitt [Waren][waren] hervor.

## Rohstoffe

[](){ #adamantium-de-id }

### Adamantium

Spielererfahrung:

BruckAdamantium ist noch seltener als [laen][laen-de-id] !  

Pro Schicht gib es gerade mal ein Adamantium, so es überhaupt Adamantium in der Region gibt.

#### Externe Links

- [Adamantium auf Wikipedia]

<!-- From [https://wiki.eressea.de/index.php?title=Adamantium&oldid=6241] -->

### Eisen

### Holz

[](){ #laen-de-id }

### Laen

[](){ #mallorn-de-id }

### Mallorn

### Katapultmunition

### Pferd

### Stein

### Wagen

## Abbau von Rohstoffen

Beim Abbau aller Rohstoffe ist zu beachten, dass bewachende Einheiten den Abbau verhindern, wenn die bewachende Partei weder ` `[`HELFE BEWACHE`][bef-helfe] oder [`HELFE ALLES`][bef-helfe] zur eigenen Partei gesetzt hat oder die abbauende Einheit oder Partei [kontaktiert].
Dies gilt nicht, wenn die bewachende Einheit die Produzenten nicht sieht, beispielsweise weil diese [getarnt][tarnung-id] sind.

### Vom Bergbau

Eisen, Steine, Laen und in besonders alten Regionen gelegentlich sogar Adamantium, kann man im Gebirge, in Gletschern und manchmal auch in anderen Regionstypen gewinnen, wobei Laen und Adamantium ein Bergwerk und einen besonders hohen Talentwert Bergbau erfordert.
Jeder dieser Rohstoffe kann in einer Region unterschiedlich schwer abbaubar sein.
Dies ist im Report durch die Zahlenangabe nach dem Schrägstrich erkennbar.
Steht im Report beispielsweise '20 Eisen/4', so bedeutet dieses, dass noch 20 Eisen mit der Talentstufe 4 abbaubar sind.
Sind diese abgebaut, benötigen die Bergleute einen höheren Talentwert, um weiteres Eisen abzubauen.
Im allgemeinen werden die abbaubaren Rohstoffmengen mit steigender Schwierigkeit des Abbaus größer.

### Tief im Wald

Die Entwicklung der Vegetation Eresseas wird von den Jahreszeiten bestimmt.
Sobald im Frühjahr die ersten Sonnenstrahlen auf den Waldboden treffen, treiben die im Boden verborgenen Samen aus und die Schösslinge des letzten Jahres wachsen zu ausgewachsenen Bäumen heran.
Bei zu wenig Sonnenlicht (keine freien Arbeitsplätze) schlummern die Samen weiterhin im Boden.
In den Sommer- und Herbstmonaten werfen die ausgewachsenen Bäume ihre Samen herab, welche mit [`Samen`][bef-mache] bzw. `MACHE Mallornsamen` von [Kräuterkundlern][skill-krauterkunde-id] mit einem Talent von 3 bzw. 4 oder mehr eingesammelt und mit [[bef-pflanze]]`Samen/Mallornsamen` anderswo eingepflanzt werden können (Mindesttalent von 6 bzw. 7).

Wird Holz oder Mallorn gefällt, schrumpft der Wald und erholt sich nur sehr langsam.
Solange noch genug Holz vorhanden ist, kann es in beliebigen Mengen gefällt werden.
Für Mallorn, ein "magisches" Holz, welches man nur in wenigen Regionen findet, gilt Gleiches.
Mallorn vermehrt sich zwar wie Holz, jedoch wachsen Mallornsamen nur in den dafür geeigneten Regionen an.
In Mallornregionen kann mit dem Befehl [[bef-mache]]`Holz` auch Holz anstelle von Mallorn gefällt werden.
Der Bestand an Mallornbäumen wird dabei um den gleichen Betrag reduziert, als würde man Mallorn fällen.

### Und anderswo

Die in einer Region wild lebenden Pferde können von Einheiten mit dem Talent [Pferdedressur][pferdedressur] mit dem Befehl [`MACHE Pferd`][bef-mache] gefangen werden.
Wildpferde vermehren sich jede Runde.
Sie sind platz- und freiheitsliebend, und so wandern einige von ihnen in Nachbarregionen ab, wenn dort weniger Pferde leben.
Bereits eingefangene Pferde vermehren sich nur, wenn eine Einheit mit dem Talent [Pferdedressur][pferdedressur] sie in einer [Pferdezucht][pferdezucht] mit dem Befehl [`ZÜCHTE PFERDE`] züchtet.

Spielererfahrung (Solthar):

Diemaximale Anzahl Pferde in einer Region entspricht der Anzahl der [Arbeitsplätze] / 10.

In einer relativ leeren Region vermehren sie sich mit ca. 4%.
Je näher sie dem Limit kommen, desto langsamer das Wachstum.
Am schnellsten geht es bei ungefähr halben Besatz.
In einer Ebene gibt es bei 25 Pferden jede Runde ein neues.
Bei 500 Pferden kommen 10 pro Runde hinzu.
Ab 1000 Pferden tut sich nichts mehr.

Weiterhin gibt es in jeder Region maximal eine Kräuterart.
Zur Zuordnung siehe die [Kräuterliste][krauterliste].

## Siehe auch

- [Produktion][produktion]
- [Waren][waren]
- [Straßen][strassen-id]
- [Gebäude][gebaude-id]

Weiterlesen: [Waren][waren].

<!-- From [https://wiki.eressea.de/index.php?title=Rohstoffe&oldid=16865] -->

[Adamantium auf Wikipedia]: http://de.wikipedia.org/wiki/Adamantium

[kontaktiert]: ./cmd-contact.md
[bef-mache]: ./cmd-make.md
[bef-pflanze]: ./cmd-plant.md
[`ZÜCHTE PFERDE`]: ./cmd-grow.md
