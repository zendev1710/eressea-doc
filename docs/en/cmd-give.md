# GIVE

` `**`GIVE`**` `*`unit_ID amount item`*  
**`GIVE`**` `*`unit_ID`*` EACH `*`amount`*` `*`item`*  
**`GIVE`**` `*`unit_ID`*`ALL`  
**`GIVE`**` `*`unit_ID`*` ALL `*`item`*  
**`GIVE`**` `*`unit_ID`*`HERBS`  
**`GIVE`**` `*`unit_ID amount`*`MEN`  
**`GIVE`**` `*`unit_ID`*`ALL MEN`  
**`GIVE`**` `*`unit_ID`*`UNIT`  
**`GIVE`**` `*`unit_ID`*`KOMMANDO`  
**`GIVE`**` `*`unit_ID amount SHIP`*  
**`GIVE`**` 0 `*`amount item`*  
**`GIVE`**` 0 `*`amount`*`MEN`  
**`GIVE`**` 0 `*`amount`*`SHIP`

The unit transfers items, command of ships or buildings, persons, ships or even itself to other units.

## Items

With `GIVE` units can give all the goods they own to other units. The condition is that the indicated unit accepts things. This is the case if it belongs to the same faction or an allied faction (`HELP GIVE`), or if it has given this turn the [CONTACT] order for the giving unit. Monster units and certain player units with monster races also accept nothing. Those who simply want to throw away objects can also give them to peasants or throw them into the ocean (`GIB 0 "amount" "item"'`). Persons, Silver and horses respectively increase the supply of peasants, Silver and horses in a (land) region. All other items disappear.

The sending and receiving units must, of course, be in the same region. The transfer also works on the high seas, between ships and from ships to shore and vice versa.

Statt einer Anzahl kann man auch den Parameter `ALLES` (oder `ALLE`) benutzen. `GIB`*`einheit-nr`*`ALLE Schwerter` übergibt zum Beispiel alle Schwerter, die die Einheit zu dem Zeitpunkt hat. `GIB`*`einheit-nr`*`ALLES` übergibt sämtliche Gegenstände, Kräuter, Tränke und Silber, nicht aber die Personen der Einheit. Mit `GIB`*`einheit-nr`*`KRÄUTER` werden sämtliche Kräuter übergeben, welche die Einheit besitzt. Gibt man explizit den Befehl `GIB`*`einheit-nr`*`ALLE PERSONEN`, so werden alle Personen übergeben und die Einheit aufgelöst.

**Achtung:** Alle Gegenstände und Silber, die mit `GIB` übergeben wurden, sind automatisch reserviert und können auch vom Materialpool nicht mehr weiter gegeben werden! Auch `GIB` benutzt den [Materialpool], ausgenommen im Kontext von GIB ALLES, wo die Einheit nur eigene, nicht reservierte Gegenstände gibt.

Die Variante `GIB xyz JE` übergibt *anzahl* Gegenstände pro Person der Zieleinheit. Hat die Einheit xyz also zum Beispiel 10 Personen, so übergibt `GIB xyz JE 20 Silber` ihr 200 Silber.

**Tip:** Mit `@GIB` kann man automatische Übergaben einrichten. Zum Beispiel wird eine Einheit mit `@GIB abc ALLES Eisen` der Einheit abc jede Woche alles Eisen übergeben.

GIB k3f 300 Silber

           ; Gibt der Einheit k3f 300 Silber.
     
           GIB 0 5 Steine
           ; Wirft 5 Steine weg.
     
           GIB TEMP 3 7 PERSONEN
           ; Gibt 7 Personen an die neu geschaffene Einheit TEMP 3.

**Vorsicht:** Zwischen `MACHE TEMP` und `ENDE` stehen Befehle für die neue Einheit - und diese hat kein Geld. Folgendes funktioniert also nicht:

MACHE TEMP 1

           GIB TEMP 1 200 Silber  ;  sinnlos!
           REKRUTIERE 2
           NACH WESTEN
         ENDE

Stattdessen muss es so geschrieben werden:

GIB TEMP 1 200 Silber

         MACHE TEMP 1
           REKRUTIERE 2
           NACH WESTEN
         ENDE
         ; GIB TEMP 1 200 Silber  ;  oder hier!

## Personen und Einheiten

Will man Personen verschiedener Einheiten zusammenführen, so geschieht dies mit `GIB`*`einheit-nr`*`anzahl PERSONEN`. Dabei werden dann auch die [Talente] vermischt, und man sollte die Gegenstände nicht vergessen, da sie evtl. den Bauern zufallen, wenn die Einheit keine Personen mehr hat.

