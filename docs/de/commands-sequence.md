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

|--------------|--------------------|
| Weiterlesen: | [Kurzbeschreibung] |

[Kurzbeschreibung]: ./commands-list.md "Kurzbeschreibung"

<!-- From [https://wiki.eressea.de/index.php?title=Befehlsreihenfolge/de&oldid=13925] -->

  [GRUPPE]: ./cmd-group.md "GRUPPE"
  [MACHE TEMP]: ./cmd-make.md "MACHE"
  [BENENNE]: ./cmd-name.md "BENENNE"
  [BESCHREIBE]: ./cmd-describe.md "BESCHREIBE"
  [BEWACHE NICHT]: ./cmd-guard.md "BEWACHE"
  [HELFE]: ./cmd-help.md "HELFE"
  [KÄMPFE]: ./cmd-combat.md "KÄMPFE"
  [KAMPFZAUBER]: ./cmd-combatspell.md "KAMPFZAUBER"
  [TARNE]: ./cmd-hide.md "TARNE"
  [URSPRUNG]: ./cmd-origin.md "URSPRUNG"
  [ZEIGE]: ./cmd-show.md "ZEIGE"
  [BANNER]: ./cmd-banner.md "BANNER"
  [EMAIL]: ./cmd-email.md "EMAIL"
  [OPTION]: ./cmd-option.md "OPTION"
  [PASSWORT]: ./cmd-password.md "PASSWORT"
  [KONTAKTIERE]: ./cmd-contact.md "KONTAKTIERE"
  [BOTSCHAFT]: ./cmd-message.md "BOTSCHAFT"
  [BETRETE]: ./cmd-enter.md "BETRETE"
  [BENUTZE]: ./cmd-use.md "BENUTZE"
  [VERLASSE]: ./cmd-leave.md "VERLASSE"
  [ATTACKIERE]: ./cmd-attack.md "ATTACKIERE"
  [RESERVIERE]: ./cmd-reserve.md "RESERVIERE"
  [BEANSPRUCHE]: ./cmd-claim.md "BEANSPRUCHE"
  [GIB KOMMANDO]: ./cmd-give.md "GIB"
  [VERGISS]: ./cmd-forget.md "VERGISS"
  [REKRUTIERE]: ./silver.md#recruiting "REKRUTIERE"
  [ZERSTÖRE]: ./cmd-destroy.md "ZERSTÖRE"
  [FOLGE]: ./cmd-follow.md "FOLGE"
  [BEFÖRDERE]: ./cmd-promote.md "BEFÖRDERE"
  [BEZAHLE NICHT]: ./cmd-pay-not.md "BEZAHLE"
  [STIRB]: ./cmd-quit.md "STIRB"
  [ZAUBERE]: ./cmd-cast.md "ZAUBERE"
  [LEHRE]: ./cmd-teach.md "LEHRE"
  [LERNE]: ./cmd-learn.md "LERNE"
  [FORSCHE]: ./cmd-research.md "FORSCHE"
  [PFLANZE]: ./cmd-plant.md "PFLANZE"
  [SPIONIERE]: ./cmd-spy.md "SPIONIERE"
  [ZÜCHTE]: ./cmd-grow.md "ZÜCHTE"
  [UNTERHALTE]: ./cmd-entertain.md "UNTERHALTE"
  [ARBEITE]: ./cmd-work.md "ARBEITE"
  [TREIBE]: ./cmd-tax.md "TREIBE"
  [KAUFE]: ./cmd-buy.md "KAUFE"
  [VERKAUFE]: ./cmd-sell.md "VERKAUFE"
  [BEKLAUE]: ./camouflage.md "BEKLAUE"
  [NACH]: ./cmd-move.md "NACH"
  [ROUTE]: ./cmd-route.md "ROUTE"
  [FAHRE]: ./cmd-ride.md "FAHRE"
  [TRANSPORTIERE]: ./cmd-carry.md "TRANSPORTIERE"
  [DEFAULT]: ./cmd-default.md "DEFAULT"
  [SORTIERE]: ./cmd-sort.md "SORTIERE"
  [NUMMER]: ./cmd-number.md "NUMMER"
  [Erläuterungen]: #erläuterungen
  [Materialpool]: ./items-pool.md "Materialpool"
  [Befehle]: ./commands.md "Befehle"
  [Befehlsreihenfolge (E3)]: ./commands.mdsreihenfolge_(E3) "Befehlsreihenfolge (E3)"
