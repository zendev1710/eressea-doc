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

Continue reading: [Short Description].

[Short Description]: ./commands-list.md "Kurzbeschreibung"  

<!-- From [https://wiki.eressea.de/index.php?title=Befehlsreihenfolge/en&oldid=13988] -->

[GROUP]: ./cmd-group.md "GROUP"
[MAKE TEMP]: ./cmd-make.md "MAKE"
[NAME]: ./cmd-name.md "NAME"
[DESCRIBE]: ./cmd-describe.md "DESCRIBE"
[GUARD NOT]: ./cmd-guard.md "GUARD"
[HELP]: ./cmd-help.md "HELP"
[COMBAT]: ./cmd-combat.md "COMBAT"
[COMBATSPELL]: ./cmd-combatspell.md "COMBATSPELL"
[HIDE]: ./cmd-hide.md "HIDE"
[ORIGIN]: ./cmd-origin.md "ORIGIN"
[SHOW]: ./cmd-show.md "SHOW"
[BANNER]: ./cmd-banner.md "BANNER"
[EMAIL]: ./cmd-email.md "EMAIL"
[OPTION]: ./cmd-option.md "OPTION"
[PASSWORD]: ./cmd-password.md "PASSWORD"
[CONTACT]: ./cmd-contact.md "CONTACT"
[MESSAGE]: ./cmd-message.md "MESSAGE"
[ENTER]: ./cmd-enter.md "ENTER"
[USE]: ./cmd-use.md "USE"
[LEAVE]: ./cmd-leave.md "LEAVE"
[ATTACK]: ./cmd-attack.md "ATTACK"
[RESERVE]: ./cmd-reserve.md "RESERVE"
[CLAIM]: ./cmd-claim.md "CLAIM"
[GIVE CONTROL]: ./cmd-give.md "GIVE"
[FORGET]: ./cmd-forget.md "FORGET"
[RECRUIT]: ./silver.md#recruiting "RECRUIT"
[DESTROY]: ./cmd-destroy.md "DESTROY"
[FOLLOW]: ./cmd-follow.md "FOLLOW"
[PROMOTE]: ./cmd-promote.md "PROMOTE"
[PAY NOT]: ./cmd-pay-not.md "PAY"
[QUIT]: ./cmd-quit.md "QUIT"
[CAST]: ./cmd-cast.md "CAST"
[TEACH]: ./cmd-teach.md "TEACH"
[LEARN]: ./cmd-learn.md "LEARN"
[RESEARCH]: ./cmd-research.md "RESEARCH"
[PLANT]: ./cmd-plant.md "PLANT"
[SPY]: ./cmd-spy.md "SPY"
[GROW]: ./cmd-grow.md "GROW"
[ENTERTAIN]: ./cmd-entertain.md "ENTERTAIN"
[WORK]: ./cmd-work.md "WORK"
[TAX]: ./cmd-tax.md "TAX"
[BUY]: ./cmd-buy.md "BUY"
[SELL]: ./cmd-sell.md "SELL"
[STEAL]: ./camouflage.md "STEAL"
[MOVE]: ./cmd-move.md "MOVE"
[ROUTE]: ./cmd-route.md "ROUTE"
[RIDE]: ./cmd-ride.md "RIDE"
[CARRY]: ./cmd-carry.md "CARRY"
[DEFAULT]: ./cmd-default.md "DEFAULT"
[SORT]: ./cmd-sort.md "SORT"
[NUMBER]: ./cmd-number.md "NUMBER"
[notes]: #notes
[item pool]: ./items-pool.md "Materialpool"
[orders]: ./commands.md "Befehle"
[short description DE/EN]: ./commands-list.md "Diskussion:Kurzbeschreibung"
