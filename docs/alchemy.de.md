---
# cSpell:locale de
alias: alchemie
---
# Alchemie

In Eressea ist Alchemie die Kunst, natürliche Substanzen (Kräuter) in Tränke zu verwandeln.

## Tränke

In der Welt von Eressea sind alchemistische Tränke nicht nur einfache Gebräue.  
Sie sind mächtige Werkzeuge, die das Blatt wenden und das Schicksal eines Volkes stark beeinflussen können, zum Beispiel zur Unterstützung der Produktion, zur Stärkung der Truppen im Kampf oder um ein Volk besser gedeihen zu lassen.  

Tränke werden mit Hilfe von [[kraeuter|Kräutern]] und anderen Zutaten gebraut und können dann von jeder Einheit benutzt werden. Um einen Trank herstellen zu können, braucht man das Talent [Alchemie].  

Um die benötigten Kräuter finden zu können, braucht man das Talent [Kräuterkunde].

Tränke werden mit dem Befehl [[bef-mache|`MACHE "<Trank>"`]] hergestellt.  

Pro Trank braucht man diverse Zutaten.  
Welche dies sind, erfährt man aus den Rezepten, die man mit Erlangen einer neuen Stufe im Talent Alchemie automatisch für diese Stufe bekommt.  
Später kann man sie sich mit dem Befehl [[bef-zeige]] anzeigen lassen.  

Um einen Trank herstellen zu können, muss die Stufe des Alchemisten **doppelt so hoch** sein wie die Stufe des Trankes.  

Ein Alchemist kann jede Runde Talentstufe/(2\*Trankstufe) Tränke herstellen.  

Ein Alchemist der Stufe 6 kann also maximal einen Trank der Stufe 3, einen der zweiten Stufe oder drei Tränke der ersten Stufe herstellen.

!!! tip "Tipp"
    Tränke werden mit dem Befehl [[bef-benutze]]`[anzahl] "Trank" [einheit-nr]` angewendet.  

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

- [Fjordwuchs]
- [Gurgelkraut]

#### Siebenmeilentee

:   10 Leute schnell wie Pferde.  

*Stufe:* **1**.  
*Wirkung:* **Einheit**.  

Zur Zubereitung dieses Tranks benötigen Sie folgende Kräuter:

- [Blauer Baumringel]
- [Windbeutel]

#### Trank der Wahrheit

:   ***Dieser Trank hat schon seit einiger Zeit keine Funktion mehr***.

*Stufe:* 1.  
*Wirkung:* Region.  

Zur Zubereitung dieses Tranks benötigen Sie folgende Kräuter:

- [Fjordwuchs]
- [Flachwurz]

#### Wasser des Lebens

:   macht aus 10 Holz/Mallorn 10 Schößlinge/Mallornschößlinge.  

*Stufe:* **1**.  
*Wirkung:* **Region**.  

Zur Zubereitung dieses Tranks benötigen Sie folgende Kräuter:

- [Elfenlieb]
- [Knotiger Saugwurz]

### Stufe 2

#### Bauernblut

:   bis zu 100 Dämonen brauchen keinen Bauern zum Fraß.  

*Stufe:* **2**.  
*Wirkung:* **Einheit**.  

Zur Zubereitung dieses Tranks benötigen Sie folgende Zutaten:

- Bauer
- [Blauer Baumringel]
- [Fjordwuchs]
- [Höhlenglimm]

#### Schaffenstrunk

:   verdoppelt Produktivität von 10 Leuten (nur bei `MACHE`).  

*Stufe:* **2**.  
*Wirkung:* **Einheit**.  

Zur Zubereitung dieses Tranks benötigen Sie folgende Kräuter:

- [Alraune]
- [Spaltwachs]
- [Würziger Wagemut]

#### Wundsalbe

:   bringt bis zu 400 Trefferpunkte zurück.  

*Stufe:* **2**.  
*Wirkung:* **Einheit**.  

