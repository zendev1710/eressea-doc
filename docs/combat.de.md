# Krieg

Konflikte werden in Eressea nicht zu vermeiden sein. Es wird Streit um Silber, um Regionen, um Steuerrechte, um Handelsrouten und so weiter geben. Deswegen muss man sich immer nach Freunden und Alliierten umschauen, denn: "Freunde kommen und gehen, Feinde mehren sich."

## Die Seiten in einer Schlacht

Mit dem Befehl [`ATTACKIERE`] startet man den Angriff gegen den Gegner. Die `ATTACKIERE`-Befehle werden in einer zufälligen Reihenfolge ausgeführt. Bei einer Attacke sammeln sich die Einheiten aller Seiten in der Region und kämpfen als Einzelpersonen gegeneinander. Eine Schlacht dauert maximal sechs Runden: fünf reguläre Kampfrunden und eventuell noch die Runde 0 (Null), die [Taktikerrunde].

Die angreifende Seite besteht aus allen Einheiten, welche `ATTACKIERE`-Befehle gegen eine oder mehrere Einheiten der verteidigenden Partei gegeben haben.

Die verteidigende Seite besteht aus den Einheiten der verteidigenden Partei, die angegriffen wurden, wo der Gegner also `ATTACKIERE`*`einheit-nr`* gemacht hat, und allen Einheiten, die kampfbereit sind (also [`KÄMPFE`]`,`[`KÄMPFE AGGRESSIV`][`KÄMPFE`]`,`[`KÄMPFE HINTEN`][`KÄMPFE`] oder [`KÄMPFE DEFENSIV`][`KÄMPFE`] gesetzt haben). Außerdem helfen alle kampfbereiten Einheiten alliierter Parteien, also jener, die [`HELFE KÄMPFE`] für die angegriffene Partei gesetzt haben.

Es gibt also unterschiedliche Gründe, warum eine Einheit am Kampf teilnimmt. Diese sind in der Reihenfolge ihrer Priorität:

1. Die kampfbereite Einheit greift eine andere Einheit an. Dann nimmt sie in jedem Fall am Kampf teil.
2. Die Einheit wird von einer anderen Einheit angegriffen. Dann gliedert sie sich entsprechend ihres Kampfstatus in die [Kampfreihen] ein.
3. Eine Einheit aus der eigenen Partei wird von jemandem attackiert. Dann nimmt die Einheit am Kampf teil, wenn sie weder `KÄMPFE NICHT` noch `KÄMPFE FLIEHE` gesetzt hat. In letzterem Fall kommt sie nicht auf die Idee, zu [flüchten], da sie ja nicht selbst bedroht ist.
4. Eine Einheit aus einer verbündeten Partei (also einer Partei, der man `HELFE KÄMPFE` gesetzt hat) wird von jemandem attackiert. Dann nimmt die Einheit am Kampf teil, wenn sie nicht `KÄMPFE NICHT` oder `KÄMPFE FLIEHE` gesetzt hat. Wiederum wird eine Einheit mit `KÄMPFE FLIEHE` nicht [flüchten], da sie keiner direkten Bedrohung ausgesetzt ist.

Alliierte helfen also automatisch nur Verteidigern und *nur dann, wenn der Verteidiger nicht selber attackiert hat*. Angegriffene verteidigen sich mit dem Rest der Partei, wenn dieser sich nicht explizit aus dem Kampf heraushält. Für einen Angriff spielt der Kampfstatus primär keine Rolle: außer Verteidigern werden nur solche Einheiten in den Kampf verwickelt, die einen [`ATTACKIERE`] Befehl gegeben haben. Einheiten, die jedoch [`KÄMPFE NICHT`][`KÄMPFE`] oder [`KÄMPFE FLIEHE`][`KÄMPFE`] gesetzt haben, können aber nicht angreifen.

Um also einen Feind gemeinsam anzugreifen, muss jede angreifende Partei mindestens eine Einheit des Feindes attackieren. Um sich gemeinsam gegen Angreifer zu wehren, müssen sich die verteidigenden Parteien nur gegenseitig helfen.

Prinzipiell gilt jeder als alliiert, dem [`HELFE KÄMPFE`] gesetzt wurde, und der niemanden attackiert hat, dem [`HELFE KÄMPFE`] gesetzt wurde.

**Beispiel 1:** A hilft B und C. C attackiert B, deshalb greift A in den Kampf mit ein: B ist alliiert. Partei C gilt nicht als alliiert, weil sie einen Alliierten angreift.  
Wer kämpft nun gegen wen?  
Ich kämpfe gegen meine Feinde. Meine Feinde sind Parteien, die mich angreifen, die ich angreife, oder die einen Alliierten (nach der Definition von eben) angreifen.

**Beispiel 2:** A hilft B und C. B und C attackieren sich gegenseitig. Dann hilft A weder B noch C, denn keiner von ihnen gilt als alliiert, und keiner ist ein Feind von A.

