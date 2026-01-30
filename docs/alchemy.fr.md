---
# cSpell:locale fr
alias: alchimie
---
# Alchimie

## Potions

Les **potions** sont préparées à l'aide de [[herbs|plantes]] et d'autres ingrédients, et peuvent ensuite être utilisées par n'importe quelle **unité**.  
Pour fabriquer une potion, il faut des unités compétentes en [alchimie], et pour trouver les plantes nécessaires, il faut des unités maîtrisant l'[herboristerie].

Les potions sont produites avec l'ordre [[cmd-make|`MAKE "<nom de la potion>"`]].  
Une potion nécessite plusieurs ingrédients.  
Les recettes sont données à chaque fois que l'on atteint le niveau requis pour les concocter.  
Plus tard, on pourra les retrouver avec l'ordre [[cmd-show]].  
Pour pouvoir fabriquer une potion, le niveau de l'alchimiste doit être deux fois plus élevé que le niveau de la potion.  
Un alchimiste peut chaque tour créer (niveau de compétence)/(niveau de potion\*2) potions.  
Un alchimiste de niveau 6 peut donc fabriquer au maximum une potion de niveau 3, une potion de niveau 2 ou trois potions de niveau 1.  

Si vous souhaitez utiliser une potion, vous le faites avec l'ordre [[cmd-use|USE &#91;quantité&#93; "&lt;nom de la potion&gt;" &#91;ID d'unité&#93;]].  
*L'identifiant d'unité (ID)* ne doit être spécifié **uniquement** pour la potion de **[pain d'andouille]**.  

Une potion ne peut pas être divisée entre plusieurs unités.  
On peut cependant diviser une grande unité en plusieurs unités plus petites après l'utilisation de la potion en en conservant les effets.  

La plupart des potions profitent à l'unité qui les utilise.  
Les exceptions sont les potions qui se rapportent à une région - dans ce cas, l'effet est obtenu dans la région où se trouve l'unité au début du tour - ou celles qui affectent d'autres unités ([pain d'andouille]).  

En général, une potion affecte 10 personnes ou 10 biens pendant le tour où elle est utilisée, comme indiqué dans sa recette.  
Les potions qui affectent les objets d'une unité expirent si elles ne peuvent pas être utilisées parce que l'unité ne possède plus ces objets.  
De nombreuses potions fonctionnent de telle sorte qu'un trop grand nombre de personnes dans l'unité importe peu, c'est-à-dire qu'avec 12 personnes et une potion (qui fonctionne pour 10), l'effet n'affecte que 10 des 12 personnes.  
Cela n'est pas possible avec le [sang de berserker], car les personnes n'agissent pas comme une unité au combat.  
Ici, il est nécessaire que toutes les personnes de l'unité aient l'effet de la potion avant le combat, sinon cela ne fonctionnera pas !  

L'"effet résiduel" des potions n'expire pas pour toutes les potions;
par exemple, une personne peut bénéficier de l'effet de l'[huile de cervelle] ou du [breuvage de labeur] pendant dix semaines après l'avoir utilisé.  

### Sang de berserker

<!-- cspell:disable -->
*Berserkers blood (EN), Berserkerblut (DE)*.
<!-- cspell:enable -->

:   10 personnes reçoivent un modificateur d'attaque de **+1** au combat.

*Objectif :* renforcer l'attaque.  
*Niveau requis :* **3**.  
*Cible :* **unité**.  

Plantes nécessaires pour concocter cette potion :

- 1 [racine plate]
- 1 [mandragore]
- 1 [pourriture de sable]
- 1 [tsugas blancs]

### Huile de cervelle

<!-- cspell:disable -->
*Brain wax (EN), Gehirnschmalz (DE)*.
<!-- cspell:enable -->

:   jusqu'à 10 personnes : augmente les chances **d'apprentissage d'une compétence**.