Zur Zubereitung dieses Tranks benötigen Sie folgende Kräuter:

- [Blauer Baumringel]
- [Weißer Wüterich]
- [Würziger Wagemut]

### Stufe 3

#### Berserkerblut

:   10 Leute im Kampf Angriff +1.  

*Stufe:* **3**.  
*Wirkung:* **Einheit**.  

Zur Zubereitung dieses Tranks benötigen Sie folgende Kräuter:

- [Alraune]
- [Flachwurz]
- [Sandfäule]
- [Weißer Wüterich]

#### Dumpfbackenbrot

:   bei 10 Leuten: kein Lernen oder Lehrer bringt nichts oder vergessen 1 Woche des besten Talents.  

*Stufe:* **3**.  
*Wirkung:* **(fremde) Einheit**.  

Zur Zubereitung dieses Tranks benötigen Sie folgende Kräuter:

- [Eulenauge]
- [Fjordwuchs]
- [Grüner Spinnerich]
- [Höhlenglimm]

#### Gehirnschmalz

:   erhöhte Lernchance für 10 Personen.  

*Stufe:* **3**.  
*Wirkung:* **Einheit**.  

Zur Zubereitung dieses Tranks benötigen Sie folgende Kräuter:

- [Gurgelkraut]
- [Steinbeißer]
- [Wasserfinder]
- [Windbeutel]

#### Nestwärme

:   [Insekten] können auch im Winter rekrutieren.  

*Stufe:* **3**.  
*Wirkung:* **Region**.  

Zur Zubereitung dieses Tranks benötigen Sie folgende Kräuter:

- [Eisblume]
- [Grüner Spinnerich]
- [Kakteenschwitz]
- [Spaltwachs]

#### Pferdeglück

:   50 Pferde vermehren sich bis zu vier mal.  

*Stufe:* **3**.  
*Wirkung:* **Region**.  

Zur Zubereitung dieses Tranks benötigen Sie folgende Kräuter:

- [Blauer Baumringel]
- [Kakteenschwitz]
- [Knotiger Saugwurz]
- [Sandfäule]

### Stufe 4

#### Bauernlieb

:   gibt bis zu 1000 Bauern in der Region die zehnfache Chance, sich zu vermehren.  

*Niveau*: **4**.  
*Cible*: **Region**.  

Zur Zubereitung dieses Tranks benötigen Sie folgende Kräuter:

- [Alraune]
- [Blasenmorchel]
- [Elfenlieb]
- [Schneekristall]
- [Steinbeißer]

#### Elixier der Macht

:   gibt 10 Personen fünffache Trefferpunkte.  

*Stufe:* **4**.  
*Wirkung:* **Einheit**.  

Zur Zubereitung dieses Tranks benötigen Sie folgende Kräuter:

- [Blasenmorchel]
- [Drachenblut]
- [Elfenlieb]
- [Grüner Spinnerich]
- [Wasserfinder]
- [Windbeutel]

#### Heiltrank

:   eine Person überlebt sonst tödlichen Schaden; pro Person nur einmal pro Woche möglich.  

*Stufe:* **4**.  
*Wirkung:* **Einheit**.  

Zur Zubereitung dieses Tranks benötigen Sie folgende Kräuter:

- [Eisblume]
- [Elfenlieb]
- [Gurgelkraut]
- [Spaltwachs]
- [Windbeutel]

## Tränke – Übersichtstabelle

| Name                 | Stufe | Wirkung              |
|----------------------|:-----:|----------------------|
| [Trank der Wahrheit] |   1   | Region               |
| [Siebenmeilentee]    |   1   | Einheit              |
| [Goliathwasser]      |   1   | Einheit              |
| [Wasser des Lebens]  |   1   | Region               |
| [Bauernblut]         |   2   | Einheit[^1]          |
| [Schaffenstrunk]     |   2   | Einheit              |
| [Wundsalbe]          |   2   | Einheit              |
| [Berserkerblut]      |   3   | Einheit              |
| [Dumpfbackenbrot]    |   3   | (fremde) Einheit[^2] |
| [Gehirnschmalz]      |   3   | Einheit              |
| [Pferdeglück]        |   3   | Region               |
| [Nestwärme]          |   3   | Region               |
| [Bauernlieb]         |   4   | Region               |
| [Elixier der Macht]  |   4   | Einheit              |
| [Heiltrank]          |   4   | Einheit              |

