---
# cSpell:locale fr
alias: faction-fr
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# Faction

Dans Eressea, un joueur dirige ce que l'on appelle une **faction**.  

Une faction est au départ composée d'une seule **unité** d'une personne, puis progressivement d'un grand nombre d'unités.  

Une unité est composée d'une, de quelques ou même de milliers de personnes de la **[[races|race]]** de la faction.  

Chaque unité peut posséder autant d'objets et [[argent|d'argent]] (***silver***) qu'elle le souhaite, et peut apprendre toutes les [[competences]] d'Eressea.  
Vous pouvez donner aux unités des [[ordres]] à chaque tour, qu'elles exécuteront du mieux possible.

Vous êtes éliminé du jeu lorsque votre faction n'a plus aucun membre, c'est-à-dire lorsque toutes les unités ont été détruites ou dissoutes, ou lorsque aucun ordre n'a été reçu pendant cinq tours consécutifs (5 NMR).

## Unités

La faction commence la partie avec une **unité**, composée d'une personne avec 2 500 Silver, 10 Bois, 4 Pierres et un [cadeau de départ spécifique à la race choisie][debut-du-6eme-monde].

!!! Tip "Astuce"
    Si vous ne savez pas à quoi sert l'objet cadeau, essayez l'ordre [[cmd-show|`SHOW <Item>`]].

Cette première personne n'est en aucun cas spéciale;  
il s'agit simplement de la première personne appartenant à votre nouvelle faction.  
Vous pouvez [recruter][recruter] de nouvelles personnes, également [[objets|produire des objets]], construire des [[batiments]] ou des [bateaux][bateaux], capturer des [chevaux][chevaux-et-chariots], forger des [[tableaux-relatifs-a-la-guerre|armes]] et ainsi de suite.  

Les nouvelles unités sont créées en les générant avec une unité existante à l'aide de l'ordre [[cmd-make|`MAKE TEMP`]].  
Une nouvelle unité n'a pas encore de personnes : vous devez d'abord y [[cmd-give|transférer]] les personnes d'une autre unité ou en recruter, ce qui nécessite de [l'argent][depenses].  
Les unités créées par des unités sur des bateaux ou dans des bâtiments commenceront à l'intérieur du même bateau ou bâtiment.  

Une faction ne peut pas avoir plus d'un certain nombre d'unités, connu sous le nom de **limite d'unités**.  
Celle-ci est actuellement de 2500 unités et est également affichée dans le rapport.  
La limite d'unités empêche la création de nouvelles unités.  
Cela n'a pas d'importance si des unités sont dissoutes plus tard dans le tour.  
Dans certaines circonstances, il est possible qu'une faction ait plus d'unités que la limite d'unités.  
Les unités en trop ne sont pas supprimées ; il n'est alors plus possible de créer de nouvelles unités jusqu'à ce que le nombre d'unités soit à nouveau inférieur à la limite.  

Exemple d'unités :

```text
    * Konrad Rabenhelm (tb2), 1 human, front, guard the region, skills:
        melee 1, taxation 2, has: sword, 20 silver, "TAX";
        Konrad Rabenhelm ist ein typischer Ritter seines Ordens. Der Orden der
        Gerechtigkeit ist bekannt für seine düsteren und zurückhaltenden
        Mitglieder. Sie scheinen alle an einem finsteren Erlebnis zu nagen.
       
      - Botschafter des Clans (2ow), anonymous, 1 dwarf, has: horse,
        silverbag; Der Botschafter ist auf der Suche nach befreundeten Völkern
        und solchen, die es werden wollen.
       
      + Kieselnasen (kies), Gesteinsfreunde (135), 4 trolls, has: 1 cart, 30 gems.
```

Vos propres unités sont marquées du caractère '*'.  
Les unités des autres factions sont marquées d'un '-', ou '+' si vous [[alliances|êtes allié]] à cette faction.

Chaque unité possède un identifiant unique (ID) attribué par le système et utilisé pour tous les ordres.  
Dans le premier cas ici l'ID est ***tb2***.  
Dans Eressea, les identifiants des unités sont définis en *base 36*, donc constitués uniquement de caractères alphanumériques en minuscules.  

Chaque unité a également un nom ("Konrad Rabenhelm") ainsi peut-être qu'une description (après le point-virgule).  
Ensuite, les possessions visibles et, si l'information.  
La plupart des descriptions que vous rencontrerez au cours du jeu seront en allemand, car la majorité des joueurs est également allemande.  
Vous pouvez utiliser la langue qui vous convient pour nommer et décrire vos unités, mais gardez à l'esprit l'impact que cela peut avoir sur l'expérience de vos co-joueurs.est disponible, les compétences sont indiquées.

