---
# cSpell:locale fr
alias: cmd-leave-fr
---

# LEAVE

**`LEAVE`**  

Avec cet ordre, L'unité abandonne le bateau ou le bâtiment dans lequel elle se trouve.  

En utilisant l'ordre [`ENTER`][cmd-enter-fr] ou [`MOVE`][cmd-move-fr], les unités quitteront parfois automatiquement leurs bateaux ou leurs bâtiments.
Cependant, cela ne fonctionne pas toujours : si l'unité est le capitaine d'un bateau et utilise l'ordre `MOVE`, elle tentera de naviguer dans la direction voulue, même s'il y a une terre à cet endroit.  

Un capitaine doit d'abord quitter son bateau, avec l'ordre `LEAVE`;
Les autres marins peuvent utiliser l'ordre `MOVE` pour se déplacer sur terre et quitter automatiquement le bateau.

Si une unité quitte un bâtiment ou un bateau dont elle a le commandement, cela ne passe pas nécessairement à l'unité suivante dans le rapport.  
Dans cette situation, il est préférable d'utiliser [`GIVE unit-id COMMAND`][cmd-give-fr], pour contrôler la passation du commandement.  
L'ordre des unités lors de l'évaluation n'est pas toujours celui du rapport.
Si vos propres unités se trouvent dans le bâtiment ou sur le bateau, le commandement leur reviendra.

Si l'unité est sur un bateau et que la région est gardée par une faction non alliée, elle doit d'abord quitter le bateau si elle souhaite effectuer certaines actions.  
Pour plus d'informations, consultez [`GUARD`][cmd-guard-fr].  

L’ordre `LEAVE` ne fonctionne pas en haute mer.
Une façon de laisser les gens sauter par-dessus bord est de donner l'ordre `GIVE 0 [number] MEN`.  
Une autre solution **réservée aux Aquariens** et qui ne tue pas de membres de l'unité est de [nager][nager].

<!-- From [https://wiki.eressea.de/index.php?title=LEAVE&oldid=15184] -->

[cmd-enter-fr]: [[cmd-enter-fr]]
[cmd-give-fr]: [[cmd-give-fr]]
[cmd-move-fr]: [[cmd-move-fr]]
[cmd-guard-fr]: [[cmd-guard-fr]]