## Kräutermatrix

| Kraut               | [SM]             | [GW]             | [WL]             | [BA]             | [ST]             | [WS]             | [BE]             | [DB]             | [GS]             | [PG]             | [NW]             | [BL]             | [EM]             | [HT]             |
|---------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|
| [Alraune]           |                  |                  |                  |                  | :material-check: |                  | :material-check: |                  |                  |                  |                  | :material-check: |                  |                  |
| [Blasenmorchel]     |                  |                  |                  |                  |                  |                  |                  |                  |                  |                  |                  | :material-check: | :material-check: |                  |
| [Blauer Baumringel] | :material-check: |                  |                  | :material-check: |                  | :material-check: |                  |                  |                  | :material-check: |                  |                  |                  |                  |
| [Eisblume]          |                  |                  |                  |                  |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  | :material-check: |
| [Elfenlieb]         |                  |                  | :material-check: |                  |                  |                  |                  |                  |                  |                  |                  | :material-check: | :material-check: | :material-check: |
| [Eulenauge]         |                  |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  |                  |                  |                  |                  |
| [Fjordwuchs]        |                  | :material-check: |                  | :material-check: |                  |                  |                  | :material-check: |                  |                  |                  |                  |                  |                  |
| [Flachwurz]         |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  |                  |                  |                  |                  |                  |
| [Grüner Spinnerich] |                  |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  | :material-check: |                  | :material-check: |                  |
| [Gurgelkraut]       |                  | :material-check: |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  |                  |                  | :material-check: |
| [Höhlenglimm]       |                  |                  |                  | :material-check: |                  |                  |                  | :material-check: |                  |                  |                  |                  |                  |                  |
| [Kakteenschwitz]    |                  |                  |                  |                  |                  |                  |                  |                  |                  | :material-check: | :material-check: |                  |                  |                  |
| [Knotiger Saugwurz] |                  |                  | :material-check: |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  |                  |                  |
| [Sandfäule]         |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  | :material-check: |                  |                  |                  |                  |
| [Schneekristall]    |                  |                  |                  |                  |                  |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  |
| [Spaltwachs]        |                  |                  |                  |                  | :material-check: |                  |                  |                  |                  |                  | :material-check: |                  |                  | :material-check: |
| [Wasserfinder]      |                  |                  |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  |                  | :material-check: |                  |
| [Weißer Wüterich]   |                  |                  |                  |                  |                  | :material-check: | :material-check: |                  |                  |                  |                  |                  |                  |                  |
| [Windbeutel]        | :material-check: |                  |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  |                  | :material-check: | :material-check: |
| [Würziger Wagemut]  |                  |                  |                  |                  | :material-check: | :material-check: |                  |                  |                  |                  |                  |                  |                  |                  |
| [Steinbeißer]       |                  |                  |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  | :material-check: |                  |                  |

Weiterlesen: [[kraeuter]].

[^1]: Wirkt auf die Einheit, aber alle Dämonen der Partei in der Region bedienen sich davon, wenn etwas übrig ist.  
    Es reicht also, eine Einheit (pro Region) damit zu bestücken, solange sie genug Bauernblut für alle Dämonen trinkt.
[^2]: Der Trank wird auf eine andere Einheit mit dem Befehl `BENUTZE Dumpfbackenbrot <einheit-nr>` angewandt.  
    Hierbei ist zu beachten: Ist das [[tarnung|Tarnungstalent]] des Anwenders kleiner oder gleich [Wahrnehmung] + 2 des Opfers, so geht die Anwendung fehl.  
    Im Falle dass die Anwendung schief geht, bleibt das [Dumpfbackenbrot] beim Anwender und er bekommt eine Fehlermeldung.

