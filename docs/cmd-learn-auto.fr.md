---
# cSpell:locale fr
alias: cmd-learn-auto-fr
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# LEARN AUTO

**`LEARN AUTO`**` `*`compétence`*  

Grâce à l'ordre, le serveur tente d'automatiser [l'apprentissage][cmd-learn-fr] et [l'enseignement][cmd-teach-fr] dans une région pour toutes les unités d'une faction utilisant cet ordre pour la compétence spécifiée.  
Cependant, l'utilisation simultanée sur une même compétence de `TEACH` et `LEARN AUTO` n'est pas autorisée.  

Si plusieurs unités dans une région donnent l'ordre `LEARN AUTO <compétence>`, par exemple `LEARN AUTO sailing`, le serveur sélectionne les unités parmi les unités qui doivent enseigner afin que les autres obtiennent le maximum de résultats d'apprentissage.  
Comme avec un simple `TEACH`, chaque personne qui a un professeur apprend deux fois plus vite.  

Il n'est pas nécessaire de diviser les unités.  
Par exemple, si une unité de 10 personnes T7 et une unité de 10 personnes T5 ont toutes deux donné l'ordre `LEARN AUTO`, alors une personne de l'unité T7 enseignera aux 10 membres de l'unité T5, les 9 autres apprendront normalement.  
Avec de simples ordres `LEARN`, il aurait fallu diviser l'unité, ce qui peut être fastidieux.  

Cet effet s'applique également à moins de 10 apprenants.  
Une personne qui enseigne à 6 apprenants ayant donné l'ordre `LEARN AUTO` a 4 chances sur 10 d’apprendre pendant une semaine.  

Si aucun élève ne peut être automatiquement affecté, l’unité apprend normalement.  

`LEARN AUTO` ne fonctionne pas avec des compétences coûteuses, ni en combinaison avec l'ordre `TEACH` : les autres unités qui passent des ordres `LEARN` ou `TEACH` n’interviennent pas dans l’affectation automatique des enseignants.  
Une unité qui utilise l'ordre `LEARN AUTO` ne peut pas bénéficier de l'enseignement d'un maître ayant donné l'ordre `TEACH` le visant.  

Il peut toujours être judicieux d'utiliser `TEACH` et `LEARN AUTO` en parallèle pour différentes unités.  

Les avantages de l'association `TEACH` et `LEARN` sont les suivants :

- Les unités avec des compétences coûteuses peuvent bénéficier de l'enseignement
- Une unité peut enseigner des unités dans différentes compétences
- Les enseignants et les apprenants ne doivent pas nécessairement appartenir à la même faction
- Les unités qui ne sont pas autorisées à enseigner (par exemple la plupart des familiers) peuvent toujours bénéficier d'un enseignement

Les avantages de `LEARN AUTO` sont les suivants :

- C'est un travail moins détaillé et l'ordre peut être laissé tel quel pendant plusieurs semaines
- Les unités qui ne sont pas pleinement utilisées comme enseignants utilisent la capacité restante pour apprendre eux-mêmes

Expérience de jeu  (XolgrimA) :

Un ordre `LEARN AUTO` s'applique à un ensemble de 128 unités au maximum par région et compétence.  
Si plusieurs unités d'une faction dans une région donnent l'ordre, un deuxième ensemble est formé qui met en place une chaîne d'enseignement/apprentissage indépendamment du premier.  

<!-- From [https://wiki.eressea.de/index.php?title=LEARN\_AUTO&oldid=15393] -->

[cmd-learn-fr]: [[cmd-learn-fr]]
[cmd-teach-fr]: [[cmd-teach-fr]]
