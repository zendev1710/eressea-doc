---
# cSpell:locale fr
alias: alchimie
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD051 MD052 -->
# Alchimie

Dans Eressea, l'alchimie est l'art de transformer des substances naturelles (plantes) en potions.

## Potions

Dans le monde d'Eressea, les potions ne sont pas de simples breuvages.
Ce sont de puissants outils capables de renverser le cours des événements et d'influencer grandement le destin d'un peuple, par exemple pour soutenir la production, renforcer les troupes au combat ou aider un peuple à prospérer.  

Les potions sont préparées à l'aide de [[herbs|plantes]], et peuvent ensuite être utilisées par n'importe quelle **unité**.  

Une potion ne pèse rien.

### Fabrication

Seule une personne sufisamment compétente en [alchimie][alchimie]{title="Alchemy"}, appelée alchimiste, peut fabriquer une potion.  

!!! warning "Remarque"
    Une faction compte au plus **3 alchimistes**.

Les potions sont concoctées avec l'ordre [[cmd-make|`MAKE "<nom de la potion>"`]].  

Une potion nécessite plusieurs ingrédients.  
La recette de préparation d'une potion est dévoilée à l'alchimiste quand son niveau de compétence vient d'augmenter et qu'il correspond au niveau d'une nouvelle potion.  

!!! tip "Astuce"
    La recette peut être ensuite retrouvée à tout moment avec l'ordre [[cmd-show|`SHOW "<nom potion>"`]].  

Pour pouvoir concocter une potion, le niveau de l'alchimiste doit être **2 fois plus élevé** que celui de la potion.  
Un alchimiste de niveau T pourra donc produire à chaque tour un nombre de potions N calculé ainsi :
$$
N = \frac{T_{\text{unité}}}{Niveau_{\text{potion}}*2}
$$

*Ex. Un alchimiste **T6** peut produire 1 potion N3 ($6\,/\,(3\,\times\,2)=1$), 1 potion N2 ($6\,/\,(2\,\times\,2)=1$) ou 3 potions N1 ($6\,/\,(1\,\times\,2)=3$).*  

!!! note "Note"
    Les plantes peuvent être [[cmd-research|découvertes]] dans une région puis [[cmd-make|récoltées]] par une unité compétente en [herboristerie][herboristerie]{title="Herbalism"}.

### Utilisation

L'ordre [`USE [<quantité>] "<nom potion>" [<unit-id>]`][cmd-use] permet d'utiliser une ou plusieurs potions en sa possession.  

Remarque: l'identifiant d'unité `<unit-id>` est à renseigner **uniquement** pour le **[pain d'andouille]**.  

Une potion ne peut pas être partagée entre plusieurs unités.  
On peut cependant diviser une unité de plusieurs membres en plusieurs unités plus petites après l'utilisation de la potion en en conservant les effets.  

Les potions ont toutes un effet positif, à l'exception du [pain d'andouille].  

