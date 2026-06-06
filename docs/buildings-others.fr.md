---
# cSpell:locale fr
alias: batiments-speciaux
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD042 MD052 -->
# Bâtiments spéciaux

Les bâtiments construits dans une région **procurent des avantages** importants aux unités qui les occupent.

Ils sont construits avec l'ordre [MAKE "type de bâtiment"][cmd-make] et peuvent être agrandis avec l'ordre [MAKE "type de bâtiment" ID-bâtiment][cmd-make].

Exemple : `MAKE`&nbsp;[Lighthouse] (création) ou `MAKE`&nbsp;[Harbour]&nbsp;`xyz` (agrandissement).

!!! info
    La construction d'un bâtiment nécessite un niveau de compétence minimal en [maçonnerie][maconnerie]{title="Masonry"}.

!!! note "Remarque"
    Certains bâtiments sont d'une taille maximale déterminée, d'autres non.

Le tableau récapitulatif ci-dessous comprend, dans l'ordre, pour chaque type de bâtiment :

- Les coûts de construction : nombre de pierres, bois, fers et silver
- Le niveau requis en maçonnerie pour la construction
- Les frais **d'entretien** : nombre de ressources (pierres, bois ou chevaux) et de silver
- Sa taille maximale
- Sa capacité : elle se rapporte uniquement aux personnes pouvant bénéficier du bâtiment

| Bâtiment                                                    | Pierres | Bois | Fers | Silver | Niv. |     Silver | Ressource | Taille Max. |    Capacité |
|-------------------------------------------------------------|--------:|-----:|-----:|-------:|-----:|-----------:|-----------|------------:|------------:|
| [Phare][phare]{title="Lighthouse"}                          |       2 |    1 |    1 |    100 |    3 |        100 | --        |          -- | 4 personnes |
| [Mine][mine-fr-id]{title="Mine"}                            |       5 |   10 |    1 |    250 |    4 |        500 | --        |          -- |      taille |
| [Carrière][carriere]{title="Quarry"}                        |       1 |    5 |    1 |    250 |    2 |        250 | --        |          -- |      taille |
| [Scierie][scierie]{title="Sawmill"}                         |       5 |    5 |    3 |    200 |    3 |        250 | --        |          -- |      taille |
| [Forge][forge]{title="Smithy"}                              |       5 |    5 |    2 |    200 |    3 |        300 | 1 bois    |          -- |      taille |
| [Haras][haras]{title="Stable"}                              |       2 |    4 |    1 |    100 |    2 |        150 | --        |          -- |      taille |
| [Port][port]{title="Harbour"}                               |       5 |    5 |   -- |    250 |    3 |        250 | --        |          25 |      taille |
| [Caravansérail][caravanserail]{title="Caravanserai"}        |       1 |    5 |    1 |    500 |    2 |      3 000 | 2 chevaux |          10 |      taille |
| [Académie][academie]{title="Academy"}                       |       5 |    5 |    1 |    500 |    3 |      1 000 | --        |          25 |      taille |
| [Tour de mage][tour-de-mage]{title="Mage Tower"}[^1]        |       5 |    3 |    3 |    500 |    5 |      1 000 | --        |          50 | 2 personnes |
| [Barrage][barrage]{title="Dam"}                             |       5 |   10 |    1 |    500 |    4 |      1 000 | 3 bois    |          50 |      taille |
| [Tunnel][tunnel-fr-id]{title="Tunnel"}                      |      10 |    5 |    1 |    300 |    6 |        100 | 2 pierres |         100 |      taille |
| [Auberge][auberge]{title="Inn"}                             |       4 |    3 |    1 |    200 |    2 | 5 X taille | --        |          -- |      taille |
| [Monument][monument-fr-id]{title="Monument"}                |       1 |    1 |    1 |    400 |    4 |         -- | --        |          -- |      taille |
| [Cercle de Pierres][cercle-de-pierres]{title="Stonecircle"} |       5 |    5 |   -- |     -- |    2 |         -- | --        |         100 | 3 personnes |

!!! warning "Attention"

    **Un bâtiment est actif uniquement** si :

    - Ses [frais d'entretien] ont été **payés** en début de tour
    - Le nombre de personnes qui l'occupent est **inférieur ou égal** à sa taille (cette règle ne s'applique pas à certains bâtiments, comme le [phare])

