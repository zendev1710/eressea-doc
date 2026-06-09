---
# cSpell:locale fr
alias: cmd-make-fr
---
<!-- disable MD052 because of mkdocs autorefs plugin usage -->
<!-- markdownlint-disable MD042 MD052 -->
# MAKE

**`MAKE TEMP`**` `*`unit-alias-id`*`["`*`nom`*`"]`  
**`MAKE`**`[`*`niveau`*`]`*`type_batiment`*`[`*`id_batiment`*`]`  
**`MAKE`**`[`*`niveau`*`]`*`type_bateau`*  
**`MAKE`**`[`*`niveau`*`] SHIP [`*`bateau-id`*`]`  
**`MAKE`**`[`*`niveau`*`] Road`*`direction`*  
**`MAKE`**`[`*`quantité`*`] HERBS`  
**`MAKE`**`[`*`quantité`*`]`*`objet`*  

L'ordre `MAKE` est l'ordre de production général.  

Pour en savoir plus, voir le chapitre [Production][production-fr-id].

## Objets

Les [[objets]] et les [[ressources|matières premières]] sont créés avec `MAKE [`*`number`*`]`*`item`*` `.  
Selon l'objet, une certaine compétence et peut-être aussi certaines matières premières sont nécessaires.  
Sans préciser la *quantité*, l'unité produira autant d'items que de personnes dans l'unité, de niveaux de compétence et éventuellement de matières premières le permettent.  

