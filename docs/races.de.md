---
alias: rassen
---
# Rassen

Neben den Menschen gibt es in Eressea noch viele andere Rassen (Parteitypen), unter denen du wählen kannst. Jede Rasse hat gewisse Vor- und Nachteile, die sich durch [Boni bzw. Mali] in einigen Talenten äußern und manchmal gewisse andere spezielle Fähigkeiten; außerdem hat jede Rasse verschiedene [Rekrutierungskosten][Boni bzw. Mali]. Eine Person wiegt in der Regel 10 Gewichtseinheit (GE) und kann 5,4 GE tragen. Ausnahmen sind Trolle, Goblins und verschiedene Monster.

Zu Anfang des Spiels musst du dir eine Rasse aussuchen, die du fortan spielen willst. Diese Rasse wird bei der Anmeldung angegeben und kann danach nicht mehr geändert werden. Die Auswahl sollte also gut überdacht werden.

Einen schnellen Überblick gibt es in der [Tabelle rassenspezifischer Vor- und Nachteile][Boni bzw. Mali].

## Dämonen

Dämonen sind grausam und unberechenbar. Sie fressen die Bauern der Umgebung und überraschen immer wieder mit neuen Fähigkeiten oder deren Verlust.

**Achtung!** Dämonen sind denkbar ungeeignet für unerfahrene Eressea-Spieler!

- Alle Talente, in denen sie mindestens Talentstufe 1 haben (vor Rassenmalus), verschieben sich mit einer Wahrscheinlichkeit von 25% um bis zu 3 Lernwochen nach oben (mit 60% Chance) oder unten (mit 40% Chance; das Talent steigt oder sinkt also, nicht beides). Die Verschiebung erfolgt nach den langen Befehlen und der Bewegung. Negative Talentwerte entstehen dabei nicht; ein Talent kann nicht unter 0 fallen.
- Dämonen fressen jede Runde Bauern. Ein Bauer ernährt zehn Dämonen, und Dämonen, die keine Nahrung bekommen, verlieren Trefferpunkte und unterliegen der Talenthalbierung nach der normalen [Hungerregel].
- [Rekrutierte] Dämonen werden nicht vom Bauernpool abgezogen. Aus spieltechnischen Gründen gilt aber trotzdem das Rekrutierungslimit.
- Gibt man Dämonen mit [`GIB 0`] an die Bauern, kehren diese in ihre Heimatsphäre zurück, sie werden nicht zu Bauern.
- Dämonen können sich als eine andere Rasse [tarnen].
- Im Nahkampf bewirkt jeder Treffer eines Dämons bei einem Gegner eine "1-Personen-Panik": die betroffene Person hat -1 auf ihr Kampftalent.
- Verwundete Dämonen regenerieren sich mit 7,5% ihrer Trefferpunkte.

## Elfen

Elfen sind ein geradezu magisches Volk. Schwere Arbeiten sind nicht unbedingt ihre Stärke, dafür umso mehr die Magie der Natur und des Verborgenen, sowie ihre Bogenschützen.

- Jeder Elf in der Region (bis zu maximal 1/8 der [Regionskapazität] für Bauern, das entspricht z.B. bis zu 250 Elfen in einem Sumpf) erhöht die Chance eines Baums, in einer Sommer- oder Herbstwoche einen Samen abzuwerfen. Das kann je nach Anzahl der Elfen einen ganz deutlichen Unterschied ausmachen.
- Elfen haben in Wäldern zusätzlich Tarnung und Wahrnehmung +1 und Taktik +2.
- Elfen dürfen sechs (statt fünf) [Magier] besitzen.
- Elfenmagier regenerieren Aura 25% schneller
- Elfen machen mit Bögen einen Schadenspunkt mehr.
- Nur Elfen können [Elfenbögen] bauen.

## Goblins

Goblins sind alleine klein und schwach; sie verlassen sich lieber auf List oder Überzahl. Bei ihnen gilt: "Masse statt Klasse."

