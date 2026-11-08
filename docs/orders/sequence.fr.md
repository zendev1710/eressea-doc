---
# cSpell:locale fr
alias: sequence-des-ordres
---

# Séquence des ordres

Les ordres d'Eressea sont exécutés dans un ordre fixe.  
Les ordres qui sont dans une même séquence sont exécutés en même temps ou l'ordre d'exécution n'a aucune importance.

<!-- TODO: add piracy in sequence? -->
<!-- TODO: a word about commands which are not orders (next, unit, locale, eressea)? about learn auto? -->
1. Les nouveaux ordres par défaut sont définis
2. [`GROUP`][cmd-group-fr], [`MAKE TEMP`][cmd-make-fr]
3. [`NAME`][cmd-name-fr], [`DESCRIBE`][cmd-describe-fr], [`GUARD NOT`][cmd-guard-fr], [`HELP`][cmd-help-fr], [`COMBAT`][cmd-combat-fr], [`COMBATSPELL`][cmd-combatspell-fr], [`HIDE`][cmd-hide-fr], [`ORIGIN`][cmd-origin-fr], [`SHOW`][cmd-show-fr]
4. [`BANNER`][cmd-banner-fr], [`EMAIL`][cmd-email-fr], [`OPTION`][cmd-option-fr], [`PASSWORD`][cmd-password-fr]
5. [`CONTACT`][cmd-contact-fr]
6. [`MESSAGE`][cmd-message-fr]
7. [`ENTER`][cmd-enter-fr]; 1er essai
8. [`USE`][cmd-use-fr]
9. [`LEAVE`][cmd-leave-fr]
10. [`ENTER`][cmd-enter-fr]; 2ème essai
11. [`ATTACK`][cmd-attack-fr]
12. [`RESERVE`][cmd-reserve-fr], [`CLAIM`][cmd-claim-fr]
13. [`ENTER`][cmd-enter-fr]; 3ème essai
14. [`GIVE CONTROL`][cmd-give-fr]
15. [`FORGET`][cmd-forget-fr]
16. [`GIVE CONTROL`][cmd-give-fr]
17. [`RECRUIT`][cmd-recruit-fr][^1]
18. [`DESTROY`][cmd-destroy-fr]
19. [`FOLLOW`][cmd-follow-fr] est défini
20. [`PROMOTE`][cmd-promote-fr]
21. [`PAY NOT`][cmd-pay-not-fr] définit pour la fonctionnalité et les coûts d'entretien du bâtiment concerné.
22. Les coûts d'entretien des bâtiments soumis à l'obligation d'entretien s'appliquent ; sinon, ils n'ont aucune fonctionnalité !
23. [`QUIT`][cmd-quit-fr]
24. [`CAST`][cmd-cast-fr]
25. [`TEACH`][cmd-teach-fr]
26. [`LEARN`][cmd-learn-fr]
27. [`MAKE TEMP`][cmd-make-fr][^1]
28. [`RESEARCH`][cmd-research-fr], [`PLANT`][cmd-plant-fr], [`SPY`][cmd-spy-fr], [`GROW`][cmd-grow-fr]
29. [`ENTERTAIN`][cmd-entertain-fr][^1]
30. [`WORK`][cmd-work-fr][^1]
31. [`TAX`][cmd-tax-fr][^1]
32. [`BUY`][cmd-buy-fr][^1]
33. [`SELL`][cmd-sell-fr][^1]
34. [`STEAL`][cmd-steal-fr][^1]
35. Les bateaux dont l'équipage est insuffisant subissent des dommages
36. [`ENTER`][cmd-enter-fr]; 4ème essai
37. [`MOVE`][cmd-move-fr] et [`ROUTE`][cmd-route-fr], incluant [`RIDE`][cmd-ride-fr] et [`CARRY`][cmd-carry-fr] sont exécutés et les unités ayant reçu l'ordre `FOLLOW` d'autres unités le font.
38. [`GUARD NOT`][cmd-guard-fr] cela n'est possible que si l'unité n'a pas bougé.
39. Les bateaux dérivent en haute mer
40. [`DEFAULT`][cmd-default-fr]
41. Les unités vides sont supprimées
42. Les paysans, les chevaux et les forêts se multiplient, si possible ; des paysans se déplacent vers d'autres régions.
43. Les Silver pour l'entretien des unités est déduit
44. [`SORT`][cmd-sort-fr]
45. [`NUMBER`][cmd-number-fr]

Les ordres ne doivent toutefois pas nécessairement être saisis dans cet ordre.  
Il est tout à fait permis d'écrire :

```text
GIVE TEMP 5 300 Silver
MAKE TEMP 5
    RECRUIT 1
    COMBAT NOT
    LEARN FORESTRY
END
```

La nouvelle unité est d'abord créée, ne se bat pas, reçoit 300 Silver, recrute 1 personne et apprend finalement la [sylviculture][sylviculture]{title="Forestry"} - bien que cela ne corresponde pas à l'ordre dans lequel les ordres ont été saisis.

## Notes explicatives

