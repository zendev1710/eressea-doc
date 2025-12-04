# MACHE

**`MACHE`**[<sup>`L`</sup>]`[`*`anzahl`*`]`*`gegenstand`*  
**`MACHE`**[<sup>`L`</sup>]`[`*`anzahl`*`] KRÄUTER`  
**`MACHE TEMP`**` `*`unit-alias-nr`*`["`*`name`*`"]`  
**`MACHE`**[<sup>`L`</sup>]`[`*`stufen`*`]`*`gebäudetyp`*`[`*`gebäude-nr`*`]`  
**`MACHE`**[<sup>`L`</sup>]`[`*`stufen`*`]`*`schiffstyp`*  
**`MACHE`**[<sup>`L`</sup>]`[`*`stufen`*`] SCHIFF [`*`schiff-nr`*`]`  
**`MACHE`**[<sup>`L`</sup>]`[`*`stufen`*`] STRASSE`*`richtung`*` `

Der Befehl `MACHE` ist der allgemeine Produktionsbefehl. Mehr dazu auch im Kapitel [Produktion].

## Gegenstände

[Gegenstände] und [Rohstoffe] werden mit `MACHE [`*`anzahl`*`]`*`gegenstand`*` ` hergestellt. Je nach Gegenstand wird ein bestimmtes Talent und vielleicht auch noch bestimmte Rohstoffe benötigt. Ohne Angabe von *anzahl* wird die Einheit so viele Gegenstände produzieren, wie Personen, Talent und evtl. Rohstoffe es ihr ermöglichen.

### Tränke

Das Herstellen eines Trankes ist sehr aufwendig und kann nur von besonders talentierten Alchemisten durchgeführt werden. Details dazu findest du im [Alchemie-Kapitel].

### Kräuter

Kräuter werden mit dem Befehl `MACHE KRÄUTER` von Einheiten mit dem Talent [Kräuterkunde] hergestellt. Details dazu im Kapitel über [Kräuter].

## Einheiten

Wenn du eine neue Einheit erschaffst (`MACHE TEMP xy`), gibst du der Einheit eine Alias-Nummer, denn du weißt ja zu diesem Zeitpunkt noch nicht, welche Nummer für die Einheit schlussendlich noch frei sein wird. Für alle anderen Befehle kannst du nun diesen Alias verwenden (mit dem Wort TEMP davor, zum Beispiel `GIB TEMP xy 100 Silber`). Bei der Suche nach einer TEMP-Einheit wird erst in der eigenen Partei gesucht, dann in fremden Parteien. Wenn also du und eine andere Partei eine Einheit mit der ID *TEMP xy* haben, wird deine eigene Einheit gewählt. Mit ein wenig Absprache können also auch TEMP-Einheiten fremder Parteien angesprochen werden.

Die Alias-Nummer wird als Nummer der Einheit benutzt, wenn diese noch nicht belegt ist. Ebenso kannst du schon hier einen Namen der Einheit angeben. So lassen sich die Befehle

     MACHE TEMP 1
        BENENNE EINHEIT "Clowns"
        NUMMER EINHEIT lach

verkürzen auf

     MACHE TEMP lach "Clowns"

Pro Partei sind maximal 2500 Einheiten erlaubt. Hat die Partei 2500 oder mehr Einheiten, so können mit `MACHE TEMP` keine neuen Einheiten geschaffen werden, es müssen erst andere Einheiten z.B. durch Zusammenfassen gelöscht werden. Da das Auflösen leerer Einheiten in der Befehlsreihenfolge weit hinten kommt, können neue TEMP-Einheiten erst in der folgenden Woche geschaffen werden.

Nach diesem Befehl werden die Befehle für die neue Einheit angegeben, bis der Befehl ENDE folgt.

Die neue Einheit muss allerdings noch Mitglieder bekommen, sonst wird sie stillschweigend am Ende der Runde wieder gelöscht! Sie muss also rekrutieren oder Personen übergeben bekommen. Wenn die neue Einheit Mitglieder neu rekrutieren soll, muss sie auch genug Geld dafür erhalten. Erhält sie das nicht, wird die Einheit niemanden rekrutieren können und am Ende der Woche stillschweigend entfernt werden. Bekommt die Einheit Geld, rekrutiert aber keine Mitglieder, löst sie sich ebenfalls auf und das Geld fällt [wieder einer Einheit der eigenen Partei zu].

     EINHEIT 17;       Kämpfer [15,700$]
     MACHE TEMP 1
        BENENNE EINHEIT "Drachenreiter"
        LERNE Hiebwaffen
     ENDE
     GIB TEMP 1 5 PERSONEN
      
     GIB TEMP 2 100 Silber
     MACHE TEMP 2
        REKRUTIERE 1
        BENENNE EINHEIT "Späher"
        DEFAULT "LERNE Wahrnehmung"
        NACH Westen
     ENDE

## Gebäude

