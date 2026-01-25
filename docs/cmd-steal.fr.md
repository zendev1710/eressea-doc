---
# cSpell:locale fr
alias: cmd-steal-fr
---
# `STEAL`

*Ordre [long].*

**`STEAL`**` `*`unit-id`*  

Cet ordre tente de voler l'unité spécifiée.  

Si la compétence de [Discrétion] des auteurs de [vol] est supérieure à la compétence de [Perception] des victimes (cela prend en compte la compétence de perception de la meilleure unité de la région), les victimes remarquent seulement qu'elles ont été volées, mais non par qui.  
Les auteurs volent **50 Silver** par personne et par différence de niveau de compétence (entre les deux compétences vol et perception).  

Si la perception des victimes et la dissimulation des auteurs sont de même niveau, le vol ne réussira pas et les victimes deviendront méfiantes.  
Si la perception des victimes est plus élevée que la dissimulation des auteurs, ces derniers seront pris sur le fait et identifiés.  

!!! warning "Attention"
    Les voleurs volent toujours dans la [réserve d'argent].  
    Cela signifie que l'argent peut être volé sur d'autres unités qui n'ont pas été directement ciblées par les voleurs.

!!! note
    Pendant les premières semaines, une faction est [[puppy-protection|immunisée]] contre le vol.

## Voir aussi

- [[money]]
- [[camouflage]]

<!-- From [https://wiki.eressea.de/index.php?title=STEAL&oldid=16749] -->

[long]: ./commands.md#ordres-courts-et-longs

[Discrétion]: ./skills-list.md#discretion "Stealth"
[Perception]: ./skills-list.md#perception
[réserve d'argent]: ./items-pool.md#reserve-et-give
[vol]: ./camouflage.md#vol-de-silver