**Beispiel 3:** A attackiert B und C. Sind B und C nicht alliiert, helfen sie einander trotzdem gegen A, denn A ist ein gemeinsamer Feind. Wenn also B noch Fronttruppen hat, C aber nur noch Bogenschützen, dann stellen sich die Truppen von B schützend vor C. Ausnahme: Wenn B und C verfeindet sind, weil z.B. B gegen einen zusätzlichen Alliierten D von C kämpft, dann helfen Sie sich nicht untereinander, auch nicht gegen A.

**Beispiel 4:** A und B attackieren C. Dann helfen sie sich gegen C (auch, wenn sie nicht alliiert sind), da sie ja einen gemeinsamen Feind haben.

Spielererfahrung:Es ist eigentlich noch ein bisschen komplizierter.

**Achtung:** Falsch gesetzte Helfe-Stati oder ATTACKIERE-Befehle haben schon so manchen Kampf ganz anders ausgehen lassen, als es erwartet wurde. Freunde blieben plötzlich tatenlos im Lager zurück oder kämpften gar plötzlich gegeneinander. Ein paar Tips helfen, die gröbsten Schnitzer zu verhindern:

- Du solltest regelmäßig deine Helfe-Stati kontrollieren zu allen Verbündeten. Am besten ist HELFE ALLES für alle, mit denen du in einen Kampf geraten *könntest*. Misstrauen tut hier oft weh.
- Nach Möglichkeit sollte nur eine [`GRUPPE`] vorhanden sein.
- Von deiner Partei sollten entweder alle Kampfeinheiten ATTACKIERE-Befehle haben oder keine. Wenn nur ein Teil deiner Einheiten attackiert, kann es sein, dass der Rest nicht am Kampf teilnimmt, wenn ein Verbündeter angegriffen wird.
- Es ist ratsam, alle feindlichen Einheiten anzugreifen. Mindestens solltest du von jeder feindlichen Partei eine Einheit angreifen. Beachte auch, dass durch Parteitarnung nicht immer klar sein könnte, wer wirklich zu welcher Partei gehört. Eine andere Strategie könnte sein, überhaupt nur eine feindliche Einheit anzugreifen und vielleicht zu hoffen, dass auf der Gegenseite falsch HELFE-Stati zu Verwirrung fühlen. Ob dies ein ehrenwertes Vorgehen wäre, wollen wir hier nicht beurteilen.

## Die Schlacht

Eine Schlacht dauert fünf Kampfrunden zuzüglich einer eventuellen Taktikerrunde. In jeder Kampfrunde schlagen die Kämpfenden in einer zufälligen Reihenfolge zu.

Man beachte, dass an einem Kampf teilnehmende Personen (das sind Personen, die im Kampfbericht aufgelistet werden) grundsätzlich keine weiteren langen Befehle ausführen können. Ausnahmen sind [Kämpfe auf See] und Kämpfe in Regionen, die *zu Kampfbeginn* von mindestens einer Einheit, die dem Kämpfer [`HELFE BEWACHE`][`HELFE KÄMPFE`] gesetzt hat, oder aus der eigenen Partei ist, bewacht wird. In diesem Fall sind weitere lange Befehle möglich.

### Kampfreihen

Im Kampf gibt es vier Kampfreihen. Diese bestehen nur aus den Einheiten, die auch wirklich am Kampf teilnehmen (s.o.). Für weitere Informationen über die Kampfstati siehe [KÄMPFE][`KÄMPFE`].

1. Reihe: Hier stehen alle Einheiten, die [`KÄMPFE`] oder [`KÄMPFE AGGRESSIV`][`KÄMPFE`] gesetzt haben.
2. Reihe: Hier stehen alle Einheiten, die [`KÄMPFE HINTEN`][`KÄMPFE`] oder [`KÄMPFE DEFENSIV`][`KÄMPFE`] gesetzt haben.
3. Reihe: Hier stehen alle Einheiten, die [`KÄMPFE NICHT`][`KÄMPFE`] gesetzt haben.
4. Reihe: Hier stehen alle Einheiten, die gerade versuchen, zu fliehen. Also die, die [`KÄMPFE FLIEHE`][`KÄMPFE`] gesetzt haben und solche, die entsprechend viele Trefferpunkte verloren haben (siehe auch [Flucht]).

Nur die ersten beiden Kampfreihen nehmen aktiv am Kampf teil, können also zuschlagen, schießen und getroffen werden. Nicht kampfbereite Einheiten, die direkt angegriffen werden, nehmen erst am Kampf teil, wenn eine der vorderen Reihen überrannt wird. Fliehende Einheiten versuchen natürlich zu fliehen (siehe [hier][Flucht]).

Einheiten, die in der 2. Reihe kämpfen, können erst direkt im Nahkampf angegriffen werden, wenn sie an die Front kommen (das kann z.B. passieren, wenn die 1. Reihe überrannt wird, s.u.). Gegen Angriffe gegnerischer Fernkämpfer verteidigen sie sich mit dem besten Kampftalent.

Kampfzauber von Magiern können hinter und an der Front gezaubert werden; davon abgesehen, werden sie sich - wie alle anderen auch - bewaffnen und kämpfen.

### Überrennen

