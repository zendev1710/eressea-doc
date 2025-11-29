# Befehl

## Konventionen

In diesen Regeln gelten die folgenden Konventionen:

     GIB einheit-nr [anzahl|ALLES] [gegenstand]

- Schlüsselwörter wie GIB, MACHE, NICHT sind in Großbuchstaben gesetzt. Das ist nicht Pflicht, wir empfehlen es aber.
- Platzhalter sind in Kleinbuchstaben. Sie sollen nicht wörtlich übernommen werden, sondern müssen durch konkrete Werte ersetzt werden, also zum Beispiel einheit-nr durch die Nummer der gewünschten Einheit. Manchmal schreiben wir dies auch als &lt;einheit-nr&gt;, in diesem Fall sind die &lt;- und &gt;-Symbole *nicht* zu übernehmen.
- Worte in \[\]-Klammern sind optional. Sie können also weggelassen werden, ändern dadurch aber die Bedeutung des Befehls. Alternativen sind dabei durch | getrennt. Obiges Beispiel lässt also `GIB 123 ALLES` oder auch `GIB abc 4 Schwert` zu.

## Syntax

Bis auf das Passwort und die Parteinummer sind dem Server Groß- und Kleinschreibung egal. `lerNE armBRUSTschiessen` ist völlig legal (wird aber nicht empfohlen, da es für Menschen schwer lesbar ist).

Gegenstände sollten immer in der *Einzahl* stehen, also `GIB xyz 100 Schwert` oder `MACHE 15 Stein`. Im Report tauchen Gegenstände oft in der Mehrzahl auf und in Befehlen wird sie meist verstanden, aber du solltest dir bewusst machen, dass der Server natürliche Sprache nicht versteht, auch wenn die Befehle fast so aussehen.

Viele Befehle lassen sich abkürzen, wobei du es nicht übertreiben solltest, da dies fehlerträchtig ist: VER passt auf VERGISS, VERKAUFE und VERLASSE und wird darum als Fehler angemerkt; hier solltest du also mindestens vier Buchstaben verwenden. Außerdem sind allzu kryptische Verkürzungen nicht sonderlich leserlich, wenn du später deine Züge durchsiehst... Am sichersten ist es immer noch, wenn du deine Befehle nicht abkürzt, zumal es Befehle, Gegenstände und Talente geben kann, die absichtlich nicht in der Anleitung stehen, aber ähnlich anfangen wie bekannte Befehle, Gegenstände und Talente.

