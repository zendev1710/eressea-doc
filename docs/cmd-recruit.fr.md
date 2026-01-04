---
# cSpell:locale fr, en
alias: cmd-recruit-fr
---
# RECRUIT

**`RECRUIT`**` `*`number`*

Cela implique l'embauche de nouvelles personnes parmi les agriculteurs de la région.  

Selon la [[races|race]], vous devez dépenser entre 40 et 150 Silver en [[skills-modifiers|coût de recrutement]] par personne embauchée.  
L'unité qui recrute de nouveaux membres doit posséder cet argent.  
Lorsqu'une nouvelle unité est créée, vous devez lui donner l'argent nécessaire pour qu'elle puisse recruter.  
Si l'unité qui recrute n'a pas assez d'argent, elle l'obtient de la [réserve d'argent].  

Vous ne pouvez recruter que des personnes de la race de votre faction.  
Les unités de [migrants] ne recrutent donc plus de migrants.  
Les agriculteurs d'une région n'ont pas de race.  
Ils ne « décident » à quelle race ils appartiennent qu’au moment de leur recrutement.  

Seuls 2,5% des agriculteurs d'une région peuvent être recrutés par tour.  
Le nombre exact apparaît dans le rapport, dans les informations relatives à la région.  
Si plusieurs factions recrutent, les recrues disponibles seront réparties « équitablement » entre elles.  
Si plusieurs unités d'une faction recrutent, les recrues qui lui sont affectées seront affectées par ordre d'arrivée des unités dans la région.  
Cela signifie que les unités qui arrivent plus tard peuvent repartir les mains vides.  

**Exemple** :

Faction A has RECRUIT 10, Faction B has RECRUIT 1, Faction C has two units each with RECRUIT 2.  

Il y a 160 agriculteurs dans la région, donc 4 recrues.  
Il y a 1 1/3 de recrues par faction.  
La faction B en veut juste un et l’obtient.  
Les factions A et C se battent pour les 3 recrues restantes.  
L'un ne reçoit qu'une seule recrue, l'autre reçoit 2 recrues.  
Quelle que soit la division, la deuxième unité de la Faction C ne reçoit aucune recrue car la première a déjà besoin de toutes.  
Il ne faut donc pas trop se fier à la division exacte et il est préférable de toujours en discuter avec d'autres factions.  

Si vous embauchez des membres supplémentaires dans une unité existante, **les compétences de l'unité sont diluées** car les nouveaux n'ont aucune compétence.  
Les niveaux de compétence accumulés de l'ancienne unité sont simplement répartis entre le nouveau nombre de membres (voir [Mélange de compétences]).  

Après avoir recruté, vous pourrez certainement exécuter d’autres ordres.  

## Voir aussi

- [Recrutement]

<!-- From [https://wiki.eressea.de/index.php?title=RECRUIT&oldid=15790] -->

[réserve d'argent]: ./items-pool.md#reserve-dargent
[migrants]: ./races.md#humains
[Mélange de compétences]: ./skills.md#melanger-les-competences
[Recrutement]: ./silver.md#recruter
