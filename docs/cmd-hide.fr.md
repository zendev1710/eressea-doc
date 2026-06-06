---
# cSpell:locale fr
alias: cmd-hide-fr
---
<!-- disable MD052 because of mkdocs autorefs plugin usage -->
<!-- markdownlint-disable MD041 MD042 MD052 -->
[](){ #cmd-hide-fr-id }

# HIDE

**`HIDE`**`[`*`niveau`*`]`  
**`HIDE`**`FACTION [NOT]`  
**`HIDE`**`FACTION NUMBER [`*`number`*`]`  
**`HIDE`**` `*`race`*  

Avec la première variante, vous pouvez ajuster l'intensité avec laquelle une unité essaie de se camoufler.
Le `niveau` spécifié ne peut évidemment pas être supérieur au niveau de l'unité en [discrétion][skill-discretion-id]{title="Stealth"}.  

Si aucun paramètre n'est spécifié, le maximum est défini.  

Avec l'ordre `HIDE FACTION`, vous pouvez essayer de cacher votre affiliation à une faction.
L'affiliation à la faction est alors affichée en tant qu'affiliation **anonyme** aux autres joueurs.  
Contrairement au mécanisme standard de détection en fonction des niveaux de furtivité versus perception, l'affiliation à une faction d'une telle unité ne peut être identifiée **qu'en utilisant l'[espionnage][espionnage-id]**.  

Avec `HIDE FACTION NOT` cette anonymisation sera à nouveau annulée et les autres joueurs verront l'affiliation correcte de la faction - s'ils sont suffisamment "conscients" (en termes de perception) et voient l'unité dans leur rapport.  

`HIDE FACTION NUMBER number` camoufle l'unité avec l'identifiant de faction spécifié, afin qu'elle puisse se déguiser par appartenance factice à n'importe quelle autre faction.  
Il n’existe pas de moyen simple de voir à travers cette forme de camouflage.  
Pour paraître à nouveau comme appartenant à votre propre faction, vous devez passer le même ordre avec en spécifiant le paramètre `number` à la valeur de votre propre identifiant de faction.  
La faction spécifiée doit être connue de la faction qui donne l'ordre, c'est-à-dire apparaître dans son rapport, sinon l'ordre échouera.  

Les factions qui reçoivent un ordre [`HELP xyz FACTION DISGUISE`][cmd-help] de la faction de l'unité (ou du groupe) peut voir la véritable affiliation de la faction de l'unité qui aura donné l'ordre.  

Jusqu’ici, c’est relativement simple.  

Cependant, ce camouflage présente quelques fonctionnalités spéciales, qui sont répertoriées ici sans ordre particulier :

- La race (apparente) de l’unité ne change pas réellement; un gobelin reste un gobelin, même s'il prétend appartenir à la faction des elfes de lumière
- Les unités ne changent pas de comportement à cause du camouflage.
  Par exemple, ils ne donnent pas d’argent aux alliés de la faction sous laquelle ils se déguisent.
  Donc si vous souhaitez perfectionner le camouflage, vous devez former un groupe avec les unités et définir des statuts d'aide appropriés pour ce groupe.
  Les unités masquées de cette manière ne peuvent pas entrer soudainement dans des bâtiments ou des bateaux dans lesquels elles ne sont pas autorisées à entrer, ni collecter des taxes là où il leur est normalement interdit de le faire.
- Au combat, ces unités forment leur propre armée.
  Exemple : soit 3 groupes, les Elfes des Bois, les Elfes des Rivières et les Nains de Fer.
  Toutes les factions ont chacune une unité : *Elfe des Bois*, *Elfe des Rivières* et *Nain de Fer*.
  Tandis que *Elfe des Bois* se déguise en *Elfe des Rivières*, toutes les autres unités conservent leur véritable identité.
  Maintenant, *Nain de Fer* attaque *Elfe des Rivières*.
  Cela signifie que trois armées apparaissent dans le rapport de bataille : une armée de Nains de Fer et deux armées d'Elfes des Rivières.

Cependant, [[cmd-group]] a également pour effet secondaire d'avoir plusieurs armées.  
De cette façon, vous ne pouvez pas voir si les unités se font passer pour une faction étrangère ou si la personne en question possède simplement plusieurs groupes.

Avec `HIDE <race>` les [démons][demons-fr-id] peuvent se déguiser en une autre race.

## Voir aussi

- [Espionnage][espionnage-id]{title="Espionage"}
- [Discrétion][discretion-id]{title="Stealth"}
- [Perception][skill-perception-fr-id]{title="Perception"}

<!-- From [https://wiki.eressea.de/index.php?title=HIDE&oldid=15791] -->

[cmd-help]: [[cmd-help]]
