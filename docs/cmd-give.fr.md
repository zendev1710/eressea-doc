---
# cSpell:locale fr, en
alias: cmd-give-fr
---
# GIVE

**`GIVE`**` `*`ID-unité`*`HERBS`  
**`GIVE`**` `*`ID-unité`*`KOMMANDO`  
**`GIVE`**` `*`ID-unité`*`UNIT`  
**`GIVE`**` `*`ID-unité quantité`*`MEN`  
**`GIVE`**` `*`ID-unité quantité objet`*  
**`GIVE`**` `*`ID-unité quantité SHIP`*  
**`GIVE`**` `*`ID-unité`*`ALL MEN`  
**`GIVE`**` `*`ID-unité`*`ALL`  
**`GIVE`**` `*`ID-unité`*` ALL `*`objet`*  
**`GIVE`**` `*`ID-unité`*` EACH `*`quantité`*` `*`objet`*  
**`GIVE`**` 0 `*`quantité`*`MEN`  
**`GIVE`**` 0 `*`quantité`*`SHIP`  
**`GIVE`**` 0 `*`quantité objet`*

L'unité transfère des objets, le commandement de bateaux ou de bâtiments, des personnes, des bateaux ou même elle-même à d'autres unités.

## Objets

Avec `GIVE` les unités peuvent donner toutes les marchandises qu'elles possèdent à d'autres unités. La condition est que l'unité indiquée accepte des choses. C'est le cas si elle appartient à la même faction ou à une faction alliée (`HELP GIVE`), ou si elle a donné ce tour-ci l'ordre [[cmd-contact]] pour l'unité donatrice. Les unités de monstres et certaines unités de joueurs avec des races de monstres n'acceptent rien non plus. Ceux qui veulent simplement se débarrasser d'objets peuvent aussi les donner aux paysans ou les jeter dans l'océan (`GIVE 0`*`quantité" "objet`*). Les personnes, les Silver et les chevaux augmentent respectivement la réserve de paysans, de Silver et de chevaux d'une région (terrestre). Tous les autres objets disparaissent.

L'unité donatrice et l'unité réceptrice doivent bien entendu se trouver dans la même région. Le transfert fonctionne également en haute mer, entre bateaux et de bateaux à terre et inversement.

Statt einer Anzahl kann man auch den Parameter `ALLES` (oder `ALLE`) benutzen. `GIVE`*`unit-id`*`ALLE Schwerter` übergibt zum Beispiel alle Schwerter, die die Einheit zu dem Zeitpunkt hat. `GIVE`*`unit-id`*`ALLES` übergibt sämtliche Gegenstände, Kräuter, Tränke und Silber, nicht aber die Personen der Einheit. Mit `GIVE`*`unit-id`*`herb` werden sämtliche Kräuter übergeben, welche die Einheit besitzt. Gibt man explizit den Befehl `GIVE`*`unit-id`*`ALLE PERSONS`, so werden alle Personen übergeben und die Einheit aufgelöst.

**Achtung:** Alle Gegenstände und Silber, die mit `GIVE` übergeben wurden, sind automatisch reserviert und können auch vom Materialpool nicht mehr weiter gegeben werden! Auch `GIVE` benutzt den [Materialpool], ausgenommen im Kontext von GIVE ALLES, wo die Einheit nur eigene, nicht reservierte Gegenstände gibt.

Die Variante `GIVE xyz JE` übergibt *anzahl* Gegenstände pro Person der Zieleinheit. Hat die Einheit xyz also zum Beispiel 10 Personen, so übergibt `GIVE xyz JE 20 Silber` ihr 200 Silber.

**Tip:** Mit `@GIVE` kann man automatische Übergaben einrichten. Zum Beispiel wird eine Einheit mit `@GIVE abc ALLES Eisen` der Einheit abc jede Woche alles Eisen übergeben.

GIVE k3f 300 Silber

           ; Gibt der Einheit k3f 300 Silber.
     
           GIVE 0 5 Steine
           ; Wirft 5 Steine weg.
     
           GIVE TEMP 3 7 PERSONS
           ; Gibt 7 Personen an die neu geschaffene Einheit TEMP 3.

**Vorsicht:** Zwischen `MAKE TEMP` und `END` stehen Befehle für die neue Einheit - und diese hat kein Geld. Folgendes funktioniert also nicht:

