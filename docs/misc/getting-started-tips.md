# Anfängertipps

Achtet bei der Befehlseingabe darauf, dass ihr die richtige Parteinummer und die richtigen Einheitennummern verwendet habt. Setzt ein [Passwort] und vergesst es nicht.

Es ist für alle interessanter, wenn ihr eure Partei und alle Einheiten auf originelle Art und Weise benennt. Beachtet dabei bitte, dass Eressea ein Fantasy-Rollenspiel ist - Namen wie "Barney's Folterknechte der Fernbedienung" (ja, sowas gab es wirklich!) passen partout nicht in die Atmosphäre von Eressea.

Wenn ihr euch nicht sicher seid, oder Fragen habt, wendet Euch am besten an den Discord Channel von Eressea \[[\[1\]][1]\]. Das geht per Browser, installiertem Programm oder App. Man wird euch hier sicher Tips für die ersten Züge geben oder eure Fragen beantworten. Mit Fragen könnt ihr euch auch im [PbEm-Spiele-Forum] melden. Dort hat Eressea ein eigenes Sub-Forum.

Die meisten Spieler benutzen [Magellan], ein Programm, was den CR (Computer Report) liest, übersichtlich darstellt, bei der Erstellung der Befehle hilft und viele Fehler anzeigt.

Dann gibt es noch [ECheck], ein Programm, mit dem man seine Züge auf ihre Korrektheit überprüfen kann. ECheck wird vom Server automatisch auf die eingehenden Züge angesetzt und das Ergebnis zurückgeschickt. Verwendet ECheck zu Hause mit der Option -e um zu überprüfen, ob eure Befehle wie erwartet interpretiert werden. ECheck überprüft nur die Schreibweise der Befehle und die Reihenfolge der Parameter. Die Semantik (also Sinn und Unsinn der Befehle) wird von ECheck nicht erfasst, wobei ECheck jedoch verschiedene Tests bezüglich Silber ausführen kann, wenn die [Zugvorlage] des Servers benutzt wird.

Steckt euch mehrere Ziele, die ihr erreichen wollt. Eines der ersten Ziele sollte die Erkundung der Umgebung sein. Nur so findet ihr wichtige Berg- und Waldregionen, in denen ihr Erz abbauen und Holz fällen könnt. Schickt also einige Einheiten mit nur einer Person und gebt ihnen genug Silber mit, um sich eine Weile über Wasser zu halten. Vorsicht: das Silber für die Rekrutierung muss dabei eingerechnet werden!

Erschafft weitere Einheiten und lernt ein paar Talente, die ihr in den nächsten drei bis vier Runden zu brauchen gedenkt:

Hier ist vor allem [Unterhaltung] essenziell, um Geld zu verdienen. Ohne entsprechendes Silber wird eure Partei nicht wachsen können. Auch [Steuereintreiber] sind eine gute Einnahmequelle; hierfür braucht man z.B. Metalle ([Bergbau]) oder Holz ([Holzfällen]), um Waffen wie Schwerter oder Speere zu bauen; und natürlich brauchen die Steuereintreiber ein entsprechendes Waffentalent ([Steuereintreiben], [Waffentalente]).

[Wahrnehmung] ist ein sehr wichtiges Talent, das von Anfängern häufig unterschätzt wird. Nur Wahrnehmer sind in der Lage, getarnte Einheiten zu sehen und diese an einem [Diebstahl] zu hindern! Es lohnt sich also, gleich zu Anfang zumindest für die Heimatregion(en) je einen Wahrnehmer zu rekrutieren und durchlernen zu lassen. Ratsam ist auch das frühe Bauen von [Burgen], zumindest auf Stufe 2, "Handelsposten", (benötigte Talente: [Steinbau][Bergbau] für die Steine und [Burgenbau] zum Bau der Burg), damit [Handel] getrieben werden kann, und natürlich die Ausbildung der nötigen Händler und Transporteure (in der Regel Reiter) sowie deren Ausstattung ([Pferde und ggf. Wägen]). Handel zu verstehen ist für Anfänger nicht ganz leicht, aber es lohnt sich.

Einheiten mit teuren Talenten wie [Taktiker], [Alchemisten] usw. sollte man erst später ausbilden, da ihre Ausbildung sehr viel Silber verschlingt (200 Silber pro Runde). [Magier] auszubilden kostet noch mehr Silber, doch ein Magier mit Kampfzaubern kann im Konfliktfall große Vorteile bringen. Und Magier aller Magiegebiete können bereits sehr früh einen Zauber zum Silberverdienen sprechen, sodass sich hier eine frühe Investition (vor allem für Rassen mit +1 in Magie) lohnt.

