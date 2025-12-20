---
# cSpell:locale en
alias:
    name: auto-learning-chains
    text: Automated learning chains
---
# Automated learning chains

Magellan offers a user-friendly *Teacher Plugin* that automatically assigns teachers and students after a little initial setup.
It uses a [genetic algorithm] to calculate teacher-student relationships.
Details regarding the evaluation function, selection, recombination, or mutation are unknown.

[Teacher Plugin]

Furthermore, there are other, often alliance-internal, tools and script collections that also automate teacher-student relationships.
This usually occurs according to "assignment rules" or using search methods such as A* search.
However, search methods are only partially suitable due to the exponentially growing number of possible combinations and likely perform worse than a genetic algorithm.
A comparison of the quality of the solutions found is still pending.

<!-- From [https://wiki.eressea.de/index.php?title=Automatisierung\_Lernketten&oldid=2577] -->

[genetic algorithm]: http://de.wikipedia.org/wiki/Genetischer_Algorithmus
[Teacher Plugin]: http://magellan.log-out.net/plugins_teacher_de.php