[](){ #make-potions-fr-id }

### Potions

Concocter une potion est très complexe et ne peut être réalisé que par des alchimistes particulièrement talentueux.  
Les détails peuvent être trouvés dans le chapitre sur [[alchimie|l'alchimie]].

### Plantes

Les plantes sont produites avec l'ordre `MAKE HERBS` par des unités maîtrisant l'[herboristerie].
Pour plus de détails, voir le chapitre sur les [[plantes]].

## Unités

Lorsque vous créez une nouvelle unité (`MAKE TEMP xyz`), vous lui attribuez un alias d'identifiant (son identifiant réel n'est pas encore connu).  
Pour tout autre ordre, vous pouvez référencer l'unité par cet alias (en incluant le mot `TEMP`, par exemple `GIVE TEMP xyz 100 silver`).
Lorsque vous recherchez une unité `TEMP`, votre propre faction est recherchée en premier, puis les autres factions.
Donc, si vous et une autre faction avez tous les deux une unité `TEMP` avec l'ID **`xyz`**, votre propre unité sera toujours choisie.
Ainsi, avec un peu de coordination, les unités `TEMP` d'autres factions peuvent également être contactées.

L'alias d'identifiant sera utilisé comme nouvel identifiant de l'unité s'il n'est pas déjà pris.
Vous pouvez également attribuer un nom à la nouvelle unité.  

Les ordres :

```text
MAKE TEMP 1
    NAME UNIT "Clowns"
    NUMBER UNIT funy
```

peut être raccourci à :

```text
MAKE TEMP funy "Clowns"
```

Un maximum de 2 500 unités est autorisé par faction.
Si le groupe compte 2 500 unités ou plus, aucune nouvelle unité ne peut plus être créée avec l'ordre `MAKE TEMP`;  
d'autres unités doivent d'abord être supprimées, par exemple en les fusionnant.  
La suppression des unités vides intervenant en fin de séquence des ordres, de nouvelles unités `TEMP` ne pourront être créées que la semaine suivante.  

Les ordres qui suivent l'ordre `MAKE TEMP` sont affectés à la nouvelle unité jusqu'à la prochaine instruction `END` rencontrée.  

Cependant, la nouvelle unité doit toujours avoir des membres, sinon elle sera silencieusement supprimée à la fin du tour !
Il faut donc qu'elle recrute ou qu'on lui donne une personne au moins.  
Si la nouvelle unité veut recruter de nouveaux membres, elle doit également recevoir suffisamment d’argent pour le faire.  
Si elle ne reçoit pas cette information, l'unité ne pourra recruter personne et sera silencieusement retirée à la fin de la semaine.  
Si l'unité reçoit de l'argent mais ne recrute aucun membre, elle est également dissoute et l'argent revient aux [autres unités de leur propre faction][dissolution-des-unites].  

```text
UNIT 17;   Combattants [15,700$]
    MAKE TEMP 1
        NAME UNIT "dragon riders"
        LEARN melee
    END
    GIVE TEMP 1 5 MEN
     
    GIVE TEMP 2 100 silver
    MAKE TEMP 2
        RECRUIT 1
        NAME UNIT "scouts"
        DEFAULT "LEARN perception"
        MOVE west
    END
```

## Bâtiments

Pour ériger un nouveau bâtiment, utilisez l'ordre `MAKE [`*`niveau`*`]`*`<type bâtiment>`* (voir [bâtiments][batiments-id]).  
Pour continuer à construire (agrandir un batiment), l'ordre est `MAKE [levels]`*`<type bâtiment>`*` `*`building_id`*.  
Le type de bâtiment peut être remplacé par `CASTLE` lors de la poursuite de la construction, même s'il s'agit d'un type de bâtiment différent.  

Les châteaux et bien d’autres bâtiments peuvent être agrandis autant que vous le souhaitez.  
Afin de construire des châteaux, l'unité doit avoir des compétences en maçonnerie et en pierres;
d'autres bâtiments nécessitent généralement également du bois, du fer et de l'argent en diverses quantités.

[](){ #make-bateaux-id }

## Bateaux

Avec `MAKE`*`type bateau`* une unité commence à construire un nouveau [bateau][bateaux-id].  
Cela nécessite une compétence en matière de construction navale, et du bois.
On peut continuer à construire avec `MAKE [`*`niveau`*`] SHIP`*`ID bateau`*.
Les bateaux ne peuvent pas être agrandis comme les châteaux : le type est déterminé au début de la construction.  
Les bateaux ne peuvent être construits qu'à la taille définie selon leur type.

Avec les bâtiments ainsi que les bateaux, vous pouvez spécifier avec *niveau* combien de points de taille vous souhaitez ajouter.  

- première semaine : `MAKE longboat`. Un nouveau bateau est construit et reçoit l'identifiant 76 de la part du serveur.
- deuxième semaine : `MAKE SHIP 76`. Poursuit la construction d'une [chaloupe][chaloupe]{title="Longboat"} d'identifiant 76.

[](){ #make-routes-id }

## Routes

Pour faciliter les déplacements dans une région comportant des routes et des ponts, utilisez l'ordre `MAKE ROAD`*`direction`*.  
Pour construire des [[routes]], l'unité a besoin de la compétence [construction de routes][construction-de-routes]{title="Roadwork"} et des [[objets|pierres]].  
Dans les glaciers, il faut au préalable un [tunnel][tunnel-fr-id], dans les déserts un [caravansérail][caravanserail] et dans les marais un [barrage][barrage]{title="Dam"}.  
Une pierre est utilisée par point de compétence en construction de route.
Entre 50 et 250 pierres sont nécessaires pour chaque direction souhaitée, selon les [[terrain-types]].  
Les routes ne fonctionnent que si elles sont complètes.

Expérience de jeu (Solthar) :

Sauf lors de la construction d'un nouveau bâtiment, vous pouvez échanger le type en `MAKE type xyz` avec `CASTLE` ou tout autre type de bâtiment.  

`MAKE <type>` ou `MAKE SHIP` sans autres paramètres, la construction du bâtiment ou du bateau dans lequel se trouve actuellement l'unité se poursuit.

!!! warning "Attention"
    Si l'unité se trouve dans un bâtiment, `MAKE lighthouse` ne démarre pas un nouveau bâtiment, mais continue de construire l'ancien.

## Exemples

```text
MAKE 5 sword ; produit 5 épées (au plus)
MAKE water~of~life ; produit autant de potions *water of life* que les matières premières et la compétence le permettent
MAKE HERBS
LEAVE
MAKE lighthouse ; commence à construire un nouveau phare
MAKE lighthouse xyz ; agrandit le phare xyz
LEAVE
MAKE CASTLE xyz ; continue de construire xyz (quel que soit le type de bâtiment)
MAKE 5 Trireme ; commence à construire une nouvelle trirème
MAKE SHIP abc ; continue de construire le bateau abc (la trirème)
MAKE ROAD SE ; continue ou commence à construire une route en direction du sud-est
MAKE Trireme abc ; incorrect : démarre une nouvelle trirème (ce qui n'était pas voulu)
MAKE building xyz ; incorrect : only CASTLE or building type is allowed
```

## Voir aussi

- [Production][production-fr-id]
- [[alchimie|Alchimie]]

<!-- From [https://wiki.eressea.de/index.php?title=MAKE/fr&oldid=16448] -->
