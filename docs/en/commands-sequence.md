# Orders Sequence

Eressea's orders are evaluated in a fixed sequence. Orders with the same number are executed at the same time or the exact sequence is irrelevant.

1. new default orders are set
2. [GROUP], [MAKE TEMP]
3. [NAME], [DESCRIBE], [GUARD NOT], [HELP], [COMBAT], [COMBATSPELL], [HIDE], [ORIGIN], [SHOW]
4. [BANNER], [EMAIL], [OPTION], [PASSWORD]
5. [CONTACT]
6. [MESSAGE]
7. [ENTER]; 1st attempt
8. [USE]
9. [LEAVE]
10. [ENTER]; 2nd attempt
11. [ATTACK]
12. [RESERVE], [CLAIM]
13. [ENTER]; 3rd attempt
14. [GIVE CONTROL]
15. [FORGET]
16. [GIVE][GIVE CONTROL]
17. [RECRUIT]\*
18. [DESTROY]
19. [FOLLOW] is set
20. [PROMOTE]
21. [PAY NOT]; stops operation and maintenance costs for the corresponding building.
22. maintenance costs for buildings are accounted for. If they cannot be raised, the building has no effect for that turn!
23. [QUIT]
24. [CAST]
25. [TEACH]
26. [LEARN]
27. [MAKE][MAKE TEMP] \*
28. [RESEARCH], [PLANT], [SPY], [GROW]
29. [ENTERTAIN] \*
30. [WORK] \*
31. [TAX] \*
32. [BUY] \*
33. [SELL] \*
34. [STEAL] \*
35. ships with insufficient crew suffer damage
36. ENTER; 4th attempt
37. [MOVE] and [ROUTE], including [RIDE] and [CARRY] are executed, and units ordered to FOLLOW other units do so
38. [GUARD][GUARD NOT]; this only works if the unit has not moved.
39. ships drift on the high seas
40. [DEFAULT]
41. empty units are removed
42. peasants, horses and trees grow, if possible; the remaining peasants move into other regions
43. silver for units maintenance is subtracted
44. [SORT]
45. [NUMBER]

\* Orders marked like this are divided "fairly"; see [notes] below.

However, the orders do not necessarily have to be entered in this order. It is perfectly permissible to enter the following:

    GIVE TEMP 5 300 Silver
    MAKE TEMP 5
      RECRUIT 1
      COMBAT NOT
      LEARN FORESTRY
    END

Here the orders sequence is: The new unit is first created, no longer joins combats, receives 300 silver, recruits 1, and finally learns forestry - although this is not the sequence in which the orders were written.

## Notes

Orders of the same rank from different units are normally processed in the sequence in which they appear in the report. For example, first all GIVE orders of the first unit, then all GIVE orders of the second unit, then all RECRUIT orders of the first unit, then the second and so on. The [item pool] also usually works in this way: units higher up in the region are first "asked" if the can share a certain item. However, this sequence can be changed by certain commands. These include `ENTER, LEAVE, MAKE TEMP, GIVE CONTROL` and `GIVE SHIP`. The exact behavior is not guaranteed! Therefore, if in doubt, give orders in such a way that the unit sequence does not matter.

For orders where the result has an upper limit, for example the maximum number of trees in the region for `MAKE wood`, the maximum number of recruits to `RECRUIT` or the region's money for `ENTERTAIN` and `TAX`, it may happen that several units are in competition. In this case, we try to distribute the scarce good in proportion to the quantity that each unit could produce if it were unlimited. In this case, there may be gaps and a unit may end up with nothing. The `SELL`, `BUY` and `WORK` orders are also affected.

About ENTER 1st/2nd/3rd/4th attempt  
This means that you can still enter a castle before an attack. After the fight, a unit may try to enter again, as the former owner might be dead or has fled in the meantime.

It does not mean that units leaving a ship can still attack in the same turn, as the server remembers who left ships and intercepts it accordingly.

## See also

- [orders]
- [short description]
- [short description DE/EN]
- [Befehlsreihenfolge (E3)]

|     |     |
| --- | --- |
| Continue reading: | [Short Description] |

