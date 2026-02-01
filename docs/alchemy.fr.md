---
# cSpell:locale fr
alias: alchimie
---
# Alchimie

## Potions

Les **potions** sont préparées à l'aide de [[herbs|plantes]], et peuvent ensuite être utilisées par n'importe quelle **unité**.  

### Fabrication

Seule une unité sufisamment compétente en [alchimie] peut fabriquer une potion.  

Les potions sont concoctées avec l'ordre [[cmd-make|`MAKE "<nom de la potion>"`]].  

Une potion nécessite plusieurs ingrédients.  
La recette de préparation d'une potion est dévoilée à l'alchimiste quand son niveau de compétence vient d'augmenter et qu'il correspond au niveau d'une nouvelle potion.  

!!! tip "Astuce"

    La recette peut être ensuite retrouvée à tout moment avec l'ordre [[cmd-show|`SHOW "<nom potion>"`]].  

Pour pouvoir concocter une potion, le niveau de l'alchimiste doit être **2 fois plus élevé** que celui de la potion.  
Un alchimiste de niveau T pourra donc produire à chaque tour un nombre de potions N calculé ainsi :
$$N = \frac{T_{\text{unité}}}{Niveau_{\text{potion}}*2}$$

*Ex. Un alchimiste **T6** peut produire 1 potion N3 ($6\,/\,(3\,\times\,2)=1$), 1 potion N2 ($6\,/\,(2\,\times\,2)=1$) **ou** 3 potions N1 ($6\,/\,(1\,\times\,2)=3$).*  

!!! note "Note"
    Les plantes peuvent être découvertes dans une région puis récoltées par une unité compétente en [herboristerie].

### Utilisation

L'ordre [[cmd-use|`USE <quantité> "<nom potion>" <unit-id>`]] permet d'utiliser une ou plusieurs potions en sa possession.  

Remarque: l'identifiant d'unité `<unit-id>` est à renseigner **uniquement** pour le **[pain d'andouille]**.  

Une potion ne peut pas être divisée entre plusieurs unités.  
On peut cependant diviser une unité de plusieurs membres en plusieurs unités plus petites après l'utilisation de la potion en en conservant les effets.  

Les potions ont toutes un effet positif, à l'exception du [pain d'andouille].  