Hat eine Partei und ihre Verbündeten mehr als dreimal so viele Personen in der Frontreihe, wie ihre Gegner gegenüber, dann müssen alle gegnerischen Einheiten aus der 2. Reihe aufrücken. Die 1. Reihe wurde überrannt. Die 3. Reihe rückt dann in die 2. Reihe vor und nimmt am Kampf teil. Befinden sich dann immer noch zu wenig Personen in der 1. Reihe, rücken die folgenden Reihen auf, bis wieder genug Personen in der 1. Reihe sind. Dieses Verhältnis wird vor jeder Kampfrunde überprüft.

## Die Musterung der Einheiten

Nun bewaffnen sich die Einheiten: jede Person in einer Einheit rüstet sich mit einer Nah- und Fernkampfwaffe und einer Rüstung, die sie gebrauchen kann, aus. Dabei bevorzugt sie diejenigen Waffen, bei denen sie in der Summe aus Attacke und Parade das höchste Talent hat. Magier, die einen Kampfzauber gesetzt haben, benutzen diesen zum Angriff. Für die Verteidigung benötigen sie aber eine Waffe (und ein passendes Kampftalent), sonst gelten sie als [unbewaffnet][6.2 Boni und Mali].

**Vorsicht:** ungebrauchte Waffen oder Rüstungen werden nicht automatisch an unbewaffnete oder ungerüstete Einheiten weiter verteilt.

Während des Kampfes wird die Waffe nicht mehr gewechselt, es sei denn, es kann eine bessere Waffe von einer Person aus der gleichen Einheit übernommen werden, die bereits gestorben ist (die überlebenden Kämpfer benutzen jeweils die besten verfügbaren Waffensets).

Ein Fernkämpfer, der plötzlich in der ersten Reihe angegriffen wird, muss zu einer Nahkampfwaffe greifen (sofern er eine besitzt und das entsprechende Talent zumindest auf Stufe 1 hat), sonst verteidigt er sich [ohne Waffe][6.2 Boni und Mali].

**Beispiele:** Eine Einheit mit 20 Personen hat 15 Schwerter, 10 Schilde und 5 Kettenhemden. Dann werden 5 Personen mit Schwert, Schild und Kettenhemd kämpfen, 5 weitere mit Schwert und Schild, 5 nur mit einem Schwert und die letzten 5 Kämpfer bleiben unbewaffnet. Eine Einheit mit 10 Personen und 10 Schwertern und 10 Kriegsäxten wird mit Schwertern kämpfen, da diese den besseren Bonus haben, obwohl sie wahrscheinlich weniger Schaden verursachen!

## Die Taktikerrunde

Vor der Schlacht wird der beste [Taktiker] aller teilnehmenden Einheiten bestimmt. Ein Taktiker, der in der ersten Reihe kämpft, bekommt einen Bonus von +1 auf sein Taktik-Talent. Steht er in der 3. oder 4. Reihe, reduziert sich sein Talent um 1. Um ein wenig "Tagesform" und Glück einfließen zu lassen, erhält jeder Taktiker einen zufälligen Bonus, der bei 0 startet und rein theoretisch sehr groß werden kann, wobei die Wahrscheinlichkeit dafür immer geringer wird, je größer der Bonus ist.

Die Seite mit dem besten Taktikwert kann in der 0. Runde attackieren (die sogenannte "Taktikerrunde"), ohne dass der Feind in dieser Runde auch angreifen kann. Wie viele Schläge sie ausführen, hängt von der Differenz zwischen dem besten Taktikwert auf der Gewinnerseite zur Verliererseite zusammen: Pro Punkt Unterschied hat jede Person eine 10-prozentige Chance, in der Taktikerrunde anzugreifen.

**Beispiel:** Seite A hat eine Person mit Taktik 4 in der ersten Reihe. Seite B hat 10 Personen mit Taktik 4 in der dritten Reihe. Also hat Seite A effektiv Taktik 5 und Seite B Taktik 3. Wenn der zufällige Bonus nicht wäre, würde die eine Person von Seite A mit 20% Wahrscheinlichkeit in der Taktikerrunde angreifen. Wenn dagegen die Person von Seite A eine 0 als Bonus würfelt, muss mindestens eine Person von Seite B eine 2 würfeln. Andernfalls hat Seite A die Taktikerrunde. Nehmen wir an, das beste Würfelergebnis von Seite B ist eine 5 (das ist unwahrscheinlich, aber durchaus möglich). Die Differenz für Seite B ist also 3 + 5 - (5 + 0) = 3. Dann schlägt jede Person auf Seite B in Runde 0 mit 30% Wahrscheinlichkeit zu. Das können 0 bis 10 Personen sein, im langfristigen Mittel sind es aber etwa 3 Schläge.

## Helden

Helden sind besonders starke Kämpfer. Sie müssen zuvor mit dem Befehl [BEFÖRDERE] ernannt worden sein. Helden können in jeder Kampfrunde 5 mal angreifen.

Achtung! Dies gilt nicht für magische Angriffe und auch nicht für Armbrüste und Katapulte.

Für nähere Informationen siehe [BEFÖRDERE].

## Der Kampf zwischen zwei Personen