Auch eine kleine Vorsorge, falls die Nachbarn nicht sehr friedlich sein sollten, wäre ratsam. Also ein Plan, wie man seine Partei zum Ende der anfänglichen Immunität vor Angriffen wappnet.

Schreibt reichhaltig Kommentare in eure Befehlsdateien, damit ihr in den nächsten Runden auch wisst, wofür dies oder das gemacht wurde. Es ist eine gute Idee, die Befehle nach Regionen zu gruppieren, so dass man ein paar Zeilen an Kommentaren für die Region zur Verfügung hat. Ein guter Ausgangspunkt für eure neue Befehlsdatei ist die an der Auswertung angehängte [Zugvorlage] für den nächsten Zug. Bei jeder Einheit kann man noch anmerken, was sie produziert, für wen sie es produziert, wohin sie unterwegs ist, oder welche Art von Handel sie treibt. Hier ein Beispiel für diese Kommentare:

       REGION 4,4 ; Lochinver
       ; Vorsicht vor der dunklen Horde
       ; abgeholzt?

       UNIT zbt;           Bogenbauer Jog'nabat und seine Sippe [4;100$]
          MAKE Schwerter
          Gib sjur 5 Schwerter ; wahrscheinlich gibt er nur die 4, die er
                               ; letzte Runde hatte

       UNIT sjur;          Fuhrmann Sjur [2;243$]
         // Kapazität: 420 = 7 Steine; Silber!
         Gib 7jht 7 Steine
         Route Südwest West Pause Ost Nordost Pause

Der Kommentar hinter dem [UNIT-Befehl] wird vom Programm in die Zugvorlage eingesetzt; hinter dem Namen der Einheit steht in \[ \], wie viele Personen in der Einheit sind und wieviel Geld sie dabei hat (hier also 4 Personen mit 100 Silber und 2 mit 243 Silber).

Vorsicht vor den Unterhaltskosten. Große Einheiten brauchen sehr viel Geld, und wenn sie es nicht haben, werden Leute verhungern. Es reicht, wenn in einer Region eine eigene Einheit genug Silber hat, um alle anderen Einheiten zu ernähren. Dabei sollte man Einheiten, die die Region verlassen, nicht vergessen!

In den ersten Runden kann man noch vom Startkapital leben, aber bald braucht man aber ein ständiges Einkommen. Dieser Schatz ist im Allgemeinen nach vier bis sechs Runden aufgebraucht. Einnahmen erwirtschaftet man am schnellsten mit Steuereintreibern und Unterhaltern, und der [Handel][2] mit Luxusgütern verspricht langfristig große Gewinne.

Plant die ersten Wochen vollständig durch. Man kann genau ausrechnen, wieviele Unterhalter, Steuereintreiber, Waffenbauer, Holzfäller ect. man ausheben kann und braucht.

Wenn das Spiel beginnt, sitzen manchmal Einheiten mehrerer Parteien eng benachbart zueinander. Sprecht euch ab und teilt eure Aufgaben auf, damit ihr euch möglichst effizient ausbreiten könnt. Pflegt Kontakt mit vielen Parteien, dies macht das Spiel spannend und es wird euch später helfen. Gerät man in Konflikte, ist es gut zu wissen, dass man nicht alleine dasteht. Kontakte erlauben euch einen Informationsaustausch, z.B. für Karteninformation; sie ermöglichen es, Erfahrungen und Tipps auszutauschen, und besonders das gegenseitige Lehren ist sehr hilfreich.

Um Kontakt mit den anderen Parteien aufzunehmen, beschafft euch die Liste der anderen Parteien in euren Regionen mit [OPTION] ADRESSEN und kontaktiert sie direkt. Verwendet den Befehl [MESSAGE] REGION, um die Mitspieler auf euch aufmerksam zu machen.

Um die Ziele zu erreichen, die ihr euch gesteckt habt, solltet ihr keine Ausgaben scheuen. Das Startkapital ist zur Investition gedacht. Der erste fördert im großen Stil Eisen, der zweite schmiedet Schwerter und der dritte bildet Kämpfer aus. Daneben könnt ihr euch schon eine Reihe weiterer Aufgaben stellen: Kartographieren, Magier-Ausbildung, Schiffbau, Burgenbau, Aufstellen einer Diebesgilde, Aufbau einer kleinen Handelskarawane mit Pferden und Wagen... Für diese Aufgaben könnt ihr wiederum ein paar kleine neue Einheiten erschaffen.