[Short Description]: /Spezial:Meine_Sprache/Kurzbeschreibung "Spezial:Meine Sprache/Kurzbeschreibung"  

Abgerufen von „[https://wiki.eressea.de/index.php?title=Befehlsreihenfolge/en&oldid=13988]“

[Kategorien][]:

- [Befehle]
- [Regeln/en]

  [GROUP]: /Spezial:Meine_Sprache/GRUPPE "Spezial:Meine Sprache/GRUPPE"
  [MAKE TEMP]: /Spezial:Meine_Sprache/MACHE "Spezial:Meine Sprache/MACHE"
  [NAME]: /Spezial:Meine_Sprache/BENENNE "Spezial:Meine Sprache/BENENNE"
  [DESCRIBE]: /Spezial:Meine_Sprache/BESCHREIBE "Spezial:Meine Sprache/BESCHREIBE"
  [GUARD NOT]: /Spezial:Meine_Sprache/BEWACHE "Spezial:Meine Sprache/BEWACHE"
  [HELP]: /Spezial:Meine_Sprache/HELFE "Spezial:Meine Sprache/HELFE"
  [COMBAT]: /Spezial:Meine_Sprache/K%C3%84MPFE "Spezial:Meine Sprache/KÄMPFE"
  [COMBATSPELL]: /Spezial:Meine_Sprache/KAMPFZAUBER "Spezial:Meine Sprache/KAMPFZAUBER"
  [HIDE]: /Spezial:Meine_Sprache/TARNE "Spezial:Meine Sprache/TARNE"
  [ORIGIN]: /Spezial:Meine_Sprache/URSPRUNG "Spezial:Meine Sprache/URSPRUNG"
  [SHOW]: /Spezial:Meine_Sprache/ZEIGE "Spezial:Meine Sprache/ZEIGE"
  [BANNER]: /Spezial:Meine_Sprache/BANNER "Spezial:Meine Sprache/BANNER"
  [EMAIL]: /Spezial:Meine_Sprache/EMAIL "Spezial:Meine Sprache/EMAIL"
  [OPTION]: /Spezial:Meine_Sprache/OPTION "Spezial:Meine Sprache/OPTION"
  [PASSWORD]: /Spezial:Meine_Sprache/PASSWORT "Spezial:Meine Sprache/PASSWORT"
  [CONTACT]: /Spezial:Meine_Sprache/KONTAKTIERE "Spezial:Meine Sprache/KONTAKTIERE"
  [MESSAGE]: /Spezial:Meine_Sprache/BOTSCHAFT "Spezial:Meine Sprache/BOTSCHAFT"
  [ENTER]: /Spezial:Meine_Sprache/BETRETE "Spezial:Meine Sprache/BETRETE"
  [USE]: /Spezial:Meine_Sprache/BENUTZE "Spezial:Meine Sprache/BENUTZE"
  [LEAVE]: /Spezial:Meine_Sprache/VERLASSE "Spezial:Meine Sprache/VERLASSE"
  [ATTACK]: /Spezial:Meine_Sprache/ATTACKIERE "Spezial:Meine Sprache/ATTACKIERE"
  [RESERVE]: /Spezial:Meine_Sprache/RESERVIERE "Spezial:Meine Sprache/RESERVIERE"
  [CLAIM]: /Spezial:Meine_Sprache/BEANSPRUCHE "Spezial:Meine Sprache/BEANSPRUCHE"
  [GIVE CONTROL]: /Spezial:Meine_Sprache/GIB "Spezial:Meine Sprache/GIB"
  [FORGET]: /Spezial:Meine_Sprache/VERGISS "Spezial:Meine Sprache/VERGISS"
  [RECRUIT]: /Spezial:Meine_Sprache/REKRUTIERE "Spezial:Meine Sprache/REKRUTIERE"
  [DESTROY]: /Spezial:Meine_Sprache/ZERST%C3%96RE "Spezial:Meine Sprache/ZERSTÖRE"
  [FOLLOW]: /Spezial:Meine_Sprache/FOLGE "Spezial:Meine Sprache/FOLGE"
  [PROMOTE]: /Spezial:Meine_Sprache/BEF%C3%96RDERE "Spezial:Meine Sprache/BEFÖRDERE"
  [PAY NOT]: /Spezial:Meine_Sprache/BEZAHLE "Spezial:Meine Sprache/BEZAHLE"
  [QUIT]: /Spezial:Meine_Sprache/STIRB "Spezial:Meine Sprache/STIRB"
  [CAST]: /Spezial:Meine_Sprache/ZAUBERE "Spezial:Meine Sprache/ZAUBERE"
  [TEACH]: /Spezial:Meine_Sprache/LEHRE "Spezial:Meine Sprache/LEHRE"
  [LEARN]: /Spezial:Meine_Sprache/LERNE "Spezial:Meine Sprache/LERNE"
  [RESEARCH]: /Spezial:Meine_Sprache/FORSCHE "Spezial:Meine Sprache/FORSCHE"
  [PLANT]: /Spezial:Meine_Sprache/PFLANZE "Spezial:Meine Sprache/PFLANZE"
  [SPY]: /Spezial:Meine_Sprache/SPIONIERE "Spezial:Meine Sprache/SPIONIERE"
  [GROW]: /Spezial:Meine_Sprache/Z%C3%9CCHTE "Spezial:Meine Sprache/ZÜCHTE"
  [ENTERTAIN]: /Spezial:Meine_Sprache/UNTERHALTE "Spezial:Meine Sprache/UNTERHALTE"
  [WORK]: /Spezial:Meine_Sprache/ARBEITE "Spezial:Meine Sprache/ARBEITE"
  [TAX]: /Spezial:Meine_Sprache/TREIBE "Spezial:Meine Sprache/TREIBE"
  [BUY]: /Spezial:Meine_Sprache/KAUFE "Spezial:Meine Sprache/KAUFE"
  [SELL]: /Spezial:Meine_Sprache/VERKAUFE "Spezial:Meine Sprache/VERKAUFE"
  [STEAL]: ./camouflage.md "Spezial:Meine Sprache/BEKLAUE"
  [MOVE]: /Spezial:Meine_Sprache/NACH "Spezial:Meine Sprache/NACH"
  [ROUTE]: /Spezial:Meine_Sprache/ROUTE "Spezial:Meine Sprache/ROUTE"
  [RIDE]: /Spezial:Meine_Sprache/FAHRE "Spezial:Meine Sprache/FAHRE"
  [CARRY]: /Spezial:Meine_Sprache/TRANSPORTIERE "Spezial:Meine Sprache/TRANSPORTIERE"
  [DEFAULT]: /Spezial:Meine_Sprache/DEFAULT "Spezial:Meine Sprache/DEFAULT"
  [SORT]: /Spezial:Meine_Sprache/SORTIERE "Spezial:Meine Sprache/SORTIERE"
  [NUMBER]: /Spezial:Meine_Sprache/NUMMER "Spezial:Meine Sprache/NUMMER"
  [notes]: #notes
  [item pool]: /Spezial:Meine_Sprache/Materialpool "Spezial:Meine Sprache/Materialpool"
  [orders]: /Spezial:Meine_Sprache/Befehle "Spezial:Meine Sprache/Befehle"
  [short description DE/EN]: /Spezial:Meine_Sprache/Diskussion:Kurzbeschreibung "Spezial:Meine Sprache/Diskussion:Kurzbeschreibung"
  [Befehlsreihenfolge (E3)]: /Spezial:Meine_Sprache/Befehlsreihenfolge_(E3) "Spezial:Meine Sprache/Befehlsreihenfolge (E3)"
  [https://wiki.eressea.de/index.php?title=Befehlsreihenfolge/en&oldid=13988]: https://wiki.eressea.de/index.php?title=Befehlsreihenfolge/en&oldid=13988
  [Kategorien]: /Spezial:Kategorien "Spezial:Kategorien"
  [Befehle]: /Kategorie:Befehle "Kategorie:Befehle"
  [Regeln/en]: /index.php?title=Kategorie:Regeln/en&action=edit&redlink=1 "Kategorie:Regeln/en (Seite nicht vorhanden)"