- Wenn sie mit mindestens zehnfacher Übermacht angreifen, erhalten sie Angriffsbonus von +1 auf ihre Attacken.
- Goblins sind mit 6 GE leichter als andere Rassen, dafür ist aber auch ihre Tragekapazität von 4,4 GE geringer.
- Wenn Goblins mit einem Tarnungstalent von mindestens 4 [klauen], bekommen sie mindestens 50 Silber, selbst dann, wenn sie erwischt werden.
- Unbewaffnete Goblins haben nicht den üblichen Malus von -2 auf ihre Verteidigung.
- Verwundete Goblins regenerieren sich mit 10% ihrer Trefferpunkte.

## Halblinge

Halblinge sind kleine Gesellen mit haarigen Füßen. Sie sind gute Händler und verstehen es, die Bauern zu unterhalten. Sie sind gute Baumeister, Pferde und [Schiffe] überlassen sie aber lieber anderen. Der Umgang mit Waffen zählt nicht gerade zu ihren Stärken.

- Halblinge, die in einem Kampf versuchen zu [fliehen], haben dabei eine Grundchance von 50% (alle anderen Rassen 25%). Die maximale Chance ist bei ihnen 90% (sonst 75%, siehe [`KÄMPFE FLIEHE`]).
- Halblinge haben einen Angriffs- und Schadens-Bonus von je +5 im Kampf gegen [Drachen].
- Halblinge nehmen durch Hungern mehr Schaden als andere Rassen. (Zwischen 8 und 17 Punkten (1d10+7) Schaden.)

## Insekten

Insekten leben in einem streng organisiertem Staat. Sie hassen die Kälte und fühlen sich in feuchten oder heißen Gegenden am wohlsten. Ihr harter Panzer schützt sie vor so manchen Übergriffen.

Insekten sind nicht sehr geeignet für unerfahrene Eressea-Spieler!

- Insekten mögen Wärme und Feuchtigkeit und hassen die Kälte: In Wüsten und Sümpfen haben sie +1 auf alle Talente, in denen sie wenigstens Talent 1 haben, in Gebirgen und Gletschern -1.
- Insekten können Gletscher nicht betreten und dort auch nicht rekrutiert werden, es ist ihnen zu kalt. Insekten, welche trotzdem in einen Gletscher gelangen, verlieren Trefferpunkte und unterliegen der Talenthalbierung nach der normalen [Hungerregel].
- Insekten können in den Wintermonaten Herdfeuer, Eiswind und Schneebann nur in Wüsten rekrutieren. Es kann allerdings durch [Alchemie] ein [Trank] (Nestwärme) hergestellt werden, der die Rekrutierung in anderem Terrain möglich macht.
- Insekten sind automatisch durch ihren Chitinpanzer geschützt. Diese Rüstung wirkt zur Hälfte additiv zu einer Rüstung, die Insekten tragen (siehe [hier]).
- Insekten bekommen einen [Taktik]-Bonus, wenn sie in Massen auftreten. Ein Insektentaktiker bekommt einen Bonus von (log<sub>10</sub> (Anzahl der Kämpfer in seinem Heer)) - 1 auf Taktik. Das kann bei sehr wenigen Kämpfern auch einen Malus ergeben! Außerdem sind Einheiten aus verschiedenen [Gruppen] in der Regel in verschiedenen Heeren!
- Insekten können in Wüsten und Sümpfen auch ohne Burgen [handeln].

## Katzen

Die Katzen zählen kaum zu den Handwerkern. Ihre feinen Sinne und ihre Geschmeidigkeit helfen jedoch bei einigen Dingen, die andere erst mühsam erlernen müssen.

- "Sieben Leben": Katzen überleben einen ansonsten tödlichen Treffer mit 1/7 Wahrscheinlichkeit; sie haben dann wieder volle Trefferpunkte.
- Katzen benutzen keine Plattenpanzer.
- Ihre Gewandtheit verleiht Katzen einen Bonus von +1 auf Verteidigung

## Meermenschen

