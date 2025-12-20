---
# cSpell:locale en
alias:
    name: orders-sequence
    text: Orders sequence
---
# Orders sequence

Eressea's orders are evaluated in a fixed sequence. Orders with the same number are executed at the same time or the exact sequence is irrelevant.

1. new default orders are set
2. [[cmd-group]], [MAKE TEMP]
3. [[cmd-name]], [[cmd-describe]], [GUARD NOT], [[cmd-help]], [[cmd-combat]], [[cmd-combatspell]], [[cmd-hide]], [[cmd-origin]], [[cmd-show]]
4. [[cmd-banner]], [[cmd-email]], [[cmd-option]], [[cmd-password]]
5. [[cmd-contact]]
6. [[cmd-message]]
7. [[cmd-enter]]; 1st attempt
8. [[cmd-use]]
9. [[cmd-leave]]
10. [[cmd-enter]]; 2nd attempt
11. [[cmd-attack]]
12. [[cmd-reserve]], [[cmd-claim]]
13. [[cmd-enter]]; 3rd attempt
14. [GIVE CONTROL]
15. [[cmd-forget]]
16. [[cmd-give]][GIVE CONTROL]
17. [[cmd-recruit]]\*
18. [[cmd-destroy]]
19. [[cmd-follow]] is set
20. [[cmd-promote]]
21. [PAY NOT]; stops operation and maintenance costs for the corresponding building.
22. maintenance costs for buildings are accounted for. If they cannot be raised, the building has no effect for that turn!
23. [[cmd-quit]]
24. [[cmd-cast]]
25. [[cmd-teach]]
26. [[cmd-learn]]
27. [[cmd-make]][MAKE TEMP] \*
28. [[cmd-research]], [[cmd-plant]], [[cmd-spy]], [[cmd-grow]]
29. [[cmd-entertain]] \*
30. [[cmd-work]] \*
31. [[cmd-tax]] \*
32. [[cmd-buy]] \*
33. [[cmd-sell]] \*
34. [[cmd-steal]] \*
35. ships with insufficient crew suffer damage
36. ENTER; 4th attempt
37. [[cmd-move]] and [[cmd-route]], including [[cmd-ride]] and [[cmd-carry]] are executed, and units ordered to FOLLOW other units do so
38. [[cmd-guard]][GUARD NOT]; this only works if the unit has not moved.
39. ships drift on the high seas
40. [[cmd-default]]
41. empty units are removed
42. peasants, horses and trees grow, if possible; the remaining peasants move into other regions
43. silver for units maintenance is subtracted
44. [[cmd-sort]]
45. [[cmd-number]]

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

[Short Description]: ./commands-list.md  

<!-- From [https://wiki.eressea.de/index.php?title=Befehlsreihenfolge/en&oldid=13988] -->

[GROUP]: ./cmd-group.md
[MAKE TEMP]: ./cmd-make.md
[NAME]: ./cmd-name.md
[DESCRIBE]: ./cmd-describe.md
[GUARD NOT]: ./cmd-guard.md
[HELP]: ./cmd-help.md
[COMBAT]: ./cmd-combat.md
[COMBATSPELL]: ./cmd-combatspell.md
[HIDE]: ./cmd-hide.md
[ORIGIN]: ./cmd-origin.md
[SHOW]: ./cmd-show.md
[BANNER]: ./cmd-banner.md
[EMAIL]: ./cmd-email.md
[OPTION]: ./cmd-option.md
[PASSWORD]: ./cmd-password.md
[CONTACT]: ./cmd-contact.md
[MESSAGE]: ./cmd-message.md
[ENTER]: ./cmd-enter.md
[USE]: ./cmd-use.md
[LEAVE]: ./cmd-leave.md
[ATTACK]: ./cmd-attack.md
[RESERVE]: ./cmd-reserve.md
[CLAIM]: ./cmd-claim.md
[GIVE CONTROL]: ./cmd-give.md
[FORGET]: ./cmd-forget.md
[RECRUIT]: ./silver.md#recruiting
[DESTROY]: ./cmd-destroy.md
[FOLLOW]: ./cmd-follow.md
[PROMOTE]: ./cmd-promote.md
[PAY NOT]: ./cmd-pay-not.md
[QUIT]: ./cmd-quit.md
[CAST]: ./cmd-cast.md
[TEACH]: ./cmd-teach.md
[LEARN]: ./cmd-learn.md
[RESEARCH]: ./cmd-research.md
[PLANT]: ./cmd-plant.md
[SPY]: ./cmd-spy.md
[GROW]: ./cmd-grow.md
[ENTERTAIN]: ./cmd-entertain.md
[WORK]: ./cmd-work.md
[TAX]: ./cmd-tax.md
[BUY]: ./cmd-buy.md
[SELL]: ./cmd-sell.md
[STEAL]: ./camouflage.md
[MOVE]: ./cmd-move.md
[ROUTE]: ./cmd-route.md
[RIDE]: ./cmd-ride.md
[CARRY]: ./cmd-carry.md
[DEFAULT]: ./cmd-default.md
[SORT]: ./cmd-sort.md
[NUMBER]: ./cmd-number.md
[notes]: #notes
[item pool]: ./items-pool.md
[orders]: ./commands.md
[short description DE/EN]: ./commands-list.md