*Objectif :* accélérer l'apprentissage.  
*Niveau requis :* **3**.  
*Cible :* **unité**.  

Plantes nécessaires pour concocter cette potion :

- 1 [herbe de clairon]
- 1 [herbe de roche]
- 1 [waterfinder]
- 1 [gousse]

### Breuvage de labeur

<!-- cspell:disable -->
*Busybeer (EN), Schaffenstrunk (DE)*.
<!-- cspell:enable -->

:   **Double la productivité** de 10 hommes utilisant l'ordre **`MAKE`**.

*Objectif :* accélérer la production.  
*Niveau requis :* **2**.  
*Cible :* **unité**.  

Plantes nécessaires pour concocter cette potion :

- 1 [cire fissurée]
- 1 [mandragore]
- 1 [témérité piquante]

### Pain d'andouille

<!-- cspell:disable -->
*Duncebun (EN), Dumpfbackenbrot (DE)*.
<!-- cspell:enable -->

:   pour 10 personnes : pas d'apprentissage, ou l'enseignant n'apporte rien, ou oubli d'1 semaine de la meilleure compétence.

*Objectif :* ralentir l'apprentissage d'une unité (adverse).  
*Niveau requis :* **3**.  
*Cible :* unité \[étrangère\].  

Plantes nécessaires pour concocter cette potion :