In jeder Schlacht kämpfen die Armeen personenweise gegeneinander, egal wie groß sie sind. Dabei wird folgendermaßen vorgegangen:

- Die Attacke des Angreifers und die Parade des Verteidigers sind (zunächst) so hoch, wie ihr Waffentalent.
- Boni/Mali addieren: Zur Attacke des Angreifers und zur Parade des Verteidigers werden eventuelle [Boni und Mali][6.2 Boni und Mali] addiert.
- Handelt es sich bei dem Angreifer um einen Fernkämpfer, wird der so modifizierte Paradewert seines Gegners halbiert.
- Die Basis-Trefferchance (BT) eines Angreifers liegt grundsätzlich bei 30%.
- Werte voneinander abziehen: Für jeden Punkt Differenz zwischen der Attacke des Angreifers und der Parade des Verteidigers wird jetzt die BT um 5% erhöht bzw erniedrigt. Die tatsächliche Trefferchance ergibt sich also aus folgender Formel: (Attacke(Angreifer)-Parade(Verteidiger)) \* 5% + 30%.
- Anfängerglück: Schlägt der Angriff fehl, hat der Angreifer zusätzlich eine 10%ige Chance, seinen Angriff doch noch zu verwandeln: Er kann ein zweites Mal zuschlagen und zwar mit einer um 90 bis 99% (Zufall) erhöhten Trefferchance. Dadurch haben stark benachteiligte Kämpfer die Möglichkeit, zumindest einige Zufallstreffer zu landen.

Jede Person attackiert einmal pro Kampfrunde (außer [Helden] und einigen Monstern).

Gelingt einem Kämpfer ein Treffer, so fügt er dem Gegner Schaden zu. Dabei verursachen verschiedene Waffen auch verschieden starken Schaden (Schadenspunkte, siehe [Waffeneigenschaften]). Außerdem lohnt es sich, hohe Waffentalente zu haben: hat man mehr Talentstufen als der Gegner, so erhöht sich der Schaden bei einem Schlag um einen Punkt pro zwei Talentstufen Unterschied. Dabei werden reine Talentwerte gerechnet, Boni durch Pferde, Burgen usw. zählen nicht. Dies gilt für Fern- und Nahkampf gleichermaßen. Daneben gibt es noch eine gewisse vom Talentunterschied abhängige Chance, dass man einen kritischen Treffer landet, der bis zum fünffachen Waffenschaden verursachen kann.

Hat eine Person mehr Schadenspunkte hinnehmen müssen, als sie "einstecken kann" (siehe [Rasseneigenschaften]; dabei addieren sich die verschiedenen Treffer im Kampf), so stirbt sie.

Trägt ein Kämpfer eine Rüstung, so kann diese einen Teil (oder gar alle) der Schadenspunkte auffangen. Allerdings wird man durch Rüstung unbeweglicher, und im Gegenzug erhöht sich die Chance, überhaupt getroffen zu werden (siehe [diese] Tabelle). Gegen Armbrüste wirkt eine Rüstung nur zur Hälfte (abgerundet).

Manche Wesen oder Waffen sind auch in der Lage magischen Schaden zu verursachen. Gegen magischen Schaden ist eine normale Rüstung wirkungslos. Es zählt nur die [Magieresistenz] welche sich durch bestimmte Ausrüstungsgegenstände und Zauber steigern lässt.

Außerdem gibt es noch das Talent Ausdauer, mit dem man seinen Körper stählt und so mehr Trefferpunkte erleiden kann, ohne daran zu sterben (siehe [diese Tabelle]).

### Fernkampf

Schusswaffen und Katapulte können am besten aus der zweiten Reihe heraus benutzt werden. Hier sind sie vor den Nahkämpfern des Gegners durch die erste Reihe geschützt.

Fernkämpfer können auch in die zweite Reihe schießen. Sie suchen sich aus allen Gegnern in der ersten oder zweiten Reihe zufällig ein Ziel aus.

Armbrüste haben zudem die Eigenschaft, Rüstungen zu durchbohren: Gegen einen Armbrust-Treffer wirkt die Rüstung nur zur Hälfte (abgerundet).

Die Tabelle unten zeigt, wie sich die Schusswaffen unterscheiden. Einen Bogen zu benutzen ist sehr schwer (Offensivbonus -2), dafür kann man jede Kampfrunde schießen. Armbrüste sind viel einfacher zu bedienen (OB 0), aber können nur jede dritte Kampfrunde schießen. Katapulte schießen immer in der ersten Runde (das kann die Taktikrunde oder Runde 1 sein) und verursachen dabei schwere Schäden.

Gegen Fernkampfwaffen parieren angegriffene Personen nur mit ihrem halben Talent. Einheiten in der ersten Reihe verteidigen sich aber mit ihrem vollem Talentwert, wenn die Fernkämpfereinheit auch in der ersten Reihe steht.

**Achtung!** Wenn ein Fernkämpfer in die erste Reihe gerät (z.B. weil diese [überrannt][Kampfreihen] wurde), muss er sich mit einer Nahkampfwaffe verteidigen. Wenn er diese nicht hat oder nicht damit umgehen kann (also sein entsprechendes Talent kleiner als 1 ist), verteidigt er sich [unbewaffnet][6.2 Boni und Mali]!

