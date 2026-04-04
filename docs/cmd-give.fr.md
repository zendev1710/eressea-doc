---
# cSpell:locale fr
alias: cmd-give-fr
---
<!-- disable MD052 because of mkdocs autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# `GIVE`

**`GIVE`**` `*`ID-unité`*`HERBS`  
**`GIVE`**` `*`ID-unité`*`COMMAND`  
**`GIVE`**` `*`ID-unité`*`UNIT`  
**`GIVE`**` `*`ID-unité quantité`*`MEN`  
**`GIVE`**` `*`ID-unité quantité objet`*  
**`GIVE`**` `*`ID-unité quantité SHIP`*  
**`GIVE`**` `*`ID-unité`*`ALL MEN`  
**`GIVE`**` `*`ID-unité`*`ALL`  
**`GIVE`**` `*`ID-unité`*` ALL `*`objet`*  
**`GIVE`**` `*`ID-unité`*` EACH `*`quantité`*` `*`objet`*  
**`GIVE`**` 0 `*`quantité`*`MEN`  
**`GIVE`**` 0 `*`quantité`*`SHIP`  
**`GIVE`**` 0 `*`quantité objet`*  

L'unité transfère des objets, le commandement de bateaux ou de bâtiments, des personnes, des bateaux ou même elle-même à d'autres unités.

## Transfert d'objets

Avec `GIVE` les unités peuvent donner toutes les marchandises qu'elles possèdent à d'autres unités.
La condition est que l'unité indiquée accepte des choses.  
C'est le cas si elle appartient à la même faction ou à une faction alliée (`HELP GIVE`), ou si elle a donné ce tour-ci l'ordre [[cmd-contact]] pour l'unité donatrice.  
Les unités de monstres et certaines unités de joueurs avec des races de monstres n'acceptent rien non plus.  
Ceux qui veulent simplement se débarrasser d'objets peuvent aussi les donner aux paysans ou les jeter dans l'océan (`GIVE 0`*`quantité" "objet`*).  
Les personnes, les silver et les chevaux augmentent respectivement la réserve de paysans, de silver et de chevaux d'une région (terrestre).  
Tous les autres objets disparaissent.  

L'unité donatrice et l'unité réceptrice doivent bien entendu se trouver dans la même région.
Le transfert fonctionne également en haute mer, entre bateaux et de bateau à la terre ferme et inversement.  

<!-- TODO: translate in french -->
Au lieu d'une quantité, vous pouvez également utiliser le paramètre `ALL`.  
`GIVE`*`unit-id`*`ALL Swords`, par exemple, remet toutes les épées que l'unité possède à ce moment-là.  
`GIVE`*`unit-id`*`ALL` remet tous les objets, plantes, potions et argent, mais pas les personnes de l'unité.  
Avec `GIVE`*`unit-id`*`herb`, toutes les plantes dont dispose l'unité sont remises.  

En donnant explicitement l'ordre `GIVE`*`unit-id`*`ALL MEN`, toutes les personnes sont remises et l'unité est dissoute.  