Player experience: Solthar Willst du einer Einheit einer anderen Partei Personen übergeben, reicht ein einfaches HELFE GIB nicht aus, sondern die Empfängereinheit muss die übergebende Einheit KONTAKTIEREN. Falls die Empfängereinheit eine [Migranteneinheit] ist, darf sie außerdem zum Zeitpunkt der Übergabe keine Personen haben. Am besten sollte sie also eine leere TEMP-Einheit sein. Beispiel:

```
 EINHEIT a; Partei X
 GIB TEMP x ALLES PERSONEN
 Einheit b; Partei Y
 MACHE TEMP x
 KONTAKTIERE EINHEIT a
 ENDE
```

[Migranteneinheit]: /Spezial:Meine_Sprache/Rassen#Menschen "Spezial:Meine Sprache/Rassen"

Mit `GIB`*`einheit-nr`*`EINHEIT` wird die komplette Einheit mit allen Gegenständen einer anderen Partei gegeben, d.h. sie wechselt zur Partei der Empfänger-Einheit, und wird nicht zur Empfängereinheit zugefügt! Die Einheit führt in der Runde keine weiteren Befehle aus!

**[E3A — Das Dritte Zeitalter]**

In E3 können maximal 5 Personen pro Runde von einer Partei aufgenommen werden

## Kommando

Hat die Einheit zudem ein Schiff oder ein Gebäude unter ihrem Kommando - ist sie also die erste aufgeführte Einheit im Schiff oder in dem Gebäude - kann sie das Kommando auch an eine andere Einheit übergeben. Die Einheit mit dem Kommando bestimmt, welche anderen Einheiten das Schiff oder das Gebäude betreten dürfen.

`GIB einheit KOMMANDO` sollte man immer anwenden, auch wenn die Einheit mit dem Kommando das Schiff oder Gebäude verlässt und die folgende Einheit das Kommando erhalten soll. Die Reihenfolge der Einheiten ist während der Auswertung nicht immer die dem Report entsprechende. Neue Besitzer eines Gebäudes werden am Ende der Runde an die erste Position im Gebäude gestellt und profitieren somit eventuell erst in der Folgerunde von dem Gebäude (z.B. Bergbaubonus). Das Kommando kann nicht an Einheiten ohne Personen (z.B. nach einem Kampf oder "leere" TEMP-Einheiten) übergeben werden.

## Konvoi

Mit `GIB`*`einheit-nr`*` `*`anzahl`*`SCHIFF` übergibt der Besitzer eines Schiffes oder Konvois die Anzahl Schiffe. Die übergebende und empfangende Einheit müssen der selben Partei angehören, HELFE ALLES oder KONTAKTIERE genügt nicht. Ist die anderen Einheit ebenfalls Besitzer eines Schiffes wird ein [Konvoi] gebildet. Konvois bestehen immer aus Schiffen des gleichen Typs. Boote können keine Konvois bilden und die Schiffe müssen an der gleichen Küste liegen.

## Siehe auch

- [RESERVIERE]
- [Materialpool]
- [Schiff]
- [Gebäude]

Abgerufen von „[https://wiki.eressea.de/index.php?title=GIB/en&oldid=15995]“

[Kategorie][]:

- [Befehle/en]

  [CONTACT]: /Spezial:Meine_Sprache/KONTAKTIERE "Spezial:Meine Sprache/KONTAKTIERE"
  [Materialpool]: /Spezial:Meine_Sprache/Materialpool "Spezial:Meine Sprache/Materialpool"
  [Talente]: ./skills.md "Spezial:Meine Sprache/Talente"
  [E3A — Das Dritte Zeitalter]: /Das_dritte_Zeitalter "Das dritte Zeitalter"
  [Konvoi]: /Spezial:Meine_Sprache/Schiff#Konvoi "Spezial:Meine Sprache/Schiff"
  [RESERVIERE]: /Spezial:Meine_Sprache/RESERVIERE "Spezial:Meine Sprache/RESERVIERE"
  [Schiff]: /Spezial:Meine_Sprache/Schiff "Spezial:Meine Sprache/Schiff"
  [Gebäude]: /Spezial:Meine_Sprache/Geb%C3%A4ude "Spezial:Meine Sprache/Gebäude"
  [https://wiki.eressea.de/index.php?title=GIB/en&oldid=15995]: https://wiki.eressea.de/index.php?title=GIB/en&oldid=15995
  [Kategorie]: /Spezial:Kategorien "Spezial:Kategorien"
  [Befehle/en]: /index.php?title=Kategorie:Befehle/en&action=edit&redlink=1 "Kategorie:Befehle/en (Seite nicht vorhanden)"