<!-- From [https://wiki.eressea.de/index.php?title=Tränke&oldid=16967] -->

[Alchemie]: ./skills-list.md#alchemie
[Wahrnehmung]: ./skills-list.md#wahrnehmung
[Kräuterkunde]: ./skills-list.md#krauterkunde
[Insekten]: ./races.md#insekten

[Alraune]: ./herbs.md#alraune
[Blasenmorchel]: ./herbs.md#blasenmorchel
[Blauer Baumringel]: ./herbs.md#blauer-baumringel
[Eisblume]: ./herbs.md#eisblume
[Elfenlieb]: ./herbs.md#elfenlieb
[Eulenauge]: ./herbs.md#eulenauge
[Fjordwuchs]: ./herbs.md#fjordwuchs
[Flachwurz]: ./herbs.md#flachwurz
[Grüner Spinnerich]: ./herbs.md#gruner-spinnerich
[Gurgelkraut]: ./herbs.md#gurgelkraut
[Höhlenglimm]: ./herbs.md#hohlenglimm
[Kakteenschwitz]: ./herbs.md#
[Knotiger Saugwurz]: ./herbs.md#knotiger-saugwurz
[Sandfäule]: ./herbs.md#sandfaule
[Schneekristall]: ./herbs.md#schneekristall
[Spaltwachs]: ./herbs.md#spaltwachs
[Wasserfinder]: ./herbs.md#wasserfinder
[Weißer Wüterich]: ./herbs.md#weier-wuterich
[Windbeutel]: ./herbs.md#windbeutel
[Würziger Wagemut]: ./herbs.md#wurziger-wagemut
[Steinbeißer]: ./herbs.md#steinbeier

[Siebenmeilentee]: ./alchemy.md#siebenmeilentee
[Goliathwasser]: ./alchemy.md#goliathwasser
[Wasser des Lebens]: ./alchemy.md#wasser-des-lebens
[Bauernblut]: ./alchemy.md#bauernblut
[Schaffenstrunk]: ./alchemy.md#schaffenstrunk
[Wundsalbe]: ./alchemy.md#wundsalbe
[Berserkerblut]: ./alchemy.md#berserkerblut
[Dumpfbackenbrot]: ./alchemy.md#dumpfbackenbrot
[Gehirnschmalz]: ./alchemy.md#gehirnschmalz
[Pferdeglück]: ./alchemy.md#pferdegluck
[Nestwärme]: ./alchemy.md#nestwarme
[Bauernlieb]: ./alchemy.md#bauernlieb
[Elixier der Macht]: ./alchemy.md#elixier-der-macht
[Heiltrank]: ./alchemy.md#heiltrank

[SM]: ./alchemy.md#siebenmeilentee "Siebenmeilentee"
[GW]: ./alchemy.md#goliathwasser "Goliathwasser"
[WL]: ./alchemy.md#wasser-des-lebens "Wasser des Lebens"
[BA]: ./alchemy.md#bauernblut "Bauernblut"
[ST]: ./alchemy.md#schaffenstrunk "Schaffenstrunk"
[WS]: ./alchemy.md#wundsalbe "Wundsalbe"
[BE]: ./alchemy.md#berserkerblut "Berserkerblut"
[DB]: ./alchemy.md#dumpfbackenbrot "Dumpfbackenbrot"
[GS]: ./alchemy.md#gehirnschmalz "Gehirnschmalz"
[PG]: ./alchemy.md#pferdegluck "Pferdeglück"
[NW]: ./alchemy.md#nestwarme "Nestwärme"
[BL]: ./alchemy.md#bauernlieb "Bauernlieb"
[EM]: ./alchemy.md#elixier-der-macht "Elixier der Macht"
[HT]: ./alchemy.md#heiltrank "Heiltrank"
