---
# cSpell:locale de
alias: befehlsreihenfolge
---

# Befehlsreihenfolge

Die Befehle von Eressea werden in einer festen Reihenfolge ausgewertet. Befehle, die unter der selben Nummer stehen, werden zur gleichen Zeit ausgeführt oder die Reihenfolge spielt keine Rolle.

1. neue Default-Befehle werden gesetzt
2. [`GRUPPE`][bef-gruppe], [`MACHE TEMP`][bef-mache]
3. [`BENENNE`][bef-benenne], [`BESCHREIBE`][bef-beschreibe], [`BEWACHE NICHT`][bef-bewache], [`HELFE`][bef-helfe], [`KÄMPFE`][bef-kampfe-id], [`KAMPFZAUBER`][bef-kampfzauber], [`TARNE`][bef-tarne], [`URSPRUNG`][bef-ursprung], [`ZEIGE`][bef-zeige]
4. [`BANNER`][bef-banner], [`EMAIL`][bef-email], [`OPTION`][bef-option], [`PASSWORT`][bef-passwort]
5. [`KONTAKTIERE`][bef-kontaktiere]
6. [`BOTSCHAFT`][bef-botschaft]
7. [`BETRETE`][bef-betrete]; 1. Versuch
8. [`BENUTZE`][bef-benutze]
9. [`VERLASSE`][bef-verlasse]
10. [`BETRETE`][bef-betrete]; 2. Versuch
11. [`ATTACKIERE`][bef-attackiere]
12. [`RESERVIERE`][bef-reserviere], [`BEANSPRUCHE`][bef-beanspruche]
13. [`BETRETE`][bef-betrete]; 3. Versuch
14. [`GIB KOMMANDO`][bef-gib]
15. [`VERGISS`][bef-vergiss]
16. [`GIB`][bef-gib]
17. [`REKRUTIERE`][bef-rekrutiere] \*
18. [`ZERSTÖRE`][bef-zerstore-id]
19. [`FOLGE`][bef-folge] wird gesetzt
20. [`BEFOERDERE`][bef-befordere-id]
21. [`BEZAHLE NICHT`][bef-bezahle-nicht] Stellt Funktion und Unterhaltskosten für das entsprechende Gebäude ein.
22. Unterhaltskosten für unterhaltspflichtige Gebäude fallen an; sonst haben sie keine Funktion!
23. [`STIRB`][bef-stirb]
24. [`ZAUBERE`][bef-zaubere]
25. [`LEHRE`][bef-lehre]
26. [`LERNE`][bef-lerne]
27. [`MACHE TEMP`][bef-mache] \*
28. [`FORSCHE`][bef-forsche], [`PFLANZE`][bef-pflanze], [`SPIONIERE`][bef-spioniere], [ZÜCHTE][bef-zuchte-id]
29. [`UNTERHALTE`][bef-unterhalte] \*
30. [`ARBEITE`][bef-arbeite] \*
31. [`TREIBE`][bef-treibe] \*
32. [`KAUFE`][bef-kaufe] \*
33. [`VERKAUFE`][bef-verkaufe] \*
34. [`BEKLAUE`][bef-beklaue] \*
35. Schiffe mit mangelnder Besatzung nehmen Schäden
36. `BETRETE`[bef-betrete]; 4. Versuch
37. [`NACH`][bef-nach] und [`ROUTE`][bef-route], dabei wird auch [`FAHRE`][bef-fahre] und [`TRANSPORTIERE`][bef-transportiere] ausgeführt und Verfolger folgen
38. [`BEWACHE NICHT`][bef-bewache] an; das geht nur, wenn die Einheit sich nicht bewegt hat
39. Schiffe treiben auf hoher See
40. [`DEFAULT`][bef-default]
41. leere Einheiten werden beseitigt
42. die Bauern, Pferde und Wälder vermehren sich, falls möglich; die übriggebliebenen Bauern wandern umher
43. Silber für die Versorgung der Einheiten wird abgezogen
44. [`SORTIERE`][bef-sortiere]
45. [`NUMMER`][bef-nummer]

\* So markierte Befehle werden "gerecht" aufgeteilt. Siehe [Erläuterungen][erlauterungen-id] unten.

Die Befehle müssen aber nicht zwingend in dieser Reihenfolge eingegeben werden. Es ist durchaus zulässig, folgendes einzugeben:

    GIB TEMP 5 300 Silber
    MACHE TEMP 5
      REKRUTIERE 1
      KÄMPFE NICHT
      LERNE HOLZFÄLLEN
    ENDE

Die neue Einheit wird zuerst erschaffen, kämpft nicht mehr, erhält 300 Silber, rekrutiert 1 und lernt schlussendlich Holzfällen - obwohl das nicht der Reihenfolge entspricht, in der die Befehle eingegeben wurden.

