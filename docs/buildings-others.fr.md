---
# cSpell:locale fr, en
alias: batiments-speciaux
---
# Bâtiments spéciaux

Les bâtiments construits dans une région **procurent des avantages** importants aux unités qui les occupent.

Ils sont construits avec l'ordre [MAKE "type de bâtiment"] et peuvent être agrandis avec l'ordre [MAKE "type de bâtiment" ID-bâtiment][MAKE "type de bâtiment"].

Exemple : `MAKE`[`Lighthouse`] (création) ou `MAKE`[`Harbour`]`xyz` (agrandissement).

!!! info

    La construction d'un bâtiment nécessite un niveau de compétence minimal en [maçonnerie].

> Note : certains bâtiments sont d'une taille maximale déterminée, d'autres non.

Le tableau récapitulatif ci-dessous comprend, dans l'ordre, pour chaque type de bâtiment :

- Les coûts de construction : nombre de pierres, bois, fers et pièces d'argent
- Le niveau requis en maçonnerie pour la construction
- Les frais **d'entretien** : nombre de ressources (pierres, bois ou chevaux) et de pièces d'argent
- Sa taille maximale
- Sa capacité : elle se rapporte uniquement aux personnes pouvant bénéficier du bâtiment

| Bâtiment            | Pierres | Bois | Fers | Pièces | Niv. |     Pièces | Ressource |     Taille Max. |    Capacité |
|---------------------|--------:|-----:|-----:|-------:|-----:|-----------:|-----------|----------------:|------------:|
| [Phare]             |       2 |    1 |    1 |    100 |    3 |        100 | --        | *pas de limite* | 4 personnes |
| [Mine]              |       5 |   10 |    1 |    250 |    4 |        500 | --        | *pas de limite* |      taille |
| [Carrière]          |       1 |    5 |    1 |    250 |    2 |        250 | --        | *pas de limite* |      taille |
| [Scierie]           |       5 |    5 |    3 |    200 |    3 |        250 | --        | *pas de limite* |      taille |
| [Forge]             |       5 |    5 |    2 |    200 |    3 |        300 | 1 bois    | *pas de limite* |      taille |
| [Haras]             |       2 |    4 |    1 |    100 |    2 |        150 | --        | *pas de limite* |      taille |
| [Port]              |       5 |    5 |   -- |    250 |    3 |        250 | --        |              25 |      taille |
| [Caravanserail]     |       1 |    5 |    1 |    500 |    2 |       3000 | 2 chevaux |              10 |      taille |
| [Académie]          |       5 |    5 |    1 |    500 |    3 |       1000 | --        |              25 |      taille |
| [Tour de mage]\*    |       5 |    3 |    3 |    500 |    5 |       1000 | --        |              50 | 2 personnes |
| [Barrage]           |       5 |   10 |    1 |    500 |    4 |       1000 | 3 bois    |              50 |      taille |
| [Tunnel]            |      10 |    5 |    1 |    300 |    6 |        100 | 2 pierres |             100 |      taille |
| [Auberge]           |       4 |    3 |    1 |    200 |    2 | 5 X taille | --        | *pas de limite* |      taille |
| [Monument]          |       1 |    1 |    1 |    400 |    4 |         -- | --        | *pas de limite* |      taille |
| [Cercle de Pierres] |       5 |    5 |   -- |     -- |    2 |         -- | --        |             100 | 3 personnes |

\*: également 2 mallorns et 2 laens par point de taille

!!! warning "Attention"

    **Un bâtiment n'est actif que** si :

    - Ses [frais d'entretien] ont été **payés** en début de tour
    - Le nombre de personnes qui l'occupent est **inférieur ou égal** à sa taille (cette règle ne s'applique pas à certains bâtiments, comme le [phare])