- 1 [lichen des cavernes]
- 1 [champignon des fjords]
- 1 [œil de chouette]
- 1 [lierre d'araignée]

[[cmd-use|À l'utilisation]], l'effet de la potion peut durer jusqu'à **10 semaines** par personne.

!!! note
    Vous pouvez l'appliquer à une unité avec l'ordre `USE "Duncebun" <ID unité cible>`.  
    L'effet de la potion échoue si la compétence `Stealth` de l'unité agissante est inférieure ou égale au niveau de `Perception` **+ 2** de la victime.  
    Dans ce cas, vous obtenez un message d'erreur et le [pain d'andouille] n'est pas consommé (il reste à l'unité).

### Élixir de pouvoir

<!-- cspell:disable -->
*Elixir of power (EN), Elixier der Macht (DE)*.
<!-- cspell:enable -->

:   10 personnes ont leurs **points de vie multipliés par 5**.

*Objectif :* augmenter les points de vie d'une unité.  
*Niveau requis :* **4**.  
*Cible :* **unité**.  

Plantes nécessaires pour concocter cette potion :

- 1 [[sang-de-dragon]]
- 1 [morille]
- 1 [amour d'Elfes]
- 1 [lierre d'araignée]
- 1 [waterfinder]
- 1 [gousse]

### Eau de Goliath

<!-- cspell:disable -->
*Goliath water (EN), Goliathwasser (DE)*.
<!-- cspell:enable -->

:   10 hommes peuvent porter autant que 10 chevaux.

*Objectif :* augmenter la capacité à transporter.  
*Niveau requis :* **1**.  
*Cible :* **unité**.  

Plantes nécessaires pour concocter cette potion :

- 1 [herbe de clairon]
- 1 [champignon des fjords]

### Potion de guérison

<!-- cspell:disable -->
*Healing potion (EN), Heiltrank (DE)*.
<!-- cspell:enable -->

:   Une personne survit à des dommages mortels (une seule fois par personne et par tour).

*Objectif :* augmenter les chances de survie au combat.  
*Niveau requis :* **4**.  
*Cible :* **unité**.  

Plantes nécessaires pour concocter cette potion :

- 1 [herbe de clairon]
- 1 [amour d'Elfes]
- 1 [cire fissurée]
- 1 [bégonia des glaces]
- 1 [gousse]

### Bien-être des chevaux

<!-- cspell:disable -->
*Horsepower potion (EN), Pferdeglück (DE)*.
<!-- cspell:enable -->

:   Potion qui procure un état de grâce aux chevaux qui, incidemment, favorise les naissances.  
    **50 chevaux** mettent au monde jusqu'à **4 poulains**.

*Objectif :* augmenter les ressources d'une région (chevaux).  
*Niveau requis :* **3**.  
*Cible :* **région**.  

Plantes nécessaires pour concocter cette potion :

- 1 [champignon cobalt]
- 1 [racine de nœud]
- 1 [peyote]
- 1 [pourriture de sable]

### Onguent de soin

<!-- cspell:disable -->
*Ointment (EN), Wundsalbe (DE)*.
<!-- cspell:enable -->

:   Soigne jusqu'à 400 points de vie.

*Objectif :* soigner une unité.  
*Niveau requis :* **2**.  
*Cible :* **unité**.  

Plantes nécessaires pour concocter cette potion :

- 1 [champignon cobalt]
- 1 [témérité piquante]
- 1 [tsugas blancs]

### Sang de paysan

<!-- cspell:disable -->
*Peasant blood (EN), Bauernblut (DE)*.
<!-- cspell:enable -->

:   Jusqu'à 100 démons peuvent se passer de tuer des paysans.

*Objectif :* augmenter les ressources d'une région (paysans) où des démons sont présents.  
*Niveau requis :* **2**.  
*Cible :* **unité**.  

Éléments nécessaires pour concocter cette potion :

- 1 [lichen des cavernes]
- 1 [champignon cobalt]
- 1 [champignon des fjords]
- 1 **paysan**

!!! note
    Une *Peasant blood* agit sur l'unité, mais tous les démons de la faction de la région l'utilisent s'il en reste.  
    Il vous suffit donc d'équiper une seule unité (par région), à condition qu'elle boive suffisamment de *Peasant blood* pour tous les démons.

### Amour des paysans

<!-- cspell:disable -->
*Peasant love potion (EN), Bauernlieb (DE)*.
<!-- cspell:enable -->

:   1 000 paysans **croissent deux fois plus vite** que la normale.

*Objectif :* augmenter les ressources d'une région (paysans).  
*Niveau requis*: **4**.  
*Cible*: **région**.  

Plantes nécessaires pour concocter cette potion :

- 1 [morille]
- 1 [amour d'Elfes]
- 1 [mandragore]
- 1 [herbe de roche]
- 1 [pétale de cristal de neige]

### Chaleur du nid

<!-- cspell:disable -->
*Potion of nest warmth (EN), Nestwärme (DE)*.
<!-- cspell:enable -->

:   Permet aux **[Insectes]** de recruter **même en hiver**.

*Objectif :* permettre le recrutement d'Insectes en hiver.  
*Niveau requis :* **3**.  
*Cible :* **région**.  

Plantes nécessaires pour concocter cette potion :

- 1 [cire fissurée]
- 1 [bégonia des glaces]
- 1 [peyote]
- 1 [lierre d'araignée]

### Potion de vérité

<!-- cspell:disable -->
*Potion of truth (EN), Trank der Wahrheit (DE)*.
<!-- cspell:enable -->

:   ***Cette potion n'a plus aucune fonction***.

*Niveau requis :* 1.  
*Cible :* région.  

Plantes nécessaires pour concocter cette potion :

- 1 [champignon des fjords]
- 1 [racine plate]

### Thé des sept lieues

<!-- cspell:disable -->
*Seven mile tea (EN), Siebenmeilentee (DE)*.
<!-- cspell:enable -->

:   10 hommes à pied peuvent se déplacer **aussi vite qu'à cheval**.

*Objectif :* augmenter la vitesse de déplacement.  
*Niveau requis :* **1**.  
*Cible :* **unité**.  

Plantes nécessaires pour concocter cette potion :

- 1 [champignon cobalt]
- 1 [gousse]

### Eau de vie

<!-- cspell:disable -->
*Water of life (EN), Wasser des Lebens (DE)*.
<!-- cspell:enable -->

:   Transforme 10 bois (ou mallorn) en 10 pousses (ou pousses de mallorns).

*Objectif :* augmenter les ressources d'une région (arbres et mallorns).  
*Niveau requis :* **1**.  
*Cible :* **région**.  

Plantes nécessaires pour concocter cette potion :

- 1 [amour d'Elfes]
- 1 [racine de nœud]

## Tableau récapitulatif

| Potion                  | Abr. | Niv. | Cible                   |
|-------------------------|:----:|:----:|-------------------------|
| [eau de Goliath]        |  GW  |  1   | Unité                   |
| [potion de vérité]      |  PT  |  1   | Région                  |
| [thé des sept lieues]   |  SM  |  1   | Unité                   |
| [eau de vie]            |  WL  |  1   | Région                  |
| [breuvage de labeur]    |  BZ  |  2   | Unité                   |
| [onguent de soin]       |  OM  |  2   | Unité                   |
| [sang de paysan]        |  PB  |  2   | Unité[^1]               |
| [sang de berserker]     |  BK  |  3   | Unité                   |
| [huile de cervelle]     |  BW  |  3   | Unité                   |
| [pain d'andouille]      |  DB  |  3   | Unité \[étrangère\][^2] |
| [bien-être des chevaux] |  HP  |  3   | Région                  |
| [chaleur du nid]        |  NW  |  3   | Région                  |
| [élixir de pouvoir]     |  EP  |  4   | Unité                   |
| [potion de guérison]    |  HL  |  4   | Unité                   |
| [amour des paysans]     |  PL  |  4   | Région                  |

[^1]: Le [sang de paysan] agit sur l'unité, mais tous les démons de la faction dans la région s'en servent s'il en reste.  
    Il suffit donc d'en équiper une unité (par région), tant qu'elle boit assez de sang de paysan pour tous les démons.
[^2]: la potion agit à une unité ciblée avec l'ordre `USE "Duncebun" <ID unité cible>`.  
    À cet égard, il convient de noter que si la compétence `Stealth` de l'utilisateur est inférieure ou égale à la `Perception` **+ 2** de la victime, la tentative échoue.  
    Si la tentative échoue, le [pain d'andouille] reste chez l'utilisateur et il reçoit un message d'erreur.

## Plantes et leur utilisation

| Plante                     | PT | SM | GW | WL | PB | BZ | OM | BK | DB | BW | HP | NW | PL | EP | HL |
|----------------------------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| morille                    |    |    |    |    |    |    |    |    |    |    |    |    | X  | X  |    |
| herbe de clairon           |    |    | X  |    |    |    |    |    |    | X  |    |    |    |    | X  |
| lichen des cavernes        |    |    |    |    | X  |    |    |    | X  |    |    |    |    |    |    |
| champignon cobalt          |    | X  |    |    | X  |    | X  |    |    |    | X  |    |    |    |    |
| amour d'Elfes              |    |    |    | X  |    |    |    |    |    |    |    |    | X  | X  | X  |
| champignon des fjords      | X  |    | X  |    | X  |    |    |    | X  |    |    |    |    |    |    |
| racine plate               | X  |    |    |    |    |    |    | X  |    |    |    |    |    |    |    |
| cire fissurée              |    |    |    |    |    | X  |    |    |    |    |    | X  |    |    | X  |
| bégonia des glaces         |    |    |    |    |    |    |    |    |    |    |    | X  |    |    | X  |
| racine de nœud             |    |    |    | X  |    |    |    |    |    |    | X  |    |    |    |    |
| mandragore                 |    |    |    |    |    | X  |    | X  |    |    |    |    | X  |    |    |
| œil de chouette            |    |    |    |    |    |    |    |    | X  |    |    |    |    |    |    |
| peyote                     |    |    |    |    |    |    |    |    |    |    | X  | X  |    |    |    |
| herbe de roche             |    |    |    |    |    |    |    |    |    | X  |    |    | X  |    |    |
| pourriture de sable        |    |    |    |    |    |    |    | X  |    |    | X  |    |    |    |    |
| pétale de cristal de neige |    |    |    |    |    |    |    |    |    |    |    |    | X  |    |    |
| lierre d'araignée          |    |    |    |    |    |    |    |    | X  |    |    | X  |    | X  |    |
| témérité piquante          |    |    |    |    |    | X  | X  |    |    |    |    |    |    |    |    |
| waterfinder                |    |    |    |    |    |    |    |    |    | X  |    |    |    | X  |    |
| tsugas blancs              |    |    |    |    |    |    | X  | X  |    |    |    |    |    |    |    |
| gousse                     |    | X  |    |    |    |    |    |    |    | X  |    |    |    | X  | X  |

Poursuivre la lecture : [[herbs|plantes]].

<!-- From [https://wiki.eressea.de/index.php?title=Tränke/fr&oldid=16931] -->

[alchimie]: ./skills-list.md#alchimie
[herboristerie]: ./skills-list.md#herboristerie
[Insectes]: ./races.md#insectes
[morille]: ./herbs.md#morille "Bubblemorel"
[herbe de clairon]: ./herbs.md#herbe-de-clairon "Bugleweed"
[lichen des cavernes]: ./herbs.md#lichen-des-cavernes "Cave lichen"
[champignon cobalt]: ./herbs.md#champignon-cobalt "Cobalt fungus"
[amour d'Elfes]: ./herbs.md#amour-delfes "Elvendear"
[champignon des fjords]: ./herbs.md#champignon-des-fjords "Fjord fungus"
[racine plate]: ./herbs.md#racine-plate "Flatroot"
[cire fissurée]: ./herbs.md#cire-fissuree "Gapgrowth"
[bégonia des glaces]: ./herbs.md#begonia-des-glaces "Ice begonia"
[racine de nœud]: ./herbs.md#racine-de-nud "Knotroot"
[mandragore]: ./herbs.md#mandragore "Mandrake"
[œil de chouette]: ./herbs.md#il-de-chouette "Owlsgaze"
[herbe de roche]: ./herbs.md#herbe-de-roche "Rock weed"
[pourriture de sable]: ./herbs.md#pourriture-de-sable "Sand reeker"
[pétale de cristal de neige]: ./herbs.md#petale-de-cristal-de-neige "Snowcrystal petal"
[lierre d'araignée]: ./herbs.md#lierre-daraignee "Spider ivy"
[témérité piquante]: ./herbs.md#temerite-piquante "Tangy temerity"
[waterfinder]: ./herbs.md#tamaris "Waterfinder"
[tsugas blancs]: ./herbs.md#tsugas-blancs "White hemlocks"
[gousse]: ./herbs.md#gousse "Windbag

[eau de Goliath]: #eau-de-goliath "Goliath water"
[eau de vie]: #eau-de-vie "Water of life"
[breuvage de labeur]: #breuvage-de-labeur "Busybeer"
[onguent de soin]: #onguent-de-soin "Ointment"
[sang de paysan]: #sang-de-paysan "Peasant blood"
[sang de berserker]: #sang-de-berserker "Berserkers blood"
[huile de cervelle]: #huile-de-cervelle "Brain wax"
[pain d'andouille]: #pain-dandouille "Duncebun"
[chaleur du nid]: #chaleur-du-nid "Potion of nest warmth"
[amour des paysans]: #amour-des-paysans "Peasant love potion"
[potion de vérité]: ./alchemy.md#potion-de-verite "Potion of truth"
[thé des sept lieues]: ./alchemy.md#the-des-sept-lieues "Seven mile tea"
[bien-être des chevaux]: ./alchemy.md#bien-etre-des-chevaux "Horsepower potion"
[élixir de pouvoir]: ./alchemy.md#elixir-de-pouvoir "Elixir of power"
[potion de guérison]: ./alchemy.md#potion-de-guerison "Healing potion"