Katapulte benötigen Munition. Diese kann mittels [MACHE Katapultmunition] durch einen Steinbauer mit Talent 3 aus Steinen produziert werden und wiegt 10 Gewichtseinheiten. Eine Munitionseinheit entspricht dabei einer Salve.

Schusswaffen - Proben, Zeitaufwand und Treffer

| Waffe                             | Talent            | Offensivbonus | Nachladen |
|-----------------------------------|-------------------|---------------|-----------|
| Armbrust / Mallornarmbrust        | Armbrustschießen  | 0             | 2         |
| Katapult                          | Katapultbedienung | \-4           | 5         |
| Bogen / Mallornbogen / Elfenbogen | Bogenschießen     | \-2           | 0         |

Dabei ist unter Nachladen angegeben, wie lange es dauert, die Waffe wieder schussbereit zu machen. Ein Katapult kann also in jedem Kampf nur einmal eingesetzt werden. Eine Armbrust kann demnach jede dritte Runde schießen, Bögen sogar jede Runde.

### Boni und Mali

Verschiedene Faktoren können die Chance, jemanden zu treffen (Attacke) oder einen Treffer abzuwehren (Parade), modifizieren. Alle Boni und Mali wirken sich direkt auf das Talent aus und werden vor einer eventuellen Talent-Halbierung durch Fernkämpfer angerechnet. Die Schadenspunkte, die eine Person austeilt, werden durch die Boni und Mali nicht verändert, hier zählen die unmodifizierten Talentwerte. Siehe verkürzt auch [diese Tabelle][1].

Unbewaffnete  
Als unbewaffnet gelten auch Personen, die kein passendes Waffentalent zu ihrer Waffe haben.

Unbewaffnete Personen kämpfen mit einem Talent von -2.

Fernkämpfer, die in einen Nahkampf geraten und nicht auf eine Nahkampfwaffe (und ein entsprechendes Talent) zurückgreifen können, verteidigen sich mit einem Talent von -2. Sie können aber noch mit ihrer Fernkampfwaffe angreifen.

Goblins verteidigen sich mit +/-0.

Das Talent, mit dem Orks in den unbewaffneten Kampf gehen, bestimmt sich aus der Stufe ihres besten Nahkampftalents -3.

Manche Rassen (i.A. nur Vertraute) können das Talent Unbewaffneter Kampf lernen und haben dann keinen Abzug, wenn sie ohne Waffe kämpfen.



Burgenbonus  
Personen in Burgen sind zusätzlich geschützt. Burginsassen erhalten je nach Größe der Burg einen Bonus bei der Parade, wenn sie zur verteidigenden Seite gehören und die Burg groß genug ist, um sie zu beherbergen. Dabei gibt eine Befestigung +1, ein Turm +2 usw. bis zur Zitadelle, die +5 gibt. Greifen die Burginsassen selber an, erhalten sie den Burgenbonus zur Parade nicht mehr. Der Burgenbonus gilt auch gegen Fernkämpfer!



Pferdebonus  
In Ebenen, Wüsten und Hochländern können Nahkämpfer in der ersten Reihe auf freiem Feld ein Pferd benutzen. Um ein Pferd in den Kampf zu reiten, braucht man ein Reiten Talent von mindestens 2. Reiter bekommen einen Bonus von +2 auf Attacke und Parade, weil sie schneller und wendiger sind. Keinen Pferdebonus erhalten Personen, die innerhalb einer Burg stehen, vom Burgenbonus profitieren und attackiert werden. Trolle können Pferde nicht im Kampf nutzen!



Lanzenbonus  
Berittene Speer- und Lanzenträger erhalten einen weiteren Bonus von +1 zur Attacke.



Pikenbonus  
Speer- und Hellebardenträger, die kein Pferd benutzen, erhalten gegen berittene Truppen einen Bonus von +1 zur Parade.



Waffenmodifikatoren  
Auch [Waffenmodifikatoren][Waffeneigenschaften] gelten in diesem Sinne als Boni und Mali.

Eine Hellebarden-Einheit hat also (zusätzlich zu eventuellen anderen Boni oder Mali) +2 auf ihre Parade. Wenn sie selbst nicht reitet und gegen einen Reiter kämpft, wird ihr Paradewert für diesen Moment noch einmal um +1 erhöht.

**Beispiele:**

- Basiswert des Angreifers: BT = 30%  

Angreifer mit Talent 3, Verteidiger Talent 4 -&gt; Trefferchance=25%  
Verteidiger steht in Zitadelle -&gt; Parade +5 -&gt; Trefferchance=0%  
Der Angreifer hat also nur eine Chance von 10% ("Anfängerglück"), überhaupt noch einen zweiten Versuch zu bekommen, und dann nochmal eine 90 bis 99%ige den Treffer zu landen. Insgesamt hat er also lediglich 9 bis 9,9% Chance, den Verteidiger zu treffen. Er ist ja auch (durch die Zitadelle) wirklich stark im Nachteil.