Texte, die Leerzeichen enthalten, müssen in Anführungszeichen (") eingeschlossen werden oder die Leerzeichen durch ~ (Tilde) ersetzt. Ferner dürfen Umlaute durch die entsprechende Umschreibung (Ä=AE usw.) ersetzt werden:

     BENENNE Schiff "Großer Blauer Vogel"
     GIB einh 5 Würziger~Wagemut
     KAEMPFE HINTEN

Es ist möglich, einfache Anführungszeichen (') zu benutzen und zu kombinieren. Was dabei genau herauskommt, solltest du lieber ausprobieren, weil sich das genaue Verhalten immer mal verändern kann.

     BOTSCHAFT REGION 'Sprich "Freund" und tritt ein'
     BENENNE BURG xyz "Helm's Deep"
     DEFAULT 'MACHE 1 "Wasser des Lebens"'

Auch so genannte Maskierung (escaping) durch das Zeichen \\ sind möglich, aber nicht unbedingt empfohlen:

     BOTSCHAFT REGION "Sprich \"Freund\" und tritt ein"
     BENENNE BURG xyz 'Helm\'s Deep'
     DEFAULT 'MACHE 1 Wasser\~des\~Lebens'

Es ist übrigens nicht nötig, sich auf das lateinische Alphabet zu beschränken. In Namen und Beschreibungen ist der volle Unicode-Zeichensatz möglich:

     BENENNE EINHEIT "Σωκράτης"
     BOTSCHAFT REGION "🨀 شاه مات"

Natürlich solltest darauf achten, von anderen auch verstanden zu werden.

## Die Zugvorlage

Am einfachsten ist es, wenn du die Zugvorlage verwendest, die am Ende der Auswertung steht. Dort sind alle Einheiten aufgeführt, so dass du niemanden vergisst. Solltest du einmal keine Befehle einschicken, werden die Befehle der Zugvorlage trotzdem automatisch ausgeführt. Auch wenn du nur für einen Teil deiner Einheiten Befehle einsendest, werden für die restlichen Einheiten die Befehle der Zugvorlage ausgeführt. Sollte deine Auswertung keine Zugvorlage (mit der Endung .txt) enthalten, kannst du sie mit dem Befehl [`OPTION ZUGVORLAGE`] wieder einschalten.

## Kurze und lange Befehle

Es gibt in Eressea kurze und lange Befehle.

Die langen Befehle sind:

[ARBEITE], [ATTACKIERE], [BEKLAUE], [FAHRE], [FOLGE], [FORSCHE], [KAUFE], [LEHRE], [LERNE], [MACHE] (Ausnahme: MACHE TEMP), [NACH], [PFLANZE], [PIRATERIE], [ROUTE], [SPIONIERE], [TREIBE], [UNTERHALTE], [VERKAUFE], [ZAUBERE], [ZERSTÖRE], [ZÜCHTE].

Alle anderen Befehle sind kurze Befehle ([Kurzbeschreibung] aller Befehle). Du kannst beliebig viele kurze Befehle pro Einheit eingeben. Eine Einheit kann in der Regel nur einen langen Befehl haben. Es gibt ein paar Ausnahmen, die so genannten pseudolangen Befehle (`ATTACKIERE, FOLGE, KAUFE, VERKAUFE, ZAUBERE`), von denen unter Umständen mehrere gegeben werden können. Näheres in der Beschreibung der einzelnen Befehle.

Wird einer Einheit ein langer Befehl gegeben, wird sie diesen als Default-Befehl übernehmen und damit den vorherigen Default-Befehl ersetzen. Der Default-Befehl steht in der [Zugvorlage][3 Die Zugvorlage] immer als Vorschlag für einen langen Befehl. Du brauchst also einem Pferdedresseur nur einmal den Befehl MACHE pferd zu geben und dieser Befehl erscheint solange in der Zugvorlage, bis sie einen anderen langen Befehl erhält (z.B. LERNE Pferdedressur). Sinnvollerweise werden nicht alle langen Befehle als Default-Befehle übernommen. Das betrifft z.B. NACH, ATTACKIERE und FOLGE. Weiteres zu Default-Befehlen auf der Seite zum Befehl [DEFAULT].

Eine Einheit, die eine Runde arbeitete, in der kommenden Runde nach Norden zog und dann keinen Befehl mehr bekam, wird sich in der darauf folgenden Runde niederlassen und wieder arbeiten (es sei denn natürlich, sie erhält in dieser Runde einen anderen langen Befehl).

Bitte beachte, dass pro Einheit nur ein Befehl pro Einheit im normalen Report (NR) angezeigt wird. Die restlichen Default-Befehle werden in der Zugvorlage und im Computerreport angezeigt.

## Kurze Befehle dauerhaft ausführen

Manchmal ist es sinnvoll, dass ein kurzer Befehl jede Runde ausgeführt wird, so z.B. GIB, weil die Bergarbeiter das abgebaute Eisen ständig an die Schmiede liefern sollen.

Hierzu kannst du vor jeden kurzen Befehl ein @ (At-Zeichen, Klammeraffe) setzen. Solche Befehle werden einfach in die Zugvorlage der kommenden Runde kopiert und - so du sie nicht wieder löschst - wieder ausgeführt.

**Ein Beispiel**:

     EINHEIT berg;         Bergarbeiter [5,400$,U500]
       MACHE Eisen
       @GIB schm ALLES Eisen;   immer an die Schmiede liefern
     EINHEIT schm;         Schmiede [3,1343$,U250]
       MACHE Schwerter

**Hinweis:** Es gibt eine Obergrenze an Befehlen, die für eine Einheit gespeichert werden. Diese liegt derzeit bei 128 Befehlen, was für die meisten Zwecke leicht ausreichen sollte.

## Fehler unterdrücken

Es kann vorkommen, dass du Fehler bei der Ausführung eines Befehls bewusst in Kauf nimmst. Durch Voranstellen eines Ausrufezeichens (!) kannst du die Servermeldungen, die diesen Befehl betreffen, unterdrücken.

**Ein Beispiel**:

     EINHEIT berg;         Bergarbeiter
       MACHE Eisen
       !@GIB tran ALLES Eisen;   Der Transporter ist nicht immer da; wir wollen darüber keine Fehlermeldung
     EINHEIT tran;         Transporter
       ROUTE w PAUSE o PAUSE ;   Wir pendeln zwischen zwei Regionen
       !@GIB schm ALLES Eisen;   Im Westen übergeben wir das Eisen an die Schmiede

Das birgt natürlich das Risiko, dass du Fehler übersiehst, mit denen du nicht gerechnet hast.

## Siehe auch

- [Befehlsreihenfolge]
- [Kurzbeschreibung]
- [DEFAULT]

|     |     |
| --- | --- |
| Weiterlesen: | [Befehlsreihenfolge] |

[Befehlsreihenfolge]: /Spezial:Meine_Sprache/Befehlsreihenfolge "Spezial:Meine Sprache/Befehlsreihenfolge"

Abgerufen von „[https://wiki.eressea.de/index.php?title=Befehl&oldid=16787]“

[Kategorien][]:

- [Befehle][1]
- [Regeln]

  [`OPTION ZUGVORLAGE`]: /OPTION "OPTION"
  [ARBEITE]: /Spezial:Meine_Sprache/ARBEITE "Spezial:Meine Sprache/ARBEITE"
  [ATTACKIERE]: /Spezial:Meine_Sprache/ATTACKIERE "Spezial:Meine Sprache/ATTACKIERE"
  [BEKLAUE]: ./camouflage.md "Spezial:Meine Sprache/BEKLAUE"
  [FAHRE]: /Spezial:Meine_Sprache/FAHRE "Spezial:Meine Sprache/FAHRE"
  [FOLGE]: /Spezial:Meine_Sprache/FOLGE "Spezial:Meine Sprache/FOLGE"
  [FORSCHE]: /Spezial:Meine_Sprache/FORSCHE "Spezial:Meine Sprache/FORSCHE"
  [KAUFE]: /Spezial:Meine_Sprache/KAUFE "Spezial:Meine Sprache/KAUFE"
  [LEHRE]: /Spezial:Meine_Sprache/LEHRE "Spezial:Meine Sprache/LEHRE"
  [LERNE]: /Spezial:Meine_Sprache/LERNE "Spezial:Meine Sprache/LERNE"
  [MACHE]: /Spezial:Meine_Sprache/MACHE "Spezial:Meine Sprache/MACHE"
  [NACH]: /Spezial:Meine_Sprache/NACH "Spezial:Meine Sprache/NACH"
  [PFLANZE]: /Spezial:Meine_Sprache/PFLANZE "Spezial:Meine Sprache/PFLANZE"
  [PIRATERIE]: /Spezial:Meine_Sprache/PIRATERIE "Spezial:Meine Sprache/PIRATERIE"
  [ROUTE]: /Spezial:Meine_Sprache/ROUTE "Spezial:Meine Sprache/ROUTE"
  [SPIONIERE]: /Spezial:Meine_Sprache/SPIONIERE "Spezial:Meine Sprache/SPIONIERE"
  [TREIBE]: /Spezial:Meine_Sprache/TREIBE "Spezial:Meine Sprache/TREIBE"
  [UNTERHALTE]: /Spezial:Meine_Sprache/UNTERHALTE "Spezial:Meine Sprache/UNTERHALTE"
  [VERKAUFE]: /Spezial:Meine_Sprache/VERKAUFE "Spezial:Meine Sprache/VERKAUFE"
  [ZAUBERE]: /Spezial:Meine_Sprache/ZAUBERE "Spezial:Meine Sprache/ZAUBERE"
  [ZERSTÖRE]: /Spezial:Meine_Sprache/ZERST%C3%96RE "Spezial:Meine Sprache/ZERSTÖRE"
  [ZÜCHTE]: /Spezial:Meine_Sprache/Z%C3%9CCHTE "Spezial:Meine Sprache/ZÜCHTE"
  [Kurzbeschreibung]: /Spezial:Meine_Sprache/Kurzbeschreibung "Spezial:Meine Sprache/Kurzbeschreibung"
  [DEFAULT]: /Spezial:Meine_Sprache/DEFAULT "Spezial:Meine Sprache/DEFAULT"
  [https://wiki.eressea.de/index.php?title=Befehl&oldid=16787]: https://wiki.eressea.de/index.php?title=Befehl&oldid=16787
  [Kategorien]: /Spezial:Kategorien "Spezial:Kategorien"
  [1]: /Kategorie:Befehle "Kategorie:Befehle"
  [Regeln]: /Kategorie:Regeln "Kategorie:Regeln"
