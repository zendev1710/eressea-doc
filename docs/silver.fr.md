---
# cSpell:locale fr
alias: argent
---
# Argent

L'argent mène le monde - c'est aussi le cas dans Eressea.  
Il y a plusieurs façons d'en obtenir : [[cmd-work|travailler]], [[cmd-entertain|divertir]], [[cmd-tax|collecter les impôts]] ou [commercer].  

Le travail (`WORK`) est plus une sorte de palliatif, les unités qui travaillent gagnent à peine de quoi se nourrir.  
Vous pouvez gagner beaucoup d'argent avec le divertissement (`ENTERTAIN`) et les impôts (`TAX`).  
Surtout au début de votre aventure, le commerce peut être la plus grande source de revenus, des profits de quelques milliers d'argent sont possibles, à condition que les régions aient les produits de luxe appropriés.  

L'argent a son propre poids : 100 silver équivalent à une unité de poids.  
Lors du calcul du poids, il est courant d'arrondir à l'unité supérieure; un seul silver peut surcharger une unité.  

Comme les personnes (de la plupart des [[races]]) peuvent porter 5,4 UW/kg, elles peuvent transporter jusqu'à 540 silvers;  
lorsqu'elles en portent 541 une seule personne est surchargée.  
Un bateau (capacité de 50 UW/kg) par exemple, peut transporter une personne (10 kg dans la plupart des cas) avec 4000 silvers; 4001 pièces serait une surcharge.  

## Dépenses

### Recruter

Si l'on veut recruter des personnes, il faut suffisamment d'argent, car les candidats au recrutement sont souvent particulièrement avides ...  
Pour chaque personne recrutée, il faut dépenser, selon la race, entre 40 et 150 Silver en frais de recrutement.  
Le coût du recrutement dépend de la race et est indiqué dans ce [[races|tableau]].  

Garder empêche le recrutement (sauf en cas d'utilisation de `HELP`).  

### Frais d'entretien

Chaque joueur et chaque paysan a besoin de 10 Silver à chaque tour pour pouvoir acheter sa nourriture.  
Les unités d'une même faction dans la même région s'aident cependant mutuellement, c'est-à-dire qu'il suffit en principe qu'une unité ait assez de Silver pour toutes les personnes présentes (ce qui peut toutefois être fatal en cas d'erreur, si personne d'autre n'a de silvers !)  
Si votre propre faction n'a pas assez d'argent, d'autres factions qui ont mis [[cmd-help|`HELP SILVER`]] avec votre faction aident aussi (voir [[alliances]]).  
Les unités qui se déplacent doivent être ravitaillées là où elles arrivent.  
Pour l'entretien des unités, on utilise aussi des silver, qui a été préalablement [[cmd-reserve|réservé]].  
Sans suffisamment de silvers, les gens souffrent de la faim (voir ci-dessous).  

Certains bâtiments ont également besoin de frais d'entretien hebdomadaires pour fonctionner.  
Ces frais d'entretien sont dûs dès le début du tour, ils doivent donc être perçus dès le premier tour et sont dûs dès que le bâtiment a été commencé (donc également pour les bâtiments à moitié construits).  
S'il n'y a pas assez d'argent disponible, la fonction du bâtiment ne peut pas être utilisée.  

En savoir plus : les [[batiments]].  

## Famine

### La Famine pour les unités des joueurs

Les unités affamées subissent des dégâts, et donc perdent des points de vie.  
Les halflings affamés proportionnellement plus que les autres races.  
La santé d'une unité apparaît dans le rapport.  
L'unité sera exhausted, wounded ou badly wounded.  
Cependant, une unité non déjà affaiblie ne mourra pas au cours de la première semaine.  

Une unité affamée ne peut pas donner de personnes à d'autres unités.  
De plus, les unités affamées voient leur score de talent chuter de moitié, ne régénèrent pas de points de vie et apprennent beaucoup plus lentement que d'habitude.  
Cependant, les unités affamées ou blessées peuvent encore exécuter des ordres longs.  

Au fil du temps, les unités blessées se rétablissent.  
Les unités régénèrent normalement 5 % de leurs points de vie maximum par tour (certaines races davantage), avec un minimum d'un point par personne dans l'unité.  
Les unités de Morts-vivants ne se régénèrent pas  

