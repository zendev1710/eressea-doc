---
# cSpell:locale fr, en
alias: alchimie
---
# Alchimie

## Potions

Les **potions** sont préparées à l'aide de [[herbs|plantes]] et d'autres ingrédients, et peuvent ensuite être utilisées par n'importe quelle **unité**.
Pour fabriquer une potion, il faut des unités avec la compétence [Alchemy], et pour trouver les plantes nécessaires, il faut des unités avec la compétence [Herbalism].

Les potions sont produites avec l'ordre [[cmd-make|`MAKE "<nom de la potion>"`]].
Une potion nécessite plusieurs ingrédients.
Les recettes sont données à chaque fois que l'on atteint le niveau requis pour les concocter.
Plus tard, on pourra les retrouver avec la commande [[cmd-show]].
Pour pouvoir fabriquer une potion, le niveau de l'alchimiste doit être deux fois plus élevé que le niveau de la potion.
Un alchimiste peut chaque tour créer (niveau de compétence)/(niveau de potion\*2) potions.
Un alchimiste de niveau 6 peut donc fabriquer au maximum une potion de niveau 3, une potion de niveau 2 ou trois potions de niveau 1.

Si vous souhaitez utiliser une potion, vous le faites avec l'ordre [[cmd-use|USE &#91;quantité&#93; "&lt;nom de la potion&gt;" &#91;ID d'unité&#93;]].  
*L'identifiant d'unité (ID)* ne doit être spécifié **uniquement** pour la potion **[Duncebun]**.

Une potion ne peut pas être divisée entre plusieurs unités.
On peut cependant diviser une grande unité en plusieurs unités plus petites après l'utilisation de la potion en en conservant les effets.

La plupart des potions profitent à l'unité qui les utilise.
Les exceptions sont les potions qui se rapportent à une région - dans ce cas, l'effet est obtenu dans la région où se trouve l'unité au début du tour - ou celles qui affectent d'autres unités (potion Duncebun).

En général, une potion affecte 10 personnes ou 10 biens pendant le tour où elle est utilisée, comme indiqué dans sa recette.
Les potions qui affectent les objets d'une unité expirent si elles ne peuvent pas être utilisées parce que l'unité ne possède plus ces objets.
De nombreuses potions fonctionnent de telle sorte qu'un trop grand nombre de personnes dans l'unité importe peu, c'est-à-dire qu'avec 12 personnes et une potion (qui fonctionne pour 10), l'effet n'affecte que 10 des 12 personnes.
Cela n'est pas possible avec la potion "berserks blood", car les personnes n'agissent pas comme une unité au combat.
Ici, il est nécessaire que toutes les personnes de l'unité aient l'effet de la potion avant le combat, sinon cela ne fonctionnera pas !

L'"effet résiduel" des potions n'expire pas pour toutes les potions;
par exemple, une personne peut bénéficier de l'effet de "Brain wax" ou de "busybeer" pendant dix semaines après l'avoir utilisé.

### Berserkers blood

:   10 personnes reçoivent un modificateur d'attaque **de +1** au combat.

*Objectif :* renforcer l'attaque.  
*Niveau requis :* **3**.  
*Cible :* **unité**.  

Plantes nécessaires pour concocter cette potion :

- 1 flatroot
- 1 mandrake
- 1 sand reeker
- 1 white hemlock

### Brain wax

:   jusqu'à 10 personnes : augmente les chances **d'apprentissage d'une compétence**.

*Objectif :* accélérer l'apprentisssage.  
*Niveau requis :* **3**.  
*Cible :* **unité**.  

Plantes nécessaires pour concocter cette potion :

- 1 bugleweed
- 1 rock weed
- 1 waterfinder
- 1 windbag

### Busybeer

:   **Double la productivité** de 10 hommes utilisant l'ordre **`MAKE`**.

*Objectif :* accélérer la production.  
*Niveau requis :* **2**.  
*Cible :* **unité**.  

Plantes nécessaires pour concocter cette potion :

- 1 gapgrowth
- 1 mandrake
- 1 tangy temerity

### Duncebun

:   pour 10 personnes : pas d'apprentissage où l'enseignant n'apporte rien ou oublie 1 semaine de la meilleure compétence.

*Objectif :* ralentir l'apprentidssage d'une unité (adverse).  
*Niveau requis :* **3**.  
*Cible :* unité \[étrangère\].  

Plantes nécessaires pour concocter cette potion :

- 1 cave lichen
- 1 fjord fungus
- 1 owlsgaze
- 1 spider ivy

