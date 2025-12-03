# MAKE

**`MAKE TEMP`**` `*`unit-alias-id`*`["`*`nom`*`"]`  
**`MAKE`**`[`*`niveau`*`]`*`type_batiment`*`[`*`id_batiment`*`]`  
**`MAKE`**`[`*`niveau`*`]`*`type_bateau`*  
**`MAKE`**`[`*`niveau`*`] SHIP [`*`bateau-id`*`]`  
**`MAKE`**`[`*`niveau`*`] Road`*`direction`*  
**`MAKE`**`[`*`quantité`*`] HERBS`  
**`MAKE`**`[`*`quantité`*`]`*`objet`*

La commande `MAKE` est la commande de production générale. Pour en savoir plus, voir le chapitre [production].

## Objets

[Gegenstände] und [Rohstoffe] werden mit `MAKE [`*`anzahl`*`]`*`gegenstand`*` ` hergestellt. Je nach Gegenstand wird ein bestimmtes Talent und vielleicht auch noch bestimmte Rohstoffe benötigt. Ohne Angabe von *anzahl* wird die Einheit so viele Gegenstände produzieren, wie Personen, Talent und evtl. Rohstoffe es ihr ermöglichen.

### Tränke

Das Herstellen eines Trankes ist sehr aufwendig und kann nur von besonders talentierten Alchemisten durchgeführt werden. Details dazu findest du im [Alchemie-Kapitel].

### Kräuter

Kräuter werden mit dem Befehl `MAKE HERBS` von Einheiten mit dem Talent [Kräuterkunde] hergestellt. Details dazu im Kapitel über [Kräuter].

## Einheiten

Wenn du eine neue Einheit erschaffst (`MAKE TEMP xy`), gibst du der Einheit eine Alias-Nummer, denn du weißt ja zu diesem Zeitpunkt noch nicht, welche Nummer für die Einheit schlussendlich noch frei sein wird. Für alle anderen Befehle kannst du nun diesen Alias verwenden (mit dem Wort TEMP davor, zum Beispiel `GIVE TEMP xy 100 Silber`). Bei der Suche nach einer TEMP-Einheit wird erst in der eigenen Partei gesucht, dann in fremden Parteien. Wenn also du und eine andere Partei eine Einheit mit der ID *TEMP xy* haben, wird deine eigene Einheit gewählt. Mit ein wenig Absprache können also auch TEMP-Einheiten fremder Parteien angesprochen werden.

Die Alias-Nummer wird als Nummer der Einheit benutzt, wenn diese noch nicht belegt ist. Ebenso kannst du schon hier einen Namen der Einheit angeben. So lassen sich die Befehle

MAKE TEMP 1

        NAME UNIT "Clowns"
        NUMBER UNIT lach

verkürzen auf

MAKE TEMP lach "Clowns"

Pro Partei sind maximal 2500 Einheiten erlaubt. Hat die Partei 2500 oder mehr Einheiten, so können mit `MAKE TEMP` keine neuen Einheiten geschaffen werden, es müssen erst andere Einheiten z.B. durch Zusammenfassen gelöscht werden. Da das Auflösen leerer Einheiten in der Befehlsreihenfolge weit hinten kommt, können neue TEMP-Einheiten erst in der folgenden Woche geschaffen werden.

Nach diesem Befehl werden die Befehle für die neue Einheit angegeben, bis der Befehl END folgt.

Die neue Einheit muss allerdings noch Mitglieder bekommen, sonst wird sie stillschweigend am Ende der Runde wieder gelöscht! Sie muss also rekrutieren oder Personen übergeben bekommen. Wenn die neue Einheit Mitglieder neu rekrutieren soll, muss sie auch genug Geld dafür erhalten. Erhält sie das nicht, wird die Einheit niemanden rekrutieren können und am Ende der Woche stillschweigend entfernt werden. Bekommt die Einheit Geld, rekrutiert aber keine Mitglieder, löst sie sich ebenfalls auf und das Geld fällt [wieder einer Einheit der eigenen Partei zu].

UNIT 17; Kämpfer \[15,700$\]

     MAKE TEMP 1
        NAME UNIT "Drachenreiter"
        LEARN Hiebwaffen
     END
     GIVE TEMP 1 5 PERSONS
      
     GIVE TEMP 2 100 Silber
     MAKE TEMP 2
        RECRUIT 1
        NAME UNIT "Späher"
        DEFAULT "LEARN Wahrnehmung"
        MOVE Westen
     END

## Gebäude

Um ein neues Gebäude zu errichten, verwendest du *`MAKE`*`[`*`stufen`*`]`*`Gebäudetyp`* (siehe [Gebäude]). Willst du an einem Gebäude weiterbauen, so lautet der Befehl dafür *`MAKE`*`[`*`stufen`*`]`*`Gebäudetyp`*` `*`gebäude-nr`*. Der *Gebäudetyp* kann beim Weiterbauen auch durch BURG ersetzt werden, auch wenn es sich um ein anderes Gebäude handelt. Burgen und viele andere Gebäude können beliebig ausgebaut werden. Um Burgen zu bauen, muss die Einheit das Talent Burgenbau und Steine haben, andere Gebäude erfordern i.d.R. weiterhin Holz, Eisen und Silber in verschiedenen Mengen.