La compétence Sailing n'est réduite que d'un niveau lorsque les unités sont affamées.  
Néanmoins, la famine en mer est une situation critique.  
D'une part, personne d'autre que les [aquariens] ne peut y travailler, on dépend donc d'un apport extérieur de Silvers.  
D'autre part, il peut arriver qu'en raison de la réduction de compétence, on n'ait plus assez de niveaux de Sailing pour manœuvrer le bateau, ce qui fait que le bateau subit des [[bateaux|dommages]] et dérive.  

La faim est presque mortelle au contact de l'ennemi, par exemple en cas de vol ou d'erreur de planification.  
Les unités perdent des points de vie et se battent beaucoup moins bien ensuite lors d'un éventuel combat.  
Si elles survivent malgré tout à un tel combat, elles risquent de continuer à avoir faim parce qu'elles n'ont pas pu travailler à cause du combat (voir [Fin de bataille]).  

Si l'unité maîtrise l'[Endurance] à un niveau élevé, il peut arriver, après avoir été affamé, qu'une unité soit [très forte] selon le rapport (c'est-à-dire qu'elle ait plus de points de vie qu'elle ne devrait normalement en avoir).  

### Famine des paysans

Les paysans ont eux aussi besoin de subsistance, qu'ils gagnent généralement eux-mêmes et qu'ils prélèvent dans les réserves de la région.  
Lorsque les réserves de la région sont épuisées, les paysans meurent de faim.  
Cela peut avoir plusieurs causes :

- La région est surpeuplée. Dans une plaine sans arbres, où chaque paysan gagne 12 silvers, seuls 12 000 paysans peuvent survivre à long terme, car seuls 10 000 paysans travaillent tout en gagnant 1 200 00$, ce qui ne suffit que pour 12 000 paysans.
  À court terme, le nombre de paysans peut être plus élevé tant qu'il reste suffisamment de Silver dans les réserves de la région.
- La région n'est pas surpeuplée, mais les unités des joueurs [[cmd-work|travaillent]] et occupent donc une partie des emplois.
- Les paysans gagnent suffisamment de silvers, mais les unités de joueurs [[cmd-tax|taxent]] avant que les paysans n'aient pu subvenir à leurs besoins.
- De plus, des rumeurs circulent sur des événements particuliers qui peuvent temporairement ou définitivement dégrader la fertilité d'une région, empêchant les paysans de subvenir à leurs besoins.

Les paysans affamés peuvent ressusciter plus tard sous la forme de [morts-vivants].  

## Revenus

### Travail

