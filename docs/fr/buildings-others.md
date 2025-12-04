# Bâtiments spéciaux

Les bâtiments sont construits avec l'ordre [MAKE "type de bâtiment"] et peuvent être agrandis avec [MAKE "type de bâtiment" ID-bâtiment][MAKE "type de bâtiment"].

- Exemples : `MAKE`[`Lighthouse`] (créé) ou `MAKE`[`Harbour`]`xyz` (agrandi).
- Ces bâtiments nécessitent un niveau de compétence minimum en Masonry, qui est indiqué dans le tableau. Certains bâtiments sont d'une taille déterminée.
- Un bâtiment n'est actif que si sa maintenance a été payée en début de tour.
- Si le nombre de personnes à l'intérieur du bâtiment est supérieur à sa taille personne ne bénéficie de ses avantages. (sauf cas spécial comme le Lighthouse)

Voici un tableau récapitulatif, des explications plus détaillées suivent ci-dessous.

Building; see also table on [Construction d'un château]  
The capacity refers only to the persons who can benefit from the building.  
\*: also 2 Mallorn and 2 Laen per size point

| Buildings      | Building costs |      |      |        | Skill | Upkeep  |          | Max. | Capacity   |
|----------------|----------------|------|------|--------|-------|---------|----------|------|------------|
|                | Stone          | Wood | Iron | Silver |       | Silver  | Resource |      |            |
| [Lighthouse]   | 2              | 1    | 1    | 100    | 3     | 100     | \-/-     | none | 4 persons  |
| [Mine]         | 5              | 10   | 1    | 250    | 4     | 500     | \-/-     | none | size       |
| [Quarry]       | 1              | 5    | 1    | 250    | 2     | 250     | \-/-     | none | size       |
| [Sawmill]      | 5              | 5    | 3    | 200    | 3     | 250     | \-/-     | none | size       |
| [Smithy]       | 5              | 5    | 2    | 200    | 3     | 300     | 1 wood   | none | size       |
| [Stable]       | 2              | 4    | 1    | 100    | 2     | 150     | \-/-     | none | size       |
| [Harbour]      | 5              | 5    | \-/- | 250    | 3     | 250     | \-/-     | 25   | size       |
| [Caravanserai] | 1              | 5    | 1    | 500    | 2     | 3000    | 2 horses | 10   | size       |
| [Academy]      | 5              | 5    | 1    | 500    | 3     | 1000    | \-/-     | 25   | size       |
| [Mage Tower]\* | 5              | 3    | 3    | 500    | 5     | 1000    | \-/-     | 50   | 2 Personen |
| [Dam]          | 5              | 10   | 1    | 500    | 4     | 1000    | 3 wood   | 50   | size       |
| [Tunnel]       | 10             | 5    | 1    | 300    | 6     | 100     | 2 stones | 100  | size       |
| [Inn]          | 4              | 3    | 1    | 200    | 2     | 5\*size | \-/-     | none | size       |
| [Monument]     | 1              | 1    | 1    | 400    | 4     | \-/-    | \-/-     | none | size       |
| [Stonecircle]  | 5              | 5    | \-/- | \-/-   | 2     | \-/-    | \-/-     | 100  | 3 Persons  |

## Lighthouse

|                          |                                      |
|--------------------------|--------------------------------------|
| Costs per point of size: | 2 stones, 1 wood, 1 iron, 100 Silver |
| Skill required:          | 3                                    |
| Maintenance per turn:    | 100 Silver                           |
| Maximum size:            | none                                 |
| Capacity:                | 4 units                              |

| Size | Perception | Visibility |
|------|------------|------------|
| 10   | 3          | 1          |
| 10   | 6          | 2          |
| 100  | 9          | 3          |
| 1000 | 12         | 4          |
| etc  |            |            |

- Débutant à la taille 10, Le phare réduit la possibilité qu'un navire dérive suite à une tempête. Cet effet s'étend à log10 (taille du phare)+ 1 régions autour du bâtiment.
- Le phare donne aux occupants (jusqu'à 4 unités seulement) des informations sur les navires visibles dans un rayon de log10 (taille du phare)+ 1 régions. L'unité doit avoir une perception d'au moins distance×3. Un rapport provenant d'une région océanique située à trois hexs de distance ne peut être obtenu que si le phare est d'au moins une taille de 100 et que l'unité a au moins une perception de 9.

## Mine

|                          |                                       |
|--------------------------|---------------------------------------|
| Costs per point of size: | 5 stones, 10 wood, 1 iron, 250 Silver |
| Skill required:          | 4                                     |
| Maintenance per turn:    | 500 Silver                            |
| Maximum size:            | none                                  |
| Capacity:                | 1 person per 1 size                   |

- Seule la moitié du fer extrait par les unités situées à l'intérieur de la mine est déduite des ressources de la région. Cet effet fonctionne de manière cumulative avec tous les avantages raciaux correspondants.
- Les unités à l'intérieur de la mine ont +1 en mining pour l'extraction, mais ceci ne s'applique pas au niveau requis pour atteindre une couche plus profonde.
- Pour extraire du laen il est nécessaire d'être dans une mine.

**Exemple:**

- Dans une mine, un humain ayant mining 2 peut extraire 3 fer à la couche 1 ou 2. Cependant, en raison de l'arrondi, 2 fers sont déduits de la réserve de la région.
- 1 unité d'humain de 2 personnes niveau 4. Elle produit 8 fer et prélève 8 fer des ressources de la région. Dans une mine la même unité produit 10 fer (4+1\*2) et prélève seulement 5 fer (10/2).
- 1 unité de 2 nains niveau 4. Elle produit 8 fer et prélève 5 fer des ressources de la région (don spécial des nains 60%). Dans une mine la même unité de nains produit 10 fer (4+1\*2) et prélève seulement 3 fer (10\*60%/2).

## Quarry

|                          |                                     |
|--------------------------|-------------------------------------|
| Costs per point of size: | 1 stone, 5 wood, 1 iron, 250 Silver |
| Skill required:          | 2                                   |
| Maintenance per turn:    | 250 Silver                          |
| Maximum size:            | none                                |
| Capacity:                | 1 person per 1 size                 |

- Seule la moitié de la pierre extraite par les unités situées à l'intérieur de la quarry est déduite des ressources de la région. Cet effet fonctionne de manière cumulative avec tous les avantages raciaux correspondants.
- Les unités à l'intérieur de la quarry ont +1 en quarrying pour l'extraction, mais ceci ne s'applique pas au niveau requis pour atteindre une couche plus profonde.

**Exemple:**

- 10 trolls produisent 40 pierres dans une région. En raison des capacités spéciales des trolls, la réserve de la région n'est réduite que de 30 pierres.

Si les trolls sont à l'intérieur d'une carrière, la réserve sera réduite de 15 Pierres.

S'il ne reste que 7 pierres dans la région, les trolls ne peuvent produire que 9 pierres mais 18 dans une carrière.

## Sawmill

|                          |                                     |
|--------------------------|-------------------------------------|
| Costs per point of size: | 5 stone, 5 wood, 3 iron, 200 Silver |
| Skill required:          | 3                                   |
| Maintenance per turn:    | 250 Silver                          |
| Maximum size:            | none                                |
| Capacity:                | 1 person per 1 size                 |

- Seule la moitié du wood/saplings/mallorn produit par les unités dans une scierie est déduite des ressources de la région. Ce nombre est arrondi au supérieur (c'est-à-dire que si une unité, dans une scierie, produit 11 bois, 6 arbres seront coupés).
- Les unités à l'intérieur d'une scierie bénéficient d'un bonus de +1 à leur compétence forestry.

**Example:** Avec une potion de [water of life] et 10 wood vous pouvez créer du bois dans une scierie. Avec l'ordre [USE 1 water~of~life] vous créez 10 saplings en utilisant 10 wood. Vous les coupez instananément dans la scierie, produisant ainsi 20 wood.

## Smithy

|                          |                                     |
|--------------------------|-------------------------------------|
| Costs per point of size: | 5 stone, 5 wood, 2 iron, 200 Silver |
| Skill required:          | 3                                   |
| Maintenance per turn:    | 300 Silver, 1 wood                  |
| Maximum size:            | none                                |
| Capacity:                | 1 person per 1 size                 |

- Les unités à l'intérieur n’ont besoin que de la moitié de la quantité normale de fer pour fabriquer des armes et des armures en fer. Le Laen n'est pas économisé.
- Les unités à l'intérieur d'une forge bénéficient d'un bonus de +1 à leur compétence weaponsmithing et armoursmithing.

## Stable

|                          |                                     |
|--------------------------|-------------------------------------|
| Costs per point of size: | 2 stone, 4 wood, 1 iron, 100 Silver |
| Skill required:          | 2                                   |
| Maintenance per turn:    | 150 Silver                          |
| Maximum size:            | none                                |
| Capacity:                | 1 person per 1 size                 |

- Les unités à l'intérieur d'une écurie peuvent reproduire des chevaux en utilisant l'ordre [GROW] HORSES. Pour cela l'unité a besoin de la compétence Taming et d'au moins 2 chevaux (en sa possession).
- La chance d'élever des chevaux correspond à la compétence de l'unité. De plus, l'unité dispose d'un nombre de tentatives égal à son niveau. Si une unité est T5, il dispose de 5 tentatives à 5% chacune pour élever un cheval.
- Pour chaque tentative l'unité a besoin d'un cheval. Si le nombre de chevaux disponibles est insuffisant, les tentatives sont annulées. 5 chevaux sont nécessaires dans l'exemple précédent.

## Harbour

|                          |                                            |
|--------------------------|--------------------------------------------|
| Costs per point of size: | 5 stone, 5 wood, 250 Silver                |
| Total cost:              | 125 stone, 125 wood, 6250 Silver           |
| Skill required:          | 3                                          |
| Maintenance per turn:    | 250 Silver                                 |
| Maximum size:            | 25                                         |
| Capacity:                | persons according to size, unlimited ships |

- Permet aux navires plus gros qu'un boat d'accoster dans des régions qui ne sont ni des plaines ni des forêts.
- Une région avec un port peut être utilisée comme une « région canal », c'est-à-dire qu'un navire dans le port peut naviguer dans n'importe quelle autre direction maritime.
- Dans les deux cas, la condition préalable est que le propriétaire du port soit membre de la même faction ou qu'il ait paramétré un [HELP GUARD] avec la faction du Capitaine.
- Le propriétaire du port reçoit 10 % de tout l'argent gagné grâce au commerce, en plus des éventuels revenus provenant des châteaux.
- Le propriétaire reçoit également (2\*Trade)% de tous les biens de luxe qui se trouvent à bord des navires entrants. Sauf si l'unité qui transporte les marchandises a un niveau de dissimulation supérieur au niveau de perception du propriétaire du port, ou si le capitaine du navire est allié avec le propriétaire du port.
- Dans une région dotée d'un port, les prix des biens de luxe augmenteront avec une probabilité de 20 % au lieu des 10 % normaux.
- Un port ne fonctionnera que s’il est entièrement construit. Il ne peut y avoir qu'un seul port par région. Celui qui termine un port en premier en est le propriétaire. Un port à moitié terminé peut être détruit avec l'ordre [DESTROY].

## Academy

|                          |                                            |
|--------------------------|--------------------------------------------|
| Costs per point of size: | 5 stone, 5 wood, 1 iron, 500 Silver        |
| Total cost:              | 125 stone, 125 wood, 25 iron, 12500 Silver |
| Skill required:          | 3                                          |
| Maintenance per turn:    | 1000 Silver                                |
| Maximum size:            | 25                                         |
| Capacity:                | persons according to size                  |

- Les unités qui apprennent dans une académie ont 1/3 de chance d'apprendre une fois de plus cette semaine, et si elles ont un professeur, elles ont 2/3 de chance.
- Apprendre dans une académie coûte 50 pièces d'argent par personne pour les compétences qui peuvent normalement être apprises sans aucun frais et le double de la somme d'argent pour les compétences qui coûtent quelque chose pour les apprendre.
- Les enseignants qui enseignent aux élèves d'une académie ont également une chance d'apprendre, qui peut aller jusqu'à 1/3 en fonction du nombre de leurs élèves. Ils n’ont pas besoin d’être eux-mêmes dans une académie pour cela.
- Une académie ne fonctionnera que si elle est entièrement construite !

## Mage Tower

|                          |                                                                    |
|--------------------------|--------------------------------------------------------------------|
| Costs per point of size: | 5 stone, 3 wood, 3 iron, 2 mallorn, 2 laen, 500 Silver             |
| Total cost:              | 250 stone, 150 wood, 150 iron, 100 mallorn, 100 laen, 25000 Silver |
| Skill required:          | 5                                                                  |
| Maintenance per turn:    | 1000 Silver                                                        |
| Maximum size:            | 50                                                                 |
| Capacity:                | 2 Persons                                                          |

- Dans une tour de mage, un mage régénère 75 % d'aura en plus.
- La puissance de chaque sort lancé à l’intérieur d’une tour de mage est augmentée comme si le sort était lancé d’un niveau supérieur.
- Les erreurs arrivent beaucoup moins souvent.
- Le bâtiment lui-même a une résistance à la magie augmentée de 40%.
- Une tour de mage ne fonctionnera que si elle est entièrement construite !

## Caravanserai

|                          |                                         |
|--------------------------|-----------------------------------------|
| Costs per point of size: | 1 stone, 5 wood, 1 iron, 500 Silver     |
| Total cost:              | 10 stone, 50 wood, 10 iron, 5000 Silver |
| Skill required:          | 2                                       |
| Maintenance per turn:    | 3000 Silver, 2 horses                   |
| Maximum size:            | 10                                      |
| Capacity:                | persons according to size               |

- Un caravansérail permet de construire des routes dans les déserts. Si le caravansérail est détruit, la moitié des routes seront également détruites. Une route achevée demeure si l'entretien du bâtiment n'est pas payé.
- Dans les déserts, double le volume du commerce possible. Le propriétaire reçoit une part des recettes des ventes comme dans les règles des châteaux ([table des chateaux]).
- Un caravansérail ne fonctionnera que s’il est entièrement construit !

## Dam

|                          |                                            |
|--------------------------|--------------------------------------------|
| Costs per point of size: | 5 stone, 10 wood, 1 iron, 500 Silver       |
| Total cost:              | 250 stone, 500 wood, 50 iron, 25000 Silver |
| Skill required:          | 4                                          |
| Maintenance per turn:    | 1000 Silver, 3 wood                        |
| Maximum size:            | 50                                         |
| Capacity:                | persons according to size                  |

- Un barrage vous permet de construire des routes dans les marécages. Si le barrage est détruit, la moitié des routes seront également détruites. Une route achevée demeure si l'entretien du bâtiment n'est pas payé.
- Le barrage ne fonctionnera que s’il est entièrement construit !

## Tunnel

|                          |                                              |
|--------------------------|----------------------------------------------|
| Costs per point of size: | 10 stone, 5 wood, 1 iron, 300 Silver         |
| Total cost:              | 1000 stone, 500 wood, 100 iron, 30000 Silver |
| Skill required:          | 6                                            |
| Maintenance per turn:    | 100 Silver, 2 stone                          |
| Maximum size:            | 100                                          |
| Capacity:                | persons according to size                    |

- Un tunnel permet de construire des routes sur des glaciers. Si le tunnel est détruit, la moitié des routes seront également détruites. Une route achevée demeure si l'entretien du bâtiment n'est pas payé.
- Un tunnel ne fonctionnera que s’il est entièrement construit !

## Inn

|                          |                                     |
|--------------------------|-------------------------------------|
| Costs per point of size: | 4 stone, 3 wood, 1 iron, 200 Silver |
| Skill required:          | 2                                   |
| Maintenance per turn:    | 5 Silver per 1 size                 |
| Maximum size:            | none                                |
| Capacity:                | 1 person per 1 size                 |

- Les unités à l'intérieur d'une auberge se régénèrent 50 % plus rapidement.
- Toutes les personnes à l'intérieur d'une auberge ont besoin de 14 silver par semaine pour vivre au lieu des 10 normales.

## Monument

|                          |                                     |
|--------------------------|-------------------------------------|
| Costs per point of size: | 1 stone, 1 wood, 1 iron, 400 Silver |
| Skill required:          | 4                                   |
| Maintenance per turn:    | none                                |
| Maximum size:            | none                                |
| Capacity:                | 1 person per 1 size                 |

- Le nom et la description du monument ne peuvent être renseignés qu'une seule fois. Cela ne pourra plus jamais être modifié.
- Un monument n'a aucune fonctionnalité.

## Stonecircle

|                          |                     |
|--------------------------|---------------------|
| Costs per point of size: | 5 stone, 5 wood     |
| Total cost:              | 500 stone, 500 wood |
| Skill required:          | 2                   |
| Maintenance per turn:    | none                |
| Maximum size:            | 100                 |
| Capacity:                | 3 persons           |

- Un cercle de pierres peut être béni grâce à un [puissant sort]. Cela développe alors des effets étranges. Entre autres choses, il semble attirer les chevaux elfiques extrêmement rares. De plus, les magiciens présents dans le bâtiment peuvent interrompre la connexion entre l'espace astral et le monde réel.
- Dans un cercle de pierres béni, un mage régénère 50 % d’aura en plus.
- La puissance de tout sort lancé dans un cercle de pierres béni augmente comme si le sort avait été lancé avec un niveau supplémentaire.
- Les occupants ont 30% de résistance à la magie supplémentaire.
- Un cercle de pierres ne fonctionnera que s’il est entièrement construit et béni !

## Voir aussi

- [Bâtiments]
- [Châteaux]
- [Production]

|              |               |
|--------------|---------------|
| En savoir plus : | [factionpool] |

[water of life]: ./alchemy.md "Tränke"
[USE 1 water~of~life]: ./cmd-use.md "BENUTZE"
[GROW]: ./cmd-grow.md "ZÜCHTE"
[HELP GUARD]: ./cmd-help.md "HELFE"
[DESTROY]: ./cmd-destroy.md "ZERSTÖRE"
[table des chateaux]: ./castles.md#übersicht "Burgen"
[puissant sort]: ./spells-descriptions.md#segne-steinkreis "Zauberbeschreibungen E2"
[Bâtiments]: ./buildings.md "Gebäude"
[Châteaux]: ./castles.md "Burgen"
[Production]: ./production.md "Produktion"
[factionpool]: ./factions-pool.md "Parteipool"
[Construction d'un château]: ./castles.md#aperçu "Construction d'un château"
[Lighthouse]: #lighthouse
[Mine]: #mine
[Quarry]: #quarry
[Sawmill]: #sawmill
[Smithy]: #smithy
[Stable]: #stable
[Harbour]: #harbour
[Caravanserai]: #caravanserai
[Academy]: #academy
[Mage Tower]: #mage-tower
[Dam]: #dam
[Tunnel]: #tunnel
[Inn]: #inn
[Monument]: #monument
[Stonecircle]: #stonecircle
[MAKE "type de bâtiment"]: ./cmd-make.md "MACHE"
[`Lighthouse`]: #lighthouse
[`Harbour`]: #harbour
