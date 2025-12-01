# Materialpool

Besonders bei größeren Parteien verliert man als Spieler in einigen Regionen die Übersicht, zumal "Geldverteilen" eher eine langweilige Fleißarbeit ist und den Spielspaß wenig fördert.

## Der Silberpool

Der Silberpool übernimmt beim Spielen das Verteilen von Geld, so dass z.B. bei [REKRUTIERE] die Einheit automatisch genug Geld bekommt (sofern in der Region vorhanden) oder das Lernen teurer Talente versorgt wird. Trotzdem wird überall in der Anleitung darauf hingewiesen, dass Einheiten genug Geld dabei haben müssen. Dies ist nur, um zu vermeiden, dass es vergessen wird.

Ebenso werden [Gebäude] aus dem Pool versorgt, sofern das Silber am Rundenanfang in der Region vorhanden ist. Kann die Einheit, der das Gebäude gehört, dieses nicht aus eigener Tasche oder aus dem Pool bezahlen, kann das Gebäude nicht funktionieren. Am Ende der Runde wird die Einheit erneut versuchen, aus den eigenen Silbervorräten oder aus dem Pool der eigenen Partei das Gebäude zu bezahlen.

TEMP-Einheiten können nicht reservieren. Sie bestreiten die Rekrutierungskosten aus dem Silberpool, sofern notwendig, sollten aber Silber und Gegenstände, welche sie in eine andere Region mitnehmen oder sofort verarbeiten sollen, mit [GIB] übergeben bekommen. Vorsicht: wenn TEMP-Einheiten Silber bekommen, benutzen sie dieses auch zum Rekrutieren! Sollen sie also Silber in eine andere Region mitnehmen, muss das Rekrutierungssilber zusätzlich übergeben werden.

Für den Unterhalt von Einheiten gelten besondere Regeln: hier wird alles Silber der Region benutzt, ohne Rücksicht auf vorherige Reservierungen. Einheiten geben kein Silber, das sie für ihren eigenen Unterhalt brauchen, an Einheiten weg, um deren Unterhalt zu bezahlen.

## Der Materialpool

Der Materialpool ist die logische Fortführung des Silberpools: jede Einheit, die etwas benötigt, z.B. Steine und Holz für den Gebäudebau, holt sich dies automatisch von anderen eigenen Einheiten in der Region.

Die Pools gelten nur für die eigene Partei. Fremden Einheiten müssen Gegenstände explizit übergeben werden.

Achtung, die Pools funktionieren nicht nur bei der Produktion, also im Wesentlichen für den Befehl [MACHE], sondern im Grunde für alles, insbesondere auch bei den Befehlen [RESERVIERE], [GIB], [BENUTZE], [ZAUBERE], [REKRUTIERE]. Hat die Einheit einen Gegenstand nicht, so holt sie sich diesen aus dem Materialpool, um ihn zu verarbeiten, zu übergeben oder zu reservieren. Braucht jedoch eine Einheit Waffen für einen Angriff oder das Eintreiben von Steuern, müssen diese explizit übergeben oder reserviert werden, da hier der Materialpool nicht wirkt.

Unerfahrene Parteien sollten den Materialpool gründlich planen, da man leicht Einheiten Ressourcen "klaut", mit denen man nicht rechnete, und somit "beklaute" Einheiten nicht oder nicht genug produzieren kann, während die andere Einheit mehr Ressourcen verbrauchte und mehr produzierte, als beabsichtigt.

### Beispiel 1

     EINHEIT a ; Steinbauer, haben 30 Eisen
     MACHE 20 Eisen
     @GIB c ALLES Eisen
     ;
     EINHEIT b ; Burgenbauer, haben kein Eisen
     RESERVIERE 10 Eisen
     MACHE 10 Schwert
     ;
     EINHEIT c; Depot, hat kein Eisen
     LERNE Tarnung

**Ergebnis:**