- Diesmal steht der Verteidiger nicht in der Zitadelle:  

Basiswert des Angreifers -&gt; BT = 30%  
Angreifer mit Talent 3, Verteidiger Talent 4 -&gt; Trefferchance = 25%  
Angreifer mit Pferdebonus -&gt; Attacke +2 -&gt; Trefferchance = 35%

- Eine Schwertkämpferin mit Hiebwaffen 3 gegen einen Reiter mit Reiten 1 und Stangenwaffen 2: Sie kämpft mit Attacke 3 (Talent 3) gegen Parade 2 (Talent 2, ohne Pferdebonus - der Reiter kann nicht gut genug reiten).  

Die Angreiferin hat also eine Trefferchance von 35%.

- Ein Bogenschütze mit Talent 9 greift aus der 2. Reihe eine Lanzenreiterin mit Reiten 3 und Stangenwaffen 9 an. Er attackiert mit 7 (Malus von 2 durch den Bogen) gegen eine Parade von 5 (der Paradewert wird halbiert und abgerundet: Talent 9, +2 Pferdebonus -&gt; (9+2)/2=5).  

Der Angreifer hat also eine Trefferchance von (7 - 5) \* 5% + 30% = 40%

- Eine Lanzenreiterin mit Reiten 3 und Stangenwaffen 9 greift einen Bogenschützen mit Talent 9 in der 1. Reihe an.
  - Sie attackiert mit 12 (Talent 9, +2 Pferdebonus und +1 Lanzenbonus) gegen eine Parade von -2 (Schütze ohne Waffe für den Nahkampf).  

Die Angreiferin hat eine Trefferchance von 100%; sie wird also in jedem Fall treffen...

- - Sie pariert mit ihrem vollen Paradewert (also Waffentalent + Pferdebonus = 11) gegen die Fernkampfwaffe, da der Schütze in der 1. Reihe steht, und der Schütze muss auf seinen Talentwert den Malus 2 (durch den Bogen) hinnehmen.  

Der Schütze greift also effektiv mit einer Attacke von 7 gegen die Reiterin mit einer Parade von 11 an. Er hat also eine Trefferchance von (7 - 11) \* 5% + 30% = 10%.

- Eine Speerträgerin mit Stangenwaffen 3 in einer Burg greift eine Reiterin mit Reiten 2 und Stangenwaffen 3 an.
  - Sie attackiert mit 3 (Talent 3, kein Pikenbonus bei der Attacke; kein Burgenbonus, da sie den Angriff begonnen hat) gegen 5 (Talent 3, +2 Pferdebonus, kein Lanzenbonus bei der Parade).  

Die Angreiferin hat eine Trefferchance von (3-5)\*5%+30%=20%.

- - Sie pariert mit 4 (Talent 3, kein Burgenbonus, da sie selbst angegriffen hat; +1 Pikenbonus) gegen 6 (+2 Pferdebonus und +1 Lanzenbonus).  

Die Angegriffene hat eine Trefferchance von (6 - 4) \* 5% + 30% = 40%.

- Ein Reiter mit Reiten 2 und Hiebwaffen 2 gegen einen Speerträger mit Stangenwaffen 3:
  - Er attackiert mit 4 (Talent 2, +2 Pferdebonus) gegen 4 (Talent 3 und +1 Pikenbonus).  

Der Angreifer hat also eine Trefferchance von 30%.

- - Der Speerträger schlägt zurück mit 3 gegen 4 (der Pikenbonus gilt nur bei der Parade, nicht bei der Attacke).  

Der Speerträger hat also eine Trefferchance von 25%.

- Ein Lanzenreiter mit Reiten 2 und Stangenwaffen 3 greift eine gleich gute Kollegin an. Er kämpft mit 6 (Talent 3, +2 Pferdebonus, +1 Lanzenbonus) gegen 5 (Talent 3, +2 Pferdebonus)  

Der Angreifer hat damit eine Trefferchance von 35%.

Hieraus folgt, dass man eine Burg relativ gut halten kann, dass man aber aus einer Burg heraus möglichst keine Angriffe starten sollte, denn damit verliert man seinen Bonus bei der Verteidigung. Hieraus folgt auch, dass Speerträger ein wenig wirksamer gegen berittene Truppen sind als Schwertträger.

## Die Flucht

Personen, die [KÄMPFE FLIEHE][`KÄMPFE`] gesetzt haben und [attackiert][`ATTACKIERE`] werden, versuchen zu fliehen. Dies tun sie vor jeder Kampfrunde, es kann also sein, dass sie erst (weitere) Treffer hinnehmen müssen, bevor die Flucht gelingt.

Personen mit [`KÄMPFE`] oder [`KÄMPFE HINTEN`][`KÄMPFE`], die nur noch 20% ihrer Trefferpunkte haben und Personen mit [`KÄMPFE DEFENSIV`][`KÄMPFE`] oder [`KÄMPFE NICHT`][`KÄMPFE`], die nur nur noch 90% ihrer Trefferpunkte haben, versuchen ebenfalls zu fliehen, aber erst, wenn sie im Kampf einen Treffer abbekommen haben. Dabei zählen auch Treffer, deren Schadenspunkte vollständig von der Rüstung aufgehalten wurden und fehlgeschlagene Trefferversuche. Das soll verhindern, dass Einheiten, die schon vor dem Kampf angeschlagen waren, fliehen, obwohl sie nicht tatsächlich in Gefahr waren.

