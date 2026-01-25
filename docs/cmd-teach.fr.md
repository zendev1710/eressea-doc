---
# cSpell:locale fr
alias: cmd-teach-fr
---
# `TEACH`

*Ordre [long].*

**`TEACH`**` `*`unit-id`*`[`*`unit-id`*`]...`  

Pour réduire le temps nécessaire à une autre unité pour apprendre une compétence, tu peux lui enseigner cette compétence.  
Pour cela, l’unité d’enseignement (maître) doit être **supérieure d’au moins 2 niveaux** à l’unité d’apprentissage (élève) dans la compétence concernée.  
Cela signifie que l’unité d’apprentissage apprend deux fois plus vite que si elle essayait d’améliorer ses compétences par elle-même.  

Cet ordre enseigne à toutes les unités renseignées la compétence qu'elles apprennent.  
Les élèves doivent donc apprendre pendant que le maître enseigne.  
Plusieurs entités peuvent être renseignées.  
Cependant, une unité enseignante ne peut permettre qu'à 10 élèves par tour de bénéficier de leurs connaissances.  
Plusieurs maîtres peuvent également enseigner à un grand groupe d'élèves.  

La compétence à enseigner ne doit **PAS** être spécifiée - la compétence acquise par l'élève est automatiquement enseignée.  
Il peut également s'agir de compétences différentes, à condition que l'enseignant maîtrise ces compétences suffisamment mieux que les élèves.  

Si tu souhaites enseigner des unités d'autres factions, tu dois avoir reçu l'ordre [[cmd-help|`HELP GUARD`]] de cette faction, ou l'unité à enseigner doit [[cmd-contact|contacter]] l'enseignant.  

**Exemple** :

```text
TEACH xxxx yyyy TEMP 2 zzzz
```

Avec l'ordre [[cmd-learn-auto]], le serveur **tente d'automatiser** l'apprentissage et l'enseignement dans une région au sein d'une faction.  

!!! warning "Attention"
    L'utilisation simultanée d'ordres `TEACH` et `LEARN AUTO` par les unités d'une même faction dans une région n'est pas autorisée.

<!-- From [https://wiki.eressea.de/index.php?title=TEACH&oldid=16726] -->

[long]: ./commands.md#ordres-courts-et-longs
