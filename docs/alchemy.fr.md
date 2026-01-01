---
# cSpell:locale fr, en
alias: alchimie
---
# Alchemy

## Potions

Les **potions** alchimiques sont préparées à l'aide de [[herbs|plantes]] et d'autres ingrédients, et peuvent ensuite être utilisées par n'importe quelle unité.
Pour fabriquer une potion, il faut des unités avec la compétence [Alchemy], et pour trouver les plantes nécessaires, il faut des unités avec la compétence [Herbalism].

Les potions sont créées avec l'ordre [[cmd-make|`MAKE "<nom de la potion>"`]].
Chaque potion nécessite plusieurs ingrédients.
Les recettes sont données à chaque fois que l'on atteint le niveau requis pour les concocter.
Plus tard, on pourra les retrouver avec la commande [[cmd-show]].
Pour pouvoir fabriquer une potion, le niveau de l'alchimiste doit être deux fois plus élevé que le niveau de la potion.
Un alchimiste peut chaque tour créer (niveau de compétence)/(niveau de potion\*2) potions.
Un alchimiste de niveau 6 peut donc fabriquer au maximum une potion de niveau 3, une potion de niveau 2 ou trois potions de niveau 1.

Si vous souhaitez utiliser une potion, vous le faites avec l'ordre [[cmd-use|USE &#91;quantité&#93; "&lt;nom de la potion&gt;" &#91;ID d'unité&#93;]].
*L'identifiants d'unité (ID)* ne doit être spécifié que pour la potion Duncebun.

Une potion ne peut pas être divisée entre plusieurs unités.
On peut cependant diviser une grande unité en plusieurs unités plus petites après l'utilisation de la potion en en conservant les effets.

La plupart des potions profitent à l'unité qui les utilise.
Les exceptions sont les potions qui se rapportent à une région - dans ce cas, l'effet est obtenu dans la région où se trouve l'unité au début du tour - ou celles qui affectent d'autres unités (potion Duncebun).

En général, une potion affecte 10 personnes ou 10 biens pendant le tour où elle est utilisée, comme indiqué dans sa recette.
Les potions qui affectent les objets d'une unité expirent si elles ne peuvent pas être utilisées parce que l'unité ne possède plus ces objets.
De nombreuses potions fonctionnent de telle sorte qu'un trop grand nombre de personnes dans l'unité importe peu, c'est-à-dire qu'avec 12 personnes et une potion (qui fonctionne pour 10), l'effet n'affecte que 10 des 12 personnes.
Cela n'est pas possible avec la potion "berserks blood", car les personnes n'agissent pas comme une unité au combat.
Ici, il est nécessaire que toutes les personnes de l'unité aient l'effet de la potion avant le combat, sinon cela ne fonctionnera pas !

L'"effet résiduel" des potions n'expire pas pour toutes les potions, par exemple, une personne peut bénéficier de l'effet de "Brain wax" ou de "busybeers" pendant dix semaines après l'avoir utilisé.

### Berserkers blood

:   10 personnes reçoivent un modificateur d'attaque **de +1** au combat.

**Niveau requis**: 3.  
**Cible**: unité.  

To be made, this potion requires the following herbs:

- 1 flatroot
- 1 mandrake
- 1 sand reeker
- 1 white hemlock

### Brain wax

:   jusqu'à 10 personnes : augmente les chances **d'apprentissage d'une compétence**.

**Niveau requis**: 3.  
**Cible**: unité.  

To be made, this potion requires the following herbs:

- 1 bugleweed
- 1 rock weed
- 1 waterfinder
- 1 windbag

### Busybeer

:   **Double la productivité** de 10 hommes utilisant l'ordre **`MAKE`**.

**Niveau requis**: 2.  
**Cible**: unité.  

To be made, this potion requires the following herbs:

- 1 gapgrowth
- 1 mandrake
- 1 tangy temerity

### Duncebun

:   pour 10 personnes : pas d'apprentissage où l'enseignant n'apporte rien ou oublie 1 semaine de la meilleure compétence.

**Niveau requis**: 3.  
**Cible**: unité \[étrangère\].  

To be made, this potion requires the following herbs:

