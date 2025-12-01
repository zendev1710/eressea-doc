# Potions

Les **potions** alchimiques sont préparées à l'aide de [Plantes] et d'autres ingrédients, et peuvent ensuite être utilisées par n'importe quelle unité. Pour fabriquer une potion, il faut des unités avec la compétence [Alchemy], et pour trouver les plantes nécessaires, il faut des unités avec la compétence [Herbalism][Alchemy].

Les potions sont créées avec l'ordre [`MAKE`]`"nom_de_la_Potion"`. Chaque potion nécessite plusieurs ingrédients. Les recettes sont données à chaque fois que l'on atteint le niveau requis pour les concocter. Plus tard, on pourra les retrouver avec la commande [SHOW]. Pour pouvoir fabriquer une potion, le niveau de l'alchimiste doit être deux fois plus élevé que le niveau de la potion. Un alchimiste peut chaque tour créer (niveau de compétence)/(niveau de potion\*2) potions. Un alchimiste de niveau 6 peut donc fabriquer au maximum une potion de niveau 3, une potion de niveau 2 ou trois potions de niveau 1.

Si vous souhaitez utiliser une potion, vous le faites avec l'ordre [`USE`]`[quantité] "nom_de_la_potion" [ID d'unité]`. Les numéros d'unité (ID) ne doivent être spécifiés que pour la potion Duncebun. Une potion ne peut pas être divisée entre plusieurs unités. On peut cependant diviser une grande unité en plusieurs unités plus petites après l'utilisation de la potion en en conservant les effets.

La plupart des potions profitent à l'unité qui les utilise. Les exceptions sont les potions qui se rapportent à une région - dans ce cas, l'effet est obtenu dans la région où se trouve l'unité au début du tour - ou celles qui affectent d'autres unités (potion Duncebun).

En général, une potion affecte 10 personnes ou 10 biens pendant le tour où elle est utilisée, comme indiqué dans sa recette. Les potions qui affectent les objets d'une unité expirent si elles ne peuvent pas être utilisées parce que l'unité ne possède plus ces objets. De nombreuses potions fonctionnent de telle sorte qu'un trop grand nombre de personnes dans l'unité importe peu, c'est-à-dire qu'avec 12 personnes et une potion (qui fonctionne pour 10), l'effet n'affecte que 10 des 12 personnes. Cela n'est pas possible avec la potion "berserks blood", car les personnes n'agissent pas comme une unité au combat. Ici, il est nécessaire que toutes les personnes de l'unité aient l'effet de la potion avant le combat, sinon cela ne fonctionnera pas !

L'"effet résiduel" des potions n'expire pas pour toutes les potions, par exemple, une personne peut bénéficier de l'effet de "Brain wax" ou de "busybeers" pendant dix semaines après l'avoir utilisé.

## Liste des potions

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |Liste des Potions
| Niveau | Abbr | Nom | Ingrédients | Description | Cible |
| 1   | Sm  | Seven mile tea | cobalt fungus, windbag | 10 hommes à pied peuvent se déplacer aussi vite que s'ils montaient à cheval | Unité |
| 1   | Gw  | Goliath water | bugleweed, fjord fungus | 10 hommes peuvent porter autant que 10 chevaux | Unité |
| 1   | WL  | Water of life | elvendear, knotroot | Transforme 10 bois ou mallorn en 10 mallorns/pouces | Region |
| 1   | TW  | Potion of truth | flatroot, fjord fungus | Cette potion n'a plus aucune fonction | Region |
| 2   | St  | Busybeer | mandrake, gapgrowth, tangy temerity | Double la productivité de 10 hommes utilisant l'ordre `MAKE`. | Unité |
| 2   | Ws  | Ointment | cobalt fungus, white hemlock, tangy temerity | Soigne jusqu'à 400 points de vie | Unité |
| 2   | Ba  | Peasant blood | cave lichen, fjord fungus, cobalt fungus, Peasant | Jusqu'à 100 démons peuvent se passer de tuer des paysans | Unité\* |
| 3   | Gs  | Brain wax | waterfinder, rock weed, windbag, bugleweed | jusqu'à 10 personnes : Augmente les chances d'apprentissage d'une compétence | Unité |
| 3   | Db  | Duncebun | owlsgaze, spider ivy, cave lichen, fjord fungus | pour 10 personnes : pas d'apprentissage ou l'enseignant n'apporte rien ou oublie 1 semaine de la meilleure compétence | (foreign) Unité\*\* |
| 3   | Nw  | Potion of nest warmth | ice begonia, spider ivy, gapgrowth, peyote | Permet aux insectes de recruter même en hiver | Region |
| 3   | Pg  | Horsepower potion | cobalt fungus, sand reeker, peyote, knotroot | 50 chevaux mettent au monde jusqu'à 4 poulains | Region |
| 3   | Be  | Berserkers blood | white hemlock, mandrake, flatroot, sand reeker | 10 personnes reçoivent un modificateur d'attaque de +1 au combat | Unité |
| 4   | Bl  | Peasant love potion | mandrake, snowcrystal petal, rock weed, bubblemorel, elvendear | 1000 paysans croissent deux fois plus vite que la normale | Region |
| 4   | EM  | Elixir of power | elvendear, waterfinder, windbag, spider ivy, bubblemorel, Dragon blood | 10 personnes ont leurs points de vie quintuplés | Unité |
| 4   | Ht  | Healing potion | bugleweed, windbag, ice begonia, elvendear, gapgrowth | une personne survit à des dommages mortels ; possible une seule fois par personne et par semaine | Unité |

\* Agit sur l'unité, mais tous les démons de la faction dans la région s'en servent s'il en reste. Il suffit donc d'en équiper une unité (par région), tant qu'elle boit assez de "peasant blood" pour tous les démons.

\*\* La potion s'applique à une autre unité avec l'ordre `USE "Duncebun" <unit−id>`. A cet égard, il convient de noter que : Si la compétence stealth de l'utilisateur est inférieure ou égale à la perception + 2 de la victime, la tentative échoue. Si la tentative échoue, le Duncebun reste chez l'utilisateur et il reçoit un message d'erreur.

## Tableau des Plantes

| Herb | TW  | Sm  | Gw  | WL  | Ba  | St  | Ws  | Be  | Db  | Gs  | Pg  | Nw  | Bl  | EM  | Ht  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| flatroot | X   |     |     |     |     |     |     | X   |     |     |     |     |     |     |     |
| tangy temerity |     |     |     |     |     | X   | X   |     |     |     |     |     |     |     |     |
| owlsgaze |     |     |     |     |     |     |     |     | X   |     |     |     |     |     |     |
| spider ivy |     |     |     |     |     |     |     |     | X   |     |     | X   |     | X   |     |
| cobalt fungus |     | X   |     |     | X   |     | X   |     |     |     | X   |     |     |     |     |
| elvendear |     |     |     | X   |     |     |     |     |     |     |     |     | X   | X   | X   |
| bugleweed |     |     | X   |     |     |     |     |     |     | X   |     |     |     |     | X   |
| knotroot |     |     |     | X   |     |     |     |     |     |     | X   |     |     |     |     |
| bubblemorel |     |     |     |     |     |     |     |     |     |     |     |     | X   | X   |     |
| waterfinder |     |     |     |     |     |     |     |     |     | X   |     |     |     | X   |     |
| peyote |     |     |     |     |     |     |     |     |     |     | X   | X   |     |     |     |
| sand reeker |     |     |     |     |     |     |     | X   |     |     | X   |     |     |     |     |
| windbag |     | X   |     |     |     |     |     |     |     | X   |     |     |     | X   | X   |
| fjord fungus | X   |     | X   |     | X   |     |     |     | X   |     |     |     |     |     |     |
| mandrake |     |     |     |     |     | X   |     | X   |     |     |     |     | X   |     |     |
| rock weed |     |     |     |     |     |     |     |     |     | X   |     |     | X   |     |     |
| gapgrowth |     |     |     |     |     | X   |     |     |     |     |     | X   |     |     | X   |
| cave lichen |     |     |     |     | X   |     |     |     | X   |     |     |     |     |     |     |
| ice begonia |     |     |     |     |     |     |     |     |     |     |     | X   |     |     | X   |
| white hemlock |     |     |     |     |     |     | X   | X   |     |     |     |     |     |     |     |
| snowcrystal petal |     |     |     |     |     |     |     |     |     |     |     |     | X   |     |     |

|     |     |
| --- | --- |
| Weiterlesen: | [plantes] |

[plantes]: ./herbs.md "Plantes"

<!-- From [https://wiki.eressea.de/index.php?title=Tränke/fr&oldid=16931] -->

[Alchemy]: ./skills-list.md "Liste des compétences"
[`MAKE`]: ./cmd-make.md "MACHE"
[SHOW]: ./cmd-show.md "SHOW"
[`USE`]: ./cmd-use.md "USE"
