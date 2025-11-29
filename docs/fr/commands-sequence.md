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

[brève description]: /Spezial:Meine_Sprache/Kurzbeschreibung "Spezial:Meine Sprache/Kurzbeschreibung"

<!-- Récupéré depuis [https://wiki.eressea.de/index.php?title=Befehlsreihenfolge/fr&oldid=13985] -->

[Kategorien][]:

- [Befehle]
- [Regeln/fr]

  [Befehlsreihenfolge]: /Befehlsreihenfolge "Befehlsreihenfolge"
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
  [notes explicatives]: #Erläuterungen
  [item pool]: /Spezial:Meine_Sprache/Materialpool "Spezial:Meine Sprache/Materialpool"
  [ordres]: /Spezial:Meine_Sprache/Befehle "Spezial:Meine Sprache/Befehle"
  [brève description]: /Spezial:Meine_Sprache/Kurzbeschreibung "Spezial:Meine Sprache/Kurzbeschreibung"
  [brève description DE/EN]: /Spezial:Meine_Sprache/Diskussion:Kurzbeschreibung "Spezial:Meine Sprache/Diskussion:Kurzbeschreibung"
  [Befehlsreihenfolge (E3)]: /Spezial:Meine_Sprache/Befehlsreihenfolge_(E3) "Spezial:Meine Sprache/Befehlsreihenfolge (E3)"
  [https://wiki.eressea.de/index.php?title=Befehlsreihenfolge/fr&oldid=13985]: https://wiki.eressea.de/index.php?title=Befehlsreihenfolge/fr&oldid=13985
  [Kategorien]: /Spezial:Kategorien "Spezial:Kategorien"
  [Befehle]: /Kategorie:Befehle "Kategorie:Befehle"
  [Regeln/fr]: /index.php?title=Kategorie:Regeln/fr&action=edit&redlink=1 "Kategorie:Regeln/fr (Seite nicht vorhanden)"