La plupart des potions profitent à l'unité qui les utilise.  
Mais certaines s'appliquent à une région. Dans ce cas, l'effet est obtenu dans la région où se trouve l'unité au début du tour - ou celles qui affectent d'autres unités ([pain d'andouille]).  

En général, une potion affecte 10 personnes ou 10 biens pendant le tour où elle est utilisée, comme indiqué dans sa recette.  
Les potions qui affectent les objets d'une unité expirent si elles ne peuvent pas être utilisées parce que l'unité ne possède plus ces objets.  
De nombreuses potions fonctionnent de telle sorte qu'un trop grand nombre de personnes dans l'unité importe peu, c'est-à-dire qu'avec 12 personnes et une potion (qui fonctionne pour 10), l'effet n'affecte que 10 des 12 personnes.  

Cela n'est pas possible avec le [sang de berserker], car les personnes n'agissent pas comme une unité au combat.  
Ici, il est nécessaire que toutes les personnes de l'unité aient l'effet de la potion avant le combat, sinon cela ne fonctionnera pas !  

L'effet "résiduel" des potions n'expire pas pour toutes les potions.  
Par exemple, une personne peut bénéficier de l'effet de l'[huile de cervelle] ou du [breuvage de labeur] pendant dix semaines après l'avoir utilisé.  

## Liste des potions

Vous trouverez ci-dessous la liste des potions par ordre croissant de niveau.

### Niveau 1

#### Eau de Goliath

<!-- cspell:disable -->
*Goliath water (EN), Goliathwasser (DE)*.
<!-- cspell:enable -->

:   10 hommes peuvent porter autant que 10 chevaux.

*Objectif :* augmenter la capacité à transporter.  
*Niveau :* **1**.  
*Cible :* **unité**.  

Plantes nécessaires pour concocter cette potion :

- [herbe de clairon]
- [champignon des fjords]

#### Eau de vie

<!-- cspell:disable -->
*Water of life (EN), Wasser des Lebens (DE)*.
<!-- cspell:enable -->

:   Transforme 10 bois (ou mallorn) en 10 pousses (ou pousses de mallorns).

*Objectif :* augmenter les ressources d'une région (arbres et mallorns).  
*Niveau :* **1**.  
*Cible :* **région**.  

Plantes nécessaires pour concocter cette potion :

- [amour d'Elfes]
- [racine de nœud]

#### Potion de vérité

<!-- cspell:disable -->
*Potion of truth (EN), Trank der Wahrheit (DE)*.
<!-- cspell:enable -->

:   ***Cette potion n'a plus aucune fonction***.

*Niveau :* 1.  
*Cible :* région.  

Plantes nécessaires pour concocter cette potion :

- [champignon des fjords]
- [racine plate]

#### Thé des sept lieues

<!-- cspell:disable -->
*Seven mile tea (EN), Siebenmeilentee (DE)*.
<!-- cspell:enable -->

:   10 hommes à pied peuvent se déplacer **aussi vite qu'à cheval**.

*Objectif :* augmenter la vitesse de déplacement.  
*Niveau :* **1**.  
*Cible :* **unité**.  

Plantes nécessaires pour concocter cette potion :

- [champignon cobalt]
- [gousse]

### Niveau 2

#### Breuvage de labeur

<!-- cspell:disable -->
*Busybeer (EN), Schaffenstrunk (DE)*.
<!-- cspell:enable -->

:   **Double la productivité** de 10 hommes utilisant l'ordre **`MAKE`**.

*Objectif :* accélérer la production.  
*Niveau :* **2**.  
*Cible :* **unité**.  

Plantes nécessaires pour concocter cette potion :

- [cire fissurée]
- [mandragore]
- [témérité piquante]

#### Onguent de soin

<!-- cspell:disable -->
*Ointment (EN), Wundsalbe (DE)*.
<!-- cspell:enable -->

:   Soigne jusqu'à 400 points de vie.

*Objectif :* soigner une unité.  
*Niveau :* **2**.  
*Cible :* **unité**.  

Plantes nécessaires pour concocter cette potion :

- [champignon cobalt]
- [témérité piquante]
- [tsuga blanc]

#### Sang de paysan

<!-- cspell:disable -->
*Peasant blood (EN), Bauernblut (DE)*.
<!-- cspell:enable -->

:   Jusqu'à 100 démons peuvent se passer de tuer des paysans.

*Objectif :* augmenter les ressources d'une région (paysans) où des démons sont présents.  
*Niveau :* **2**.  
*Cible :* **unité**.  

!!! warning "Remarque"
    Pour la préparation de cette potion, un paysan doit être sacrifié.

Éléments nécessaires pour concocter cette potion :

- [lichen des cavernes]
- [champignon cobalt]
- [champignon des fjords]
- **paysan**

!!! note
    Une *Peasant blood* agit sur l'unité, mais tous les démons de la faction de la région l'utilisent s'il en reste.  
    Il vous suffit donc d'équiper une seule unité (par région), à condition qu'elle boive suffisamment de *Peasant blood* pour tous les démons.

### Niveau 3

#### Bien-être des chevaux

<!-- cspell:disable -->
*Horsepower potion (EN), Pferdeglück (DE)*.
<!-- cspell:enable -->

:   Potion qui procure un état de grâce aux chevaux qui, incidemment, favorise les naissances.  
    **50 chevaux** mettent au monde jusqu'à **4 poulains**.

*Objectif :* augmenter les ressources d'une région (chevaux).  
*Niveau :* **3**.  
*Cible :* **région**.  

Plantes nécessaires pour concocter cette potion :

- [champignon cobalt]
- [racine de nœud]
- [peyote]
- [pourriture de sable]

#### Chaleur du nid

<!-- cspell:disable -->
*Potion of nest warmth (EN), Nestwärme (DE)*.
<!-- cspell:enable -->

:   Permet aux **[Insectes]** de recruter **même en hiver**.

*Objectif :* permettre le recrutement d'Insectes en hiver.  
*Niveau :* **3**.  
*Cible :* **région**.  

Plantes nécessaires pour concocter cette potion :

- [cire fissurée]
- [bégonia des glaces]
- [peyote]
- [lierre d'araignée]

#### Huile de cervelle

<!-- cspell:disable -->
*Brain wax (EN), Gehirnschmalz (DE)*.
<!-- cspell:enable -->

:   jusqu'à 10 personnes : augmente les chances **d'apprentissage d'une compétence**.

*Objectif :* accélérer l'apprentissage.  
*Niveau :* **3**.  
*Cible :* **unité**.  

Plantes nécessaires pour concocter cette potion :

- [herbe de clairon]
- [herbe de roche]
- [tamaris]
- [gousse]

#### Pain d'andouille

<!-- cspell:disable -->
*Duncebun (EN), Dumpfbackenbrot (DE)*.
<!-- cspell:enable -->

:   pour 10 personnes : pas d'apprentissage, ou l'enseignant n'apporte rien, ou oubli d'1 semaine de la meilleure compétence.

*Objectif :* ralentir l'apprentissage d'une unité (adverse).  
*Niveau :* **3**.  
*Cible :* unité étrangère.  

Plantes nécessaires pour concocter cette potion :

- [lichen des cavernes]
- [champignon des fjords]
- [œil de chouette]
- [lierre d'araignée]

[[cmd-use|À l'utilisation]], l'effet de la potion peut durer jusqu'à **10 semaines** par personne.

!!! note
    Vous pouvez l'appliquer à une unité avec l'ordre `USE "Duncebun" <ID unité cible>`.  
    L'effet de la potion échoue si la compétence `Stealth` de l'unité agissante est inférieure ou égale au niveau de `Perception` **+ 2** de la victime.  
    Dans ce cas, vous obtenez un message d'erreur et le [pain d'andouille] n'est pas consommé (il reste à l'unité).

#### Sang de berserker

<!-- cspell:disable -->
*Berserkers blood (EN), Berserkerblut (DE)*.
<!-- cspell:enable -->

:   10 personnes reçoivent un modificateur d'attaque de **+1** au combat.

*Objectif :* renforcer l'attaque.  
*Niveau :* **3**.  
*Cible :* **unité**.  

Plantes nécessaires pour concocter cette potion :

- [racine plate]
- [mandragore]
- [pourriture de sable]
- [tsuga blanc]

### Niveau 4

#### Amour des paysans

<!-- cspell:disable -->
*Peasant love potion (EN), Bauernlieb (DE)*.
<!-- cspell:enable -->

:   1 000 paysans **croissent deux fois plus vite** que la normale.

*Objectif :* augmenter les ressources d'une région (paysans).  
*Niveau*: **4**.  
*Cible*: **région**.  

Plantes nécessaires pour concocter cette potion :

- [morille]
- [amour d'Elfes]
- [mandragore]
- [herbe de roche]
- [pétale de cristal de neige]

#### Élixir de pouvoir

<!-- cspell:disable -->
*Elixir of power (EN), Elixier der Macht (DE)*.
<!-- cspell:enable -->

:   10 personnes ont leurs **points de vie multipliés par 5**.

*Objectif :* augmenter les points de vie d'une unité.  
*Niveau :* **4**.  
*Cible :* **unité**.  

Plantes nécessaires pour concocter cette potion :

- [[sang-de-dragon]]
- [morille]
- [amour d'Elfes]
- [lierre d'araignée]
- [tamaris]
- [gousse]

#### Potion de guérison

<!-- cspell:disable -->
*Healing potion (EN), Heiltrank (DE)*.
<!-- cspell:enable -->

:   Une personne survit à des dommages mortels (une seule fois par personne et par tour).

*Objectif :* augmenter les chances de survie au combat.  
*Niveau :* **4**.  
*Cible :* **unité**.  

Plantes nécessaires pour concocter cette potion :

- [herbe de clairon]
- [amour d'Elfes]
- [cire fissurée]
- [bégonia des glaces]
- [gousse]

## Potions - Synthèse

| Potion                  | Abr. | Niv. | Cible               |
|-------------------------|:----:|:----:|---------------------|
| [eau de Goliath]        |  GW  |  1   | Unité               |
| [eau de vie]            |  WL  |  1   | Région              |
| [potion de vérité]      |  PT  |  1   | Région              |
| [thé des sept lieues]   |  SM  |  1   | Unité               |
| [breuvage de labeur]    |  BZ  |  2   | Unité               |
| [onguent de soin]       |  OM  |  2   | Unité               |
| [sang de paysan]        |  PB  |  2   | Unité[^1]           |
| [bien-être des chevaux] |  HP  |  3   | Région              |
| [chaleur du nid]        |  NW  |  3   | Région              |
| [huile de cervelle]     |  BW  |  3   | Unité               |
| [pain d'andouille]      |  DB  |  3   | Unité étrangère[^2] |
| [sang de berserker]     |  BK  |  3   | Unité               |
| [amour des paysans]     |  PL  |  4   | Région              |
| [élixir de pouvoir]     |  EP  |  4   | Unité               |
| [potion de guérison]    |  HL  |  4   | Unité               |

[^1]: Le [sang de paysan] agit sur l'unité, mais tous les démons de la faction dans la région s'en servent s'il en reste.  
    Il suffit donc d'en équiper une unité (par région), tant qu'elle boit assez de sang de paysan pour tous les démons.
[^2]: la potion agit à une unité ciblée avec l'ordre `USE "Duncebun" <ID unité cible>`.  
    À cet égard, il convient de noter que si la compétence `Stealth` de l'utilisateur est inférieure ou égale à la `Perception` **+ 2** de la victime, la tentative échoue.  
    Si la tentative échoue, le [pain d'andouille] reste chez l'utilisateur et il reçoit un message d'erreur.

## Plantes et leur utilisation

| Plante                       |             [SM]             |             [GW]             |             [WL]             |             [PB]             |             [BZ]             |             [OM]             |             [BK]             |             [DB]             |             [BW]             |             [HP]             |             [NW]             |             [PL]             |             [EP]             |             [HL]             |
|------------------------------|:----------------------------:|:----------------------------:|:----------------------------:|:----------------------------:|:----------------------------:|:----------------------------:|:----------------------------:|:----------------------------:|:----------------------------:|:----------------------------:|:----------------------------:|:----------------------------:|:----------------------------:|:----------------------------:|
| [amour d'Elfes]              |                              |                              | :material-check:{ .success } |                              |                              |                              |                              |                              |                              |                              |                              | :material-check:{ .success } | :material-check:{ .success } | :material-check:{ .success } |
| [bégonia des glaces]         |                              |                              |                              |                              |                              |                              |                              |                              |                              |                              | :material-check:{ .success } |                              |                              | :material-check:{ .success } |
| [champignon cobalt]          | :material-check:{ .success } |                              |                              | :material-check:{ .success } |                              | :material-check:{ .success } |                              |                              |                              | :material-check:{ .success } |                              |                              |                              |                              |
| [champignon des fjords]      |                              | :material-check:{ .success } |                              | :material-check:{ .success } |                              |                              |                              | :material-check:{ .success } |                              |                              |                              |                              |                              |                              |
| [cire fissurée]              |                              |                              |                              |                              | :material-check:{ .success } |                              |                              |                              |                              |                              | :material-check:{ .success } |                              |                              | :material-check:{ .success } |
| [gousse]                     | :material-check:{ .success } |                              |                              |                              |                              |                              |                              |                              | :material-check:{ .success } |                              |                              |                              | :material-check:{ .success } | :material-check:{ .success } |
| [herbe de clairon]           |                              | :material-check:{ .success } |                              |                              |                              |                              |                              |                              | :material-check:{ .success } |                              |                              |                              |                              | :material-check:{ .success } |
| [herbe de roche]             |                              |                              |                              |                              |                              |                              |                              |                              | :material-check:{ .success } |                              |                              | :material-check:{ .success } |                              |                              |
| [lichen des cavernes]        |                              |                              |                              | :material-check:{ .success } |                              |                              |                              | :material-check:{ .success } |                              |                              |                              |                              |                              |                              |
| [lierre d'araignée]          |                              |                              |                              |                              |                              |                              |                              | :material-check:{ .success } |                              |                              | :material-check:{ .success } |                              | :material-check:{ .success } |                              |
| [mandragore]                 |                              |                              |                              |                              | :material-check:{ .success } |                              | :material-check:{ .success } |                              |                              |                              |                              | :material-check:{ .success } |                              |                              |
| [morille]                    |                              |                              |                              |                              |                              |                              |                              |                              |                              |                              |                              | :material-check:{ .success } | :material-check:{ .success } |                              |
| [œil de chouette]            |                              |                              |                              |                              |                              |                              |                              | :material-check:{ .success } |                              |                              |                              |                              |                              |                              |
| [peyote]                     |                              |                              |                              |                              |                              |                              |                              |                              |                              | :material-check:{ .success } | :material-check:{ .success } |                              |                              |                              |
| [pourriture de sable]        |                              |                              |                              |                              |                              |                              | :material-check:{ .success } |                              |                              | :material-check:{ .success } |                              |                              |                              |                              |
| [pétale de cristal de neige] |                              |                              |                              |                              |                              |                              |                              |                              |                              |                              |                              | :material-check:{ .success } |                              |                              |
| [racine de nœud]             |                              |                              | :material-check:{ .success } |                              |                              |                              |                              |                              |                              | :material-check:{ .success } |                              |                              |                              |                              |
| [racine plate]               |                              |                              |                              |                              |                              |                              | :material-check:{ .success } |                              |                              |                              |                              |                              |                              |                              |
| [tamaris]                    |                              |                              |                              |                              |                              |                              |                              |                              | :material-check:{ .success } |                              |                              |                              | :material-check:{ .success } |                              |
| [témérité piquante]          |                              |                              |                              |                              | :material-check:{ .success } | :material-check:{ .success } |                              |                              |                              |                              |                              |                              |                              |                              |
| [tsuga blanc]                |                              |                              |                              |                              |                              | :material-check:{ .success } | :material-check:{ .success } |                              |                              |                              |                              |                              |                              |                              |

Poursuivre la lecture : [[herbs|plantes]].

<!-- From [https://wiki.eressea.de/index.php?title=Tränke/fr&oldid=16931] -->

[alchimie]: ./skills-list.md#alchimie
[herboristerie]: ./skills-list.md#herboristerie
[Insectes]: ./races.md#insectes

[amour d'Elfes]: ./herbs.md#amour-delfes "Elvendear"
[bégonia des glaces]: ./herbs.md#begonia-des-glaces "Ice begonia"
[champignon cobalt]: ./herbs.md#champignon-cobalt "Cobalt fungus"
[champignon des fjords]: ./herbs.md#champignon-des-fjords "Fjord fungus"
[cire fissurée]: ./herbs.md#cire-fissuree "Gapgrowth"
[gousse]: ./herbs.md#gousse "Windbag"
[herbe de clairon]: ./herbs.md#herbe-de-clairon "Bugleweed"
[herbe de roche]: ./herbs.md#herbe-de-roche "Rock weed"
[lichen des cavernes]: ./herbs.md#lichen-des-cavernes "Cave lichen"
[lierre d'araignée]: ./herbs.md#lierre-daraignee "Spider ivy"
[mandragore]: ./herbs.md#mandragore "Mandrake"
[morille]: ./herbs.md#morille "Bubblemorel"
[pourriture de sable]: ./herbs.md#pourriture-de-sable "Sand reeker"
[peyote]: ./herbs.md#peyote "Peyote"
[pétale de cristal de neige]: ./herbs.md#petale-de-cristal-de-neige "Snowcrystal petal"
[racine de nœud]: ./herbs.md#racine-de-nud "Knotroot"
[racine plate]: ./herbs.md#racine-plate "Flatroot"
[tamaris]: ./herbs.md#tamaris "Waterfinder"
[tsuga blanc]: ./herbs.md#tsuga-blanc "White hemlocks"
[témérité piquante]: ./herbs.md#temerite-piquante "Tangy temerity"
[œil de chouette]: ./herbs.md#il-de-chouette "Owlsgaze"

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

[SM]: ./alchemy.md#the-des-sept-lieues "Thé des sept lieues (Seven mile tea)"
[GW]: ./alchemy.md#eau-de-goliath "Eau de Goliath (Goliath water)"
[WL]: ./alchemy.md#eau-de-vie "Eau de vie (Water of life)"
[PB]: ./alchemy.md#sang-de-paysan "Sang de paysan (Peasant blood)"
[BZ]: ./alchemy.md#breuvage-de-labeur "Breuvage de labeur (Busybeer)"
[OM]: ./alchemy.md#onguent-de-soin "Onguent de soin (Ointment)"
[BK]: ./alchemy.md#sang-de-berserker "Sang de berserker (Berserkers blood)"
[DB]: ./alchemy.md#pain-dandouille "Pain d'andouille (Duncebun)"
[BW]: ./alchemy.md#huile-de-cervelle "Huile de cervelle (Brain wax)"
[HP]: ./alchemy.md#bien-etre-des-chevaux "Bien-être des chevaux (Horsepower potion)"
[NW]: ./alchemy.md#chaleur-du-nid "Chaleur du nid (Potion of nest warmth)"
[PL]: ./alchemy.md#amour-des-paysans "Amour des paysans (Peasant love potion)"
[EP]: ./alchemy.md#elixir-de-pouvoir "Élixir de pouvoir (Elixir of power)"
[HL]: ./alchemy.md#potion-de-guerison "Potion de guérison ()"
