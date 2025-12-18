---
alias:
    name: orders
    text: Orders
---
# Orders

## Conventions

In diesen Regeln gelten die folgenden Konventionen:

     GIVE unit-id [anzahl|ALLES] [gegenstand]

- Schlüsselwörter wie GIVE, MAKE, NOT sind in Großbuchstaben gesetzt. Das ist nicht Pflicht, wir empfehlen es aber.
- Platzhalter sind in Kleinbuchstaben. Sie sollen nicht wörtlich übernommen werden, sondern müssen durch konkrete Werte ersetzt werden, also zum Beispiel unit-id durch die Nummer der gewünschten Einheit. Manchmal schreiben wir dies auch als &lt;unit-id&gt;, in diesem Fall sind die &lt;- und &gt;-Symbole *nicht* zu übernehmen.
- Worte in \[\]-Klammern sind optional. Sie können also weggelassen werden, ändern dadurch aber die Bedeutung des Befehls. Alternativen sind dabei durch | getrennt. Obiges Beispiel lässt also `GIVE 123 ALLES` oder auch `GIVE abc 4 Schwert` zu.

## Syntax

Bis auf das Passwort und die Parteinummer sind dem Server Groß- und Kleinschreibung egal. `lerNE armBRUSTschiessen` ist völlig legal (wird aber nicht empfohlen, da es für Menschen schwer lesbar ist).

Gegenstände sollten immer in der *Einzahl* stehen, also `GIVE xyz 100 Schwert` oder `MAKE 15 Stein`. Im Report tauchen Gegenstände oft in der Mehrzahl auf und in Befehlen wird sie meist verstanden, aber du solltest dir bewusst machen, dass der Server natürliche Sprache nicht versteht, auch wenn die Befehle fast so aussehen.

Viele Befehle lassen sich abkürzen, wobei du es nicht übertreiben solltest, da dies fehlerträchtig ist: VER passt auf FORGET, SELL und LEAVE und wird darum als Fehler angemerkt; hier solltest du also mindestens vier Buchstaben verwenden. Außerdem sind allzu kryptische Verkürzungen nicht sonderlich leserlich, wenn du später deine Züge durchsiehst... Am sichersten ist es immer noch, wenn du deine Befehle nicht abkürzt, zumal es Befehle, Gegenstände und Talente geben kann, die absichtlich nicht in der Anleitung stehen, aber ähnlich anfangen wie bekannte Befehle, Gegenstände und Talente.

