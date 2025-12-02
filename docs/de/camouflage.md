# Tarnung

Mit dem [Talent] **Tarnung** kann man sich vor anderen Einheiten tarnen. [Bewacht] eine Einheit allerdings die Region oder befindet sie sich auf einem Schiff oder in einem Gebäude, ist sie immer sichtbar.

## Gegenmaßnahmen

Getarnte Einheiten kann man mit dem Talent *Wahrnehmung* entdecken. Ist das beste Wahrnehmungstalent deiner Partei in der Region kleiner als das Tarnungstalent einer fremden Einheit, erscheint die getarnte Einheit nicht in der Auswertung - sie wird unsichtbar. Sind Wahrnehmungstalent und Tarnungstalent gleich groß, so erscheint die getarnte Einheit in der Auswertung. Dies ist die Ausgangslage wenn man das Spiel beginnt, da alle neuen Einheiten Tarnung und Wahrnehmung auf Stufe 0 haben.

## Bewachen unterlaufen

Für erfolgreich getarnte Einheiten zählen die Restriktionen von [BEWACHE][Bewacht] nicht. Sie können somit Steuern eintreiben, Ressourcen abbauen, Straßen zerstören und Bauern rekrutieren.

## Fluchtchance erhöhen

Die Standardfluchtchance einer Einheit im [Kampf] beträgt 25% (Halblinge 50%). Mit jeder Stufe Tarnung steigt die Fluchtchance der Einheit um 5%. Ein Pferd steigert die Fluchtchance einer Person einmalig um 10% (5 Pferde bringen einer Person also NICHT +50% sondern nur +10), dabei ist es nicht relevant ob die Einheit reiten kann. Die maximale Fluchtchance beträgt 75% (Halblinge 90%).

## Diebstahl von Silber

Erfolgreiche Tarner können anderen Einheiten mit dem Befehl [`BEKLAUE`] Silber stehlen. Auch hier zählt das höchste Wahrnehmungstalent der beklauten Partei in der Region. Pro Talentstufe Unterschied klaut jede klauende Person 50 Silber. Hierbei wird **immer** aus dem gesamten Silberpool der Partei in der Region gestohlen. Die bestohlene Partei erhält eine Meldung, dass sie bestohlen wurde, aber nicht, von wem. Ist das Tarnungstalent nur gleich gut wie die Wahrnehmung, klappt der Diebstahl nicht, und die bestohlene Partei erhält eine anonyme Meldung über den Versuch. Ist die Tarnung zu schlecht, bekommt die Partei, die bestohlen werden sollte, eine Meldung mit dem Namen der Diebe.

Goblins klauen, sofern sie Tarnung bis mindestens Stufe 4 gelernt haben, immer mindestens 50 Silber, auch wenn ihre Tarnung unter dem Wahrnehmungstalent liegt. Solcher Diebstahl fällt natürlich auf und ist daher nur unter bestimmten Umständen sinnvoll. Man hört, Goblinarmeen haben dem Gegner schon durch Nahrungsentzug den entscheidenden Schlag versetzt.

Rechnet man damit, erfolgreich beklaut zu werden, hilft es nur, Silber in die betroffene Region zu schaffen, da selbst die Einnahmen aus Unterhaltung, Steuereintreiben, Arbeiten und Handel von den Dieben geklaut werden können.

Diebstahl stellt hin und wieder eine effektive Möglichkeit dar, Spione zur Strecke zu bringen, die ihrerseits gut getarnt sind, da diese bei Angriffen durch ihre hohe Tarnung eine hohe Fluchtchance haben.

## Spionage

Gibt eine Einheit mit dem Talent [Spionage] den Befehl [`SPIONIERE`*`einheit-nr`*], wird ihr Spionagetalent mit dem Wert der Tarnung der Zieleinheit verglichen. Die Grundchance für einen erfolgreichen Spionageversuch ist 10%. Für jede Talentstufe, die das Spionagetalent das Tarnungstalent des Opfers übersteigt, erhöht sich dieses um 5%. Ein hohes Tarnungstalent hilft also der Einheit einen erfolgreichen Spionageversuch zu erschweren. Um eine Erfolgschance von 50% zu erreichen muss der Spion 8 Stufen besser sein. Lernt man nun wenigstens Tarnung 2 braucht der Spion überproportional länger um die 8 Stufen zu erreichen.

Ist der Spionageversuch erfolgreich, erfährt der Spion den Kampfstatus, die Gegenstände im Besitz der Einheit und die Talente. Die Parteizugehörigkeit kann zusätzlich ermittelt werden, wenn das Spionagetalent mindestens 6 Talentstufen über dem Tarnungstalent der Einheit liegt. Eine hohe Tarnung ist also sinnvoll für eine gelungene Parteitarnung.

Anschließend wird - unabhängig vom Erfolg - gewürfelt, ob der Spionageversuch bemerkt wurde. Die Wahrscheinlichkeit dafür ist (100 − SpionageSpion \* 5 + WahrnehmungOpfer \* 2)%.

## Einschätzung

Viele Völker lagern ihre Waren bei einer sehr gut getarnten Einheit pro Region ([Kampfstatus][]: `KÄMPFE NICHT` oder `FLIEHE`). Die Gegenstände sind so vor einer Vielzahl von Gefahren geschützt, solange kein gegnerischer Wahrnehmer den Tarner auffliegen lässt.

Neben diesen passiven Anwendungen von Tarnung kann man natürlich mit gut ausgebildeten Tarnern auf Informationsbeschaffung gehen oder die Möglichkeit des Diebstahls nutzen.

## Siehe auch

- [BEWACHE][Bewacht]
- [Einnahmen]

|              |          |
|--------------|----------|
| Weiterlesen: | [Reisen] |

[Reisen]: ./travel.md "Reisen"

<!-- From [https://wiki.eressea.de/index.php?title=Tarnung&oldid=17029] -->

[Talent]: ./skills.md "Talente"
[Bewacht]: ./cmd-guard.md "BEWACHE"
[Kampf]: ./war.md#die-flucht "Krieg"
[`BEKLAUE`]: ./cmd-steal.md "BEKLAUE"
[Spionage]: ./skills-list#spionage "Spionage"
[Kampfstatus]: ./cmd-combat.md "KÄMPFE"
[Einnahmen]: ./silver.md#diebstahl-der-unehrliche-weg "Einnahmen"