Meermenschen sind im Wasser zu Hause, im Gebirge fühlen sie sich dagegen unwohl. Schiffe bauen und bedienen sie so leicht, als seien es Bauklötzchen, während ihnen andere Arbeiten nicht ganz so leicht fallen.

- Alle Schiffe mit Meermenschen-Kapitän einer Meermenschen-Partei können sich ein Feld weiter [bewegen].
- Meermenschen können auch auf Schiffen [lange Befehle] ausführen. Achtung, dies hat einige implizite Folgen: Meermenschen können sich z.B. von einer an eine Landregion angrenzende Ozeanregion auf die Landregion begeben, siehe [Anschwimmen].
- Bis zu 100 Meermenschen pro Ozeanfeld können auf hoher See mit dem Befehl [[bef-arbeite]] je 10 Silber verdienen.

## Menschen

Menschen können alles ein bisschen, nichts so richtig schlecht aber auch nichts so richtig gut. Deshalb können sie die Schwächen ihrer Verbündeten oft ausgleichen und sind überall zu finden.

- Eine Menschenpartei kann einige Personen anderer Rassen haben, so genannte *Migranten*. Ein Mischen von verschiedenen Rassen in einer Einheit ist aber nicht möglich. Diese Personen kann die Partei nicht selber rekrutieren, sondern muss sie sich von anderen Parteien der entsprechenden Rassen [geben lassen][`GIB 0`]. Es gibt keine Migranten mit [teuren Talenten], also Magie, Alchemie, Kräuterkunde, Spionage und Taktik.

Die Anzahl der *Migranten* errechnet sich als 20 × log<sub>10</sub> (Parteigröße ÷ 50). Hat man durch eine Katastrophe oder Kampf plötzlich zu viele Migranten, werden diese nicht entfernt, man kann nur keine neuen mehr aufnehmen. Die Maximalzahl an Migranten wird im Report angezeigt und ist für größere Parteien fast identisch zur Zahl der [Helden]. Die folgende Tabelle enthält einige Beispiele:

Migranten

|                        |   |    |    |    |    |    |    |     |     |      |      |       |        |         |
|------------------------|---|----|----|----|----|----|----|-----|-----|------|------|-------|--------|---------|
| Personen in der Partei | 1 | 56 | 57 | 63 | 71 | 80 | 89 | 159 | 500 | 1000 | 5000 | 50000 | 500000 | 5000000 |
| Migranten              | 0 | 0  | 1  | 2  | 3  | 4  | 5  | 10  | 20  | 26   | 40   | 60    | 80     | 100     |

## Orks

Orks sind ein recht kämpferisches Volk; schon in der Kindergrube wissen sie mit einer Waffe umzugehen. Kontakte zu anderen Völkern haben sie am liebsten mit dreifacher Übermacht.

- Neu rekrutierte Orks starten mit je Talentstufe 1 in Hiebwaffen und Stangenwaffen.
- Orks verdienen mit [[bef-arbeite]] weniger als andere Rassen.
- Rekrutierte Orks werden - ähnlich dem zwergischen Eisenbonus - nur zu 50% von den Regionsbauern abgezogen. Ein rekrutierter Ork wird deshalb nur zur Hälfte vom Rekrutierungslimit der Region abgezogen. Es wird aufgerundet.
- Analog gilt: Gibt man Orks mit [`GIB 0`] an die Bauern, so werden sie nur zur Hälfte zu den Bauern addiert. Hierbei wird allerdings abgerundet.
- Unbewaffnete Orks kämpfen im Nahkampf nicht wie andere Rassen mit -2, sondern mit (bestes Nahkampftalent - 3). Zum Steuereintreiben benötigen sie trotzdem Waffen.
- Orks sind langsame Denker und lernen generell alle Nicht-Waffentalente etwas langsamer als andere Rassen.

## Trolle

Trolle stapfen wandelnden Felsbrocken gleich unübersehbar durch die Lande. Mit Steinen können sie mit ihren riesigen Kräften perfekt umgehen, dafür aber umso weniger mit Pferden, und auch das Schwimmen ist nicht ihre Meisterdisziplin.

