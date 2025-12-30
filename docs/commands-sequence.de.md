---
# cSpell:locale de
alias: befehlsreihenfolge
---
# Befehlsreihenfolge

Die Befehle von Eressea werden in einer festen Reihenfolge ausgewertet. Befehle, die unter der selben Nummer stehen, werden zur gleichen Zeit ausgeführt oder die Reihenfolge spielt keine Rolle.

1. neue Default-Befehle werden gesetzt
2. [[bef-gruppe]], [[bef-mache|MACHE TEMP]]
3. [[bef-benenne]], [[bef-beschreibe]], [BEWACHE NICHT], [[bef-helfe]], [KÄMPFE], [[bef-kampfzauber]], [[bef-tarne]], [[bef-ursprung]], [[bef-zeige]]
4. [[bef-banner]], [[bef-email]], [[bef-option]], [[bef-passwort]]
5. [[bef-kontaktiere]]
6. [[bef-botschaft]]
7. [[bef-betrete]]; 1. Versuch
8. [[bef-benutze]]
9. [[bef-verlasse]]
10. [[bef-betrete]]; 2. Versuch
11. [[bef-attackiere]]
12. [[bef-reserviere]], [[bef-beanspruche]]
13. [[bef-betrete]]; 3. Versuch
14. [GIB KOMMANDO]
15. [[bef-vergiss]]
16. [[bef-gib]][GIB KOMMANDO]
17. [[bef-rekrutiere]] \*
18. [ZERSTÖRE]
19. [[bef-folge]] wird gesetzt
20. [[bef-befoerdere]]
21. [BEZAHLE NICHT] Stellt Funktion und Unterhaltskosten für das entsprechende Gebäude ein.
22. Unterhaltskosten für unterhaltspflichtige Gebäude fallen an; sonst haben sie keine Funktion!
23. [[bef-stirb]]
24. [[bef-zaubere]]
25. [[bef-lehre]]
26. [[bef-lerne]]
27. [[bef-mache|MACHE TEMP]] \*
28. [[bef-forsche]], [[bef-pflanze]], [[bef-spioniere]], [ZÜCHTE]
29. [[bef-unterhalte]] \*
30. [[bef-arbeite]] \*
31. [[bef-treibe]] \*
32. [[bef-kaufe]] \*
33. [[bef-verkaufe]] \*
34. [[bef-beklaue]] \*
35. Schiffe mit mangelnder Besatzung nehmen Schäden
36. BETRETE; 4. Versuch
37. [[bef-nach]] und [[bef-route]], dabei wird auch [[bef-fahre]] und [[bef-transportiere]] ausgeführt und Verfolger folgen
38. [[bef-bewache|BEWACHE NICHT]] an; das geht nur, wenn die Einheit sich nicht bewegt hat
39. Schiffe treiben auf hoher See
40. [[bef-default]]
41. leere Einheiten werden beseitigt
42. die Bauern, Pferde und Wälder vermehren sich, falls möglich; die übriggebliebenen Bauern wandern umher
43. Silber für die Versorgung der Einheiten wird abgezogen
44. [[bef-sortiere]]
45. [[bef-nummer]]

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

Weiterlesen: [Kurzbeschreibung].

[Kurzbeschreibung]: ./commands-list.md

<!-- From [https://wiki.eressea.de/index.php?title=Befehlsreihenfolge/de&oldid=13925] -->

[BEWACHE NICHT]: ./cmd-guard.md
[KÄMPFE]: ./cmd-combat.md
[GIB KOMMANDO]: ./cmd-give.md
[ZERSTÖRE]: ./cmd-destroy.md
[BEZAHLE NICHT]: ./cmd-pay-not.md
[ZÜCHTE]: ./cmd-grow.md
[Erläuterungen]: ./#erlauterungen
[Materialpool]: ./items-pool.md
[Befehle]: ./commands.md
