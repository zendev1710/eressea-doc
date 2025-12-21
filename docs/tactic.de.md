---
# cSpell:locale de
alias: taktik
---
# Taktik

Vor der Schlacht wird der beste Taktiker aller teilnehmenden Einheiten bestimmt. Die Seite mit den besten Taktiker gewinnt die sogenannte "Taktikerrunde": in einem geschickten Manöver lockt er die Feinde in einen Hinterhalt und seine Verbündeten können vor der ersten Kampfrunde überraschend mit einer bestimmten Chance zuschlagen, ohne dass der Feind in dieser Runde auch angreifen kann. Sind zwei oder mehr Taktiker verschiedener Seiten gleich gut, so können alle davon in der Taktikerrunde zuschlagen. Die Chance, diesen Schlag zu machen, beträgt 10% für jeden Talentpunkt Unterschied zwischen dem besten eigenen Taktiker und dem besten Taktiker der Gegenseite, jeweils inklusive Boni oder Mali. Ab einem Talentunterschied von 10 schlagen alle Verbündeten einmal zu. Für das Nachladen zählt die Taktikerrunde auch, eine Armbrust die in der Taktikerrunde geschossen hat schießt also in Runde 3 anstelle von Runde 4 das zweite Mal. Die Taktikerrunde erlaubt auch einen zusätzlichen Fluchtversuch.

## Situationsabhängige Boni auf Taktik

Ein Taktiker, der in der ersten Reihe [[cmd-combat|kämpft]], bekommt einen Bonus von +1 auf sein Taktik-Talent. Steht er in der 3. oder 4. Reihe, reduziert sich sein Talent um 1.

Auf das Talent Taktik gibt es auch einige Rassenboni die vom Terrain abhängig sind:

| Rasse  | Terrain         | Bonus/Malus |
|--------|-----------------|-------------|
| Elf    | Wald            | +2          |
| Zwerg  | Berg, Gletscher | +1          |
| Insekt | Sumpf, Wüste    | +1          |
|        | Berg, Gletscher | \-1         |

Insekten bekommen zudem einen zusätzlichen Bonus auf das Talent Taktik, wenn sie in Massen auftreten. Ein Insektentaktiker bekommt einen Bonus von log10(Anzahl der Kämpfer in seinem Heer)-1 auf Taktik. Das kann bei sehr wenigen Kämpfern auch einen Malus ergeben! Wichtig: Es zählen wirklich nur die Kämpfer in seinem Heer. Unterschiedliche Gruppen sollte man also vermeiden und die Truppen der Bündnispartner zählen auch nicht.

| Anzahl Kämpfer | 1-9 | 10-99 | 100-999 | 1000-9.999 | 10.000-99.999 | 100.000-999.999 | ... |
|----------------|-----|-------|---------|------------|---------------|-----------------|-----|
| Massenbonus    | \-1 | 0     | +1      | +2         | +3            | +4              | ... |

## Tagesform

Um ein wenig "Tagesform" und Glück einfließen zu lassen, erhält jeder Taktiker einen zufälligen Bonus, der bei 0 startet und sehr groß werden kann, wobei die Wahrscheinlichkeit dafür immer geringer wird, je größer der Bonus ist. Besteht eine Taktiker-Einheit aus mehreren Personen, so wird für jede Person einmal gewürfelt.

| Wahrscheinlichkeit | Bonus | Sonstiges       |
|--------------------|-------|-----------------|
| 40%                | +0    |                 |
| 30%                | +1    |                 |
| 20%                | +2    |                 |
| 7%                 | +3    |                 |
| 3%                 | +3    | nochmal würfeln |

Daraus ergeben sich je nach Taktikeranzahl folgende mittleren Tagesform-Boni:

| Anzahl Taktiker |  1   |  3   |  12  |  44  | 129  | 410  | 1480 |
|-----------------|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| Mittlerer Bonus | 1,03 | 1,96 | 3,05 | 4,03 | 5,03 | 6,03 | 7,03 |

Das bedeutet 12 Taktiker Stufe X erreichen im Mittel die gleiche Stufe wie ein Taktiker Stufe X+2. Man kann also (auch) bei Taktikern fehlende Klasse durch Masse ersetzen, allerdings wird es relativ schnell sehr teuer.

## Siehe auch

- [Vom Kriege]

<!-- From [https://wiki.eressea.de/index.php?title=Taktik&oldid=9946] -->

[Vom Kriege]: ./war.md#die-taktikerrunde "Kampf"
