---
# cSpell:locale fr, en
alias: sequence-des-ordres
---
# Séquence des ordres

Les ordres d'Eressea sont exécutés dans un ordre fixe. Les ordres qui sont dans une même séquence sont exécutés en même temps ou l'ordre d'exécution n'a aucune importance.

1. les nouveaux ordres par défaut sont définis
2. [[cmd-group]], [[cmd-make|MAKE TEMP]]
3. [[cmd-name]], [[cmd-describe]], [[cmd-guard|GUARD NOT]], [[cmd-help]], [[cmd-combat]], [[cmd-combatspell]], [[cmd-hide]], [[cmd-origin]], [[cmd-show]]
4. [[cmd-banner]], [[cmd-email]], [[cmd-option]], [[cmd-password]]
5. [[cmd-contact]]
6. [[cmd-message]]
7. [[cmd-enter]]; 1. essai
8. [[cmd-use]]
9. [[cmd-leave]]
10. [[cmd-enter]]; 2. essai
11. [[cmd-attack]]
12. [[cmd-reserve]], [[cmd-claim]]
13. [[cmd-enter]]; 3. essai
14. [[cmd-give|GIVE CONTROL]]
15. [[cmd-forget]]
16. [[cmd-give|GIVE CONTROL]]
17. [[cmd-recruit]] \*
18. [[cmd-destroy]]
19. [[cmd-follow]] est défini
20. [[cmd-promote]]
21. [[cmd-pay-not|PAY NOT]] définit pour la fonctionnalité et les coûts d'entretien du bâtiment concerné.
22. Les coûts d'entretien des bâtiments soumis à l'obligation d'entretien s'appliquent ; sinon, ils n'ont aucune fonctionnalité !
23. [[cmd-quit]]
24. [[cmd-cast]]
25. [[cmd-teach]]
26. [[cmd-learn]]
27. [[cmd-make|MAKE TEMP]] \*
28. [[cmd-research]], [[cmd-plant]], [[cmd-spy]], [[cmd-grow]]
29. [[cmd-entertain]] \*
30. [[cmd-work]] \*
31. [[cmd-tax]] \*
32. [[cmd-buy]] \*
33. [[cmd-sell]] \*
34. [[cmd-steal]] \*
35. Les bateaux dont l'équipage est insuffisant subissent des dommages
36. [[cmd-enter]]; 4. essai
37. [[cmd-move]] et [[cmd-route]], incluant [[cmd-ride]] et [[cmd-carry]] sont exécutés et les unités ayant reçu l'ordre de FOLLOW d'autres unités le font.
38. [[cmd-guard|GUARD NOT]] cela n'est possible que si l'unité n'a pas bougé.
39. Les bateaux dérivent en haute mer
40. [[cmd-default]]
41. les unités vides sont supprimées
42. les paysans, les chevaux et les forêts se multiplient, si possible ; des paysans se déplacent vers d'autres régions.
43. les Silver pour l'entretien des unités est déduit
44. [[cmd-sort]]
45. [[cmd-number]]

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

Les ordres de rang égal émanant de différentes unités sont normalement traités dans l'ordre dans lequel ils apparaissent dans le rapport. Ainsi, par exemple, d'abord tous les ordres GIVE de la première unité, puis tous les ordres GIVE de la deuxième unité, ensuite tous les ordres `RECRUIT` de la première unité, puis de la seconde et ainsi de suite. La [[reserve-d-objets]] fonctionne également généralement dans cet ordre : les unités placées en premier dans l'ordre au NR sont d'abord « interrogées » pour savoir si elles peuvent donner un objet. Cependant, la prévalence peut être modifiée par certains ordres. Ceux-ci incluent `ENTER, EXIT, TEMP, GIVE COMMAND` et `GIVE SHIP`. Le comportement exact n'est pas garanti ! Par conséquent, en cas de doute, vous devez donner des ordres de telle manière que l'ordre des unités ne joue aucun rôle.

Pour les ordres dont le résultat a une limite supérieure, par exemple la quantité maximale d'arbres dans la région pour `MAKE wood`, le nombre maximal de recrues pour `recruter` ou l'argent de la région pour `ENTERTAIN` et `TAX`, il peut arriver que plusieurs unités soient en concurrence. Dans ce cas, on essaie de répartir le bien rare au prorata de la quantité que chaque unité pourrait produire s'il était illimité. Dans ce cas, il peut y avoir des écarts et une unité peut éventuellement se retrouver sans rien. Les ordres `SELL`, `BUY` et `WORK` sont également concernés.

ENTER - 1er / 2ème / 3ème / 4ème essai  
Cela signifie qu'il est encore possible d'entrer dans un château avant une attaque. Après le combat, on peut réessayer, car les anciens propriétaires peuvent être morts entre-temps ou avoir pris la fuite.

Cela ne signifie pas que les unités qui quittent un bateau peuvent attaquer dans le même tour, car le serveur se souvient de qui a quitté un bateau et en conséquence l'en empêche.

## Voir aussi

- [[ordres]]
- [[tableau-recapitulatif-des-ordres]]

Poursuivre la lecture : [[tableau-recapitulatif-des-ordres]].

<!-- From [https://wiki.eressea.de/index.php?title=Befehlsreihenfolge/fr&oldid=13985] -->

[notes explicatives]: #notes-explicatives