!!! warning "Attention"
    Tous les objets et l'argent remis avec l'ordre `GIVE` sont automatiquement réservés et ne peuvent plus être transférés depuis la réserve de matériel !  
    En outre, `GIVE` utilise la [[items-pool|réserve d'objets]], sauf dans le contexte d'un ordre `GIVE ALL`, où l'unité ne donne que ses propres objets, sans réserve.

La variante `GIVE xyz EACH` remet la quantité spécifiée d'objets **par personne** de l’unité cible.  
Par exemple, si l'unité *xyz* compte 10 personnes, avec l'ordre `GIVE xyz EACH 20 Silver`, il lui transfère au global 200 silver.

!!! tip
    Avec`@GIVE`, vous pouvez mettre en place des transferts automatiques.  
    Par exemple, une unité donnant l'ordre `@GIVE abc ALL Iron` remet chaque semaine tout le fer à l'unité *abc*.

```text
GIVE k3f 300 Silver
; Donne à l'unité k3f 300 silver.

GIVE 0 5 Stone
; Jète 5 pierres.

GIVE TEMP 3 7 MEN
; Donne 7 personnes à l'unité TEMP 3 nouvellement créée.
```

!!! Attention
    Entre `MAKE TEMP` et `END` sont spécifiés les ordres pour une unité nouvellement unité,  
    mais celle-ci **n'a pas d'argent**.

Par exemple, ce qui suit **ne marche pas** :

```text
MAKE TEMP 1
    GIVE TEMP 1 200 Silver ; Inutile!
    RECRUIT 2
    MOVE WEST
END
```

Au lieu de cela, il faut écrire :

```text
GIVE TEMP 1 200 Silver
MAKE TEMP 1
    RECRUIT 2
    MOVE WEST
END
; GIVE TEMP 1 200 Silver  ;  ou ici !
```

## Transfert d'unités

Pour réunir des personnes de différentes unités, il faut utiliser l'ordre `GIVE`*`unit-id`*`<quantité> MEN`.  
Les [[competences]] sont alors **mélangées**.

!!! warning "Attention"
    **Pensez à gérer le transfert des objets**, qui pourraient aller vers les agriculteurs (donc être perdus) si l'unité cible manque de personnes.

Expérience de jeu (Solthar) :

Si vous souhaitez confier des personnes à une unité **d’une autre faction**, un simple [[cmd-help|`HELP GIVE`]] ne suffit pas !  
**L'unité réceptrice doit également passer l'ordre [[cmd-contact]]** sur l'unité transférante.  

De plus, si l’unité d’accueil est une [unité de migrants][humains], elle ne doit contenir personne au moment du transfert.  
Idéalement, il devrait s'agir d'une unité `TEMP` vide, par exemple :

```text
UNIT a; Faction X
    GIVE TEMP x ALL MEN
UNIT b; Faction Y
    MAKE TEMP x
        CONTACT UNIT a
    END
```

<!-- TODO clarify -->
Avec `GIVE`*`unit-id`*`UNIT` l'unité complète avec tous les objets est donnée à une autre faction, mais pas à l'unité d'identifiant spécifié !  
L'unité n'exécute plus d'ordres pendant le tour après ce `GIVE` !

## Transfert de commandement

Si l'unité a également un navire ou un bâtiment sous son commandement - c'est-à-dire si elle est la première unité répertoriée dans le bateau ou bâtiment - elle peut également passer le commandement à une autre unité.  
L'unité aux commandes détermine quelles autres unités sont autorisées à entrer dans le bateau ou le bâtiment.

`GIVE unit COMMAND` devrit toujours être utilisé, même si l'unité avec le commandement quitte le bateau ou le bâtiment et que l'unité suivante doit normalement recevoir le commandement.  
L'ordre des unités lors de l'évaluation n'est pas toujours celui du rapport.  
Les nouveaux propriétaires d'un bâtiment sont placés en première position dans le bâtiment **à la fin du tour**.  
Ils ne peuvent donc bénéficier des avantages (bonus...) du bâtiment que **lors du tour suivant**.  

Le commandement ne peut pas être donné à des unités sans membre (par exemple après une bataille, ou à des unités `TEMP` "vides").  

## Transfert de convoi

Avec `GIVE`*`unit-id`*` `*`number`*`SHIP` le propriétaire d'un bateau ou d'un [convoi][convoi] remet le nombre de beteaux spécifié.  
Les unités transférantes et réceptrices doivent appartenir à la même faction (`HELP ALL` et `CONTACT` ne le permmettent pas).  
Si l'autre unité possède également un bateau, un [convoi][convoi] est formé.  
Les convois sont toujours constitués de bateaux du même type.  
Les barques ne peuvent pas former de convois et les bateaux doivent se trouver sur la même côte.  

## Voir aussi

- [[cmd-reserve]]
- [[items-pool]]
- [[ships]]
- [[buildings]]

<!-- From [https://wiki.eressea.de/index.php?title=GIVE/fr&oldid=15993] -->
