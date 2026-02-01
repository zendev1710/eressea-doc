---
# cSpell:locale fr
alias: types-de-terrain
---
# Types de terrain

<!-- TODO reorganize info. Some are partially duplicated in world.md -->

## Désert

<!-- cspell:disable -->
*Desert (EN), Wüste (DE).*
<!-- cspell:enable -->

Dans ce milieu hostile, les déplacements et le commerce sont par nature limités.  

Pour y construire des [[routes|routes]] et ainsi faciliter les déplacements, un [caravansérail] doit y être au préalable érigé et fonctionnel.  
Un caravansérail permet également d'y doubler le volume de commerce.  

Les plantes qui poussent dans le désert sont le [tamaris], le [peyote], et la [pourriture de sable].  

## Forêt

<!-- cspell:disable -->
*Forest (EN), Wald (DE).*
<!-- cspell:enable -->

Les plantes qui poussent dans les forêts sont l'[amour d'Elfes], le [champignon cobalt], l'[œil de chouette], le [lierre d'araignée], la [racine plate] et la [témérité piquante].  
Ces mêmes plantes poussent dans les plaines.  

## Glacier

<!-- cspell:disable -->
*Glacier (EN), Gletscher (DE).*
<!-- cspell:enable -->

Les plantes qui poussent sur les glaciers sont le [bégonia des glaces], le [pétale de cristal de neige] et le [tsuga blanc].  

## Haut-plateau

<!-- cspell:disable -->
*Highland (EN), Hochland (DE).*
<!-- cspell:enable -->

Les plantes qui poussent sur les hauts-plateaux sont le [champignon des fjords], la [mandragore] et la [gousse].  

## Marais

<!-- cspell:disable -->
*Swamp (EN), Sumpf (DE).*
<!-- cspell:enable -->

Les plantes qui poussent dans les marais sont l'[herbe de clairon], la [morille] et la [racine de nœud].  

## Montagne

<!-- cspell:disable -->
*Mountain (EN), Berge (DE).*
<!-- cspell:enable -->

Les plantes qui poussent dans les montagnes sont la [cire fissurée], l'[herbe de roche] et le [lichen des cavernes].  

## Plaine

<!-- cspell:disable -->
*Plain (EN), Ebene (DE).*
<!-- cspell:enable -->

Les plantes qui poussent dans les plaines sont l'[amour d'Elfes], le [champignon cobalt], l'[œil de chouette], le [lierre d'araignée], la [racine plate] et la [témérité piquante].  
Ces mêmes plantes poussent dans les forêts.  

## Volcan

<!-- cspell:disable -->
*Volcano (EN), Vulkan (DE).*
<!-- cspell:enable -->

!!! note "Note"
    Aucune plante ne pousse sur les volcans.

## Terrains - Synthèse

| Terrain        | max. travailleurs | min. travailleurs [^1] | max. arbres | Pierres pour routes |
|----------------|------------------:|-----------------------:|------------:|--------------------:|
| [Glacier]      |               100 |                     10 |          13 |                 250 |
| [Désert]       |               500 |                     50 |          63 |                 100 |
| [Volcan]       |               500 |                     50 |          63 |                 250 |
| [Montagne]     |             1 000 |                    100 |         125 |                 250 |
| [Marais]       |             2 000 |                    200 |         250 |                  75 |
| [Haut-plateau] |             4 000 |                    200 |         500 |                 100 |
| [Forêt][^2]    |            10 000 |                    200 |       1 250 |                  50 |
| [Plaine][^2]   |            10 000 |                    200 |       1 250 |                  50 |

Le nombre d'emplois disponibles varie d'une région à l'autre.  
Chaque paysan prend un emploi, chaque pousse d'arbre en prend 4, et chaque arbre en prend 8.  

Sous "max. arbres" est indiqué le nombre d'arbres/de pousses qui prendraient toute la place pour les "agriculteurs".  
Mais même la forêt la plus dense produit suffisamment de fruits, de racines ou de champignons pour que quelques-uns puissent en vivre.  
10 % des emplois d'une région, mais pas plus de 200, ne sont donc jamais bloqués par des arbres ou des pousses.  
Si le nombre d'emplois disponibles est dépassé, les unités de joueurs ne peuvent plus travailler dans cette région.

Dans les glaciers, les marais et les déserts, la construction de routes n'est possible que si des [[batiments-speciaux]] s'y trouvent.  

[^1]: quelque soit le nombre d'arbres.
[^2]: à partir d'un nombre total de **600** arbres, pousses (jeunes arbres) incluses, une plaine est considérée comme une forêt.

<!-- From [https://wiki.eressea.de/index.php?title=Geländearten/fr&oldid=9104] -->

[caravansérail]: ./buildings-others.md#caravanserail "Caravanserai"

[Désert]: ./terrains.md#desert "Desert"
[Forêt]: ./terrains.md#foret "Forest"
[Glacier]: ./terrains.md#glacier "Glacie
[Haut-plateau]: ./terrains.md#haut-plate
[Marais]: ./terrains.md#marais "Swamp"
[Montagne]: ./terrains.md#montagne "Moun
[Plaine]: ./terrains.md#plaine "Plain"
[Volcan]: ./terrains.md#volcan "Volcano"

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