[](){ #erlauterungen-id }

## Erläuterungen

Gleichrangige Befehle verschiedener Einheiten werden normalerweise in der Reihenfolge abgearbeitet, wie sie im Report erscheinen.  
Also zum Beispiel erst alle GIB-Befehle der ersten Einheit, dann alle GIB-Befehle der zweiten Einheit, später alle `REKRUTIERE`-Befehle der ersten Einheit, dann der zweiten und so fort.  
Auch der [Materialpool][materialpool] funktioniert üblicherweise in dieser Reihenfolge: Einheiten, die weiter oben in der Reihenfolge stehen, werden also zuerst "befragt", ob sie einen Gegenstand hergeben können.  
Die Reihenfolge kann sich jedoch durch bestimmte Befehle verändern. Dazu gehören `BETRETE`, `VERLASSE`, `MACHE TEMP`, `GIB KOMMANDO` und `GIB SCHIFF`.  
Das genaue Verhalten wird nicht garantiert! Deshalb sollte man im Zweifel Befehle so geben, dass die Einheitenreihenfolge dafür keine Rolle spielt.

Bei Befehlen, deren Resultat eine Obergrenze hat, z.B. die maximale Menge an Bäumen in der Region bei `MACHE Holz`, die maximale Zahl von Rekruten bei `REKRUTIERE` oder dem Regionssilber bei `UNTERHALTE` und `TREIBE`, kann es vorkommen, dass mehrere Einheiten in Konkurrenz zueinander stehen. In diesem Fall wird versucht, das knappe Gut anteilig an der Menge zu verteilen, die jede Einheit produzieren könnte, wenn es unbegrenzt wäre. Hierbei kann es zu Abweichungen kommen, und eine Einheit eventuell leer ausgehen. Ebenfalls betroffen sind die Befehle `VERKAUFE, KAUFE` und `ARBEITE`.

Betrete 1./2./3./4. Versuch  
Das bedeutet, dass man vor einem Angriff noch eine Burg betreten kann. Nach dem Kampf, kann man es nochmal versuchen, denn die Vorbesitzer könnten inzwischen tot oder geflohen sein.

Es bedeutet nicht, dass Einheiten, die ein Schiff verlassen, noch in derselben Runde attackieren können, da sich der Server merkt, wer Schiffe verlassen hat, und das entsprechend abfängt.

## Siehe auch

- [Befehle][befehl]
- [Kurzbeschreibung][kurzbeschreibung]

Weiterlesen: [Kurzbeschreibung][kurzbeschreibung].

<!-- From [https://wiki.eressea.de/index.php?title=Befehlsreihenfolge/de&oldid=13925] -->

[bef-arbeite]: [[bef-arbeite]]
[bef-attackiere]: [[bef-attackiere]]
[bef-banner]: [[bef-banner]]
[bef-beanspruche]: [[bef-beanspruche]]
[bef-beklaue]: [[bef-beklaue]]
[bef-benenne]: [[bef-benenne]]
[bef-benutze]: [[bef-benutze]]
[bef-beschreibe]: [[bef-beschreibe]]
[bef-betrete]: [[bef-betrete]]
[bef-bewache]: [[bef-bewache]]
[bef-bezahle-nicht]: [[bef-bezahle-nicht]]
[bef-botschaft]: [[bef-botschaft]]
[bef-default]: [[bef-default]]
[bef-email]: [[bef-email]]
[bef-fahre]: [[bef-fahre]]
[bef-folge]: [[bef-folge]]
[bef-forsche]: [[bef-forsche]]
[bef-gib]: [[bef-gib]]
[bef-gruppe]: [[bef-gruppe]]
[bef-helfe]: [[bef-helfe]]
[bef-kampfzauber]: [[bef-kampfzauber]]
[bef-kaufe]: [[bef-kaufe]]
[bef-kontaktiere]: [[bef-kontaktiere]]
[bef-lehre]: [[bef-lehre]]
[bef-lerne]: [[bef-lerne]]
[bef-mache]: [[bef-mache]]
[bef-nach]: [[bef-nach]]
[bef-nummer]: [[bef-nummer]]
[bef-option]: [[bef-option]]
[bef-passwort]: [[bef-passwort]]
[bef-pflanze]: [[bef-pflanze]]
[bef-rekrutiere]: [[bef-rekrutiere]]
[bef-reserviere]: [[bef-reserviere]]
[bef-route]: [[bef-route]]
[bef-sortiere]: [[bef-sortiere]]
[bef-spioniere]: [[bef-spioniere]]
[bef-stirb]: [[bef-stirb]]
[bef-tarne]: [[bef-tarne]]
[bef-transportiere]: [[bef-transportiere]]
[bef-treibe]: [[bef-treibe]]
[bef-unterhalte]: [[bef-unterhalte]]
[bef-ursprung]: [[bef-ursprung]]
[bef-vergiss]: [[bef-vergiss]]
[bef-verkaufe]: [[bef-verkaufe]]
[bef-verlasse]: [[bef-verlasse]]
[bef-zaubere]: [[bef-zaubere]]
[bef-zeige]: [[bef-zeige]]