## Schiffe

Mit `MAKE`*`schiffstyp`* beginnt eine Einheit, ein neues [Schiff] zu bauen. Dazu muss sie das Talent Schiffbau und Holz haben. Mit `MAKE [`*`stufe`*`] SHIP`*`schiff-nr`* kann sie daran weiterbauen. Schiffe können nicht wie Burgen erweitert werden, sondern der Typ wird bei Baubeginn festgelegt. An Schiffen kann nur bis zu der durch den Typ festgelegten Größe weiter gebaut werden.

Sowohl bei Gebäuden als auch bei Schiffen kannst du mit *stufen* angeben, wie viele Stufen du das Gebäude bzw. Schiff bauen / erweitern willst.

- erste Woche: `MAKE LANGBOOT`  
  Ein neues Schiff wird gebaut und bekommt vom Computer die Nummer 76.
- zweite Woche: `MAKE SHIP 76`  
  An Schiff Nr. 76 wird nun weiter gebaut.

## Straßen

Um in einer Region das Durchreisen durch Straßen und Brücken zu erleichtern, verwendest du `MAKE STRASSE`*`richtung`*. Um [Straßen] zu bauen, braucht die Einheit das Talent [Straßenbau] und [Steine][Gegenstände]. In Gletschern benötigt sie dazu vorher einen [Tunnel], in Wüsten eine [Karawanserei] und in Sümpfen einen [Damm]. Pro Talentpunkt Straßenbau wird ein Stein verbaut. Für jede gewünschte Richtung werden zwischen 50 und 250 Steine benötigt, abhängig von den [Geländearten]. Straßen funktionieren nur wenn sie vollständig sind.

Expérience de jeu : Solthar Außer beim Neubau eines Gebäudes kannst du derzeit bei MAKE gebäudetyp xyz den Typ auch durch BURG oder jeden anderen Gebäudetyp ersetzen.

`MAKE gebäudetyp` bzw. `MAKE SHIP` ohne weitere Parameter baut derzeit an dem Gebäude bzw. Schiff weiter, in dem die Einheit sich gerade befindet. **Achtung:** Falls sich die Einheit in einem Gebäude befindet, fängt MAKE Leuchtturm _kein neues_ Gebäude an, sondern baut an dem alten weiter.

## Beispiele

MAKE 5 Schwert ; stellt (maximal) 5 Schwerter her

     MAKE Wasser~des~Lebens ; stellt so viel von dem Trank her, wie Talent und Material zulassen
     MAKE HERBS
     
     LEAVE
     MAKE Leuchtturm ; fängt einen neuen Leuchtturm an
     MAKE Leuchtturm xyz ; baut am Leuchtturm xyz weiter
     
     LEAVE
     MAKE BURG xyz ; baut am Gebäude xyz weiter (egal welcher Gebäudetyp xyz ist)
     MAKE 5 Trireme ; fängt eine neue Trireme an
     MAKE SHIP abc ; baut an Schiff abc weiter
     
     MAKE STRASSE SO ; baut an der Straße nach Südosten weiter
     
     MAKE Trireme abc ; falsch: fängt neue Trireme an
     MAKE Gebäude xyz ; falsch: nur Burg oder Gebäudetyp erlaubt

## Siehe auch

- [Produktion][production]
- [Alchemie]

<!-- From [https://wiki.eressea.de/index.php?title=MAKE/fr&oldid=16448] -->

[production]: ./production.md "Produktion"
[Gegenstände]: ./items.md "Waren"
[Rohstoffe]: ./resources.md "Ressources"
[Alchemie-Kapitel]: ./skills-list.md "Liste des compétences"
[Kräuterkunde]: ./herbs.mdkunde "Planteskunde"
[Kräuter]: ./herbs.md "Plantes"
[wieder einer Einheit der eigenen Partei zu]: ./factions.mden#Auflösung_von_Einheiten "Parteien"
[Gebäude]: ./buildings.md "Gebäude"
[Schiff]: ./ships.mde "Schiffe"
[Straßen]: ./roads.md "Straßen"
[Straßenbau]: ./skills-list.md#Straßenbau "Straßenbau"
[Tunnel]: ./buildings-others.md#Tunnel "Andere Gebäude"
[Karawanserei]: ./buildings-others.md#Karawanserei "Andere Gebäude"
[Damm]: ./buildings-others.md#Damm "Andere Gebäude"
[Geländearten]: ./terrains.md "Geländearten"
[Alchemie]: ./alchemy.cmd "Alchemie"