!!! note
    Vous pouvez l'appliquer à une unité avec la commande `USE "Duncebun" <ID unité cible>`.
    L'application de la potion échoue si la compétence `Stealth` de l'unité agissante est inférieure ou égale au niveau de `Perception` **+ 2** de la victime.
    Dans ce cas, vous obtenez un message d'erreur et le Duncebun n'est pas consommé (il reste à l'unité).

### Elixir of power

:   10 personnes ont leurs **points de vie multipliés par 5**.

*Objectif :* augmenter les points de vie d'une unité.  
*Niveau requis :* **4**.  
*Cible :* **unité**.  

Plantes nécessaires pour concocter cette potion :

- 1 Dragon blood
- 1 bubblemorel
- 1 elvendear
- 1 spider ivy
- 1 waterfinder
- 1 windbag

### Goliath water

:   10 hommes peuvent porter autant que 10 chevaux.

*Objectif :* augmenter la capacité à transporter.  
*Niveau requis :* **1**.  
*Cible :* **unité**.  

Plantes nécessaires pour concocter cette potion :

- 1 bugleweed
- 1 fjord fungus

### Healing potion

:   une personne survit à des dommages mortels; possible une seule fois par personne et par semaine.

*Objectif :* augmenter les chances de survie au combat.  
*Niveau requis :* **4**.  
*Cible :* **unité**.  

Plantes nécessaires pour concocter cette potion :

- 1 bugleweed
- 1 elvendear
- 1 gapgrowth
- 1 ice begonia
- 1 windbag

### Horsepower potion

:   50 chevaux mettent au monde jusqu'à **4 poulains**.

*Objectif :* augmenter les ressources d'une région (chevaux).  
*Niveau requis :* **3**.  
*Cible :* **région**.  

Plantes nécessaires pour concocter cette potion :

- 1 cobalt fungus
- 1 knotroot
- 1 peyote,
- 1 sand reeker

### Ointment

:   Soigne jusqu'à 400 points de vie.

*Objectif :* soigner une unité.  
*Niveau requis :* **2**.  
*Cible :* **unité**.  

Plantes nécessaires pour concocter cette potion :

- 1 cobalt fungus
- 1 tangy temerity
- 1 white hemlock

### Peasant blood

:   Jusqu'à 100 démons peuvent se passer de tuer des paysans.

*Objectif :* augmenter les ressources d'une région (paysans) où des démons sont présents.  
*Niveau requis :* **2**.  
*Cible :* **unité**.  

Éléments nécessaires pour concocter cette potion :

- 1 cave lichen,
- 1 cobalt fungus
- 1 fjord fungus
- 1 **peasant**

!!! note
    Une *Peasant blood* agit sur l'unité, mais tous les démons de la faction de la région l'utilisent s'il en reste.
    Il vous suffit donc d'équiper une seule unité (par région), à condition qu'elle boive suffisamment de *Peasant blood* pour tous les démons.

### Peasant love potion

:   1000 paysans croissent deux fois plus vite que la normale.

*Objectif :* augmenter les ressources d'une région (paysans).  
*Niveau requis*: **4**.  
*Cible*: **région**.  

Plantes nécessaires pour concocter cette potion :

- 1 bubblemorel
- 1 elvendear
- 1 mandrake
- 1 rock weed
- 1 snowcrystal petal

### Potion of nest warmth

:   Permet aux **[Insectes]** de recruter **même en hiver**.

*Objectif :* permettre le recrutement d'Insectes en hiver.  
*Niveau requis :* **3**.  
*Cible :* **région**.  

Plantes nécessaires pour concocter cette potion :

- 1 gapgrowth
- 1 ice begonia
- 1 peyote
- 1 spider ivy

### Potion of truth

:   ***Cette potion n'a plus aucune fonction***.

*Niveau requis :* 1.  
*Cible :* région.  

Plantes nécessaires pour concocter cette potion :

- 1 fjord fungus
- 1 flatroot

### Seven mile tea

:   10 hommes à pied peuvent se déplacer aussi vite que s'ils montaient à cheval.

*Objectif :* augmenter la vitesse de déplacement.  
*Niveau requis :* **1**.  
*Cible :* **unité**.  

Plantes nécessaires pour concocter cette potion :

- 1 cobalt fungus
- 1 windbag

### Water of life

:   Transforme 10 bois (ou mallorn) en 10 pousses (ou pousses de mallorns).

*Objectif :* augmenter les ressources d'une région (arbres et mallorns).  
*Niveau requis :* **1**.  
*Cible :* **région**.  

Plantes nécessaires pour concocter cette potion :

- 1 elvendear
- 1 knotroot

## Tableau récapitulatif

| Potion                | Abr. | Niv. | Cible                   |
|-----------------------|:----:|:----:|-------------------------|
| Goliath water         |  GW  |  1   | Unité                   |
| Potion of truth       |  PT  |  1   | Région                  |
| Seven mile tea        |  SM  |  1   | Unité                   |
| Water of life         |  WL  |  1   | Région                  |
| Busybeer              |  BZ  |  2   | Unité                   |
| Ointment              |  OM  |  2   | Unité                   |
| Peasant blood         |  PB  |  2   | Unité[^1]               |
| Berserkers blood      |  BK  |  3   | Unité                   |
| Brain wax             |  BW  |  3   | Unité                   |
| Duncebun              |  DB  |  3   | Unité \[étrangère\][^2] |
| Horsepower potion     |  HP  |  3   | Région                  |
| Potion of nest warmth |  NW  |  3   | Région                  |
| Elixir of power       |  EP  |  4   | Unité                   |
| Healing potion        |  HL  |  4   | Unité                   |
| Peasant love potion   |  PL  |  4   | Région                  |

[^1]: agit sur l'unité, mais tous les démons de la faction dans la région s'en servent s'il en reste.
Il suffit donc d'en équiper une unité (par région), tant qu'elle boit assez de "peasant blood" pour tous les démons.  

[^2]: la potion s'applique à une autre unité avec l'ordre `USE "Duncebun" <ID unité cible>`.
À cet égard, il convient de noter que si la compétence `Stealth` de l'utilisateur est inférieure ou égale à la `Perception` **+ 2** de la victime, la tentative échoue.
Si la tentative échoue, le Duncebun reste chez l'utilisateur et il reçoit un message d'erreur.

## Plantes et leur utilisation

| Plante            | PT | SM | GW | WL | PB | BZ | OM | BK | DB | BW | HP | NW | PL | EP | HL |
|-------------------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| bubblemorel       |    |    |    |    |    |    |    |    |    |    |    |    | X  | X  |    |
| bugleweed         |    |    | X  |    |    |    |    |    |    | X  |    |    |    |    | X  |
| cave lichen       |    |    |    |    | X  |    |    |    | X  |    |    |    |    |    |    |
| cobalt fungus     |    | X  |    |    | X  |    | X  |    |    |    | X  |    |    |    |    |
| elvendear         |    |    |    | X  |    |    |    |    |    |    |    |    | X  | X  | X  |
| fjord fungus      | X  |    | X  |    | X  |    |    |    | X  |    |    |    |    |    |    |
| flatroot          | X  |    |    |    |    |    |    | X  |    |    |    |    |    |    |    |
| gapgrowth         |    |    |    |    |    | X  |    |    |    |    |    | X  |    |    | X  |
| ice begonia       |    |    |    |    |    |    |    |    |    |    |    | X  |    |    | X  |
| knotroot          |    |    |    | X  |    |    |    |    |    |    | X  |    |    |    |    |
| mandrake          |    |    |    |    |    | X  |    | X  |    |    |    |    | X  |    |    |
| owlsgaze          |    |    |    |    |    |    |    |    | X  |    |    |    |    |    |    |
| peyote            |    |    |    |    |    |    |    |    |    |    | X  | X  |    |    |    |
| rock weed         |    |    |    |    |    |    |    |    |    | X  |    |    | X  |    |    |
| sand reeker       |    |    |    |    |    |    |    | X  |    |    | X  |    |    |    |    |
| snowcrystal petal |    |    |    |    |    |    |    |    |    |    |    |    | X  |    |    |
| spider ivy        |    |    |    |    |    |    |    |    | X  |    |    | X  |    | X  |    |
| tangy temerity    |    |    |    |    |    | X  | X  |    |    |    |    |    |    |    |    |
| waterfinder       |    |    |    |    |    |    |    |    |    | X  |    |    |    | X  |    |
| white hemlock     |    |    |    |    |    |    | X  | X  |    |    |    |    |    |    |    |
| windbag           |    | X  |    |    |    |    |    |    |    | X  |    |    |    | X  | X  |

Poursuivre la lecture : [[herbs|plantes]].

<!-- From [https://wiki.eressea.de/index.php?title=Tränke/fr&oldid=16931] -->

[Alchemy]: ./skills-list.md#alchimie
[Herbalism]: ./skills-list.md#herboristerie
[Insectes]: ./races.md#insectes

[Duncebun]: #duncebun