# Séquence des ordres

Les ordres d'Eressea sont exécutés dans un ordre fixe. Les ordres qui sont dans une même séquence sont exécutés en même temps ou l'ordre d'exécution n'a aucune importance.

1. les nouveaux ordres par défaut sont définis
2. [GROUP], [MAKE TEMP]
3. [NAME], [DESCRIBE], [GUARD NOT], [HELP], [COMBAT], [COMBATSPELL], [HIDE], [ORIGIN], [SHOW]
4. [BANNER], [EMAIL], [OPTION], [PASSWORD]
5. [CONTACT]
6. [MESSAGE]
7. [ENTER]; 1. essai
8. [USE]
9. [LEAVE]
10. [ENTER]; 2. essai
11. [ATTACK]
12. [RESERVE], [CLAIM]
13. [ENTER]; 3. essai
14. [GIVE CONTROL]
15. [FORGET]
16. [GIVE][GIVE CONTROL]
17. [RECRUIT] \*
18. [DESTROY]
19. [FOLLOW] est défini
20. [PROMOTE]
21. [PAY NOT] définit pour la fonctionnalité et les coûts d'entretien du bâtiment concerné.
22. Les coûts d'entretien des bâtiments soumis à l'obligation d'entretien s'appliquent ; sinon, ils n'ont aucune fonctionnalité !
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
35. Les bateaux dont l'équipage est insuffisant subissent des dommages
36. [ENTER]; 4. essai
37. [MOVE] et [ROUTE], incluant [RIDE] et [CARRY] sont exécutés et les unités ayant reçu l'ordre de FOLLOW d'autres unités le font.
38. [GUARD][GUARD NOT] cela n'est possible que si l'unité n'a pas bougé.
39. Les bateaux dérivent en haute mer
40. [DEFAULT]
41. les unités vides sont supprimées
42. les paysans, les chevaux et les forêts se multiplient, si possible ; des paysans se déplacent vers d'autres régions.
43. les Silver pour l'entretien des unités est déduit
44. [SORT]
45. [NUMBER]

\* Les ordres ainsi marqués sont divisés "équitablement" ; voir [notes explicatives] ci-dessous.

Les ordres ne doivent toutefois pas nécessairement être saisis dans cet ordre. Il est tout à fait permis d'entrer ce qui suit :

    GIVE TEMP 5 300 Silver
    MAKE TEMP 5
      RECRUIT 1
      COMBAT NOT
      LEARN FORESTRY
    END

La nouvelle unité est d'abord créée, ne se bat pas, reçoit 300 Silver, recrute 1 personne et apprend finalement FORESTRY - bien que cela ne corresponde pas à l'ordre dans lequel les ordres ont été saisis.

## Notes explicatives

Les ordres de rang égal émanant de différentes unités sont normalement traités dans l'ordre dans lequel ils apparaissent dans le rapport. Ainsi, par exemple, d'abord tous les ordres GIVE de la première unité, puis tous les ordres GIVE de la deuxième unité, ensuite tous les ordres `RECRUIT` de la première unité, puis de la seconde et ainsi de suite. L'[item pool] fonctionne également généralement dans cet ordre : les unités placées en premier dans l'ordre au NR sont d'abord « interrogées » pour savoir si elles peuvent donner un objet. Cependant, la prévalence peut être modifiée par certains ordres. Ceux-ci incluent `ENTER, EXIT, TEMP, GIVE COMMAND` et `GIVE SHIP`. Le comportement exact n'est pas garanti ! Par conséquent, en cas de doute, vous devez donner des ordres de telle manière que l'ordre des unités ne joue aucun rôle.

Pour les ordres dont le résultat a une limite supérieure, par exemple la quantité maximale d'arbres dans la région pour `MAKE wood`, le nombre maximal de recrues pour `recruter` ou l'argent de la région pour `ENTERTAIN` et `TAX`, il peut arriver que plusieurs unités soient en concurrence. Dans ce cas, on essaie de répartir le bien rare au prorata de la quantité que chaque unité pourrait produire s'il était illimité. Dans ce cas, il peut y avoir des écarts et une unité peut éventuellement se retrouver sans rien. Les ordres `SELL`, `BUY` et `WORK` sont également concernés.

ENTER - 1er / 2ème / 3ème / 4ème essai  
Cela signifie qu'il est encore possible d'entrer dans un château avant une attaque. Après le combat, on peut réessayer, car les anciens propriétaires peuvent être morts entre-temps ou avoir pris la fuite.

Cela ne signifie pas que les unités qui quittent un navire peuvent attaquer dans le même tour, car le serveur se souvient de qui a quitté un navire et en conséquence l'en empêche.

## Voir aussi

- [ordres]
- [brève description]
- [brève description DE/EN]
- [Befehlsreihenfolge (E3)]

|     |     |
| --- | --- |
| Weiterlesen: | [brève description] |

[brève description]: ./commands-list.md "Kurzbeschreibung"

<!-- From [https://wiki.eressea.de/index.php?title=Befehlsreihenfolge/fr&oldid=13985] -->

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
  [RECRUIT]:./silver.md#recruter "RECRUIT"
  [DESTROY]: ./cmd-destroy.md "DESTROY"
  [FOLLOW]: ./cmd-follow.md "FOLLOW"
  [PROMOTE]: ./cmd-promote.md "PROMOTE"
  [PAY NOT]: ./cmd-pay-not.md "PAY"
  [QUIT]: ./cmd-quit.md "STIRB"
  [CAST]: ./cmd-cast.md "CAST"
  [TEACH]: ./cmd-teach.md "TEACH"
  [LEARN]: ./cmd-learn.md "LEARN"
  [RESEARCH]: ./cmd-research.md "RESEARCH"
  [PLANT]: ./cmd-plant.md "PLANT"
  [SPY]: ./cmd-spy.md "SPIONIERE"
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
  [notes explicatives]: #Erläuterungen
  [item pool]: ./items-pool.md "Materialpool"
  [ordres]: ./commands.md "Befehle"
  [brève description DE/EN]: /Diskussion:Kurzbeschreibung "Diskussion:Kurzbeschreibung"
  [Befehlsreihenfolge (E3)]: ./commands.mdsreihenfolge_(E3) "Befehlsreihenfolge (E3)"
