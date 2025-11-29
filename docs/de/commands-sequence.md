# Befehlsreihenfolge

Die Befehle von Eressea werden in einer festen Reihenfolge ausgewertet. Befehle, die unter der selben Nummer stehen, werden zur gleichen Zeit ausgeführt oder die Reihenfolge spielt keine Rolle.

1. neue Default-Befehle werden gesetzt
2. [GRUPPE], [MACHE TEMP]
3. [BENENNE], [BESCHREIBE], [BEWACHE NICHT], [HELFE], [KÄMPFE], [KAMPFZAUBER], [TARNE], [URSPRUNG], [ZEIGE]
4. [BANNER], [EMAIL], [OPTION], [PASSWORT]
5. [KONTAKTIERE]
6. [BOTSCHAFT]
7. [BETRETE]; 1. Versuch
8. [BENUTZE]
9. [VERLASSE]
10. [BETRETE]; 2. Versuch
11. [ATTACKIERE]
12. [RESERVIERE], [BEANSPRUCHE]
13. [BETRETE]; 3. Versuch
14. [GIB KOMMANDO]
15. [VERGISS]
16. [GIB][GIB KOMMANDO]
17. [REKRUTIERE] \*
18. [ZERSTÖRE]
19. [FOLGE] wird gesetzt
20. [BEFÖRDERE]
21. [BEZAHLE NICHT] Stellt Funktion und Unterhaltskosten für das entsprechende Gebäude ein.
22. Unterhaltskosten für unterhaltspflichtige Gebäude fallen an; sonst haben sie keine Funktion!
23. [STIRB]
24. [ZAUBERE]
25. [LEHRE]
26. [LERNE]
27. [MACHE][MACHE TEMP] \*
28. [FORSCHE], [PFLANZE], [SPIONIERE], [ZÜCHTE]
29. [UNTERHALTE] \*
30. [ARBEITE] \*
31. [TREIBE] \*
32. [KAUFE] \*
33. [VERKAUFE] \*
34. [BEKLAUE] \*
35. Schiffe mit mangelnder Besatzung nehmen Schäden
36. BETRETE; 4. Versuch
37. [NACH] und [ROUTE], dabei wird auch [FAHRE] und [TRANSPORTIERE] ausgeführt und Verfolger folgen
38. [BEWACHE][BEWACHE NICHT] an; das geht nur, wenn die Einheit sich nicht bewegt hat
39. Schiffe treiben auf hoher See
40. [DEFAULT]
41. leere Einheiten werden beseitigt
42. die Bauern, Pferde und Wälder vermehren sich, falls möglich; die übriggebliebenen Bauern wandern umher
43. Silber für die Versorgung der Einheiten wird abgezogen
44. [SORTIERE]
45. [NUMMER]

\* So markierte Befehle werden "gerecht" aufgeteilt. Siehe [Erläuterungen] unten.

Die Befehle müssen aber nicht zwingend in dieser Reihenfolge eingegeben werden. Es ist durchaus zulässig, folgendes einzugeben:

    GIB TEMP 5 300 Silber
    MACHE TEMP 5
      REKRUTIERE 1
      KÄMPFE NICHT
      LERNE HOLZFÄLLEN
    ENDE

Die neue Einheit wird zuerst erschaffen, kämpft nicht mehr, erhält 300 Silber, rekrutiert 1 und lernt schlussendlich Holzfällen - obwohl das nicht der Reihenfolge entspricht, in der die Befehle eingegeben wurden.

## Erläuterungen

Gleichrangige Befehle verschiedener Einheiten werden normalerweise in der Reihenfolge abgearbeitet, wie sie im Report erscheinen. Also zum Beispiel erst alle GIB-Befehle der ersten Einheit, dann alle GIB-Befehle der zweiten Einheit, später alle `REKRUTIERE`-Befehle der ersten Einheit, dann der zweiten und so fort. Auch der [Materialpool] funktioniert üblicherweise in dieser Reihenfolge: Einheiten, die weiter oben in der Reihenfolge stehen, werden also zuerst "befragt", ob sie einen Gegenstand hergeben können. Die Reihenfolge kann sich jedoch durch bestimmte Befehle verändern. Dazu gehören `BETRETE, VERLASSE, MACHE TEMP, GIB KOMMANDO` und `GIB SCHIFF`. Das genaue Verhalten wird nicht garantiert! Deshalb sollte man im Zweifel Befehle so geben, dass die Einheitenreihenfolge dafür keine Rolle spielt.