MAKE TEMP 1

           GIVE TEMP 1 200 Silber  ;  sinnlos!
           RECRUIT 2
           MOVE WESTEN
         END

Stattdessen muss es so geschrieben werden:

GIVE TEMP 1 200 Silber

         MAKE TEMP 1
           RECRUIT 2
           MOVE WESTEN
         END
         ; GIVE TEMP 1 200 Silber  ;  oder hier!

## Personen und Einheiten

Will man Personen verschiedener Einheiten zusammenführen, so geschieht dies mit `GIVE`*`unit-id`*`anzahl PERSONS`. Dabei werden dann auch die [Talente] vermischt, und man sollte die Gegenstände nicht vergessen, da sie evtl. den Bauern zufallen, wenn die Einheit keine Personen mehr hat.

Expérience de jeu : Solthar Willst du einer Einheit einer anderen Partei Personen übergeben, reicht ein einfaches HELP GIVE nicht aus, sondern die Empfängereinheit muss die übergebende Einheit KONTAKTIEREN. Falls die Empfängereinheit eine [Migranteneinheit][1] ist, darf sie außerdem zum Zeitpunkt der Übergabe keine Personen haben. Am besten sollte sie also eine leere TEMP-Einheit sein. Beispiel:

    ```
    UNIT a; Partei X
    GIVE TEMP x ALLES PERSONS
    Einheit b; Partei Y
    MAKE TEMP x
    CONTACT UNIT a
    END
    ```

[1]: ./races.md#menschen

Mit `GIVE`*`unit-id`*`UNIT` wird die komplette Einheit mit allen Gegenständen einer anderen Partei gegeben, d.h. sie wechselt zur Partei der Empfänger-Einheit, und wird nicht zur Empfängereinheit zugefügt! Die Einheit führt in der Runde keine weiteren Befehle aus!

**[E3A — Das Dritte Zeitalter]**

In E3 können maximal 5 Personen pro Runde von einer Partei aufgenommen werden

## Kommando

Hat die Einheit zudem ein Schiff oder ein Gebäude unter ihrem Kommando - ist sie also die erste aufgeführte Einheit im Schiff oder in dem Gebäude - kann sie das Kommando auch an eine andere Einheit übergeben. Die Einheit mit dem Kommando bestimmt, welche anderen Einheiten das Schiff oder das Gebäude betreten dürfen.

`GIVE einheit KOMMANDO` sollte man immer anwenden, auch wenn die Einheit mit dem Kommando das Schiff oder Gebäude verlässt und die folgende Einheit das Kommando erhalten soll. Die Reihenfolge der Einheiten ist während der Auswertung nicht immer die dem Report entsprechende. Neue Besitzer eines Gebäudes werden am Ende der Runde an die erste Position im Gebäude gestellt und profitieren somit eventuell erst in der Folgerunde von dem Gebäude (z.B. Bergbaubonus). Das Kommando kann nicht an Einheiten ohne Personen (z.B. nach einem Kampf oder "leere" TEMP-Einheiten) übergeben werden.

## Konvoi

Mit `GIVE`*`unit-id`*` `*`anzahl`*`SHIP` übergibt der Besitzer eines Schiffes oder Konvois die Anzahl Schiffe. Die übergebende und empfangende Einheit müssen der selben Partei angehören, HELP ALLES oder CONTACT genügt nicht. Ist die anderen Einheit ebenfalls Besitzer eines Schiffes wird ein [Konvoi] gebildet. Konvois bestehen immer aus Schiffen des gleichen Typs. Boote können keine Konvois bilden und die Schiffe müssen an der gleichen Küste liegen.

## Voir aussi

- [[cmd-reserve]]
- [Materialpool]
- [Schiff]
- [Gebäude]

<!-- From [https://wiki.eressea.de/index.php?title=GIVE/fr&oldid=15993] -->

[CONTACT]: ./cmd-contact.md
[Materialpool]: ./items-pool.md
[Talente]: ./skills.md
[E3A — Das Dritte Zeitalter]: ./the-third-age.md
[Konvoi]: ./ships.md#konvoi
[RESERVE]: ./cmd-reserve.md
[Schiff]: ./ships.md
[Gebäude]: ./buildings.md