La plupart des potions profitent à l'unité qui les utilise.  
Mais certaines s'appliquent à une région. Dans ce cas, l'effet est obtenu dans la région où se trouve l'unité au début du tour - ou celles qui affectent d'autres unités ([pain d'andouille]).  

En général, une potion affecte 10 personnes ou 10 objets pendant le tour où elle est utilisée, comme indiqué dans sa recette.  
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

:   10 personnes peuvent porter autant que 10 chevaux.

*Objectif :* augmenter la capacité de transport.  
*Niveau :* **1**.  
*Cible :* **unité**.  

Plantes nécessaires pour concocter cette potion :

- [champignon des fjords][champignon-des-fjords]{title="Fjord fungus"}
- [herbe de clairon][herbe-de-clairon]{title="Bugleweed"}

#### Eau de vie

<!-- cspell:disable -->
*Water of life (EN), Wasser des Lebens (DE)*.
<!-- cspell:enable -->

:   Transforme 10 bois (ou mallorn) en 10 pousses (ou pousses de mallorns).

*Objectif :* augmenter les ressources d'une région (arbres et mallorns).  
*Niveau :* **1**.  
*Cible :* **région**.  

Plantes nécessaires pour concocter cette potion :

- [amour d'Elfes][amour-delfes]{title="Elvendear"}
- [racine de nœud][racine-de-nud]{title="Knotroot"}

#### Potion de vérité

<!-- cspell:disable -->
*Potion of truth (EN), Trank der Wahrheit (DE)*.
<!-- cspell:enable -->

:   ***Cette potion n'a plus aucune fonction***.

*Niveau :* 1.  
*Cible :* région.  

Plantes nécessaires pour concocter cette potion :

- [champignon des fjords][champignon-des-fjords]{title="Fjord fungus"}
- [racine plate][racine-plate]{title="Flatroot"}

#### Thé des sept lieues

<!-- cspell:disable -->
*Seven mile tea (EN), Siebenmeilentee (DE)*.
<!-- cspell:enable -->

:   10 personnes à pied peuvent se déplacer **aussi vite qu'à cheval**.

*Objectif :* augmenter la vitesse de déplacement.  
*Niveau :* **1**.  
*Cible :* **unité**.  

Plantes nécessaires pour concocter cette potion :

- [champignon cobalt][champignon-cobalt]{title="Cobalt fungus"}
- [gousse][gousse]{title="Windbag"}

### Niveau 2

#### Breuvage de labeur

<!-- cspell:disable -->
*Busybeer (EN), Schaffenstrunk (DE)*.
<!-- cspell:enable -->

:   **Double la productivité** de 10 hommes utilisant l'ordre **`MAKE`**.

*Objectif :* augmenter la productivité.  
*Niveau :* **2**.  
*Cible :* **unité**.  

Plantes nécessaires pour concocter cette potion :

- [cire fissurée][cire-fissuree]{title="Gapgrowth"}
- [mandragore][mandragore]{title="Mandrake"}
- [témérité piquante][temerite-piquante]{title="Tangy temerity"}

#### Onguent de soin

<!-- cspell:disable -->
*Ointment (EN), Wundsalbe (DE)*.
<!-- cspell:enable -->

:   Soigne jusqu'à 400 points de vie.

*Objectif :* soigner une unité.  
*Niveau :* **2**.  
*Cible :* **unité**.  

Plantes nécessaires pour concocter cette potion :

- [champignon cobalt][champignon-cobalt]{title="Cobalt fungus"}
- [témérité piquante][temerite-piquante]{title="Tangy temerity"}
- [tsuga blanc][tsuga-blanc]{title="White hemlocks"}

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

- [champignon cobalt][champignon-cobalt]{title="Cobalt fungus"}
- [champignon des fjords][champignon-des-fjords]{title="Fjord fungus"}
- [lichen des cavernes][lichen-des-cavernes]{title="Cave lichen"}
- paysan

!!! note
    Cette potion agit sur l'unité, mais tous les démons de la faction de la région l'utilisent s'il en reste.  
    Il vous suffit donc d'équiper une seule unité (par région), à condition qu'elle boive suffisamment de cette potion pour tous les démons.

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

- [champignon cobalt][champignon-cobalt]{title="Cobalt fungus"}
- [peyote][peyote]{title="Peyote"}
- [pourriture de sable][pourriture-de-sable]{title="Sand reeker"}
- [racine de nœud][racine-de-nud]{title="Knotroot"}

#### Chaleur du nid

<!-- cspell:disable -->
*Potion of nest warmth (EN), Nestwärme (DE)*.
<!-- cspell:enable -->

:   Permet aux **[Insectes][insectes]** de recruter **même en hiver**.

*Objectif :* permettre le recrutement d'Insectes en hiver.  
*Niveau :* **3**.  
*Cible :* **région**.  

Plantes nécessaires pour concocter cette potion :

- [bégonia des glaces][begonia-des-glaces]{title="Ice begonia"}
- [cire fissurée][cire-fissuree]{title="Gapgrowth"}
- [lierre d'araignée]
- [peyote][peyote]{title="Peyote"}

#### Huile de cervelle

<!-- cspell:disable -->
*Brain wax (EN), Gehirnschmalz (DE)*.
<!-- cspell:enable -->

:   Augmente les chances **d'apprentissage d'une compétence**.

*Objectif :* accélérer l'apprentissage.  
*Niveau :* **3**.  
*Cible :* **au plus 10 membres d'une unité**.  

Plantes nécessaires pour concocter cette potion :

- [gousse][gousse]{title="Windbag"}
- [herbe de clairon][herbe-de-clairon]{title="Bugleweed"}
- [herbe de roche][herbe-de-roche]{title="Rock weed"}
- [tamaris][tamaris]{title="Waterfinder"}

#### Pain d'andouille

<!-- cspell:disable -->
*Duncebun (EN), Dumpfbackenbrot (DE)*.
<!-- cspell:enable -->

:   Bloque l'apprentissage, l'enseignement, ou provoque l'oubli de la meilleure compétence pendant uen semaine.

*Objectif :* ralentir l'apprentissage d'une unité.  
*Niveau :* **3**.  
*Cible :* **10 membres d'une unité (logiquement adverse)**.  

Plantes nécessaires pour concocter cette potion :

- [champignon des fjords][champignon-des-fjords]{title="Fjord fungus"}
- [lichen des cavernes][lichen-des-cavernes]{title="Cave lichen"}
- [lierre d'araignée]
- [œil de chouette][il-de-chouette]{title="Owlsgaze"}

[[cmd-use|À l'utilisation]], l'effet de la potion peut durer jusqu'à **10 semaines** par personne.

!!! note
    Vous pouvez l'appliquer à une unité avec l'ordre `USE "Duncebun" <ID unité cible>`.  
    L'effet de la potion échoue si le niveau de [discrétion][discretion]{title="Stealth"} de l'unité agissante est inférieur ou égal **au niveau de [perception][perception]{title="Perception"} + 2** de la victime.  
    Dans ce cas, vous obtenez un message d'erreur et le [pain d'andouille] n'est pas consommé (il reste à l'unité).

#### Sang de berserker

<!-- cspell:disable -->
*Berserkers blood (EN), Berserkerblut (DE)*.
<!-- cspell:enable -->

:   L'unité reçoit un modificateur d'attaque de **+1** au combat.

*Objectif :* renforcer l'attaque.  
*Niveau :* **3**.  
*Cible :* **au plus 10 membres d'une unité**.  

Plantes nécessaires pour concocter cette potion :

- [mandragore][mandragore]{title="Mandrake"}
- [pourriture de sable][pourriture-de-sable]{title="Sand reeker"}
- [racine plate][racine-plate]{title="Flatroot"}
- [tsuga blanc][tsuga-blanc]{title="White hemlocks"}

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

- [amour d'Elfes][amour-delfes]{title="Elvendear"}
- [herbe de roche][herbe-de-roche]{title="Rock weed"}
- [mandragore][mandragore]{title="Mandrake"}
- [morille][morille]{title="Bubblemorel"}
- [pétale de cristal de neige][petale-de-cristal-de-neige]{title="Snowcrystal petal"}

#### Élixir de pouvoir

<!-- cspell:disable -->
*Elixir of power (EN), Elixier der Macht (DE)*.
<!-- cspell:enable -->

:   Les **Points de Vie sont multipliés par 5**.

*Objectif :* augmenter les Points de Vie d'une unité.  
*Niveau :* **4**.  
*Cible :* **au plus 10 membres d'une unité**.  

Plantes nécessaires pour concocter cette potion :

- [amour d'Elfes][amour-delfes]{title="Elvendear"}
- [gousse][gousse]{title="Windbag"}
- [lierre d'araignée]
- [morille][morille]{title="Bubblemorel"}
- [[sang-de-dragon]]
- [tamaris][tamaris]{title="Waterfinder"}

#### Potion de guérison

<!-- cspell:disable -->
*Healing potion (EN), Heiltrank (DE)*.
<!-- cspell:enable -->

:   Une personne survit à des dommages mortels (une seule fois par personne et par tour).

*Objectif :* augmenter les chances de survie au combat.  
*Niveau :* **4**.  
*Cible :* **unité**.  

Plantes nécessaires pour concocter cette potion :

- [amour d'Elfes][amour-delfes]{title="Elvendear"}
- [bégonia des glaces][begonia-des-glaces]{title="Ice begonia"}
- [cire fissurée][cire-fissuree]{title="Gapgrowth"}
- [gousse][gousse]{title="Windbag"}
- [herbe de clairon][herbe-de-clairon]{title="Bugleweed"}

## Potions - Synthèse

| Potion                  | Niv. | Cible               |
|-------------------------|:----:|---------------------|
| [eau de Goliath]        |  1   | Unité               |
| [eau de vie]            |  1   | Région              |
| [potion de vérité]      |  1   | Région              |
| [thé des sept lieues]   |  1   | Unité               |
| [breuvage de labeur]    |  2   | Unité               |
| [onguent de soin]       |  2   | Unité               |
| [sang de paysan]        |  2   | Unité[^1]           |
| [bien-être des chevaux] |  3   | Région              |
| [chaleur du nid]        |  3   | Région              |
| [huile de cervelle]     |  3   | Unité               |
| [pain d'andouille]      |  3   | Unité étrangère[^2] |
| [sang de berserker]     |  3   | Unité               |
| [amour des paysans]     |  4   | Région              |
| [élixir de pouvoir]     |  4   | Unité               |
| [potion de guérison]    |  4   | Unité               |

## Plantes et leur utilisation

| Plante                                                                              |             [SM]             |             [GW]             |             [WL]             |             [PB]             |             [BZ]             |             [OM]             |             [BK]             |             [DB]             |             [BW]             |             [HP]             |             [NW]             |             [PL]             |             [EP]             |             [HL]             |
|-------------------------------------------------------------------------------------|:----------------------------:|:----------------------------:|:----------------------------:|:----------------------------:|:----------------------------:|:----------------------------:|:----------------------------:|:----------------------------:|:----------------------------:|:----------------------------:|:----------------------------:|:----------------------------:|:----------------------------:|:----------------------------:|
| [amour d'Elfes][amour-delfes]{title="Elvendear"}                                    |                              |                              | :material-check:{ .success } |                              |                              |                              |                              |                              |                              |                              |                              | :material-check:{ .success } | :material-check:{ .success } | :material-check:{ .success } |
| [bégonia des glaces][begonia-des-glaces]{title="Ice begonia"}                       |                              |                              |                              |                              |                              |                              |                              |                              |                              |                              | :material-check:{ .success } |                              |                              | :material-check:{ .success } |
| [champignon cobalt][champignon-cobalt]{title="Cobalt fungus"}                       | :material-check:{ .success } |                              |                              | :material-check:{ .success } |                              | :material-check:{ .success } |                              |                              |                              | :material-check:{ .success } |                              |                              |                              |                              |
| [champignon des fjords][champignon-des-fjords]{title="Fjord fungus"}                |                              | :material-check:{ .success } |                              | :material-check:{ .success } |                              |                              |                              | :material-check:{ .success } |                              |                              |                              |                              |                              |                              |
| [cire fissurée][cire-fissuree]{title="Gapgrowth"}                                   |                              |                              |                              |                              | :material-check:{ .success } |                              |                              |                              |                              |                              | :material-check:{ .success } |                              |                              | :material-check:{ .success } |
| [gousse][gousse]{title="Windbag"}                                                   | :material-check:{ .success } |                              |                              |                              |                              |                              |                              |                              | :material-check:{ .success } |                              |                              |                              | :material-check:{ .success } | :material-check:{ .success } |
| [herbe de clairon][herbe-de-clairon]{title="Bugleweed"}                             |                              | :material-check:{ .success } |                              |                              |                              |                              |                              |                              | :material-check:{ .success } |                              |                              |                              |                              | :material-check:{ .success } |
| [herbe de roche][herbe-de-roche]{title="Rock weed"}                                 |                              |                              |                              |                              |                              |                              |                              |                              | :material-check:{ .success } |                              |                              | :material-check:{ .success } |                              |                              |
| [lichen des cavernes][lichen-des-cavernes]{title="Cave lichen"}                     |                              |                              |                              | :material-check:{ .success } |                              |                              |                              | :material-check:{ .success } |                              |                              |                              |                              |                              |                              |
| [lierre d'araignée]                                                                 |                              |                              |                              |                              |                              |                              |                              | :material-check:{ .success } |                              |                              | :material-check:{ .success } |                              | :material-check:{ .success } |                              |
| [mandragore][mandragore]{title="Mandrake"}                                          |                              |                              |                              |                              | :material-check:{ .success } |                              | :material-check:{ .success } |                              |                              |                              |                              | :material-check:{ .success } |                              |                              |
| [morille][morille]{title="Bubblemorel"}                                             |                              |                              |                              |                              |                              |                              |                              |                              |                              |                              |                              | :material-check:{ .success } | :material-check:{ .success } |                              |
| [œil de chouette][il-de-chouette]{title="Owlsgaze"}                                 |                              |                              |                              |                              |                              |                              |                              | :material-check:{ .success } |                              |                              |                              |                              |                              |                              |
| [peyote][peyote]{title="Peyote"}                                                    |                              |                              |                              |                              |                              |                              |                              |                              |                              | :material-check:{ .success } | :material-check:{ .success } |                              |                              |                              |
| [pourriture de sable][pourriture-de-sable]{title="Sand reeker"}                     |                              |                              |                              |                              |                              |                              | :material-check:{ .success } |                              |                              | :material-check:{ .success } |                              |                              |                              |                              |
| [pétale de cristal de neige][petale-de-cristal-de-neige]{title="Snowcrystal petal"} |                              |                              |                              |                              |                              |                              |                              |                              |                              |                              |                              | :material-check:{ .success } |                              |                              |
| [racine de nœud][racine-de-nud]{title="Knotroot"}                                   |                              |                              | :material-check:{ .success } |                              |                              |                              |                              |                              |                              | :material-check:{ .success } |                              |                              |                              |                              |
| [racine plate][racine-plate]{title="Flatroot"}                                      |                              |                              |                              |                              |                              |                              | :material-check:{ .success } |                              |                              |                              |                              |                              |                              |                              |
| [tamaris][tamaris]{title="Waterfinder"}                                             |                              |                              |                              |                              |                              |                              |                              |                              | :material-check:{ .success } |                              |                              |                              | :material-check:{ .success } |                              |
| [témérité piquante][temerite-piquante]{title="Tangy temerity"}                      |                              |                              |                              |                              | :material-check:{ .success } | :material-check:{ .success } |                              |                              |                              |                              |                              |                              |                              |                              |
| [tsuga blanc][tsuga-blanc]{title="White hemlocks"}                                  |                              |                              |                              |                              |                              | :material-check:{ .success } | :material-check:{ .success } |                              |                              |                              |                              |                              |                              |                              |

Poursuivre la lecture : [[herbs|plantes]].

[^1]: Le [sang de paysan] agit sur l'unité, mais tous les démons de la faction dans la région s'en servent s'il en reste.  
    Il suffit donc d'en équiper une unité (par région), tant qu'elle boit assez de sang de paysan pour tous les démons.
[^2]: la potion agit à une unité ciblée avec l'ordre `USE Duncebun <unit-id>`.  
    À cet égard, il convient de noter que si le **niveau de [discrétion]{title="Stealth"}** de l'utilisateur est **inférieur ou égal** au **niveau de [perception][perception]{title="Perception"} + 2** de la victime, la tentative échoue.  
    Si la tentative échoue, le [pain d'andouille] reste chez l'utilisateur et il reçoit un message d'erreur.

<!-- From [https://wiki.eressea.de/index.php?title=Tränke/fr&oldid=16931] -->

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
[potion de vérité]: #potion-de-verite "Potion of truth"
[thé des sept lieues]: #the-des-sept-lieues "Seven mile tea"
[bien-être des chevaux]: #bien-etre-des-chevaux "Horsepower potion"
[élixir de pouvoir]: #elixir-de-pouvoir "Elixir of power"
[potion de guérison]: #potion-de-guerison "Healing potion"

[SM]: #the-des-sept-lieues "Thé des sept lieues (Seven mile tea)"
[GW]: #eau-de-goliath "Eau de Goliath (Goliath water)"
[WL]: #eau-de-vie "Eau de vie (Water of life)"
[PB]: #sang-de-paysan "Sang de paysan (Peasant blood)"
[BZ]: #breuvage-de-labeur "Breuvage de labeur (Busybeer)"
[OM]: #onguent-de-soin "Onguent de soin (Ointment)"
[BK]: #sang-de-berserker "Sang de berserker (Berserkers blood)"
[DB]: #pain-dandouille "Pain d'andouille (Duncebun)"
[BW]: #huile-de-cervelle "Huile de cervelle (Brain wax)"
[HP]: #bien-etre-des-chevaux "Bien-être des chevaux (Horsepower potion)"
[NW]: #chaleur-du-nid "Chaleur du nid (Potion of nest warmth)"
[PL]: #amour-des-paysans "Amour des paysans (Peasant love potion)"
[EP]: #elixir-de-pouvoir "Élixir de pouvoir (Elixir of power)"
[HL]: #potion-de-guerison "Potion de guérison (Healing potion)"

[cmd-use]: [[cmd-use]]