- Einheit b holt sich zunächst 10 Eisen aus dem Materialpool von a.
- Einheit a gibt die restlichen 20 Eisen an c.
- Einheit b macht 10 Schwerter aus 10 Eisen.
- Einheit a macht 20 Eisen.
- Einheit b hat also 10 Schwerter
- Einheit a hat 20 Eisen
- Einheit c hat 20 Eisen

## RESERVIERE und GIB

Bei [RESERVIERE] und [GIB], die vor den meisten anderen Befehlen in der [Befehlsreihenfolge] kommen, gilt es ein paar besondere Dinge zu beachten. Diese gelten für den Silber- und den Materialpool gleichermaßen:

Erstens stehen Gegenstände die übergeben oder reserviert wurden nicht mehr im Pool zur Verfügung. Also kann sie nur noch die Einheit, die sie reserviert oder bekommen hat, verbrauchen.

Bei RESERVIERE-Befehlen geht die Einheit wie folgt vor: In einem ersten Durchgang reserviert jede Einheit zunächst ihre eigenen Gegenstände. Alles, was reserviert wurde, steht ab dann nicht mehr für den Pool zur Verfügung. Dann erst versuchen die Einheiten sich die Gegenstände, die sie im ersten Schritt nicht selber hatten, von anderen Einheiten aus dem Pool zu holen. Sowohl das Abarbeiten der RESERVIERE-Befehle als auch beim Holen von Gegenständen wird dabei in der Reihenfolge vorgegangen, wie die Einheiten im Report stehen - dies ist streng genommen nicht garantiert, aber seit langem die Praxis.

Wenn eine Einheit mehrere RESERVIERE-Befehle für einen Gegenstand hat, gilt dies nicht additiv. Stattdessen werden alle Befehle der Reihe nach ausgeführt. Dieses Verhalten wird jedoch im Moment ebenfalls nicht garantiert, deswegen sollte eine Einheit besser nur einen RESERVIERE-Befehl pro Gegenstand haben.

Bei der anschließenden Ausführung von GIB werden Gegenstände falls nötig ebenfalls aus dem Pool entnommen. Auch hier geht es nach Reportreihenfolge. Gegenstände, die von irgend einer Einheit (einschließlich der Einheit mit dem GIB-Befehl) reserviert wurden, werden dabei nicht weitergegeben. Übergebene Gegenstände sind anschließend ebenfalls nicht mehr im Pool. Merke: `GIB xyz ALLES` übergibt nur nicht reservierte Gegenstände der Einheit selber.

Alle anderen Befehle benutzen zunächst die eigenen, reservierten oder an sie übergebenen Gegenstände und erst danach nicht reservierte Gegenstände aus dem Pool.

### Beispiel 2

      EINHEIT a; hat 10 Silber
      LERNE Hiebwaffen
      RESERVIERE 20 Silber
      ;
      Einheit b; hat 0 Silber
      LERNE Hiebwaffen
      RESERVIERE 10 Silber
      ;
      Einheit c; hat 10 Silber
      LERNE Hiebwaffen
      RESERVIERE 10 Silber

**Ergebnis:**

- Einheit a reserviert ihre eigenen 10 Silber
- Einheit c reserviert ihre eigenen 10 Silber
- Da insgesamt nur 20 Silber in der Region vorhanden waren verfallen die übrigen RESERVIERE-Befehle
- Einheit a verbraucht ihre eigenen 10 Silber Unterhalt.
- Einheit c verbraucht ihre eigenen 10 Silber Unterhalt.
- Einheit b hungert weil kein Silber mehr übrig ist.

Hätte irgend eine Einheit zu Anfang 10 Silber mehr gehabt, hätte Einheit b nicht hungern müssen.

### Beispiel 3

      EINHEIT a; hat 20 Silber
      RESERVIERE 20 Silber
      GIB c 20 Silber
      ;
      Einheit b; hat 20 Silber
      NACH o
      ;
      Einheit c; hat 0 Silber
      NACH w

**Ergebnis:**