Bei Befehlen, deren Resultat eine Obergrenze hat, z.B. die maximale Menge an Bäumen in der Region bei `MACHE Holz`, die maximale Zahl von Rekruten bei `REKRUTIERE` oder dem Regionssilber bei `UNTERHALTE` und `TREIBE`, kann es vorkommen, dass mehrere Einheiten in Konkurrenz zueinander stehen. In diesem Fall wird versucht, das knappe Gut anteilig an der Menge zu verteilen, die jede Einheit produzieren könnte, wenn es unbegrenzt wäre. Hierbei kann es zu Abweichungen kommen, und eine Einheit eventuell leer ausgehen. Ebenfalls betroffen sind die Befehle `VERKAUFE, KAUFE` und `ARBEITE`.

Betrete 1./2./3./4. Versuch  
Das bedeutet, dass man vor einem Angriff noch eine Burg betreten kann. Nach dem Kampf, kann man es nochmal versuchen, denn die Vorbesitzer könnten inzwischen tot oder geflohen sein.

Es bedeutet nicht, dass Einheiten, die ein Schiff verlassen, noch in derselben Runde attackieren können, da sich der Server merkt, wer Schiffe verlassen hat, und das entsprechend abfängt.

## Siehe auch

- [Befehle]
- [Kurzbeschreibung]
- [Befehlsreihenfolge (E3)]

|     |     |
| --- | --- |
| Weiterlesen: | [Kurzbeschreibung] |

[Kurzbeschreibung]: /Spezial:Meine_Sprache/Kurzbeschreibung "Spezial:Meine Sprache/Kurzbeschreibung"