Um ein neues Gebäude zu errichten, verwendest du *`MACHE`*`[`*`stufen`*`]`*`Gebäudetyp`* (siehe [Gebäude]). Willst du an einem Gebäude weiterbauen, so lautet der Befehl dafür *`MACHE`*`[`*`stufen`*`]`*`Gebäudetyp`*` `*`gebäude-nr`*. Der *Gebäudetyp* kann beim Weiterbauen auch durch BURG ersetzt werden, auch wenn es sich um ein anderes Gebäude handelt. Burgen und viele andere Gebäude können beliebig ausgebaut werden. Um Burgen zu bauen, muss die Einheit das Talent Burgenbau und Steine haben, andere Gebäude erfordern i.d.R. weiterhin Holz, Eisen und Silber in verschiedenen Mengen.

## Schiffe

Mit `MACHE`*`schiffstyp`* beginnt eine Einheit, ein neues [Schiff] zu bauen. Dazu muss sie das Talent Schiffbau und Holz haben. Mit `MACHE [`*`stufe`*`] SCHIFF`*`schiff-nr`* kann sie daran weiterbauen. Schiffe können nicht wie Burgen erweitert werden, sondern der Typ wird bei Baubeginn festgelegt. An Schiffen kann nur bis zu der durch den Typ festgelegten Größe weiter gebaut werden.

Sowohl bei Gebäuden als auch bei Schiffen kannst du mit *stufen* angeben, wie viele Stufen du das Gebäude bzw. Schiff bauen / erweitern willst.

- erste Woche: `MACHE LANGBOOT`  
  Ein neues Schiff wird gebaut und bekommt vom Computer die Nummer 76.
- zweite Woche: `MACHE SCHIFF 76`  
  An Schiff Nr. 76 wird nun weiter gebaut.

## Straßen

Um in einer Region das Durchreisen durch Straßen und Brücken zu erleichtern, verwendest du `MACHE STRASSE`*`richtung`*. Um [Straßen] zu bauen, braucht die Einheit das Talent [Straßenbau] und [Steine][Gegenstände]. In Gletschern benötigt sie dazu vorher einen [Tunnel], in Wüsten eine [Karawanserei] und in Sümpfen einen [Damm]. Pro Talentpunkt Straßenbau wird ein Stein verbaut. Für jede gewünschte Richtung werden zwischen 50 und 250 Steine benötigt, abhängig von den [Geländearten]. Straßen funktionieren nur wenn sie vollständig sind.

Spielererfahrung: Solthar Außer beim Neubau eines Gebäudes kannst du derzeit bei MACHE gebäudetyp xyz den Typ auch durch BURG oder jeden anderen Gebäudetyp ersetzen.

`MACHE gebäudetyp` bzw. `MACHE SCHIFF` ohne weitere Parameter baut derzeit an dem Gebäude bzw. Schiff weiter, in dem die Einheit sich gerade befindet. **Achtung:** Falls sich die Einheit in einem Gebäude befindet, fängt MACHE Leuchtturm _kein neues_ Gebäude an, sondern baut an dem alten weiter.

## Beispiele

     MACHE 5 Schwert ; stellt (maximal) 5 Schwerter her
     MACHE Wasser~des~Lebens ; stellt so viel von dem Trank her, wie Talent und Material zulassen
     MACHE KRÄUTER
     
     VERLASSE
     MACHE Leuchtturm ; fängt einen neuen Leuchtturm an
     MACHE Leuchtturm xyz ; baut am Leuchtturm xyz weiter
     
     VERLASSE
     MACHE BURG xyz ; baut am Gebäude xyz weiter (egal welcher Gebäudetyp xyz ist)
     MACHE 5 Trireme ; fängt eine neue Trireme an
     MACHE SCHIFF abc ; baut an Schiff abc weiter
     
     MACHE STRASSE SO ; baut an der Straße nach Südosten weiter
     
     MACHE Trireme abc ; falsch: fängt neue Trireme an
     MACHE Gebäude xyz ; falsch: nur Burg oder Gebäudetyp erlaubt
     

## Siehe auch

- [Produktion]
- [Alchemie]

<!-- From [https://wiki.eressea.de/index.php?title=MACHE&oldid=16728] -->

[<sup>`L`</sup>]: ./commands.md#kurzlang "Befehl"
[Produktion]: ./production.md "Produktion"
[Gegenstände]: ./items.md "Waren"
[Rohstoffe]: ./resources.md "Rohstoffe"
[Alchemie-Kapitel]: ./skills-list.md "Liste der Talente"
[Kräuterkunde]: ./skills-list.md "Kräuterkunde"
[Kräuter]: ./herbs.md "Kräuter"
[wieder einer Einheit der eigenen Partei zu]: ./factions.md#auflösung-von-einheiten "Parteien"
[Gebäude]: ./buildings.md "Gebäude"
[Schiff]: ./ships.md "Schiffe"
[Straßen]: ./roads.md "Straßen"
[Straßenbau]: ./skills-list.md#straßenbau "Straßenbau"
[Tunnel]: ./buildings-others.md#tunnel "Andere Gebäude"
[Karawanserei]: ./buildings-others.md#karawanserei "Andere Gebäude"
[Damm]: ./buildings-others.md#damm "Andere Gebäude"
[Geländearten]: ./terrains.md "Geländearten"
[Alchemie]: ./alchemy.md "Alchemie"