- Trolle sind stark und können doppelt soviel tragen wie andere (10,8 GE), wiegen aber auch doppelt soviel (20 GE).
- Es gibt keine Troll-Kavallerie, d.h. Trolle erhalten keinen Pferdebonus. Auf den Warentransport und die Bewegungsgeschwindigkeit berittener Trolle hat das keine Auswirkungen.
- Von Trollen [abgebaute Steine] werden nur zu 75% vom "Regionsvorrat" abgezogen. Dieser Effekt ist kumulativ zu einem [Steinbruch].
- Gegen Trolle hat Kavallerie nur einen Bonus von +1.
- Trolle sind als einzige Rasse dazu in der Lage, Wagen ohne Pferde zu benutzen. Je vier Trolle können einen Wagen ziehen, sich allerdings auch nur eine Region (ohne Straße) bewegen. Genauer wird das beim Befehl [[bef-fahre]] erklärt.
- Unbewaffnete Trolle machen 2 bis 6 Trefferpunkte Schaden.
- Verwundete Trolle regenerieren sich mit 7,5% ihrer Trefferpunkte.

## Zwerge

Zwerge leben in den Bergen. Ihre Schmiedekünste sind viel gerühmt, ihre Bauten weltbekannt. Magie ist ihnen ein Gräuel, Pferde nicht ganz geheuer und auch das Wasser ist nicht gerade ihr Element.

- Von Zwergen abgebautes Eisen wird nur zu 60% vom "Regionsvorrat" abgezogen. Dieser Effekt ist kumulativ zu einem Bergwerk (siehe [hier][11] und [hier][abgebaute Steine]).
- Zwerge haben im Gebirge in Gletschern und in Eisbergen +1 auf [Taktik].
- [Zwergenmagier][Magier] regenerieren Aura 50% langsamer.

Weiterlesen: [Talentmodifikatoren].

[Talentmodifikatoren]: ./skills-modifiers.md "Talentmodifikatoren"

<!-- From [https://wiki.eressea.de/index.php?title=Rassen&oldid=16044] -->

[Boni bzw. Mali]: ./skills-modifiers.md "Talentmodifikatoren"
[Hungerregel]: ./silver.md#hunger "Hunger"
[Rekrutierte]: ./silver.md#ausgaben#rekrutieren "Ausgaben"
[`GIB 0`]: ./cmd-give.md "GIB"
[tarnen]: ./cmd-hide.md "TARNE"
[Regionskapazität]: ./world.md "Welt"
[Magier]: ./magic.md "Magic"
[Elfenbögen]: ./war-tables.md#waffeneigenschaften "Kriegstabellen"
[klauen]: ./cmd-steal.md "BEKLAUE"
[Schiffe]: ./ships.md "Schiff"
[fliehen]: ./war.md#die-flucht "Krieg"
[`KÄMPFE FLIEHE`]: ./cmd-combat.md "KÄMPFE"
[Drachen]: ./monsters.md#drachen "Drachen"
[Alchemie]: ./skills-list.md "Liste der Talente"
[Trank]: ./alchemy.md "Tränke"
[hier]: ./war-tables.md#rasseneigenschaften "Kriegstabellen"
[Taktik]: ./tactic.md "Taktik"
[Gruppen]: ./cmd-group.md "Gruppen (to be documented)"
[handeln]: ./silver.md#handel "Geld"
[bewegen]: ./travel.md "Reisen"
[lange Befehle]: ./commands.md "Befehl"
[Anschwimmen]: ./travel.md#anschwimmen "Schiffsreisen"
[bef-arbeite]: ./cmd-work.md "ARBEITE"
[teuren Talenten]: ./skills.md "Talente"
[Helden]: ./cmd-promote.md "BEFÖRDERE"
[abgebaute Steine]: ./resources.md#vom-bergbau "Rohstoffe"
[Steinbruch]: ./buildings-others.md#steinbruch "Andere Gebäude"
[bef-fahre]: ./cmd-ride.md "FAHRE"
[11]: ./buildings-others.md#bergwerk "Andere Gebäude"
