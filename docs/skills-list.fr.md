---
# cSpell:locale fr
alias: liste-des-competences
---

# Liste des compétences

Les compétence s'acquièrent progressivement avec l'ordre [`LEARN`][cmd-learn-fr].  

Elles peuvent être acquises plus rapidement à l'aide d'un [maître enseignant][cmd-teach-fr]{title="TEACH"}.  

Une unité peut apprendre une ou plusieurs des compétences décrites ci-dessous, à l'exception du [combat à mains nues][skill-combat-a-mains-nues-id]{title="Unarmed combat"}.

[](){ #skill-alchimie-id }

## [Alchimie][alchimie-id]

<!-- cspell:disable -->
*Alchemy (EN), Alchemie (DE)*.
<!-- cspell:enable -->

Cette compétence permet de concocter des [potions][potions-fr-id] à partir de [plantes][plantes]{title="Herbs"}.  

L'apprentissage de l'alchimie coûte 200 silver par tour et par personne.  

!!! note "Important"
    Une [faction][faction] ne peut compter que **3 alchimistes** au plus.

Plus d'information :

- Chapitre dédié : [l'alchimie][alchimie]
- Ordre [`MAKE`][cmd-make-fr]
- Ordre [`USE`][cmd-use-fr]

## Apprivoisement

<!-- cspell:disable -->
*Taming (EN), Pferdedressur (DE)*.
<!-- cspell:enable -->

Cette compétence permet d'obtenir des [chevaux][chevaux]{title="Horses"}.  

On peut l'utiliser de deux façons.  

L'ordre [`MAKE HORSE`][cmd-make-fr] permet de capturer des chevaux présents dans la région, à raison d'un cheval par personne et par niveau.  
Bien sûr, il n'est possible de capturer qu'au maximum le nombre de chevaux présents dans la région.  

L'ordre [`GROW HORSES`][cmd-grow-fr], donné par une unité se trouvant dans un [haras][haras]{title="Stable"}, permet la reproduction de chevaux.  

## Combat à l'arme d'hast

<!-- cspell:disable -->
*Polearm (EN), Stangenwaffen (DE)*.
<!-- cspell:enable -->

Cette compétence permet de se battre avec une [arme d'hast][armes-dhast].  

Une unité ayant acquis cette compétence et équipée d'arme(s) d'hast peut [collecter les impôts][cmd-tax-fr], à condition d'avoir également acquis la compétence de [taxation][skill-taxation-fr-id].  

[](){ #skill-combat-a-mains-nues-id }

## Combat à mains nues

<!-- cspell:disable -->
*Unarmed combat (EN), Waffenloser Kampf (DE)*.
<!-- cspell:enable -->

Cette compétence **ne peut être acquise par aucune unité jouée**.  

Seuls les monstres et autres peuples spéciaux ont cette compétence de combat à main nue (sans armes).

## Commerce

<!-- cspell:disable -->
*Trade (EN), Handeln (DE)*.
<!-- cspell:enable -->

Cette compétence permet d'acheter et de vendre des [biens de luxe][biens-de-luxe], dans les **régions comportant un [château][chateaux]{title="Castle"}**.  

10 biens de luxe peuvent être échangés par personne, niveau de compétence et tour.  

Plus d'information :

- Chapitre dédié : [le commerce][le-commerce]
- Ordre [`BUY`][cmd-buy-fr]
- Ordre [`SELL`][cmd-sell-fr]

## Construction de routes

<!-- cspell:disable -->
*Roadwork (EN), Straßenbau (DE)*.
<!-- cspell:enable -->

Cette compétence permet de construire des [routes][routes-id] avec des [pierres][pierre].  

Une pierre peut être posée par personne, par niveau de compétence et par tour.

[](){ #skill-construction-navale-id }

## Construction navale

<!-- cspell:disable -->
*Shipcraft (EN), Schiffbau (DE)*.
<!-- cspell:enable -->

Cette compétence permet de construire et de réparer un [nateau][bateaux-id] en [bois][bois].

[](){ #skill-discretion-id }

## Discrétion

<!-- cspell:disable -->
*Stealth (EN), Tarnung (DE)*.
<!-- cspell:enable -->

Cette compétence augmente la furtivité d'une unité.  

Une unité ayant acquis cette compétence est visible uniquement pour celles ayant un niveau de [perception][skill-perception-fr-id]{title="Perception"} supérieur ou égal à son niveau de discrétion.  
Elle n'est pas visible des autres unités.  

Une unité dissimulée grâce à sa discrétion peut aussi [voler][vol-de-silver] ou déjouer la [vigilance][cmd-guard-fr] des gardes de région.  

Plus d'information :  [compétence de discrétion en détail][discretion-id].  

[](){ #skill-divertissement-id }

## Divertissement

<!-- cspell:disable -->
*Entertainment (EN), Unterhaltung (DE)*.
<!-- cspell:enable -->

Capacité à divertir la population.  

Si les paysans ont suffisamment d'argent, il est possible de gagner 20 Silver par personne, par niveau de compétence et par tour.

[](){ #skill-endurance-fr-id }

## Endurance

<!-- cspell:disable -->
*Endurance (EN), Ausdauer (DE)*.
<!-- cspell:enable -->

Cette capacité permet à une unité d'encaisser plus de points de dégâts au combat et de mieux résister à la [famine][famine]{title="Starvation"}.  

En pratique, une unité [bénéficie d'un bonus de PV][table-endurance-fr-id], dont la valeur est fonction de son **niveau en endurance** et de **son peuple**.  

## Équitation

<!-- cspell:disable -->
*Riding (EN), Reiten (DE)*.
<!-- cspell:enable -->

Aptitude à monter à cheval.  

Une personne équipée d'un [cheval][cheval]{title="Horse"} :

- se déplace plus **rapidement** dès qu'elle est **T1**
- bénéficie d'un **bonus de cavalerie au combat** dès qu'elle est **T2**

Par personne et par niveau de compétence, il est possible :

- de mener `(4 X Niveau) + 1` chevaux sur une région (sur 2 régions avec une route praticable)
- de monter `2 X Niveau` chevaux sur 2 régions (sur 3 régions avec une route praticable)

[](){ #skill-espionnage-id }

## Espionnage

<!-- cspell:disable -->
*Espionage (EN), Spionage (DE)*.
<!-- cspell:enable -->

Nécessaire pour utiliser l'ordre [`SPY`][cmd-spy-fr] et ainsi obtenir des informations secrètes sur les unités des autres factions (compétences, véritable appartenance à une faction...).  

Apprendre l'espionnage coûte 100 Silver par personne pour chaque tentative d'apprentissage.

## Extraction de pierres

<!-- cspell:disable -->
*Quarrying (EN), Steinbau (DE)*.
<!-- cspell:enable -->

Capacité à extraire des pierres à partir d'une carrière.  

Une pierre peut être extraite par personne, par niveau de compétence et par tour.

À partir du niveau **3**, la compétence permet de produire des grosses pierres utilisées comme projectiles (munitions) de catapulte.

Les gisements à exploiter sont limités par niveau (voir [ressources minières][ressources-minieres]) : on voit uniquement le nombre de pierres qui se trouvent dans la couche supérieure.  
S'il n'y a pas de pierres dans la couche (niveau de compétence X 2), on ne voit rien.

## Extraction minière

<!-- cspell:disable -->
*Mining (EN), Bergbau (DE)*.
<!-- cspell:enable -->

Cette compétence permet d'extraire du [fer][fer]{title="Iron"}, du [laen][laen-fr-id]{title="Laen"} ou de l'[adamantium][adamantium-fr-id]{title="Adamantium"}.  
Il est possible d'extraire **un fer par personne, par niveau de compétence et par tour**.  

Notez que les [gisements sont limités][ressources-minieres] par niveau.
On ne voit que la quantité de fer qui se trouve sur la couche supérieure.
Pour la prospection, on ne voit pas plus que la couche (niveau en extraction minière X 2). Si la couche est plus profonde on ne verra rien.

!!! note
    L'extraction de [laen][laen-fr-id]{title="Laen"} nécessite une [mine][mine-fr-id]{title="Mine"} et une compétence de **niveau 7**.  
    L'extraction d'[adamantium][adamantium-fr-id] nécessite une [mine][mine-fr-id]{title="Mine"} et une compétence de **niveau 7**.

## Fabrication d'armes

<!-- cspell:disable -->
*Weaponsmithing (EN), Waffenbau (DE)*.
<!-- cspell:enable -->

Permet la [fabrication d'armes][production-d-armes-id] en [bois][bois] et en [métal][fer].

## Fabrication d'armures

<!-- cspell:disable -->
*Armoursmithing (EN), Rüstungsbau (DE)*.
<!-- cspell:enable -->

Permet la [fabrication d'armures][production-d-armures-id] en [fer][fer], en [laen][laen-fr-id]{title="Laen"} ou en [adamantium][adamantium-fr-id].

## Fabrication de chariots

<!-- cspell:disable -->
*Cartmaking (EN), Wagenbau (DE)*.
<!-- cspell:enable -->

Permet la fabrication de chariots et de catapultes avec du bois.

5 bois sont nécessaires pour fabriquer un chariot.  
Une unité peut fabriquer un chariot par personne et niveau de compétence.  

À partir du niveua **5**, il faudra 10 bois pour fabriquer une catapulte.

## Herboristerie

<!-- cspell:disable -->
*Herbalism (EN), Kräuterkunde (DE)*.
<!-- cspell:enable -->

Permet de récolter des [plantes][plantes-id] pour concocter des [potions][alchimie].  

Le coût d'apprentissage est de **200 silver par semaine et par personne**.

À un niveau élevé on peut aussi utiliser les ordres [`RESEARCH HERBS`][cmd-research-fr] et [`MAKE SEEDS`][cmd-make-fr] (voir [Production][production-fr-id]) et [`PLANT`][cmd-plant-fr].  
Même avec un niveau élevé on peut ne trouver que peu ou pas de plantes.

## Maçonnerie

<!-- cspell:disable -->
*Masonry (EN), Burgenbau (DE)*.
<!-- cspell:enable -->

Permet de construire des [bâtiments spéciaux][batiments-speciaux] et des [châteaux][chateaux]{title="Castle"}.

## [Magie][magie-fr-id]

<!-- cspell:disable -->
*Magic (EN), Magie (DE)*.
<!-- cspell:enable -->

Permet de lancer des sorts de combat et d'autres types de sorts.  

L'apprentissage de la magie [coûte de l'argent][magie] par personne et par tour, en fonction du niveau.

[](){ #skill-melee-fr-id }

## Mêlée

<!-- cspell:disable -->
*Melee (EN), Hiebwaffen (DE)*.
<!-- cspell:enable -->

Capacité à se battre avec une arme de mêlée (sword, claymore, axe, laensword).  

Une unité ayant acquis cette compétence et équipée d'arme(s) de mêlée peut [collecter les impôts][cmd-tax-fr], à condition d'avoir également acquis la compétence de [taxation][skill-taxation-fr-id].  

[](){ #skill-perception-fr-id }

## Perception

<!-- cspell:disable -->
*Perception (EN), Wahrnehmung (DE)*.
<!-- cspell:enable -->

Capacité à détecter les unités [dissimulées][discretion-id].  

Cette compétence permet également d'éviter le [vol][vol-de-silver].  

## Sylviculture

<!-- cspell:disable -->
*Forestry (EN), Holzfällen (DE)*.
<!-- cspell:enable -->

Capacité à abattre des arbres et des mallorns pour faire du [bois][bois]{title="Wood"}.  

!!! note "Note"
    Veillez à bien gérer les [ressources forestières][ressources-forestieres] des régions que vous [gardez][cmd-guard-fr].

## [Tactique][tactique]

<!-- cspell:disable -->
*Tactics (EN), Taktik (DE)*.
<!-- cspell:enable -->

Cette compétence permet de former un [tacticien][tacticien].  

Lors d'un combat, le camp avec le meilleur tacticien [bénéficie d'attaques supplémentaires][tour-du-tacticien].  

L'apprentissage de la tactique coûte 200 silver par tour et par personne.  

!!! warning "Important"
    Un expert tacticien peut modifier le cours et l'issue d’une bataille.  

[](){ #skill-taxation-fr-id }

## Taxation

<!-- cspell:disable -->
*Taxation (EN), Steuereintreiben (DE)*.
<!-- cspell:enable -->

Cette compétence permet de collecter les impôts auprès des paysans.  

Une unité peut collecter 20 silver auprès des paysans, par niveau de compétence et par personne **[armée et prête au combat][arme-et-pret-au-combat]**.  

Cette compétence n'augmente pas en l'utilisant, pas plus que la compétence d'arme correspondante.  

## Tir à l'arbalète

<!-- cspell:disable -->
*Crossbow (EN), Armbrustschießen (DE)*.
<!-- cspell:enable -->

Avec une arbalète : se battre.  
Avec en plus la compétence taxation : collecter les impôts (TAX).

## Tir à l'arc

<!-- cspell:disable -->
*Bow (EN), Bogenschießen (DE)*.
<!-- cspell:enable -->

Avec un bow (arc) : se battre. Avec en plus la compétence taxation : collecter les impôts (TAX).

## Tir à la catapulte

<!-- cspell:disable -->
*Catapult (EN), Katapultbedienung (DE)*.
<!-- cspell:enable -->

Avec une catapulte et des munitions : se battre. On ne peut pas taxer avec.

## Voile

<!-- cspell:disable -->
*Sailing (EN), Segeln (DE)*.
<!-- cspell:enable -->

Capacité à naviguer.  

Avec un bateau : permet de naviguer.  

Toutes les unités sur le bateau ayant acquis cette compétence comptent dans l'équipage.

<!-- From [https://wiki.eressea.de/index.php?title=Liste\_der\_Talente/fr&oldid=15211] -->

[cmd-buy-fr]: [[cmd-buy-fr]]
[cmd-grow-fr]: [[cmd-grow-fr]]
[cmd-guard-fr]: [[cmd-guard-fr]]
[cmd-make-fr]: [[cmd-make-fr]]
[cmd-research-fr]: [[cmd-research-fr]]
[cmd-tax-fr]: [[cmd-tax-fr]]
[cmd-teach-fr]: [[cmd-teach-fr]]
[cmd-learn-fr]: [[cmd-learn-fr]]
[cmd-use-fr]: [[cmd-use-fr]]
[cmd-sell-fr]: [[cmd-sell-fr]]
[cmd-plant-fr]: [[cmd-plant-fr]]
[cmd-spy-fr]: [[cmd-spy-fr]]