- Einheit a reserviert ihre eigenen 20 Silber
- Einheit a gibt 20 Silber aus dem Materialpool an c. Ihre eigenen 20 Silber sind reserviert, also nimmt sie die 20 Silber von b.
- Einheit b geht nach Osten und wird hungern, falls dort keine andere Einheit mit Silber ist.
- Einheit c nimmt die 20 Silber nach Westen mit.

### Beispiel 4

     EINHEIT a ; hat 10 Silber, 20 Holz, 10 Eisen
     LERNE Hiebwaffen
     RESERVIERE 5 Eisen ; (1)
     GIB d ALLES Eisen ; (6)
     ;
     EINHEIT b ; hat 10 Silber, 10 Eisen
     RESERVIERE 100 Silber ; (2), (4)
     RESERVIERE 10 Holz; (5)
     GIB c 100 Silber ; (7)
     GIB d 9 Holz ; (8)
     LERNE Hiebwaffen
     ;
     EINHEIT c ; Waffenbau 10, hat 100 Silber
     RESERVIERE 100 Silber ; (3)
     MACHE 10 Speer ; (9)
     ;
     EINHEIT d ; hat 200 Silber
     LERNE Holzfällen

**Ausführung:**

- (1), (2), (3): Die Einheiten a, b, und c reservieren zunächst ihre eigenen 5 Eisen, 10 Silber, bzw. 100 Silber.
- (4): Dann erst holt sich b die restlichen 90 Silber aus dem Pool, und zwar 10 von Einheit a und 80 von Einheit d, da diese als einzige noch nicht reserviert sind.
- (5): Einheit b nimmt sich 10 Holz aus dem Pool von Einheit a.
- (6): Einheit a gibt die restlichen 5 Eisen, die nicht reserviert waren, an Einheit d.
- (7): Einheit b versucht 100 Silber an c zu übergeben; das einzige Silber, dass noch nicht reserviert ist, hat Einheit d (120), also werden 100 davon an c übergeben.
- (8): Einheit b gibt 9 Holz von Einheit a an Einheit d.
- (9): Einheit c nimmt sich zur Produktion aus dem Pool 1 Holz von Einheit a, das noch nicht reserviert ist. Sie kann also nur einen Speer bauen.
- (10): Alle Einheiten bezahlen Unterhalt (wir nehmen an, 10 Silber pro Person).

**Ergebnis:**

- Einheit a hat 0 Silber, 0 Holz, 5 Eisen.
- Einheit b hat 10 Holz, 80 Silber (20 verbraucht für Unterhalt von a und b), 10 Eisen.
- Einheit c hat 190 Silber (10 verbraucht) und einen Speer
- Einheit d hat 9 Holz und 10 Silber (10 verbraucht), 5 Eisen.

## Historische Bemerkung

In älteren Versionen war der Materialpool eine optionale Einstellung, die jeder Spieler an- oder abschalten konnte. Es gab getrennte Einstellungen für Silber und andere Gegenstände. Nun ist der Silber- und der Materialpool für alle Parteien automatisch aktiv und nicht mehr deaktivierbar.

## Siehe auch

- [GIB]
- [RESERVIERE]
- [Befehlsreihenfolge]

|     |     |
| --- | --- |
| Weiterlesen: | [Krieg] |

[Krieg]: ./war.md "Krieg"

<!-- From [https://wiki.eressea.de/index.php?title=Materialpool&oldid=17006] -->

[REKRUTIERE]:./silver.md#recruiting "REKRUTIERE"
[Gebäude]: ./buildings.md "Gebäude"
[GIB]: ./cmd-give.md "GIB"
[MACHE]: ./cmd-make.md "MACHE"
[RESERVIERE]: ./cmd-reserve.md "RESERVIERE"
[BENUTZE]: ./cmd-use.md "BENUTZE"
[ZAUBERE]: ./cmd-cast.md "ZAUBERE"
[Befehlsreihenfolge]: ./commands-sequence.md "Befehlsreihenfolge"
