---
# cSpell:locale de
alias: bef-tarne
---
# TARNE

**`TARNE`**`[`*`stufe`*`]`
**`TARNE`**`PARTEI [NICHT]`
**`TARNE`**`PARTEI NUMMER [`*`nummer`*`]`
**`TARNE`**` `*`rasse`*

Mit der ersten Variante kann man einstellen, wie "intensiv" eine Einheit sich zu tarnen versucht. `stufe` kann natürlich nicht höher als das [Talent] der Einheit sein. Ohne Parameterangabe wird das Maximum gesetzt.

Mit `TARNE PARTEI` kann man seine Parteizugehörigkeit zu verbergen versuchen. Die Parteizugehörigkeit wird für andere Spieler dann als "anonym" angezeigt. Im Gegensatz zum normalen Tarnung/Wahrnehmungs-Mechanismus kann man die Parteizugehörigkeit einer solchen Einheit nur noch mit [Spionage] erkennen. Mit `TARNE PARTEI NICHT` wird diese Anonymisierung wieder aufgehoben und andere Spieler sehen die korrekte Parteizugehörigkeit - so sie denn über ausreichend Wahrnehmung verfügen und die Einheit überhaupt in ihrem Report erspähen.

`TARNE PARTEI NUMMER nummer` tarnt die Einheit mit der angegebenen Parteinummer, sie kann sich also als einer beliebigen anderen Partei zugehörig tarnen. Es gibt keinen einfachen Weg, diese Form der Tarnung zu durchschauen. Um wieder der eigenen Partei zugehörig zu erscheinen, muß für `nummer` die eigene Parteinummer verwendet werden. Die angegebene Partei muss der Partei, welche den Befehl gibt, bekannt sein, d.h. in deren Report auftauchen, ansonsten schlägt der Befehl fehl. Parteien, die von der Partei oder Gruppe der Einheit [HELFE xyz PARTEITARNUNG] bekommen, können die wahre Parteizugehörigkeit der Einheit sehen.

Soweit, so einfach. Diese Tarnung bringt jedoch ein paar Besonderheiten mit sich, die hier in loser Reihenfolge aufgezählt werden:

- Die (scheinbare) Rasse der Einheit ändert sich dadurch nicht, ein Goblin bleibt ein Goblin, auch wenn er sich als der Partei der Lichtelfen zugehörig ausgibt.
- Die Einheiten ändern ihr Verhalten durch die Tarnung nicht. Sie spenden z.B. kein Silber an die Verbündeten der Partei, als die sie sich tarnen. Wer also die Tarnung perfektionieren will, sollte mit den Einheiten eine Gruppe bilden und für diese Gruppe entsprechende Helfe-Stati setzen.  
  So getarnte Einheiten können auch nicht plötzlich Gebäude oder Schiffe betreten, die sie ansonsten nicht betreten dürfen, oder Steuern eintreiben, wo ihnen das normalerweise untersagt ist.
- Im Kampf bilden derartige Einheiten ein eigenes Heer. Beispiel: Es gibt drei Parteien, die Waldelfen, die Flusselfen und die Eisenzwerge. Alle Parteien habe jeweils eine Einheit: Waldelf, Flusself und Eisenzwerg. Während Waldelf sich als Flusself tarnt, behalten alle anderen Einheiten ihre wahre Identität bei.  
  Nun greift der Eisenzwerg den Flusself an. Dadurch erscheinen im Kampfreport drei Heere: Die Eisenzwerge, und zwei Flusselfen-Heere.

[[bef-gruppe]] hat allerdings auch die Nebenwirkung mit den mehreren Heeren. Auf diese Weise kann man also nicht sehen ob Einheiten sich als eine fremde Partei ausgeben oder ob der Betreffende nur mehrere Gruppen hat.

Mit `TARNE rasse` können [Dämonen] sich als andere Rasse tarnen.

## Siehe auch

- [Tarnung][Talent]
- [Wahrnehmung]

<!-- From [https://wiki.eressea.de/index.php?title=TARNE&oldid=15791] -->

[Talent]: ./camouflage.md "Tarnung"
[Spionage]: ./skills-list.md "Liste der Talente"
[HELFE xyz PARTEITARNUNG]: ./cmd-help.md "HELFE"
[bef-gruppe]: ./cmd-group.md "GRUPPE"
[Dämonen]: ./races.md#daemonen "Dämonen"
[Wahrnehmung]: ./camouflage.md "Wahrnehmung"