Les ordres de rang égal émanant de différentes unités sont normalement traités dans l'ordre dans lequel ils apparaissent dans le rapport.  
Ainsi, par exemple, d'abord tous les ordres `GIVE` de la première unité, puis tous les ordres `GIVE` de la deuxième unité, ensuite tous les ordres `RECRUIT` de la première unité, puis de la seconde et ainsi de suite.  
La [réserve d'objets][reserve-d-objets-id] fonctionne également généralement dans cet ordre : les unités placées en premier dans l'ordre au NR sont d'abord « interrogées » pour savoir si elles peuvent donner un objet.  
Cependant, la prévalence peut être modifiée par certains ordres.  
Ceux-ci incluent `ENTER, EXIT, TEMP, GIVE COMMAND` et `GIVE SHIP`.  
Le comportement exact n'est pas garanti ! Par conséquent, en cas de doute, vous devez donner des ordres de telle manière que l'ordre des unités ne joue aucun rôle.

Pour les ordres dont le résultat a une limite supérieure, par exemple la quantité maximale d'arbres dans la région pour `MAKE wood`, le nombre maximal de recrues pour `recruter` ou l'argent de la région pour `ENTERTAIN` et `TAX`, il peut arriver que plusieurs unités soient en concurrence.  
Dans ce cas, on essaie de répartir le bien rare au prorata de la quantité que chaque unité pourrait produire s'il était illimité.  
Dans ce cas, il peut y avoir des écarts et une unité peut éventuellement se retrouver sans rien.  
Les ordres `SELL`, `BUY` et `WORK` sont également concernés.

ENTER - 1er / 2ème / 3ème / 4ème essai  
Cela signifie qu'il est encore possible d'entrer dans un château avant une attaque.  
Après le combat, on peut réessayer, car les anciens propriétaires peuvent être morts entre-temps ou avoir pris la fuite.

Cela ne signifie pas que les unités qui quittent un bateau peuvent attaquer dans le même tour, car le serveur se souvient de qui a quitté un bateau et en conséquence l'en empêche.

## Voir aussi

- [Ordres][ordres]

Poursuivre la lecture : [Tableau récapitulatif des ordres][tableau-recapitulatif-des-ordres].

[^1]: ordres divisés "équitablement"; voir les [notes explicatives][notes-explicatives].

<!-- From [https://wiki.eressea.de/index.php?title=Befehlsreihenfolge/fr&oldid=13985] -->

[cmd-attack-fr]: [[cmd-attack-fr]]
[cmd-banner-fr]: [[cmd-banner-fr]]
[cmd-buy-fr]: [[cmd-buy-fr]]
[cmd-carry-fr]: [[cmd-carry-fr]]
[cmd-cast-fr]: [[cmd-cast-fr]]
[cmd-claim-fr]: [[cmd-claim-fr]]
[cmd-combat-fr]: [[cmd-combat-fr]]
[cmd-combatspell-fr]: [[cmd-combatspell-fr]]
[cmd-contact-fr]: [[cmd-contact-fr]]
[cmd-default-fr]: [[cmd-default-fr]]
[cmd-describe-fr]: [[cmd-describe-fr]]
[cmd-destroy-fr]: [[cmd-destroy-fr]]
[cmd-email-fr]: [[cmd-email-fr]]
[cmd-enter-fr]: [[cmd-enter-fr]]
[cmd-entertain-fr]: [[cmd-entertain-fr]]
[cmd-follow-fr]: [[cmd-follow-fr]]
[cmd-forget-fr]: [[cmd-forget-fr]]
[cmd-give-fr]: [[cmd-give-fr]]
[cmd-group-fr]: [[cmd-group-fr]]
[cmd-grow-fr]: [[cmd-grow-fr]]
[cmd-guard-fr]: [[cmd-guard-fr]]
[cmd-help-fr]: [[cmd-help-fr]]
[cmd-hide-fr]: [[cmd-hide-fr]]
[cmd-learn-fr]: [[cmd-learn-fr]]
[cmd-leave-fr]: [[cmd-leave-fr]]
[cmd-make-fr]: [[cmd-make-fr]]
[cmd-message-fr]: [[cmd-message-fr]]
[cmd-move-fr]: [[cmd-move-fr]]
[cmd-name-fr]: [[cmd-name-fr]]
[cmd-number-fr]: [[cmd-number-fr]]
[cmd-option-fr]: [[cmd-option-fr]]
[cmd-origin-fr]: [[cmd-origin-fr]]
[cmd-password-fr]: [[cmd-password-fr]]
[cmd-pay-not-fr]: [[cmd-pay-not-fr]]
[cmd-plant-fr]: [[cmd-plant-fr]]
[cmd-promote-fr]: [[cmd-promote-fr]]
[cmd-quit-fr]: [[cmd-quit-fr]]
[cmd-recruit-fr]: [[cmd-recruit-fr]]
[cmd-research-fr]: [[cmd-research-fr]]
[cmd-reserve-fr]: [[cmd-reserve-fr]]
[cmd-ride-fr]: [[cmd-ride-fr]]
[cmd-route-fr]: [[cmd-route-fr]]
[cmd-sell-fr]: [[cmd-sell-fr]]
[cmd-show-fr]: [[cmd-show-fr]]
[cmd-sort-fr]: [[cmd-sort-fr]]
[cmd-spy-fr]: [[cmd-spy-fr]]
[cmd-steal-fr]: [[cmd-steal-fr]]
[cmd-tax-fr]: [[cmd-tax-fr]]
[cmd-teach-fr]: [[cmd-teach-fr]]
[cmd-use-fr]: [[cmd-use-fr]]
[cmd-work-fr]: [[cmd-work-fr]]