Texte, die Leerzeichen enthalten, müssen in Anführungszeichen (") eingeschlossen werden oder die Leerzeichen durch ~ (Tilde) ersetzt. Ferner dürfen Umlaute durch die entsprechende Umschreibung (Ä=AE usw.) ersetzt werden:

     NAME Schiff "Großer Blauer Vogel"
     GIVE einh 5 Würziger~Wagemut
     KAEMPFE REAR

Es ist möglich, einfache Anführungszeichen (') zu benutzen und zu kombinieren. Was dabei genau herauskommt, solltest du lieber ausprobieren, weil sich das genaue Verhalten immer mal verändern kann.

     MESSAGE REGION 'Sprich "Freund" und tritt ein'
     NAME BURG xyz "Helm's Deep"
     DEFAULT 'MAKE 1 "Wasser des Lebens"'

Auch so genannte Maskierung (escaping) durch das Zeichen \\ sind möglich, aber nicht unbedingt empfohlen:

    MESSAGE REGION "Sprich \"Freund\" und tritt ein"
    NAME BURG xyz 'Helm\'s Deep'
    DEFAULT 'MAKE 1 Wasser\~des\~Lebens'

Es ist übrigens nicht nötig, sich auf das lateinische Alphabet zu beschränken. In Namen und Beschreibungen ist der volle Unicode-Zeichensatz möglich:

    NAME UNIT "Σωκράτης"
    MESSAGE REGION "🨀 شاه مات"

Natürlich solltest darauf achten, von anderen auch verstanden zu werden.

<!-- TODO: rework ZUGVORLAGE notion-->
## Move template

The easiest way is to use the move template at the end of the evaluation.
All units are listed there so that you don't forget anyone.
If you don't send in any commands, the commands in the move template will still be executed automatically.
Even if you only send commands for some of your units, the commands in the move template will be executed for the remaining units.
If your evaluation does not contain a move template (with the extension `.txt`), you can reactivate it with the command [[cmd-option|`OPTION MOVE TEMPLATE`]].

## Short and long orders

Es gibt in Eressea kurze und lange Befehle.

Die langen Befehle sind:

[[cmd-work]], [[cmd-attack]], [[cmd-steal]], [[cmd-ride]], [[cmd-follow]], [[cmd-research]], [[cmd-buy]], [[cmd-teach]], [[cmd-learn]], [[cmd-make]] (Ausnahme: MAKE TEMP), [[cmd-move]], [[cmd-plant]], [[cmd-piracy]], [[cmd-route]], [[cmd-spy]], [[cmd-tax]], [[cmd-entertain]], [[cmd-sell]], [[cmd-cast]], [[cmd-destroy]], [[cmd-grow]].

Alle anderen Befehle sind kurze Befehle ([Kurzbeschreibung] aller Befehle). Du kannst beliebig viele kurze Befehle pro Einheit eingeben. Eine Einheit kann in der Regel nur einen langen Befehl haben. Es gibt ein paar Ausnahmen, die so genannten pseudolangen Befehle (`ATTACK, FOLLOW, BUY, SELL, CAST`), von denen unter Umständen mehrere gegeben werden können. Näheres in der Beschreibung der einzelnen Befehle.

Wird einer Einheit ein langer Befehl gegeben, wird sie diesen als Default-Befehl übernehmen und damit den vorherigen Default-Befehl ersetzen. Der Default-Befehl steht in der [Zugvorlage][3 Die Zugvorlage] immer als Vorschlag für einen langen Befehl. Du brauchst also einem Pferdedresseur nur einmal den Befehl MAKE pferd zu geben und dieser Befehl erscheint solange in der Zugvorlage, bis sie einen anderen langen Befehl erhält (z.B. LEARN Pferdedressur). Sinnvollerweise werden nicht alle langen Befehle als Default-Befehle übernommen. Das betrifft z.B. MOVE, ATTACK und FOLLOW. Weiteres zu Default-Befehlen auf der Seite zum Befehl [[cmd-default]].

Eine Einheit, die eine Runde arbeitete, in der kommenden Runde nach Norden zog und dann keinen Befehl mehr bekam, wird sich in der darauf folgenden Runde niederlassen und wieder arbeiten (es sei denn natürlich, sie erhält in dieser Runde einen anderen langen Befehl).

Bitte beachte, dass pro Einheit nur ein Befehl pro Einheit im normalen Report (NR) angezeigt wird. Die restlichen Default-Befehle werden in der Zugvorlage und im Computerreport angezeigt.

## Execute short commands permanently

Manchmal ist es sinnvoll, dass ein kurzer Befehl jede Runde ausgeführt wird, so z.B. GIVE, weil die Bergarbeiter das abgebaute Eisen ständig an die Schmiede liefern sollen.

Hierzu kannst du vor jeden kurzen Befehl ein @ (At-Zeichen, Klammeraffe) setzen. Solche Befehle werden einfach in die Zugvorlage der kommenden Runde kopiert und - so du sie nicht wieder löschst - wieder ausgeführt.

**Ein Beispiel**:

     UNIT berg;         Bergarbeiter [5,400$,U500]
       MAKE Eisen
       @GIVE schm ALLES Eisen;   immer an die Schmiede liefern
     UNIT schm;         Schmiede [3,1343$,U250]
       MAKE Schwerter

**Hinweis:** Es gibt eine Obergrenze an Befehlen, die für eine Einheit gespeichert werden. Diese liegt derzeit bei 128 Befehlen, was für die meisten Zwecke leicht ausreichen sollte.

## Suppress errors

Es kann vorkommen, dass du Fehler bei der Ausführung eines Befehls bewusst in Kauf nimmst. Durch Voranstellen eines Ausrufezeichens (!) kannst du die Servermeldungen, die diesen Befehl betreffen, unterdrücken.

**Ein Beispiel**:

     UNIT berg;         Bergarbeiter
       MAKE Eisen
       !@GIVE tran ALLES Eisen;   Der Transporter ist nicht immer da; wir wollen darüber keine Fehlermeldung
     UNIT tran;         Transporter
       ROUTE w PAUSE o PAUSE ;   Wir pendeln zwischen zwei Regionen
       !@GIVE schm ALLES Eisen;   Im Westen übergeben wir das Eisen an die Schmiede

Das birgt natürlich das Risiko, dass du Fehler übersiehst, mit denen du nicht gerechnet hast.

## See also

- [Befehlsreihenfolge]
- [Kurzbeschreibung]
- [[cmd-default]]

|--------------|----------------------|
| Weiterlesen: | [Befehlsreihenfolge] |

[Befehlsreihenfolge]: ./commands-sequence.md "Befehlsreihenfolge"

<!-- From [https://wiki.eressea.de/index.php?title=Befehl&oldid=16787] -->

[WORK]: ./cmd-work.md "WORK"
[Kurzbeschreibung]: ./commands-list.md "Kurzbeschreibung"