Une unité peut gagner de l'argent en travaillant dans l'agriculture (voir l'ordre [[cmd-work]]).  
Cependant, plus les forêts sont denses dans une région, moins il y a de surface cultivable, et moins les paysans (et aussi les unités de joueurs) peuvent travailler : par arbre, huit paysans ou joueurs ne peuvent plus travailler et chaque pousse d'arbre occupe 4 emplois.  
Le nombre maximal de personnes pouvant travailler (et non pas habiter) dans une région dépend également du type terrain (voir le tableau de la commande [[cmd-work]]).  

Un paysan gagne normalement 11 Silver par tour.  
Ce salaire peut augmenter jusqu'à 16 Silver par paysan et par tour grâce au bonus d'une citadelle (voir aussi [ce tableau]).  
Par exemple, si une citadelle est construite dans une plaine et que la forêt est coupée, 10000 paysans peuvent se nourrir en un tour et 60000 Silver supplémentaires sont ajoutés aux réserves de la région.  

Les unités des joueurs travaillant gagnent cependant moins - après tout, ce ne sont que des ouvriers auxiliaires.  
Le montant qu'elles peuvent gagner (1 silver de moins que les paysans) est indiqué d'une part dans le rapport, d'autre part dans le tableau de l'ordre [[cmd-work]].  

Garder empêche de travailler uniquement les unités se trouvant à l'intérieur d'un bateau (sauf en cas d'utilisation de `HELP`).  

### Collecter les impôts

Les unités armés et entraînés peuvent extorquer 20 Silver aux paysans avec l'ordre [[cmd-tax]] par personne et par niveau de compétence.  
Pour cela, il faut bien sûr la compétence Taxation, mais aussi une arme par personne (les catapultes ne comptent pas) et la compétence correspondante pour la maîtriser.  

Si le nombre de paysans est près du maximum de population, presque toutes les réserves de silver de la région seront utilisées par les paysans, de sorte qu'ils n'auront plus de Silver "à disposition" pour les impôts.  
Les impôts pourront tout de même être collectés (à hauteur de la réserve de la région), mais les paysans non approvisionnés mourront de faim (et donc les gains n'augmenteront pas non plus ...).  
C'est pour cela qu'il est judicieux de construire un château, car cela permet d'augmenter le salaire de base : avec 12 Silver au lieu de 11, 2000 paysans gagnent 2000 Silver de plus par tour !  

Garder empêche la collecte des taxes (sauf en cas d'utilisation de `HELP`).  

### Divertissement (Entertain)

L'argent qui reste aux paysans après les impôts est ajouté aux réserves de la région (la réserve de silver des paysans).  
Sur cette réserve, 5% peuvent être gagnés par le divertissement (Entertainment).  
Les statistiques de la région indiquent également ce montant.  
Chaque personne peut gagner jusqu'à 20 Silver par tour et niveau de compétence "entertainment" avec l'ordre [[cmd-entertain|divertir]], si les paysans ont suffisamment d'argent à disposition.  

### Exemples de possibilités de rémunération

*Revenus et frais d'entretien.*

| Région | Arbres | Paysans | Max. travailleurs | Salaire | Revenu | Entretien | Surplus | Divertissement |
|--------|:------:|:-------:|:-----------------:|:-------:|--------|:---------:|--------:|---------------:|
| Plaine |  200   |  3 742  |       8 400       |   11    | 41 162 |  37 420   |   3 742 |            187 |
| Plaine |  200   |  3 742  |       8 400       |   14    | 52 388 |  37 420   |  14 968 |            748 |
| Forêt  |  818   |  3 742  |       3 456       |   11    | 38 016 |  37 420   |     596 |             29 |
| Forêt  |  818   |  3 742  |       3 456       |   12    | 41 472 |  37 420   |   4 052 |            202 |

Pour chaque arbre, le nombre maximum de paysans pouvant travailler est diminué de 8, pour chaque jeune arbre le nombre est diminué de 4.  

Dans cet exemple, le revenu total est plus faible parce que tous les paysans ne peuvent pas travailler.  
En effet, trop d'arbres les empêchent de cultiver.  

Cela ne tient pas compte non plus de l'épargne des paysans (la réserve en silvers de la région).  
Ils vivront sur cette réserve en cas de surpopulation.  
L'argent disponible pour le divertissement est également influencé par le montant de cette réserve.  
En règle générale, il est donc possible de gagner plus grâce au divertissement (5 % de la réserve).  

Garder empêche le divertissement uniquement pour les unités se trouvant à l'intérieur d'un bateau (sauf en cas d'utilisation de `HELP`).

### Le vol : la méthode malhonnête

Outre les moyens honnêtes de gagner de l'argent, il existe une variante malhonnête : le vol.  
Les unités qui se sont dissimulées peuvent essayer de voler des Silver à d'autres unités avec l'ordre [[cmd-steal]].  

Si la compétence de [[camouflage]] du voleur est supérieure à la [perception] de la meilleure unité de la faction volée dans la région, il vole 50 silver par point de différence de compétences.  

Plus d'information : [[camouflage|le camouflage et le vol]].  

## Commerce

Dans chaque région, les paysans fabriquent un produit de luxe.  
Ce produit peut leur être acheté.  
Dans toutes les régions qui ne produisent pas ce bien, il existe une demande toujours croissante pour ces produits.  
Ceux qui n'ont pas peur des risques liés aux voyages peuvent gagner beaucoup d'argent grâce au commerce.  

Pour faire du commerce, il faut être compétent en [commerce].  
Une personne (ou une unité) peut acheter et/ou vendre au maximum 10 produits de luxe par niveau de compétence, voir [[cmd-buy]] et [[cmd-sell]].  
Les quantités respectives de biens échangés sont totalement arbitraires.  
Par exemple, une unité composée d'une personne avec une compétence de niveau 4 en commerce peut acheter 20 Gems et vendre 12 Soies et 8 Baumes par tour.  

De plus, il est nécessaire pour faire du commerce qu'il y ait dans la région un château au moins la taille d'un tradepost (comptoir commercial), dans lequel se déroule en quelque sorte le marché.  
La faction propriétaire du château n'a pas d'importance pour le commerce - les propriétaires du château ne peuvent pas (selon les règles) empêcher le commerce dans la région.  
En revanche, ils peuvent décider de le "perturber" en attaquant les marchands pour leur faire cesser leurs activités.  

Le propriétaire du plus grand château de la région reçoit une part des recettes des ventes des autres joueurs.  
Cette part de recettes est déduite des recettes des marchands.  
Si deux châteaux sont de même taille, personne ne reçoit cette part.  
Le montant du "taux d'imposition" est indiqué dans le tableau du chapitre [[chateaux]].  

Garder empêche de travailler uniquement si les unités se trouvent à l'intérieur d'un bateau (sauf en cas d'utilisation de `HELP`).  

Chaque marchandise a un prix de base fixe (voir le tableau ci-dessous).  
Il indique les prix de base des produits de luxe.  
Le nombre d'unités de produits de luxe qui peuvent être achetées sans que leur prix n'augmente est égal à 1 % du nombre de paysans de la région.  
Chaque fois que cette quantité est achetée (le total acheté par toutes les factions), le prix augmente du prix de base.  
Une région de 2 000 paysans permet d'acheter 20 objets de luxe sans en augmenter le prix d'achat.  
Le prix revient à la normale au tour suivant, les produits étant à nouveau disponibles.  

*Prix de base des biens de luxe.*

| Produits de luxe | Prix de base | Poids (kg) |
|------------------|:------------:|:----------:|
| [baume]          |      4       |     2      |
| [encens]         |      4       |     2      |
| [gemme]          |      7       |     1      |
| [huile]          |      3       |     3      |
| [myrrhe]         |      5       |     2      |
| [soie]           |      6       |     3      |
| [épice]          |      5       |     2      |

Le prix de vente d'un produit de luxe est un multiple du prix de base et est indiqué dans le rapport de la région.  
Dès que plus d'1% des paysans ont acheté un produit au cours d'un tour, le prix de vente diminue du prix de base et n'augmente à nouveau que lentement au cours des semaines suivantes.  
Chaque tour, il y a 10% de chances que le prix de vente de chaque produit de luxe augmente du prix de base.  
Dans les régions où se trouve un [port], cette chance est de 20 %.  
Si le prix de vente est déjà de 25 fois le prix de base, il n'augmentera pas davantage.  

Les prix et les maxima indiqués sont valables pour toutes les factions de la région et non par faction, mais par produit de luxe.  
Sans accord entre les factions, le prix de vente peut être "dévalué" plus vite qu'on ne le souhaiterait...  

Tous les achats et les ventes de produits de luxe sont équitablement répartis entre les factions.  
La hausse ou la baisse des prix affecte donc de manière égale tous ceux qui achètent ou vendent pendant le tour.  

Exemple :

- Supposons une région comptant 8 000 paysans.
  Elle propose de l'[encens] à 4 Silver et demande des [épices][épice] à 15 Silver.
  1 % des paysans correspond à 80.
  Si un commerçant vend 200 épices, les 80 premières épices seront vendues à 15 Silver, les 80 suivantes à 10 Silver et les 40 restantes à 5 Silver.
  La semaine suivante, les épices ne pourront plus être vendues qu'à 5 Silver.
  Sauf si le prix est remonté à 10 (10 % de probabilité, 20 % dans un [port]).
- Si 100 encens sont achetés dans cette région, les 80 premiers encens coûtent 4 silver chacun, et les 20 suivants 8 silver chacun.
  La semaine suivante, le prix de l'encens est à nouveau de 4 Silver et on peut à nouveau acheter les 80 premiers encens à ce prix.
  Si les 100 encens ont été achetés par des unités de deux factions différentes, les deux paieront (aux effets d'arrondi près) 4,8 Silver par produit de luxe.

L'argent dépensé par les commerçants pour acheter le bien de luxe disponible dans la région bénéficie aux vendeurs.  
Malgré cela, la région ne perd pas d'argent car les agriculteurs possèdent des biens de luxe avec lesquels ils peuvent payer les impôts.  
L'argent n'est pas créé à partir de rien - c'est la valeur des biens qui ont été produits dans une autre région.  
En revanche, l'argent qui a été dépensé par BUY s'ajoute à la réserve de la région.  
Des gouvernants avisés peuvent le leur reprendre en les divertissant et en les taxant.  

Il vaut la peine d'équiper un bateau et de prendre la mer.  
Bien qu'il soit possible de faire du commerce avec les deux produits fabriqués sur une île, les bénéfices restent relativement faibles.  
En revanche, si l'on revient d'une île étrangère avec une cargaison de marchandises rares, on peut réaliser des bénéfices astronomiques, quelque soit la distance entre les îles.  

!!! warning "Attention"
    Un tradepost est un préalable à tout commerce.

### Produits de luxe

#### Baume

<!-- cspell:disable -->
*Balm (EN), Balsam (DE)*.
<!-- cspell:enable -->

#### Épice

<!-- cspell:disable -->
*Spice (EN), Gewürz (DE)*.
<!-- cspell:enable -->

#### Encens

<!-- cspell:disable -->
*Incense (EN), Weihrauch (DE)*.
<!-- cspell:enable -->

#### Gemme

<!-- cspell:disable -->
*Gem (EN), Juwelen (DE)*.
<!-- cspell:enable -->

#### Huile

<!-- cspell:disable -->
*Oil (EN), Öl (DE)*.
<!-- cspell:enable -->

#### Myrrhe

<!-- cspell:disable -->
*Myrrh (EN), Myrrhe (DE)*.
<!-- cspell:enable -->

#### Soie

<!-- cspell:disable -->
*Silk (EN), Seide (DE)*.
<!-- cspell:enable -->

## Concurrence entre différentes factions

Lorsque plusieurs factions travaillent, divertissent, collectent des impôts ou font du commerce dans une région, les gains potentiels sont répartis le plus équitablement possible entre les unités.
Il est préférable de bien s'entendre avec tes colocataires s'ils sont amicaux.

Si la région est gardée par une faction étrangère, aucune de nos propres unités ne peut collecter d'impôts ni recruter.
Le travail, le divertissement et le commerce sont toutefois possibles, à moins que l'unité ne se trouve sur un bateau.

Si toutes les factions qui gardent ont paramétré [[cmd-help|`HELP GUARD`]] ou [[cmd-help|`HELP ALL`]] avec notre faction ou un ordre [[cmd-contact]] avec notre unité ou notre faction, alors la garde n'a pas d'effet.
Cela s'applique également si notre unité n'est pas vue en raison d'un niveau de stealth suffisamment bon.
Pour une unité `TEMP` (particulièrement pertinente lors du recrutement), l'unité "mère" compte, c'est à dire l'unité qui donne l'ordre `MAKE TEMP`.

## Voir aussi

- [[cmd-give]]
- [[cmd-reserve]]
- [[cmd-recruit]]
- [[reserve-d-objets]]
- [stealth]
- [[cmd-guard]]

Poursuivre la lecture : [Material Pool].

[Material Pool]: ./items-pool.md

<!-- From [https://wiki.eressea.de/index.php?title=Geld/fr&oldid=16925] -->

[endurance]: ./war-tables.md#endurance
[aquariens]: ./races.md#aquariens
[Fin de bataille]: ./war.md#fin-du-combat
[morts-vivants]: ./monsters.md#morts-vivants
[ce tableau]: ./castles.md#apercu
[commerce]: ./skills-list.md#commerce "Trade"
[port]: ./buildings-others.md#port "Harbour"
[très forte]: ./war-tables.md#etat-de-sante

[commercer]: #commerce

[baume]: #baume "Balm"
[encens]: #encens "Incense"
[gemme]: #gemme "Gem"
[huile]: #huile "Oil"
[myrrhe]: #myrrhe "Myrrh"
[soie]: #soie "Silk"
[épice]: ./silver.md#epice "Spice"
[perception]: ./skills-list.md#perception
