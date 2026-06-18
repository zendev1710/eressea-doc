---
# cSpell:locale de
alias: alchemie
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD041 MD042 MD052 -->

[](){ #alchemie-id }

# Alchemie

In Eressea ist Alchemie die Kunst, natürliche Substanzen (Kräuter) in Tränke zu verwandeln.

[](){ #tranke-id }

## Tränke

In der Welt von Eressea sind alchemistische Tränke nicht nur einfache Gebräue.  
Sie sind mächtige Werkzeuge, die das Blatt wenden und das Schicksal eines Volkes stark beeinflussen können, zum Beispiel zur Unterstützung der Produktion, zur Stärkung der Truppen im Kampf oder um ein Volk besser gedeihen zu lassen.  

Tränke werden mit Hilfe von [Kräutern][krauter] und anderen Zutaten gebraut und können dann von jeder Einheit benutzt werden. Um einen Trank herstellen zu können, braucht man das Talent [Alchemie][alchemie-id].  

Um die benötigten Kräuter finden zu können, braucht man das Talent [Kräuterkunde][krauterkunde].

Tränke werden mit dem Befehl [`MACHE "<Trank>"`][bef-mache] hergestellt.  

Pro Trank braucht man diverse Zutaten.  
Welche dies sind, erfährt man aus den Rezepten, die man mit Erlangen einer neuen Stufe im Talent Alchemie automatisch für diese Stufe bekommt.  
Später kann man sie sich mit dem Befehl [`ZEIGE`][bef-zeige] anzeigen lassen.  

Um einen Trank herstellen zu können, muss die Stufe des Alchemisten **doppelt so hoch** sein wie die Stufe des Trankes.  

Ein Alchemist kann jede Runde Talentstufe/(2\*Trankstufe) Tränke herstellen.  

Ein Alchemist der Stufe 6 kann also maximal einen Trank der Stufe 3, einen der zweiten Stufe oder drei Tränke der ersten Stufe herstellen.

!!! tip "Tipp"
    Tränke werden mit dem Befehl [`BENUTZE [anzahl] "Trank" [einheit-nr]`][bef-benutze] angewendet.  

Die Einheitennummer ist dabei nur bei Dumpfbackenbrot anzugeben, da dies der einzige Trank ist, der auf andere Einheiten wirkt.  
Ein Trank lässt sich nicht auf mehrere Einheiten aufteilen - man kann aber nach der Trank-Benutzung eine große Einheit in mehrere kleinere Einheiten aufteilen:
$$
N = \frac{T_{\text{Einheit}}}{Stufe_{\text{trank}}*2}
$$

Tränke können der Einheit nutzen, die sie anwendet, auf andere Einheiten wirken (Dumpfbackenbrot) oder sich auf eine Region beziehen - hier wird der Effekt in der Region erzielt, in der sich die Einheit bei Zugbeginn aufhält.

Ein Trank wirkt normalerweise für 10 Personen bzw. Gegenstände (dies ist in den Rezepten auch angegeben), und zwar in der Runde, in der er benutzt wurde.  
Tränke, die auf die Gegenstände einer Einheit wirken, verfallen, wenn sie nicht benutzt werden können, weil die Einheit diese Gegenstände nicht (mehr) hat.  
Viele Tränke wirken so, dass zu viele Personen in der Einheit nichts ausmachen, d.h. bei 12 Personen und einem Trank (wirkt für 10) betrifft die Wirkung eben nur 10 der 12 Leute.  
Beim "Berserkerblut" ist dies nicht möglich, da im Kampf die Beteiligten nicht als Einheit auftreten.  
Hier ist es notwendig, dass vor dem Kampf alle Personen der Einheit die Wirkung des Trankes haben, da er sonst nicht wirkt!

Die "Restwirkung" von Tränken verfällt nicht bei allen Tränken, so dass z.B. eine Person nach Anwendung von einem Gehirnschmalz oder Schaffenstrunk zehn Wochen von der Wirkung profitieren kann.

## Liste der Tränke

Nachfolgend finden Sie die Liste der Tränke in aufsteigender Reihenfolge ihrer Stufe.

### Stufe 1

#### Goliathwasser

:   10 Leute Tragkraft wie Pferde.  

*Stufe:* **1**.  
*Wirkung:* **Einheit**.  

Zur Zubereitung dieses Tranks benötigen Sie folgende Kräuter:

- [Fjordwuchs][fjordwuchs]
- [Gurgelkraut][gurgelkraut]

#### Siebenmeilentee

:   10 Leute schnell wie Pferde.  

*Stufe:* **1**.  
*Wirkung:* **Einheit**.  

Zur Zubereitung dieses Tranks benötigen Sie folgende Kräuter:

- [Blauer Baumringel][blauer-baumringel]
- [Windbeutel][windbeutel]

#### Trank der Wahrheit

:   ***Dieser Trank hat schon seit einiger Zeit keine Funktion mehr***.

*Stufe:* 1.  
*Wirkung:* Region.  

Zur Zubereitung dieses Tranks benötigen Sie folgende Kräuter:

- [Fjordwuchs][fjordwuchs]
- [Flachwurz][flachwurz]

#### Wasser des Lebens

:   macht aus 10 Holz/Mallorn 10 Schößlinge/Mallornschößlinge.  

*Stufe:* **1**.  
*Wirkung:* **Region**.  

Zur Zubereitung dieses Tranks benötigen Sie folgende Kräuter:

- [Elfenlieb][elfenlieb]
- [Knotiger Saugwurz][knotiger-saugwurz]

### Stufe 2

#### Bauernblut

:   bis zu 100 Dämonen brauchen keinen Bauern zum Fraß.  

*Stufe:* **2**.  
*Wirkung:* **Einheit**.  

Zur Zubereitung dieses Tranks benötigen Sie folgende Zutaten:

- Bauer
- [Blauer Baumringel][blauer-baumringel]
- [Fjordwuchs][fjordwuchs]
- [Höhlenglimm][hohlenglimm]

#### Schaffenstrunk

:   verdoppelt Produktivität von 10 Leuten (nur bei `MACHE`).  

*Stufe:* **2**.  
*Wirkung:* **Einheit**.  

Zur Zubereitung dieses Tranks benötigen Sie folgende Kräuter:

- [Alraune][alraune]
- [Spaltwachs][spaltwachs]
- [Würziger Wagemut][wurziger-wagemut]

#### Wundsalbe

:   bringt bis zu 400 Trefferpunkte zurück.  

*Stufe:* **2**.  
*Wirkung:* **Einheit**.  

Zur Zubereitung dieses Tranks benötigen Sie folgende Kräuter:

- [Blauer Baumringel][blauer-baumringel]
- [Weißer Wüterich][weier-wuterich]
- [Würziger Wagemut][wurziger-wagemut]

### Stufe 3

#### Berserkerblut

:   10 Leute im Kampf Angriff +1.  

*Stufe:* **3**.  
*Wirkung:* **Einheit**.  

Zur Zubereitung dieses Tranks benötigen Sie folgende Kräuter:

- [Alraune][alraune]
- [Flachwurz][flachwurz]
- [Sandfäule][sandfaule]
- [Weißer Wüterich][weier-wuterich]

#### Dumpfbackenbrot

:   bei 10 Leuten: kein Lernen oder Lehrer bringt nichts oder vergessen 1 Woche des besten Talents.  

*Stufe:* **3**.  
*Wirkung:* **(fremde) Einheit**.  

Zur Zubereitung dieses Tranks benötigen Sie folgende Kräuter:

- [Eulenauge][eulenauge]
- [Fjordwuchs][fjordwuchs]
- [Grüner Spinnerich][gruner-spinnerich]
- [Höhlenglimm][hohlenglimm]

#### Gehirnschmalz

:   erhöhte Lernchance für 10 Personen.  

*Stufe:* **3**.  
*Wirkung:* **Einheit**.  

Zur Zubereitung dieses Tranks benötigen Sie folgende Kräuter:

- [Gurgelkraut][gurgelkraut]
- [Steinbeißer][steinbeier]
- [Wasserfinder][wasserfinder]
- [Windbeutel][windbeutel]

#### Nestwärme

:   [Insekten][insekten] können auch im Winter rekrutieren.  

*Stufe:* **3**.  
*Wirkung:* **Region**.  

Zur Zubereitung dieses Tranks benötigen Sie folgende Kräuter:

- [Eisblume][eisblume]
- [Grüner Spinnerich][gruner-spinnerich]
- [Kakteenschwitz][kakteenschwitz]
- [Spaltwachs][spaltwachs]

#### Pferdeglück

:   50 Pferde vermehren sich bis zu vier mal.  

*Stufe:* **3**.  
*Wirkung:* **Region**.  

Zur Zubereitung dieses Tranks benötigen Sie folgende Kräuter:

- [Blauer Baumringel][blauer-baumringel]
- [Kakteenschwitz][kakteenschwitz]
- [Knotiger Saugwurz][knotiger-saugwurz]
- [Sandfäule][sandfaule]

### Stufe 4

#### Bauernlieb

:   gibt bis zu 1000 Bauern in der Region die zehnfache Chance, sich zu vermehren.  

*Niveau*: **4**.  
*Cible*: **Region**.  

Zur Zubereitung dieses Tranks benötigen Sie folgende Kräuter:

- [Alraune][alraune]
- [Blasenmorchel][blasenmorchel]
- [Elfenlieb][elfenlieb]
- [Schneekristall][schneekristall]
- [Steinbeißer][steinbeier]

#### Elixier der Macht

:   gibt 10 Personen fünffache Trefferpunkte.  

*Stufe:* **4**.  
*Wirkung:* **Einheit**.  

Zur Zubereitung dieses Tranks benötigen Sie folgende Kräuter:

- [Blasenmorchel][blasenmorchel]
- [Drachenblut]
- [Elfenlieb][elfenlieb]
- [Grüner Spinnerich][gruner-spinnerich]
- [Wasserfinder][wasserfinder]
- [Windbeutel][windbeutel]

#### Heiltrank

:   eine Person überlebt sonst tödlichen Schaden; pro Person nur einmal pro Woche möglich.  

*Stufe:* **4**.  
*Wirkung:* **Einheit**.  

Zur Zubereitung dieses Tranks benötigen Sie folgende Kräuter:

- [Eisblume][eisblume]
- [Elfenlieb][elfenlieb]
- [Gurgelkraut][gurgelkraut]
- [Spaltwachs][spaltwachs]
- [Windbeutel][windbeutel]

## Tränke – Übersichtstabelle

| Name                                   | Stufe | Wirkung              |
|----------------------------------------|:-----:|----------------------|
| [Trank der Wahrheit]                   |   1   | Region               |
| [Siebenmeilentee][siebenmeilentee]     |   1   | Einheit              |
| [Goliathwasser][goliathwasser]         |   1   | Einheit              |
| [wasser-des-lebens]                    |   1   | Region               |
| [Bauernblut][bauernblut]               |   2   | Einheit[^1]          |
| [Schaffenstrunk][schaffenstrunk]       |   2   | Einheit              |
| [Wundsalbe][wundsalbe]                 |   2   | Einheit              |
| [Berserkerblut][berserkerblut]         |   3   | Einheit              |
| [Dumpfbackenbrot][dumpfbackenbrot]     |   3   | (fremde) Einheit[^2] |
| [Gehirnschmalz][gehirnschmalz]         |   3   | Einheit              |
| [Pferdeglück][pferdegluck]             |   3   | Region               |
| [Nestwärme][nestwarme]                 |   3   | Region               |
| [Bauernlieb][bauernlieb]               |   4   | Region               |
| [Elixier der Macht][elixier-der-macht] |   4   | Einheit              |
| [Heiltrank][heiltrank]                 |   4   | Einheit              |

## Kräutermatrix

| Kraut                                  | [SM][siebenmeilentee]{title="Siebenmeilentee"} | [GW][goliathwasser]{title="Goliathwasser"} | [WL][wasser-des-lebens]{title="Wasser des Lebens"} | [BA][bauernblut]{title="Bauernblut"} | [ST][schaffenstrunk]{title="Schaffenstrunk"} | [WS][wundsalbe]{title="Wundsalbe"} | [BE][berserkerblut]{title="Berserkerblut"} | [DB][dumpfbackenbrot]{title="Dumpfbackenbrot"} | [GS][gehirnschmalz]{title="Gehirnschmalz"} | [PG][pferdegluck]{title="Pferdeglück"} | [NW][nestwarme]{title="Nestwärme"} | [BL][bauernlieb]{title="Bauernlieb"} | [EM][elixier-der-macht]{title="Elixier der Macht"} | [HT][heiltrank]{title="Heiltrank"} |
|----------------------------------------|------------------------------------------------|--------------------------------------------|----------------------------------------------------|--------------------------------------|----------------------------------------------|------------------------------------|--------------------------------------------|------------------------------------------------|--------------------------------------------|----------------------------------------|------------------------------------|--------------------------------------|----------------------------------------------------|------------------------------------|
| [Alraune][alraune]                     |                                                |                                            |                                                    |                                      | :material-check:                             |                                    | :material-check:                           |                                                |                                            |                                        |                                    | :material-check:                     |                                                    |                                    |
| [Blasenmorchel][blasenmorchel]         |                                                |                                            |                                                    |                                      |                                              |                                    |                                            |                                                |                                            |                                        |                                    | :material-check:                     | :material-check:                                   |                                    |
| [Blauer Baumringel][blauer-baumringel] | :material-check:                               |                                            |                                                    | :material-check:                     |                                              | :material-check:                   |                                            |                                                |                                            | :material-check:                       |                                    |                                      |                                                    |                                    |
| [Eisblume][eisblume]                   |                                                |                                            |                                                    |                                      |                                              |                                    |                                            |                                                |                                            |                                        | :material-check:                   |                                      |                                                    | :material-check:                   |
| [Elfenlieb][elfenlieb]                 |                                                |                                            | :material-check:                                   |                                      |                                              |                                    |                                            |                                                |                                            |                                        |                                    | :material-check:                     | :material-check:                                   | :material-check:                   |
| [Eulenauge][eulenauge]                 |                                                |                                            |                                                    |                                      |                                              |                                    |                                            | :material-check:                               |                                            |                                        |                                    |                                      |                                                    |                                    |
| [Fjordwuchs][fjordwuchs]               |                                                | :material-check:                           |                                                    | :material-check:                     |                                              |                                    |                                            | :material-check:                               |                                            |                                        |                                    |                                      |                                                    |                                    |
| [Flachwurz][flachwurz]                 |                                                |                                            |                                                    |                                      |                                              |                                    | :material-check:                           |                                                |                                            |                                        |                                    |                                      |                                                    |                                    |
| [Grüner Spinnerich][gruner-spinnerich] |                                                |                                            |                                                    |                                      |                                              |                                    |                                            | :material-check:                               |                                            |                                        | :material-check:                   |                                      | :material-check:                                   |                                    |
| [Gurgelkraut][gurgelkraut]             |                                                | :material-check:                           |                                                    |                                      |                                              |                                    |                                            |                                                | :material-check:                           |                                        |                                    |                                      |                                                    | :material-check:                   |
| [Höhlenglimm][hohlenglimm]             |                                                |                                            |                                                    | :material-check:                     |                                              |                                    |                                            | :material-check:                               |                                            |                                        |                                    |                                      |                                                    |                                    |
| [Kakteenschwitz][kakteenschwitz]       |                                                |                                            |                                                    |                                      |                                              |                                    |                                            |                                                |                                            | :material-check:                       | :material-check:                   |                                      |                                                    |                                    |
| [Knotiger Saugwurz][knotiger-saugwurz] |                                                |                                            | :material-check:                                   |                                      |                                              |                                    |                                            |                                                |                                            | :material-check:                       |                                    |                                      |                                                    |                                    |
| [Sandfäule][sandfaule]                 |                                                |                                            |                                                    |                                      |                                              |                                    | :material-check:                           |                                                |                                            | :material-check:                       |                                    |                                      |                                                    |                                    |
| [Schneekristall][schneekristall]       |                                                |                                            |                                                    |                                      |                                              |                                    |                                            |                                                |                                            |                                        |                                    | :material-check:                     |                                                    |                                    |
| [Spaltwachs][spaltwachs]               |                                                |                                            |                                                    |                                      | :material-check:                             |                                    |                                            |                                                |                                            |                                        | :material-check:                   |                                      |                                                    | :material-check:                   |
| [Wasserfinder][wasserfinder]           |                                                |                                            |                                                    |                                      |                                              |                                    |                                            |                                                | :material-check:                           |                                        |                                    |                                      | :material-check:                                   |                                    |
| [Weißer Wüterich][weier-wuterich]      |                                                |                                            |                                                    |                                      |                                              | :material-check:                   | :material-check:                           |                                                |                                            |                                        |                                    |                                      |                                                    |                                    |
| [Windbeutel][windbeutel]               | :material-check:                               |                                            |                                                    |                                      |                                              |                                    |                                            |                                                | :material-check:                           |                                        |                                    |                                      | :material-check:                                   | :material-check:                   |
| [Würziger Wagemut][wurziger-wagemut]   |                                                |                                            |                                                    |                                      | :material-check:                             | :material-check:                   |                                            |                                                |                                            |                                        |                                    |                                      |                                                    |                                    |
| [Steinbeißer][steinbeier]              |                                                |                                            |                                                    |                                      |                                              |                                    |                                            |                                                | :material-check:                           |                                        |                                    | :material-check:                     |                                                    |                                    |

Weiterlesen: [Kräuter][krauter-id].

[^1]: Wirkt auf die Einheit, aber alle Dämonen der Partei in der Region bedienen sich davon, wenn etwas übrig ist.  
    Es reicht also, eine Einheit (pro Region) damit zu bestücken, solange sie genug Bauernblut für alle Dämonen trinkt.
[^2]: Der Trank wird auf eine andere Einheit mit dem Befehl `BENUTZE Dumpfbackenbrot <einheit-nr>` angewandt.  
    Hierbei ist zu beachten: Ist das [Tarnungstalent][skill-tarnung-id] des Anwenders kleiner oder gleich [Wahrnehmung][wahrnehmung] + 2 des Opfers, so geht die Anwendung fehl.  
    Im Falle dass die Anwendung schief geht, bleibt das [Dumpfbackenbrot][dumpfbackenbrot] beim Anwender und er bekommt eine Fehlermeldung.

<!-- From [https://kwiki.eressea.de/index.php?title=Tränke&oldid=16967] -->

[bef-benutze]: [[bef-benutze]]
[bef-mache]: [[bef-mache]]
[bef-zeige]: [[bef-zeige]]