- 1 cave lichen
- 1 fjord fungus
- 1 owlsgaze
- 1 spider ivy

!!! note
    You can apply it to a unité with the order USE "Duncebun" &lt;unit−id&gt;.  
    The application of the potion fails if the STEALTH skill of the acting unité is less or equal to the victim's PERCEPTION+2.
    In this case, you get an error message and the Duncebun is not used up (thus it remains to the unité).

### Elixir of power

:   10 personnes ont leurs **points de vie multipliés par 5**.

**Niveau requis**: 4.  
**Cible**: unité.  

To be made, this potion requires the following herbs:

- 1 Dragon blood
- 1 bubblemorel
- 1 elvendear
- 1 spider ivy
- 1 waterfinder
- 1 windbag

### Goliath water

:   10 hommes peuvent porter autant que 10 chevaux.

**Niveau requis**: 1.  
**Cible**: unité.  

To be made, this potion requires the following herbs:

- 1 bugleweed
- 1 fjord fungus

### Healing potion

:   une personne survit à des dommages mortels; possible une seule fois par personne et par semaine.

**Niveau requis**: 4.  
**Cible**: unité.  

To be made, this potion requires the following herbs:

- 1 bugleweed
- 1 elvendear
- 1 gapgrowth
- 1 ice begonia
- 1 windbag

### Horsepower potion

:   50 chevaux mettent au monde jusqu'à **4 poulains**.

**Niveau requis**: 3.  
**Cible**: region.  

To be made, this potion requires the following herbs:

- 1 cobalt fungus
- 1 knotroot
- 1 peyote,
- 1 sand reeker

### Ointment

:   Soigne jusqu'à 400 points de vie.

**Niveau requis**: 2.  
**Cible**: unité.  

To be made, this potion requires the following herbs:

- 1 cobalt fungus
- 1 tangy temerity
- 1 white hemlock

### Peasant blood

:   Jusqu'à 100 démons peuvent se passer de tuer des paysans.

**Niveau requis**: 2.  
**Cible**: unité.  

To be made, this potion requires the following **ingredients**:

- 1 cave lichen,
- 1 cobalt fungus
- 1 fjord fungus
- 1 **peasant**

!!! note
    A peasant blood acts on the unité, but all the faction's demons in the region use it if there are any left.  
    So you only need to equip one unité (per region), as long as it drinks enough peasant blood for all the demons.  

### Peasant love potion

:   1000 paysans croissent deux fois plus vite que la normale.

**Niveau requis**: 4.  
**Cible**: region.  

To be made, this potion requires the following herbs:

- 1 bubblemorel
- 1 elvendear
- 1 mandrake
- 1 rock weed
- 1 snowcrystal petal

### Potion of nest warmth

:   Permet aux Insectes de recruter même en hiver.

**Niveau requis**: 3.  
**Cible**: region.  

To be made, this potion requires the following herbs:

- 1 gapgrowth
- 1 ice begonia
- 1 peyote
- 1 spider ivy

### Potion of truth

:   *Cette potion n'a plus aucune fonction*.

**Niveau requis**: 1.  
**Cible**: region.  

To be made, this potion requires the following herbs:

- 1 fjord fungus
- 1 flatroot

### Seven mile tea

:   10 hommes à pied peuvent se déplacer aussi vite que s'ils montaient à cheval.

**Niveau requis**: 1.  
**Cible**: unité.  

To be made, this potion requires the following herbs:

- 1 cobalt fungus
- 1 windbag

### Water of life

:   Transforme 10 bois (ou mallorn) en 10 pousses (ou pousses de mallorns).

**Niveau requis**: 1.  
**Cible**: region.  

To be made, this potion requires the following herbs:

- 1 elvendear
- 1 knotroot

## Tableau récapitulatif

Liste des potions.

| Nom                   | Abr. | Niv. | Cible                   |
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

[^2]: la potion s'applique à une autre unité avec l'ordre `USE "Duncebun" <unit−id>`.
À cet égard, il convient de noter que si la compétence stealth de l'utilisateur est inférieure ou égale à la perception + 2 de la victime, la tentative échoue.
Si la tentative échoue, le Duncebun reste chez l'utilisateur et il reçoit un message d'erreur.

## Tableau des plantes

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