Voir aussi : [Construction d'un château].

## Phare

*Lighthouse (EN), Leuchtturm (DE)*.

| Propriété                 | Valeur                                |
|---------------------------|---------------------------------------|
| Coûts par point de taille | 2 pierres, 1 bois, 1 fers, 100 pièces |
| Niveau requis             | 3                                     |
| Maintenance par tour      | 100 pièces                            |
| Taille maximale           | *pas de limite*                       |
| Capacité                  | 4 units                               |

| Taille | Perception | Visibilité |
|--------|------------|------------|
| 10     | 3          | 1          |
| 10     | 6          | 2          |
| 100    | 9          | 3          |
| 1000   | 12         | 4          |
| etc    |            |            |

Les avantages d'un phare :

- Débutant à la taille 10, Le phare réduit la possibilité qu'un bateau dérive suite à une tempête. Cet effet s'étend à log10 (taille du phare) + 1 régions autour du bâtiment.
- Le phare donne aux occupants (jusqu'à 4 unités seulement) des informations sur les bateaux visibles dans un rayon de log10 (taille du phare) + 1 régions. L'unité doit avoir une perception d'au moins distance×3. Un rapport provenant d'une région océanique située à trois hexs de distance ne peut être obtenu que si le phare est d'au moins une taille de 100 et que l'unité a au moins une perception de 9.

## Mine

*Mine (EN), Bergwerk (DE)*.

| Propriété                 | Valeur                                 |
|---------------------------|----------------------------------------|
| Coûts par point de taille | 5 pierres, 10 bois, 1 fers, 250 pièces |
| Niveau requis             | 4                                      |
| Maintenance par tour      | 500 pièces                             |
| Taille maximale           | *pas de limite*                        |
| Capacité                  | 1 person per 1 taille                  |

- Seule la moitié du fers extrait par les unités situées à l'intérieur de la mine est déduite des ressources de la région. Cet effet fonctionne de manière cumulative avec tous les avantages raciaux correspondants.
- Les unités à l'intérieur de la mine ont +1 en mining pour l'extraction, mais ceci ne s'applique pas au niveau requis pour atteindre une couche plus profonde.
- Pour extraire du laens il est nécessaire d'être dans une mine.

**Exemple:**

- Dans une mine, un humain ayant mining 2 peut extraire 3 fers à la couche 1 ou 2. Cependant, en raison de l'arrondi, 2 fers sont déduits de la réserve de la région.
- 1 unité d'humain de 2 personnes niveau 4. Elle produit 8 fers et prélève 8 fers des ressources de la région. Dans une mine la même unité produit 10 fers (4+1\*2) et prélève seulement 5 fers (10/2).
- 1 unité de 2 nains niveau 4. Elle produit 8 fers et prélève 5 fers des ressources de la région (don spécial des nains 60%). Dans une mine la même unité de nains produit 10 fers (4+1\*2) et prélève seulement 3 fers (10\*60%/2).

## Carrière

*Quarry (EN), Steinbruch (DE)*.

| Propriété                 | Valeur                                |
|---------------------------|---------------------------------------|
| Coûts par point de taille | 1 pierres, 5 bois, 1 fers, 250 pièces |
| Niveau requis             | 2                                     |
| Maintenance par tour      | 250 pièces                            |
| Taille maximale           | *pas de limite*                       |
| Capacité                  | 1 person per 1 taille                 |

- Seule la moitié de la pierre extraite par les unités situées à l'intérieur de la quarry est déduite des ressources de la région. Cet effet fonctionne de manière cumulative avec tous les avantages raciaux correspondants.
- Les unités à l'intérieur de la quarry ont +1 en quarrying pour l'extraction, mais ceci ne s'applique pas au niveau requis pour atteindre une couche plus profonde.

**Exemple:**

- 10 trolls produisent 40 pierres dans une région. En raison des capacités spéciales des trolls, la réserve de la région n'est réduite que de 30 pierres.

Si les trolls sont à l'intérieur d'une carrière, la réserve sera réduite de 15 Pierres.

S'il ne reste que 7 pierres dans la région, les trolls ne peuvent produire que 9 pierres mais 18 dans une carrière.

## Scierie

*Sawmill (EN), Sägewerk (DE)*.

| Coûts par point de taille | 5 pierres, 5 bois, 3 fers, 200 pièces |
| Niveau requis          | 3                                   |
| Maintenance par tour    | 250 pièces                          |
| Taille maximale            |  *pas de limite*                                |
| Capacité                | 1 person per 1 taille                 |

- Seule la moitié du bois/saplings/mallorns produit par les unités dans une scierie est déduite des ressources de la région. Ce nombre est arrondi au supérieur (c'est-à-dire que si une unité, dans une scierie, produit 11 bois, 6 arbres seront coupés).
- Les unités à l'intérieur d'une scierie bénéficient d'un bonus de +1 à leur compétence forestry.

**Example:** Avec une potion de [water of life] et 10 bois vous pouvez créer du bois dans une scierie. Avec l'ordre [USE 1 water~of~life] vous créez 10 saplings en utilisant 10 bois. Vous les coupez instananément dans la scierie, produisant ainsi 20 bois.

## Forge

*Smithy (EN), Schmiede (DE)*.

| Propriété                 | Valeur                                |
|---------------------------|---------------------------------------|
| Coûts par point de taille | 5 pierres, 5 bois, 2 fers, 200 pièces |
| Niveau requis             | 3                                     |
| Maintenance par tour      | 300 pièces, 1 bois                    |
| Taille maximale           | *pas de limite*                       |
| Capacité                  | 1 person per 1 taille                 |

- Les unités à l'intérieur n’ont besoin que de la moitié de la quantité normale de fers pour fabriquer des armes et des armures en fers. Le Laen n'est pas économisé.
- Les unités à l'intérieur d'une forge bénéficient d'un bonus de +1 à leur compétence weaponsmithing et armoursmithing.

## Haras

*Stable (EN), Pferdezucht (DE)*.

| Propriété                 | Valeur                                |
|---------------------------|---------------------------------------|
| Coûts par point de taille | 2 pierres, 4 bois, 1 fers, 100 pièces |
| Niveau requis             | 2                                     |
| Maintenance par tour      | 150 pièces                            |
| Taille maximale           | *pas de limite*                       |
| Capacité                  | 1 person per 1 taille                 |

- Les unités à l'intérieur d'une écurie peuvent reproduire des chevaux en utilisant l'ordre [[cmd-grow]] HORSES. Pour cela l'unité a besoin de la compétence Taming et d'au moins 2 chevaux (en sa possession).
- La chance d'élever des chevaux correspond à la compétence de l'unité. De plus, l'unité dispose d'un nombre de tentatives égal à son niveau. Si une unité est T5, il dispose de 5 tentatives à 5% chacune pour élever un cheval.
- Pour chaque tentative l'unité a besoin d'un cheval. Si le nombre de chevaux disponibles est insuffisant, les tentatives sont annulées. 5 chevaux sont nécessaires dans l'exemple précédent.

## Port

*Harbour (EN), Hafen (DE)*.

| Propriété                 | Valeur                                         |
|---------------------------|------------------------------------------------|
| Coûts par point de taille | 5 pierres, 5 bois, 250 pièces                  |
| Coût total                | 125 pierres, 125 bois, 6250 pièces             |
| Niveau requis             | 3                                              |
| Maintenance par tour      | 250 pièces                                     |
| Taille maximale           | 25                                             |
| Capacité                  | Personnes according to taille, unlimited ships |

- Permet aux bateaux plus gros qu'un boat d'accoster dans des régions qui ne sont ni des plaines ni des forêts.
- Une région avec un port peut être utilisée comme une « région canal », c'est-à-dire qu'un bateau dans le port peut naviguer dans n'importe quelle autre direction maritime.
- Dans les deux cas, la condition préalable est que le propriétaire du port soit membre de la même faction ou qu'il ait paramétré un [HELP GUARD] avec la faction du Capitaine.
- Le propriétaire du port reçoit 10 % de tout l'argent gagné grâce au commerce, en plus des éventuels revenus provenant des châteaux.
- Le propriétaire reçoit également (2\*Trade)% de tous les biens de luxe qui se trouvent à bord des bateaux entrants. Sauf si l'unité qui transporte les marchandises a un niveau de dissimulation supérieur au niveau de perception du propriétaire du port, ou si le capitaine du bateau est allié avec le propriétaire du port.
- Dans une région dotée d'un port, les prix des biens de luxe augmenteront avec une probabilité de 20 % au lieu des 10 % normaux.
- Un port ne fonctionnera que s’il est entièrement construit. Il ne peut y avoir qu'un seul port par région. Celui qui termine un port en premier en est le propriétaire. Un port à moitié terminé peut être détruit avec l'ordre [[cmd-destroy]].

## Académie

*Academy (EN), Akademie (DE)*.

| Propriété                 | Valeur                                       |
|---------------------------|----------------------------------------------|
| Coûts par point de taille | 5 pierres, 5 bois, 1 fers, 500 pièces        |
| Coût total                | 125 pierres, 125 bois, 25 fers, 12500 pièces |
| Niveau requis             | 3                                            |
| Maintenance par tour      | 1000 pièces                                  |
| Taille maximale           | 25                                           |
| Capacité                  | Personnes according to taille                |

- Les unités qui apprennent dans une académie ont 1/3 de chance d'apprendre une fois de plus cette semaine, et si elles ont un professeur, elles ont 2/3 de chance.
- Apprendre dans une académie coûte 50 pièces d'argent par personne pour les compétences qui peuvent normalement être apprises sans aucun frais et le double de la somme d'argent pour les compétences qui coûtent quelque chose pour les apprendre.
- Les enseignants qui enseignent aux élèves d'une académie ont également une chance d'apprendre, qui peut aller jusqu'à 1/3 en fonction du nombre de leurs élèves. Ils n’ont pas besoin d’être eux-mêmes dans une académie pour cela.
- Une académie ne fonctionnera que si elle est entièrement construite !

## Tour de mage

*Mage Tower (EN), Magierturm (DE)*.

| Propriété                 | Valeur                                                                 |
|---------------------------|------------------------------------------------------------------------|
| Coûts par point de taille | 5 pierres, 3 bois, 3 fers, 2 mallorns, 2 laens, 500 pièces             |
| Coût total                | 250 pierres, 150 bois, 150 fers, 100 mallorns, 100 laens, 25000 pièces |
| Niveau requis             | 5                                                                      |
| Maintenance par tour      | 1000 pièces                                                            |
| Taille maximale           | 50                                                                     |
| Capacité                  | 2 personnes                                                            |

- Dans une tour de mage, un mage régénère 75 % d'aura en plus.
- La puissance de chaque sort lancé à l’intérieur d’une tour de mage est augmentée comme si le sort était lancé d’un niveau supérieur.
- Les erreurs arrivent beaucoup moins souvent.
- Le bâtiment lui-même a une résistance à la magie augmentée de 40%.
- Une tour de mage ne fonctionnera que si elle est entièrement construite !

## Caravanserail

*Caravanserai (EN), Karawanserei (DE)*.

| Propriété                 | Valeur                                    |
|---------------------------|-------------------------------------------|
| Coûts par point de taille | 1 pierre, 5 bois, 1 fer, 500 pièces       |
| Coût total                | 10 pierres, 50 bois, 10 fers, 5000 pièces |
| Niveau requis             | 2                                         |
| Maintenance par tour      | 3000 pièces, 2 horses                     |
| Taille maximale           | 10                                        |
| Capacité                  | Personnes according to taille             |

- Un caravansérail permet de construire des routes dans les déserts. Si le caravansérail est détruit, la moitié des routes seront également détruites. Une route achevée demeure si l'entretien du bâtiment n'est pas payé.
- Dans les déserts, double le volume du commerce possible. Le propriétaire reçoit une part des recettes des ventes comme dans les règles des châteaux ([tableau des chateaux]).
- Un caravansérail ne fonctionnera que s’il est entièrement construit !

## Barrage

*Dam (EN), Damm (DE)*.

| Propriété                 | Valeur                                       |
|---------------------------|----------------------------------------------|
| Coûts par point de taille | 5 pierres, 10 bois, 1 fer, 500 pièces        |
| Coût total                | 250 pierres, 500 bois, 50 fers, 25000 pièces |
| Niveau requis             | 4                                            |
| Maintenance par tour      | 1000 pièces, 3 bois                          |
| Taille maximale           | 50                                           |
| Capacité                  | Personnes according to taille                |

- Un barrage vous permet de construire des routes dans les marécages. Si le barrage est détruit, la moitié des routes seront également détruites. Une route achevée demeure si l'entretien du bâtiment n'est pas payé.
- Le barrage ne fonctionnera que s’il est entièrement construit !

## Tunnel

*Tunnel (EN), Tunnel (DE)*.

| Propriété                 | Valeur                                         |
|---------------------------|------------------------------------------------|
| Coûts par point de taille | 10 pierres, 5 bois, 1 fer, 300 pièces          |
| Coût total                | 1000 pierres, 500 bois, 100 fers, 30000 pièces |
| Niveau requis             | 6                                              |
| Maintenance par tour      | 100 pièces, 2 pierres                          |
| Taille maximale           | 100                                            |
| Capacité                  | Personnes according to taille                  |

- Un tunnel permet de construire des routes sur des glaciers. Si le tunnel est détruit, la moitié des routes seront également détruites. Une route achevée demeure si l'entretien du bâtiment n'est pas payé.
- Un tunnel ne fonctionnera que s’il est entièrement construit !

## Auberge

*Inn (EN), Taverne (DE)*.

| Propriété                 | Valeur                               |
|---------------------------|--------------------------------------|
| Coûts par point de taille | 4 pierres, 3 bois, 1 fer, 200 pièces |
| Niveau requis             | 2                                    |
| Maintenance par tour      | 5 pièces per 1 taille                |
| Taille maximale           | *pas de limite*                      |
| Capacité                  | 1 person per 1 taille                |

- Les unités à l'intérieur d'une auberge se régénèrent 50 % plus rapidement.
- Toutes les personnes à l'intérieur d'une auberge ont besoin de 14 silver par semaine pour vivre au lieu des 10 normales.

## Monument

*Monument (EN), Monument (DE)*.

| Propriété                 | Valeur                              |
|---------------------------|-------------------------------------|
| Coûts par point de taille | 1 pierre, 1 bois, 1 fer, 400 pièces |
| Niveau requis             | 4                                   |
| Maintenance par tour      | --                                |
| Taille maximale           | *pas de limite*                     |
| Capacité                  | 1 person per 1 taille               |

- Le nom et la description du monument ne peuvent être renseignés qu'une seule fois. Cela ne pourra plus jamais être modifié.
- Un monument n'a aucune fonctionnalité.

## Cercle de Pierres

*Stonecircle (EN), Steinkreis (DE)*.

| Propriété                 | Valeur                |
|---------------------------|-----------------------|
| Coûts par point de taille | 5 pierres, 5 bois     |
| Coût total                | 500 pierres, 500 bois |
| Niveau requis             | 2                     |
| Maintenance par tour      | --                  |
| Taille maximale           | 100                   |
| Capacité                  | 3 personnes           |

- Un cercle de pierres peut être béni grâce à un [puissant sort]. Cela développe alors des effets étranges. Entre autres choses, il semble attirer les chevaux elfiques extrêmement rares. De plus, les magiciens présents dans le bâtiment peuvent interrompre la connexion entre l'espace astral et le monde réel.
- Dans un cercle de pierres béni, un mage régénère 50 % d’aura en plus.
- La puissance de tout sort lancé dans un cercle de pierres béni augmente comme si le sort avait été lancé avec un niveau supplémentaire.
- Les occupants ont 30% de résistance à la magie supplémentaire.
- Un cercle de pierres ne fonctionnera que s’il est entièrement construit et béni !

## Voir aussi

- [Bâtiments]
- [Châteaux]
- [Production]

Poursuivre la lecture : [pool de factions].

[water of life]: ./alchemy.md
[USE 1 water~of~life]: ./cmd-use.md
[HELP GUARD]: ./cmd-help.md
[tableau des chateaux]: ./castles.md#apercu
[puissant sort]: ./spells-descriptions.md#segne-steinkreis
[Bâtiments]: ./buildings.md
[Châteaux]: ./castles.md
[Production]: ./production.md
[pool de factions]: ./faction-pool.md
[Construction d'un château]: ./castles.md#apercu
[Phare]: #phare
[Mine]: #mine
[Carrière]: ./#carriere
[Scierie]: #scierie
[Forge]: #forge
[Haras]: #haras
[Port]: #port
[Caravanserail]: #caravanserail
[Académie]: ./#academie
[Tour de mage]: #tour-de-mage
[Barrage]: #barrage
[Tunnel]: #tunnel
[Auberge]: #auberge
[Monument]: #monument
[Cercle de Pierres]: #cercle-de-pierres
[MAKE "type de bâtiment"]: ./cmd-make.md