Voir aussi : [Construction d'un château][apercu].

## Phare

<!-- cspell:disable -->
*Lighthouse (EN), Leuchtturm (DE)*.
<!-- cspell:enable -->

| Coûts par point de taille            | Niveau requis | Maintenance par tour | Taille max. | Capacité     |
|--------------------------------------|:-------------:|:--------------------:|:-----------:|--------------|
| 2 pierres, 1 bois, 1 fer, 100 silver |       3       |      100 silver      |     --      | 4 **unités** |

| Taille | Perception | Visibilité |
|-------:|-----------:|:----------:|
|     10 |          3 |     1      |
|     10 |          6 |     2      |
|    100 |          9 |     3      |
|   1000 |         12 |     4      |
|    ... |            |            |

Les avantages d'un phare :

- Débutant à la taille 10, Le phare réduit la possibilité qu'un bateau dérive suite à une tempête.
  Cet effet s'étend à log10 (taille du phare) + 1 régions autour du bâtiment.
- Le phare donne aux occupants (jusqu'à 4 unités seulement) des informations sur les bateaux visibles dans un rayon de log10 (taille du phare) + 1 régions.
  L'unité doit avoir une perception d'au moins distance × 3.
  Un rapport provenant d'une région océanique située à trois hexagones de distance ne peut être obtenu que si le phare est d'au moins une taille de 100 et que l'unité a au moins une perception de 9.

[](){ #mine-id }

## Mine

<!-- cspell:disable -->
*Mine (EN), Bergwerk (DE)*.
<!-- cspell:enable -->

| Coûts par point de taille             | Niveau requis | Maintenance par tour | Taille max. | Capacité (nb. personnes) |
|---------------------------------------|:-------------:|:--------------------:|:-----------:|--------------------------|
| 5 pierres, 10 bois, 1 fer, 250 silver |       4       |      500 silver      |     --      | *taille du bâtiment*     |

- Seule la moitié du fer extrait par les unités situées à l'intérieur de la mine est déduite des ressources de la région.
  Cet effet fonctionne de manière cumulative avec tous les avantages raciaux correspondants.
- Les unités à l'intérieur de la mine ont +1 en [extraction minière][extraction-miniere]{title="Mining"}, mais ceci ne s'applique pas au niveau requis pour atteindre une couche plus profonde.
- Pour extraire du laen il est nécessaire d'être dans une mine.

**Exemple:**

- Dans une mine, un humain T2 en [extraction minière][extraction-miniere]{title="Mining"} peut extraire 3 fers à la couche 1 ou 2.
  Cependant, en raison de l'arrondi, 2 fers sont déduits de la réserve de la région.
- 1 unité d'humain de 2 personnes niveau 4.
  Elle produit 8 fers et prélève 8 fers des ressources de la région.
  Dans une mine la même unité produit 10 fers (4+1x2) et prélève seulement 5 fers (10/2).
- 1 unité de 2 nains niveau 4.
  Elle produit 8 fers et prélève 5 fers des ressources de la région (don spécial des nains 60%).
  Dans une mine la même unité de nains produit 10 fers (4+1x2) et prélève seulement 3 fers (10\*60%/2).

## Carrière

<!-- cspell:disable -->
*Quarry (EN), Steinbruch (DE)*.
<!-- cspell:enable -->

| Coûts par point de taille           | Niveau requis | Maintenance par tour | Taille max. | Capacité (nb. personnes) |
|-------------------------------------|:-------------:|:--------------------:|:-----------:|--------------------------|
| 1 pierre, 5 bois, 1 fer, 250 silver |       2       |      250 silver      |     --      | *taille du bâtiment*     |

- Seule la moitié de la pierre extraite par les unités situées à l'intérieur de la carrière est déduite des ressources de la région.
  Cet effet fonctionne de manière cumulative avec tous les avantages raciaux correspondants.
- Les unités à l'intérieur de la carrière ont **un bonus de +1** en [extraction de pierres][extraction-de-pierres]{title="Quarrying"}, mais ceci ne s'applique pas au niveau requis pour atteindre une couche plus profonde.

**Exemple:**

10 trolls produisent 40 pierres dans une région.  
En raison des capacités spéciales des trolls, la réserve de la région n'est réduite que de 30 pierres.  

Si les trolls sont à l'intérieur d'une carrière, la réserve sera réduite de 15 pierres.  

S'il ne reste que 7 pierres dans la région, les trolls ne peuvent produire que 9 pierres mais 18 dans une carrière.  

## Scierie

<!-- cspell:disable -->
*Sawmill (EN), Sägewerk (DE)*.
<!-- cspell:enable -->

| Coûts par point de taille             | Niveau requis | Maintenance par tour | Taille max. | Capacité (nb. personnes) |
|---------------------------------------|:-------------:|:--------------------:|:-----------:|--------------------------|
| 5 pierres, 5 bois, 3 fers, 200 silver |       3       |      250 silver      |     --      | *taille du bâtiment*     |

- Seule la moitié du bois (des [pousses][jeunes-arbres-ou-pousses]{title="Saplings"}, des mallorns) produit par les unités dans une scierie est déduite des ressources de la région.
  Ce nombre est arrondi au supérieur : quand une unité produit 11 bois dans une scierie, 6 arbres sont abattus.
- Les unités à l'intérieur d'une scierie bénéficient d'un bonus de +1 en [sylviculture][sylviculture]{title="Forestry"}.

**Exemple :**

Avec une potion d'[eau de vie][eau-de-vie]{title="Water of life"} et 10 bois vous pouvez créer du bois dans une scierie.  
Avec l'ordre [[cmd-use|`USE 1 water~of~life`]] vous créez 10 [pousses][jeunes-arbres-ou-pousses]{title="Saplings"} en utilisant 10 bois.  
Vous les coupez instantanément dans la scierie, produisant ainsi 20 bois.

## Forge

<!-- cspell:disable -->
*Smithy (EN), Schmiede (DE)*.
<!-- cspell:enable -->

| Coûts par point de taille             | Niveau requis | Maintenance par tour | Taille max. | Capacité (nb. personnes) |
|---------------------------------------|:-------------:|:--------------------:|:-----------:|--------------------------|
| 5 pierres, 5 bois, 2 fers, 200 silver |       3       |  300 silver, 1 bois  |     --      | *taille du bâtiment*     |

- Les unités à l'intérieur n’ont besoin que de la moitié de la quantité normale de fers pour fabriquer des armes et des armures en fers.
  Le Laen n'est pas économisé.
- Les unités à l'intérieur d'une forge bénéficient d'un bonus de +1 à leur compétence weaponsmithing et armoursmithing.

## Haras

<!-- cspell:disable -->
*Stable (EN), Pferdezucht (DE)*.
<!-- cspell:enable -->

| Coûts par point de taille            | Niveau requis | Maintenance par tour | Taille max. | Capacité (nb. personnes) |
|--------------------------------------|:-------------:|:--------------------:|:-----------:|--------------------------|
| 2 pierres, 4 bois, 1 fer, 100 silver |       2       |      150 silver      |     --      | *taille du bâtiment*     |

- Les unités à l'intérieur d'un haras peuvent reproduire des chevaux en utilisant l'ordre [[cmd-grow|`GROW HORSES`]].
  Pour cela l'unité doit maîtriser l'[apprivoisement][apprivoisement]{title="Taming"} et d'au moins 2 chevaux (en sa possession).
- La chance d'élever des chevaux correspond à la compétence de l'unité.
  De plus, l'unité dispose d'un nombre de tentatives égal à son niveau.
  Si une unité est T5, il dispose de 5 tentatives à 5% chacune pour élever un cheval.
- Pour chaque tentative l'unité a besoin d'un cheval.
  Si le nombre de chevaux disponibles est insuffisant, les tentatives sont annulées.
  5 chevaux sont nécessaires dans l'exemple précédent.

## Port

<!-- cspell:disable -->
*Harbour (EN), Hafen (DE)*.
<!-- cspell:enable -->

| Coûts par point de taille     | Niveau requis | Maintenance par tour | Taille max. | Capacité (nb. personnes) |
|-------------------------------|:-------------:|:--------------------:|:-----------:|--------------------------|
| 5 pierres, 5 bois, 250 silver |       3       |      250 silver      |     25      | *taille du bâtiment*     |

Le coût **total** d'un port (de taille 25) est de : 125 pierres, 125 bois, 6250 silvers.  

- Permet aux bateaux plus gros qu'une [barque][barque]{title="Boat"} d'accoster dans des régions qui ne sont ni des plaines ni des forêts.
- Une région avec un port peut être utilisée comme une « région canal », c'est-à-dire qu'un bateau dans le port peut naviguer dans n'importe quelle autre direction maritime.
- Dans les deux cas, la condition préalable est que le propriétaire du port soit membre de la même faction ou qu'il ait paramétré un ordre [[cmd-help|`HELP GUARD`]] avec la faction du Capitaine.
- Le propriétaire du port reçoit 10 % de tout l'argent gagné grâce au commerce, en plus des éventuels revenus provenant des châteaux.
- Le propriétaire reçoit également (2 x Trade)% de tous les biens de luxe qui se trouvent à bord des bateaux entrants.
  Sauf si l'unité qui transporte les marchandises a un niveau de dissimulation supérieur au niveau de perception du propriétaire du port, ou si le capitaine du bateau est allié avec le propriétaire du port.
- Dans une région dotée d'un port, les prix des biens de luxe augmenteront avec une probabilité de 20 % au lieu des 10 % normaux.
- Un port ne fonctionnera que s’il est entièrement construit.
  Il ne peut y avoir qu'un seul port par région. Celui qui termine un port en premier en est le propriétaire.
  Un port à moitié terminé peut être détruit avec l'ordre [[cmd-destroy]].

Le nombre de bateaux dans un port est illimité.  

## Académie

<!-- cspell:disable -->
*Academy (EN), Akademie (DE)*.
<!-- cspell:enable -->

| Coûts par point de taille             | Niveau requis | Maintenance par tour | Taille max. | Capacité (nb. personnes) |
|---------------------------------------|:-------------:|:--------------------:|:-----------:|--------------------------|
| 5 pierres, 5 bois, 1 fers, 500 silver |       3       |     1000 silver      |     25      | *taille du bâtiment*     |

Le coût **total** d'una académie (de taille 25) est de : 125 pierres, 125 bois, 12500 silvers.  

- Les unités qui apprennent dans une académie ont 1/3 de chance d'apprendre une fois de plus cette semaine, et si elles ont un professeur, elles ont 2/3 de chance.
- Apprendre dans une académie coûte 50 silver par personne pour les compétences qui peuvent normalement être apprises sans aucun frais et le double de la somme d'argent pour les compétences qui coûtent quelque chose pour les apprendre.
- Les enseignants qui enseignent aux élèves d'une académie ont également une chance d'apprendre, qui peut aller jusqu'à 1/3 en fonction du nombre de leurs élèves.
  Ils n’ont pas besoin d’être eux-mêmes dans une académie pour cela.
- Une académie ne fonctionnera que si elle est entièrement construite !

## Tour de mage

<!-- cspell:disable -->
*Mage Tower (EN), Magierturm (DE)*.
<!-- cspell:enable -->

| Coûts par point de taille                               | Niveau requis | Maintenance par tour | Taille max. | Capacité (nb. personnes) |
|---------------------------------------------------------|:-------------:|:--------------------:|:-----------:|--------------------------|
| 5 pierres, 3 bois, 3 fer, 2 mallorn, 2 laen, 500 silver |       5       |     1000 silver      |     50      | 2                        |

Le coût **total** d'una académie (de taille 25) est de : 250 pierres, 150 bois, 150 fer, 100 mallorn, 100 laen, 25000 silver.  

- Dans une tour de mage, un mage régénère 75 % d'aura en plus.
- La puissance de chaque sort lancé à l’intérieur d’une tour de mage est augmentée comme si le sort était lancé d’un niveau supérieur.
- Les erreurs arrivent beaucoup moins souvent.
- Le bâtiment lui-même a une résistance à la magie augmentée de 40%.
- Une tour de mage ne fonctionnera que si elle est entièrement construite !

## Caravansérail

<!-- cspell:disable -->
*Caravanserai (EN), Karawanserei (DE)*.
<!-- cspell:enable -->

| Coûts par point de taille           | Niveau requis |  Maintenance par tour   | Taille max. | Capacité (nb. personnes) |
|-------------------------------------|:-------------:|:-----------------------:|:-----------:|--------------------------|
| 1 pierre, 5 bois, 1 fer, 500 silver |       2       | 3 000 silver, 2 chevaux |     10      | *taille du bâtiment*     |

Le coût **total** d'un caravansérail (de taille maximale 10) est de 10 pierres, 50 bois, 10 fers, 5 000 silver.  

- Un caravansérail permet de construire des routes dans les [déserts][desert-fr-id]{title="Desert"}.
  Si le caravansérail est détruit, la moitié des routes seront également détruites.
  Une route achevée demeure si l'entretien du bâtiment n'est pas payé.
- Dans les déserts, double le volume du commerce possible.
  Le propriétaire reçoit une part des recettes des ventes comme dans les règles des châteaux ([tableau des châteaux][apercu]).
- Un caravansérail ne fonctionnera que s’il est entièrement construit !

## Barrage

<!-- cspell:disable -->
*Dam (EN), Damm (DE)*.
<!-- cspell:enable -->

| Coûts par point de taille             | Niveau requis | Maintenance par tour | Taille max. | Capacité (nb. personnes) |
|---------------------------------------|:-------------:|:--------------------:|:-----------:|--------------------------|
| 5 pierres, 10 bois, 1 fer, 500 silver |       4       | 1000 silver, 3 bois  |     50      | *taille du bâtiment*     |

Le coût **total** d'un barrage (de taille 50) est de : 250 pierres, 500 bois, 50 fers, 25000 silver.  

- Un barrage vous permet de construire des routes dans les marécages.
  Si le barrage est détruit, la moitié des routes seront également détruites.
  Une route achevée demeure si l'entretien du bâtiment n'est pas payé.
- Le barrage ne fonctionnera que s’il est entièrement construit !

[](){ #tunnel-fr-id }

## Tunnel

<!-- cspell:disable -->
*Tunnel (EN), Tunnel (DE)*.
<!-- cspell:enable -->

| Coûts par point de taille             | Niveau requis | Maintenance par tour  | Taille max. | Capacité (nb. personnes) |
|---------------------------------------|:-------------:|:---------------------:|:-----------:|--------------------------|
| 10 pierres, 5 bois, 1 fer, 300 silver |       6       | 100 silver, 2 pierres |     100     | *taille du bâtiment*     |

Le coût **total** d'un tunnel (de taille 100) est de : 1000 pierres, 500 bois, 100 fers, 30000 silver.  

- Un tunnel permet de construire des routes sur des glaciers.
  Si le tunnel est détruit, la moitié des routes seront également détruites.
  Une route achevée demeure si l'entretien du bâtiment n'est pas payé.
- Un tunnel ne fonctionnera que s’il est entièrement construit !

## Auberge

<!-- cspell:disable -->
*Inn (EN), Taverne (DE)*.
<!-- cspell:enable -->

| Coûts par point de taille            | Niveau requis |     Maintenance par tour     | Taille max. | Capacité (nb. personnes) |
|--------------------------------------|:-------------:|:----------------------------:|:-----------:|--------------------------|
| 4 pierres, 3 bois, 1 fer, 200 silver |       2       | 5 silver par point de taille |     --      | *taille du bâtiment*     |

- Les unités à l'intérieur d'une auberge se régénèrent 50 % plus rapidement.
- Toutes les personnes à l'intérieur d'une auberge ont besoin de 14 silver par semaine pour vivre au lieu des 10 normales.

[](){ #monument-fr-id }

## Monument

<!-- cspell:disable -->
*Monument (EN), Monument (DE)*.
<!-- cspell:enable -->

| Coûts par point de taille           | Niveau requis | Maintenance par tour | Taille max. | Capacité (nb. personnes) |
|-------------------------------------|:-------------:|:--------------------:|:-----------:|--------------------------|
| 1 pierre, 1 bois, 1 fer, 400 silver |       4       |          --          |     --      | *taille du bâtiment*     |

- Le nom et la description du monument ne peuvent être renseignés qu'une seule fois. Cela ne pourra plus jamais être modifié.
- Un monument n'a aucune fonctionnalité.

## Cercle de Pierres

<!-- cspell:disable -->
*Stonecircle (EN), Steinkreis (DE)*.
<!-- cspell:enable -->

| Coûts par point de taille | Niveau requis | Maintenance par tour | Taille max. | Capacité (nb. personnes) |
|---------------------------|:-------------:|:--------------------:|:-----------:|--------------------------|
| 5 pierres, 5 bois         |       2       |          --          |     --      | 3                        |

Le coût **total** d'un Cercle de Pierres (de taille 100) est de : 500 pierres, 500 bois.  

- Un Cercle de Pierres peut être béni grâce à [ce puissant sort][g-benediction-du-cercle-de-pierres-id]{title="Bless Stone Circle"} (Gwyrrd).
  Cela développe alors des effets étranges.
  Entre autres choses, il semble attirer les chevaux elfiques extrêmement rares.
  De plus, les mages présents dans le bâtiment peuvent interrompre la connexion entre l'Astral et le monde réel.
- Dans un Cercle de Pierres béni, un mage régénère 50 % d’aura en plus.
- La puissance de tout sort lancé dans un Cercle de Pierres béni augmente comme si le sort avait été lancé avec un niveau supplémentaire.
- Les occupants ont 30% de résistance à la magie supplémentaire.
- Un Cercle de Pierres ne fonctionnera que s’il est entièrement construit et béni !

## Voir aussi

- [Bâtiments][batiments-id]
- [Châteaux][chateaux]
- [Production][production-fr-id]

Poursuivre la lecture : [réserve de faction][reserve-de-faction].

[^1]: nécessite également 2 mallorns et 2 laens par point de taille.

[cmd-make]: [[cmd-make]]