Die Grundchance für die Flucht beträgt 25% (50% für Halblinge), dazu kommen 10%, wenn man ein Pferd hat und je 5% pro Stufe im Talent Tarnung; der Maximalwert ist aber 75% (bzw. 90% für Halblinge).

Fliehende Einheiten entziehen sich dem Kampf, verbleiben aber in sicherer Entfernung zum Kampfgeschehen in der Region. Befand sich die Einheit in einem Gebäude oder auf einem Schiff an Land, verlässt sie dieses, sobald eine Person aus der Einheit während des Kampfes geflohen ist.

**Hinweis:** Es kann deshalb sinnvoll sein, Burgen- oder Schiffsinsassen zu befehlen, ihr eigenes Schiff wieder zu betreten, was sie nach dem Kampf evtl. tun können. Zu beachten ist, dass auch das Kommando wieder an die richtige Einheit übergeben werden sollte.

Besonderheiten gelten für Einheiten mit dem Status FLIEHE. Diese Einheiten können sich nach dem Kampf noch bewegen, auch wenn sie sonst keinen langen Befehl ausführen dürften. Weiterhin können diese Einheiten keine Regionen bewachen. Eine durchgeführte Bewachung wird automatisch aufgelöst, wenn die Einheit den Status FLIEHE einnimmt. Dies geschieht zu Beginn der Runde, womit alle Effekte von [`BEWACHE`] sofort aufgelöst werden.

## Kampf auf und von Schiffen

Seeschlachten werden wie Schlachten zu Land ausgefochten: Die [Schiffe] entern sich gegenseitig und die Einheiten fallen übereinander her. Nach der Schlacht ist es den Einheiten möglich, weitere lange Befehle auszuführen.

Ist ein Schiff in eine Schlacht verwickelt, so bekommt es pro Kampfrunde 5% Schaden, wenn mindestens eine Person Schaden erleidet, die auf dem Schiff ist oder zu Beginn der Runde auf dem Schiff war. Es hilft also nicht, das Schiff vor Kampfbeginn zu verlassen. Die [Taktikrunde][Taktiker] und die erste Runde wird nicht mitgezählt, so dass es immer nur maximal 20% Schaden geben kann.

Zu größeren Schäden kann es kommen, wenn Seeschlangen in den Kampf verwickelt sind. Diese Monster haben, wie auch einige Vertraute, einen Angriff der jede Kampfrunde Strukturschaden an Schiffen verursachen kann.

Ist das Schiff nach der Schlacht unterbesetzt oder leer, treibt es ohne Kontrolle im Ozean und nimmt weiteren [Schaden].

Will man mit einem Schiff Truppen in einer feindlich [[alliances|`BEWACHE`]] Region anlanden, so müssen diese erst das Schiff [`VERLASSEN`] und können erst in der folgenden Runde den Angriff starten oder sich bewegen. Dadurch hat der Gegner die Möglichkeit, entsprechend zu reagieren.

Von Land aus kann man Schiffe an der Küste sofort angreifen. Auch reihen sich Truppen auf Schiffen normal gemäß Kampf- und [`HELFE`][`HELFE KÄMPFE`]-Status in die Kampfreihen ein, falls sie oder Verbündete angegriffen werden.

## Piraterie

Mit **Piraterie** hat ein Schiffskapitän die Möglichkeit, Schiffe anderer Parteien in Nachbarregionen aufzubringen.

Der Kapitän legt sich auf die Lauer nach Schiffen, die nach ihrer Bewegung in einer Nachbarregion liegen. Dort angekommen, kann die Mannschaft in der kommenden Runde ganz normal agieren. Mit Hilfe von [`FOLGE SCHIFF`] könnte man zum Beispiel seine Opfer auch erstmal verfolgen. Bei der ganzen Geschichte sind einige Sachen zu beachten:

- Als Ziele werden nur Parteien erkannt, mit denen man nicht mit `HELFE KÄMPFE` alliiert ist.
- Werden Parteinummern angegeben ([`PIRATERIE <parteinummer> ...`]), so werden nur Kapitäne der angegebenen Parteien als Ziele erkannt.
- Der Mechanismus funktioniert auch, wenn das Piratenschiff an Land ist. Er bietet also eine effektive Möglichkeit zum Küstenschutz.
- Piraten segeln auch in Landregionen, sofern das Schiff dort landen kann. Falls es nicht landen kann, nimmt es Schaden.
- Piratenkapitäne sind dumm wie Brot. Sie können nicht einschätzen, ob ein Ziel ihnen möglicherweise überlegen ist, und werden fröhlich auch mit einem einzigen Schiff in einer feindliche Flotte von 100 Schiffen hineinfahren. Das Piratendasein hat eben seine Risiken.
- Stehen mehrere potentielle Ziele zur Auswahl, wird der Kapitän eines nach dem Zufallsprinzip aussuchen.
- Piratenflotten bleiben zusammen. Genauer gesagt: Hat bereits ein alliiertes Schiff (zu dem der Kapitän [`HELFE KÄMPFE`] gesetzt hat) aus der eigenen Region ein Opfer erkannt, so segelt unser Schiff auch in die betreffende Region, vorausgesetzt, das vom ersten Schiff erkannte Opfer ist ebenfalls ein potentielles Opfer für uns.