Kriege sollte man besonders in der Anfangsphase vermeiden - zu schnell sind wertvolle Einheiten weg, und die Einnahmen zu gering oder der Nachschub an Material versiegt.

Wenn ihr Kontakt zu einer mächtigen Partei habt, versucht, ihr etwas zu verkaufen. Versucht, Holz zu fällen, Steine zu brechen oder Eisen zu fördern. Es lohnt sich, zwei Burgen ausfindig zu machen oder selber zu bauen, um zwischen ihnen Handel zu treiben. Dafür braucht man Händler und Wagen. Kauft euch einen Wagen und zwei Pferde vom Burgherren oder baut selber einen.

Man muss mit Handelspartnern nicht alliiert sein. Verwendet den Befehl [CONTACT], um mit anderen Parteien Waren und Silber austauschen zu können, ohne alliiert zu sein.

Eine der wichtigsten Tabellen in dieser Anleitung ist die [Befehlsreihenfolge], also die Reihenfolge, in der die Befehle beim Server bearbeitet werden. Aus ihr ist ersichtlich, dass man z.B. eiem Waffenbauer durchaus noch in der selben Woche Rohstoffe geben kann, bevor er produziert ([GIVE] kommt an Position 14, [MAKE] an Position 22), man aber keine Tränke übergeben und dann sofort benutzen kann ([USE] ist an Stelle 7).

Es gibt keine Gewinner in diesem Spiel. Das Spiel dauert so lange, bis ihr an euch selber verzweifelt oder eure Feinde euch ausgerottet haben. Danach müsst ihr, falls die Spielleitung das zulässt, als neue Partei anfangen.

Und denkt immer dran: das Spiel ist ein Spiel! Es soll allen Spaß machen. Lasst euch nicht ärgern und zu unüberlegten Dingen hinreißen - wahrscheinlich ist der Spieler der fiesen und gemeinen Orks eigentlich ein netter Mensch...

## See also

- [Tipps und Tricks]
- [Hinweise]
- [Der erste Zug]
- [Grundlagen]

Continue reading: [Xontormia-Express].

[Xontormia-Express]: ./xontormia-express.md "Xontormia-Express"

<!-- From [https://wiki.eressea.de/index.php?title=Anfängertipps&oldid=17013] -->

[Passwort]: ./cmd-password.md "PASSWORD"
[1]: https://discord.gg/JyAeYJw%7CDiscord
[PbEm-Spiele-Forum]: http://www.pbem-spiele.de/
[Magellan]: ./magellan.md "Magellan"
[ECheck]: ./echeck.md "ECheck"
[Zugvorlage]: ./commands.md "Orders"
[Unterhaltung]: ./cmd-entertain.md "ENTERTAIN"
[Steuereintreiber]: ./cmd-tax.md "TAX"
[Bergbau]: ./resources.md#about-mining "Rohstoffe"
[Holzfällen]: ./resources.md#deep-in-the-forest "Rohstoffe"
[Steuereintreiben]: ./skills.md#arbeiten.2c-unterhaltung.2c-steuern-und-handel "Talente"
[Waffentalente]: ./skills.md#waffentalente-und-ausdauer "Talente"
[Wahrnehmung]: ./camouflage.md "Wahrnehmung"
[Diebstahl]: ./silver.md#diebstahl:-der-unehrliche-weg "Geld"
[Burgen]: ./castles.md "Burg"
[Burgenbau]: ./buildings.md "Gebäude"
[Handel]: ./silver.md#trade "Geld"
[Pferde und ggf. Wägen]: ./travel.md#pferd-und-wagen "Reisen"
[Taktiker]: ./tactic.md "Taktik"
[Alchemisten]: ./skills-list.md "Liste der Talente"
[Magier]: ./magic.md "Magie"
[UNIT-Befehl]: ./cmd-unit.md "UNIT"
[2]: ./silver.md#trade "Handel"
[OPTION]: ./cmd-option.md "OPTION"
[MESSAGE]: ./cmd-message.md "MESSAGE"
[CONTACT]: ./cmd-contact.md "CONTACT"
[Befehlsreihenfolge]: ./commands-sequence.md "Befehlsreihenfolge"
[GIVE]: ./cmd-give.md "GIVE"
[MAKE]: ./cmd-make.md "MAKE"
[USE]: ./cmd-use.md "USE"
[Tipps und Tricks]: ./tips-and-tricks.md "Tipps und Tricks"
[Hinweise]: ./hints.md "Hinweise"
[Der erste Zug]: ./first-round.md "Der erste Zug"
[Grundlagen]: ./basics.md "Grundlagen"