Abgerufen von „[https://wiki.eressea.de/index.php?title=Befehlsreihenfolge/de&oldid=13925]“

[Kategorien][]:

- [Befehle][1]
- [Regeln/de]

  [GRUPPE]: /Spezial:Meine_Sprache/GRUPPE "Spezial:Meine Sprache/GRUPPE"
  [MACHE TEMP]: /Spezial:Meine_Sprache/MACHE "Spezial:Meine Sprache/MACHE"
  [BENENNE]: /Spezial:Meine_Sprache/BENENNE "Spezial:Meine Sprache/BENENNE"
  [BESCHREIBE]: /Spezial:Meine_Sprache/BESCHREIBE "Spezial:Meine Sprache/BESCHREIBE"
  [BEWACHE NICHT]: /Spezial:Meine_Sprache/BEWACHE "Spezial:Meine Sprache/BEWACHE"
  [HELFE]: /Spezial:Meine_Sprache/HELFE "Spezial:Meine Sprache/HELFE"
  [KÄMPFE]: /Spezial:Meine_Sprache/K%C3%84MPFE "Spezial:Meine Sprache/KÄMPFE"
  [KAMPFZAUBER]: /Spezial:Meine_Sprache/KAMPFZAUBER "Spezial:Meine Sprache/KAMPFZAUBER"
  [TARNE]: /Spezial:Meine_Sprache/TARNE "Spezial:Meine Sprache/TARNE"
  [URSPRUNG]: /Spezial:Meine_Sprache/URSPRUNG "Spezial:Meine Sprache/URSPRUNG"
  [ZEIGE]: /Spezial:Meine_Sprache/ZEIGE "Spezial:Meine Sprache/ZEIGE"
  [BANNER]: /Spezial:Meine_Sprache/BANNER "Spezial:Meine Sprache/BANNER"
  [EMAIL]: /Spezial:Meine_Sprache/EMAIL "Spezial:Meine Sprache/EMAIL"
  [OPTION]: /Spezial:Meine_Sprache/OPTION "Spezial:Meine Sprache/OPTION"
  [PASSWORT]: /Spezial:Meine_Sprache/PASSWORT "Spezial:Meine Sprache/PASSWORT"
  [KONTAKTIERE]: /Spezial:Meine_Sprache/KONTAKTIERE "Spezial:Meine Sprache/KONTAKTIERE"
  [BOTSCHAFT]: /Spezial:Meine_Sprache/BOTSCHAFT "Spezial:Meine Sprache/BOTSCHAFT"
  [BETRETE]: /Spezial:Meine_Sprache/BETRETE "Spezial:Meine Sprache/BETRETE"
  [BENUTZE]: /Spezial:Meine_Sprache/BENUTZE "Spezial:Meine Sprache/BENUTZE"
  [VERLASSE]: /Spezial:Meine_Sprache/VERLASSE "Spezial:Meine Sprache/VERLASSE"
  [ATTACKIERE]: /Spezial:Meine_Sprache/ATTACKIERE "Spezial:Meine Sprache/ATTACKIERE"
  [RESERVIERE]: /Spezial:Meine_Sprache/RESERVIERE "Spezial:Meine Sprache/RESERVIERE"
  [BEANSPRUCHE]: /Spezial:Meine_Sprache/BEANSPRUCHE "Spezial:Meine Sprache/BEANSPRUCHE"
  [GIB KOMMANDO]: /Spezial:Meine_Sprache/GIB "Spezial:Meine Sprache/GIB"
  [VERGISS]: /Spezial:Meine_Sprache/VERGISS "Spezial:Meine Sprache/VERGISS"
  [REKRUTIERE]: /Spezial:Meine_Sprache/REKRUTIERE "Spezial:Meine Sprache/REKRUTIERE"
  [ZERSTÖRE]: /Spezial:Meine_Sprache/ZERST%C3%96RE "Spezial:Meine Sprache/ZERSTÖRE"
  [FOLGE]: /Spezial:Meine_Sprache/FOLGE "Spezial:Meine Sprache/FOLGE"
  [BEFÖRDERE]: /Spezial:Meine_Sprache/BEF%C3%96RDERE "Spezial:Meine Sprache/BEFÖRDERE"
  [BEZAHLE NICHT]: /Spezial:Meine_Sprache/BEZAHLE "Spezial:Meine Sprache/BEZAHLE"
  [STIRB]: /Spezial:Meine_Sprache/STIRB "Spezial:Meine Sprache/STIRB"
  [ZAUBERE]: /Spezial:Meine_Sprache/ZAUBERE "Spezial:Meine Sprache/ZAUBERE"
  [LEHRE]: /Spezial:Meine_Sprache/LEHRE "Spezial:Meine Sprache/LEHRE"
  [LERNE]: /Spezial:Meine_Sprache/LERNE "Spezial:Meine Sprache/LERNE"
  [FORSCHE]: /Spezial:Meine_Sprache/FORSCHE "Spezial:Meine Sprache/FORSCHE"
  [PFLANZE]: /Spezial:Meine_Sprache/PFLANZE "Spezial:Meine Sprache/PFLANZE"
  [SPIONIERE]: /Spezial:Meine_Sprache/SPIONIERE "Spezial:Meine Sprache/SPIONIERE"
  [ZÜCHTE]: /Spezial:Meine_Sprache/Z%C3%9CCHTE "Spezial:Meine Sprache/ZÜCHTE"
  [UNTERHALTE]: /Spezial:Meine_Sprache/UNTERHALTE "Spezial:Meine Sprache/UNTERHALTE"
  [ARBEITE]: /Spezial:Meine_Sprache/ARBEITE "Spezial:Meine Sprache/ARBEITE"
  [TREIBE]: /Spezial:Meine_Sprache/TREIBE "Spezial:Meine Sprache/TREIBE"
  [KAUFE]: /Spezial:Meine_Sprache/KAUFE "Spezial:Meine Sprache/KAUFE"
  [VERKAUFE]: /Spezial:Meine_Sprache/VERKAUFE "Spezial:Meine Sprache/VERKAUFE"
  [BEKLAUE]: ./camouflage.md "Spezial:Meine Sprache/BEKLAUE"
  [NACH]: /Spezial:Meine_Sprache/NACH "Spezial:Meine Sprache/NACH"
  [ROUTE]: /Spezial:Meine_Sprache/ROUTE "Spezial:Meine Sprache/ROUTE"
  [FAHRE]: /Spezial:Meine_Sprache/FAHRE "Spezial:Meine Sprache/FAHRE"
  [TRANSPORTIERE]: /Spezial:Meine_Sprache/TRANSPORTIERE "Spezial:Meine Sprache/TRANSPORTIERE"
  [DEFAULT]: /Spezial:Meine_Sprache/DEFAULT "Spezial:Meine Sprache/DEFAULT"
  [SORTIERE]: /Spezial:Meine_Sprache/SORTIERE "Spezial:Meine Sprache/SORTIERE"
  [NUMMER]: /Spezial:Meine_Sprache/NUMMER "Spezial:Meine Sprache/NUMMER"
  [Erläuterungen]: #Erläuterungen
  [Materialpool]: /Materialpool "Materialpool"
  [Befehle]: /Spezial:Meine_Sprache/Befehle "Spezial:Meine Sprache/Befehle"
  [Kurzbeschreibung]: /Spezial:Meine_Sprache/Kurzbeschreibung "Spezial:Meine Sprache/Kurzbeschreibung"
  [Befehlsreihenfolge (E3)]: /Spezial:Meine_Sprache/Befehlsreihenfolge_(E3) "Spezial:Meine Sprache/Befehlsreihenfolge (E3)"
  [https://wiki.eressea.de/index.php?title=Befehlsreihenfolge/de&oldid=13925]: https://wiki.eressea.de/index.php?title=Befehlsreihenfolge/de&oldid=13925
  [Kategorien]: /Spezial:Kategorien "Spezial:Kategorien"
  [1]: /Kategorie:Befehle "Kategorie:Befehle"
  [Regeln/de]: /index.php?title=Kategorie:Regeln/de&action=edit&redlink=1 "Kategorie:Regeln/de (Seite nicht vorhanden)"