## Das Ende

Nach der Schlacht werden die Toten gezählt, und alles brauchbare Material von ausgelöschten Einheiten wird zusammengetragen und unter den Überlebenden verteilt.

Einheiten, die im Kampf verletzt wurden, bleiben verletzt. Dies wird im Report mit angezeigt. Im Laufe der Zeit erholen sich die verletzten Einheiten wieder. Dabei regenerieren Einheiten normalerweise 5% (einige [Rassen] mehr) ihrer maximalen Trefferpunkte pro Runde, mindestens aber je einen Punkt pro Person in der Einheit. Untote Einheiten regenerieren nicht.

Wenn die Region, in der gekämpft wurde, *bei Kampfbeginn* von einer eigenen Einheit oder von einer Einheit, die zur eigenen Partei ein [`HELFE BEWACHE`][`HELFE KÄMPFE`] gesetzt hat, [[alliances|bewacht]] wurde, können alle Einheiten, die am Kampf teilnehmen (die also im Kampfreport auftauchen), noch einen langen Befehl ausführen. Das funktioniert selbst, wenn feindliche Truppen die Region ebenfalls bewachen. Es funktioniert auch, wenn man selbst angegriffen hat (also die `ATTACKE`-Befehle selbst gesetzt wurden). Hat man zu Beginn des Kampfes keine eigenen oder verbündeten Einheiten, die die Region `BEWACHEN`, können die am Kampf teilnehmenden Einheiten nach dem Kampf keine langen Befehle mehr ausführen.

Die einzigen Ausnahmen bilden Einheiten mit dem Kampfstatus [`KÄMPFE FLIEHE`][`KÄMPFE`] und Einheiten auf See. Einheiten mit dem Status `KÄMPFE FLIEHE` können sich nach dem Kampf noch bewegen, wenn sie einen der folgenden Befehle gesetzt haben: [`NACH`]`,`[`ROUTE`]` oder `[`FOLGE`][`FOLGE SCHIFF`]. Nach Kämpfen auf See kann man stets noch lange Befehle ausführen.

## Siehe auch

- [Taktik]
- [Kriegstabellen]

Weiterlesen: [[alliances|Allianz]].

<!-- From [https://wiki.eressea.de/index.php?title=Krieg&oldid=16610] -->

[6.2 Boni und Mali]: #boni-und-mali
[`ATTACKIERE`]: ./cmd-attack.md "ATTACKIERE"
[Taktikerrunde]: #taktik
[`KÄMPFE`]: ./cmd-combat.md "KÄMPFE"
[`HELFE KÄMPFE`]: ./cmd-help.md "HELFE"
[Kampfreihen]: #schlacht
[flüchten]: #flucht
[`GRUPPE`]: ./cmd-group.md "GRUPPE"
[Kämpfe auf See]: ./war.md#kampf-auf-und-von-schiffen "Kampf auf Schiffen"
[Flucht]: ./war.md#die-flucht "Die Flucht"
[Taktiker]: ./tactic.md "Taktik"
[BEFÖRDERE]: ./cmd-promote.md "BEFÖRDERE"
[Helden]: ./cmd-promote.md "BEFÖRDERUNG"
[Waffeneigenschaften]: ./war-tables.md#waffeneigenschaften "Kriegstabellen"
[Rasseneigenschaften]: ./war-tables.md#rasseneigenschaften "Kriegstabellen"
[diese]: ./war-tables.md#rüstung "Kriegstabellen"
[Magieresistenz]: ./war-tables.md#magieresistenz "Kriegstabellen"
[diese Tabelle]: ./war-tables.md#ausdauer "Kriegstabellen"
[MACHE Katapultmunition]: ./cmd-make.md "MACHE"
[1]: ./war-tables.md#kampfmodifikatoren "Kriegstabellen"
[`BEWACHE`]: ./cmd-guard.md "BEWACHE"
[Schiffe]: ./ships.md "Schiffe"
[Schaden]: ./ships.md#schiffsschaden "Schiff"
[`VERLASSEN`]: ./cmd-leave.md "VERLASSE"
[`FOLGE SCHIFF`]: ./cmd-follow.md "FOLGE"
[`PIRATERIE <parteinummer> ...`]: ./cmd-piracy.md "PIRATERIE"
[Rassen]: ./skills-modifiers.md "Talentmodifikatoren"
[`NACH`]: ./cmd-move.md "NACH"
[`ROUTE`]: ./cmd-route.md "ROUTE"
[Taktik]: ./tactic.md "Taktik"
[Kriegstabellen]: ./war-tables.md "Kriegstabellen"