Cette première unité de l'exemple est l'unité de la faction qui a reçu ce rapport.  
Elle est composée d'un Humain de sa propre faction (non affiché), possède 20 Silver et peut se battre en [mêlée][melee]{title="Melee"}, compétence dans laquelle l'unité est de niveau 1.  
Il maîtrise [[cmd-tax|taxation]] au niveau 2 (pour plus de détails : les [[competences]]).  
Comme vous pouvez le voir, Konrad a également une [[tableaux-relatifs-a-la-guerre|épée]]{title="Sword"}.  
"`TAX`" est ce qu'on appelle un ordre par [[cmd-default|défaut]].  
Si l'unité ne reçoit pas de nouveaux ordres pour le prochain tour, elle continuera à collecter des taxes.  
Un seul ordre par défaut est donné dans le NR, mais les unités peuvent parfois en avoir plus d'un.  
Ils ne seront listés que dans le CR ou dans les modèles d'ordres.  
Plus d'informations à ce sujet dans le chapitre [[ordres]].

Les unités ont un "combat status" (posture en combat), qui dans ce cas est "front" (devant).  
Les détails sont expliqués dans le chapitre sur la [[guerre]] dans la section sur [lignes de combat][lignes-de-combat] et l'explication de l'ordre [[cmd-combat]].

Une unité peut garder une région (pour plus de détails sur les conséquences, voir [[cmd-guard]]).  
Cela sera noté par "guards the region" dans le rapport.

Enfin, une unité peut être blessée lors d'un [[guerre|combat]] ou d'une [famine][famine].  
Elle sera notée *[`exhausted`][etat-de-sante]* (épuisée), *`wounded`* (blessée), ou même *`badly wounded`* (gravement blessée).

L'unité suivante porte l'identifiant ***2ow***, est composée d'un nain, d'un cheval et d'une [[bourse-d-argent|bourse d'argent]]{title="Silverbag"}.  
Cela signifie qu'elle possède au moins 500 Silver.  
Si elle avait plus de 5 000 Silver, vous verriez un coffre d'argent.  
Vous ne pouvez pas voir à quelle faction appartient l'unité car elle est [[cmd-hide|masquée]], c'est-à-dire qu'elle ne révèle pas la faction à laquelle elle appartient.  
Ce n'est probablement pas un choix très judicieux pour un "Botschafter" (ambassadeur), car vous n'avez même pas l'adresse e-mail de la faction.  
La seule chose que vous pouvez faire est de lui envoyer un [[cmd-message]].

Enfin, des alliés [Trolls][trolls] transportent des gems (joyaux).  
En plus des [Humains][humains]{title="Humans"}, [Nains][nains]{title="Dwarves"}, et [Trolls][trolls], il y a beaucoup d'autres races en Eressea.  
Elles sont décrites dans [[races|ce chapitre]].

Vous ne disposez que d'informations limitées sur les unités étrangères.  
Leur statut au combat, leurs blessures, leurs compétences, leur groupe, leur camouflage de faction ou de race, leur statut de héros et leurs sorts sont cachés.  
La plupart des objets sont visibles, mais l'argent, les herbes et les objets magiques ne sont pas visibles en détail.

### Dissolution des unités

Si une unité se retrouve sans personne à la [[sequence-des-ordres|fin du tour]] (que ce soit à cause de la famine, en donnant des personnes ou en ne les obtenant jamais), elle sera dissoute.  
Ses objets vont à une unité de votre faction, s'il y en a une, ou à une faction alliée sinon (elle doit avoir [[cmd-help|`HELP silver`]] envers cette faction, qui elle doit avoir `HELP GIVE` envers la notre).  
En général, c'est à la première unité dans l'ordre du rapport que tout revient.  
Si les deux options ne sont pas possibles, l'argent et les chevaux vont à la région et tous les autres objets sont perdus.

Expérience de jeu (Solthar) :

Il est arrivé que des objets magiques spéciaux produisent une énergie impie qui maintenait leurs porteurs dans un état entre la vie et la mort.  
Cependant, ils n'étaient plus sous le contrôle de leur ancienne faction.

## Voir aussi

- [[reserve-de-faction|Réserve de faction]]
- [[ordres]]

Poursuivre la lecture : [[races]].

<!-- From [https://wiki.eressea.de/index.php?title=Parteien/fr&oldid=16447] -->

<!-- [bateaux]: [[bateaux]] -->
