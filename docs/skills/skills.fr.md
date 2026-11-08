---
# cSpell:locale fr
alias: competences
---

# Compétences

Les compétences sont un élément essentiel qui définit une [unité][cmd-unit-fr] dans Eressea.  
Toutes les personnes d'une unité ont les mêmes compétences. Elles doivent d'abord les apprendre.  
Pour être précis, avec l'ordre [`LEARN`][cmd-learn-fr], une unité peut faire une tentative par tour pour gagner un nouveau niveau.

## Progression par usage

Certaines compétences s'améliorent également en les utilisant. Si l'unité utilise la compétence, il y a 1/3 de chances qu'elle gagne de l'expérience (et donc 2/3 de chances qu'elle n'en gagne pas).  
Ainsi, en exerçant une compétence, une unité progresse statistiquement à environ 1/3 de la vitesse d'apprentissage (par `LEARN`).

Les compétences **qui ne s'améliorent pas** en les **exerçant** sont les suivantes :

- toutes les compétences d'armes
- l'[endurance][skill-endurance-fr-id]{title="Endurance"}
- la perception
- la tactique
- la taxation

Dans la plupart des cas, la valeur de compétence affichée dans le rapport est celle à utiliser.  
Elle inclut les bonus des peuples, régionaux et des éléments comme la famine ou la magie, qui modifient la valeur de la compétence.  
Mais parfois, la valeur de compétence "brute" sans bonus est également nécessaire, notamment pour calculer les coûts d'apprentissage de la magie et les temps d'apprentissage.

## Apprendre des compétences

Atteindre un nouveau niveau de compétence devient de plus en plus difficile à chaque niveau.  
En moyenne, la progression vers un nouveau niveau de compétence avec la commande [`LEARN`][cmd-learn-fr] prend environ un nombre de semaines égal au niveau de compétence visé, sans tenir compte des modifications apportées par le [peuple][peuples] ou le terrain.  
Le temps d'apprentissage minimal est d'1 semaine. La durée maximale d'apprentissage ne dépasse pas (2 x nouveau niveau − 1).  
Les valeurs extrêmes sont moins fréquentes que la valeur moyenne. Ainsi, passer du niveau 3 au niveau 4 peut prendre jusqu'à 7 semaines, mais prendra en moyenne 4 semaines.  
Il faut en moyenne deux semaines à un [nain][nains]{title="Dwarves"} pour passer du niveau 3 au niveau 4 dans la compétence Mining, car les nains ont un modificateur de +2 pour cette compétence (4-2=2).

**Exemples :**

Passer du niveau 3 au niveau 4 prend en moyenne 4 semaines, mais parfois aussi peu qu'une semaine et parfois jusqu'à 7 semaines.  
Une [unité de nains][nains]{title="Dwarves"} avec le minage 3 dans le rapport est en fait de niveau 1 "brut", puisque les nains ont un modificateur de +2 sur le minage.  
Il faut en moyenne deux semaines pour progresser dans la compétence d'extraction minière du niveau 3 au niveau 4.

Pour réduire le temps nécessaire à l'apprentissage d'une compétence, une seconde unité, plus expérimentée que la première, peut [enseigner][cmd-teach-fr] la compétence.  
Cette unité doit avoir au moins 2 niveaux de plus que l'élève dans la compétence.  
L'unité élève apprend deux fois plus vite que si elle apprenait sans professeur. L'unité enseignante, elle, n'en tire aucune expérience.  
Un apprentissage dans une [académie][academie]{title="Academy"} permet d'apprendre plus rapidement.

Un enseignant peut avoir jusqu'à 10 élèves. Une unité enseignante peut contenir autant de personnes que souhaité.  
Si l'"unité d'élèves" a trop de personnes, cela sera pris en compte dans les chances d'apprentissage.  
Une unité peut enseigner à plusieurs unités, de même qu'une unité d'élèves peut apprendre de plusieurs unités de professeurs, chaque élève ne pouvant bien sûr tirer bénéfice que d'un seul enseignement.

**Exemple :**

```text
Unit l1; 1 Person, Endurance 3
TEACH s1
Unit l2; 1 Person, Melee 3, Endurance 3
TEACH s1 s2
Unit s1; 15 Persons, Endurance 1
LEARN Endurance
Unit s2; 10 Persons, Melee 1
LEARN Melee
```

Résultat :  
l'unité l1 forme 10 personnes de l'unité s1 en endurance.  
L'unité l2 enseigne l'endurance aux 5 personnes restantes de s1,  et enseigne les armes coupantes (mêlée) aux 5 personnes de l'unité s2.  
L'unité s1 est enseignée par l1 et l2 et apprend deux fois plus vite que la normale.  
L'unité s2 n'est enseignée qu'à moitié en endurance et n'apprend donc que 50 % plus vite.  

!!! warning "Attention"
    Si plusieurs unités de professeurs enseignent à plusieurs unités d'élèves dans différentes compétences ou niveaux de compétence, il est possible que certains élèves n'aient pas de professeur ou ne reçoivent pas le bon professeur.  
    Il n'est pas possible de faire autrement en raison de l'organisation interne d'Eressea.  
    Dans ce cas, vous devez créer des « relations claires » en restructurant les unités pédagogiques.  
    Avec l'ordre [`LEARN-AUTO`][cmd-learn-auto-fr], le serveur tente d'automatiser l'apprentissage et l'enseignement dans une région.  
    Cependant, comme cela est dû à une simple heuristique, il n’est pas garanti qu’une chaîne d’apprentissage optimale (à long terme) soit créée.  

[La magie][magie-fr-id], [l'alchimie][alchimie]{title="Alchemy"}, [l'herboristerie][herboristerie]{title="Herbalism"}, [l'espionnage][skill-espionnage-id]{title="Espionage"} et [la tactique][tactique] sont des compétences particulièrement difficiles à acquérir et coûteuses.  
Apprendre l'espionnage coûte 100 Silver par personne et par tour; 200 Silver par personne et par semaine pour l'alchimie, l'herboristerie et la tactique.  
Apprendre la magie coûte facilement plusieurs milliers de Silver à des niveaux élevés (voir ce [tableau][magie]).  
L'unité qui apprend une de ces compétences doit avoir en sa possession cette somme.  
Le fait que l'unité reçoive ou non un enseignement n'a aucune incidence sur le coût.  
Si l'unité est dans une [académie][academie]{title="Academy"}, le coût d'apprentissage des compétences payantes est doublé.  

Si l'unité en apprentissage ne dispose pas de suffisamment au moment du paiement, elle apprendra au prorata de la quantité de Silver dont elle dispose;  
par exemple si elle n'a que 500 Silver sur 550, ses chances d'apprendre diminueront d'environ 10 %.  

Dans de rares cas, une unité peut vouloir se débarrasser d'une compétence. Ceci est possible avec l'ordre [`FORGET`][cmd-forget-fr].

## Mélanger les compétences

Lorsque des personnes sont transférées ou recrutées dans une unité existante, les nouveaux niveaux de compétences sont calculés en fonction du nombre de semaines d'apprentissage que les deux unités ont eu.  
Il peut arriver que des semaines d'apprentissage soient "perdues" en raison des effets d'arrondi.  
Vous devriez donc éviter autant que possible de fusionner inutilement des unités.  

**Exemple :**

Une unité de deux personnes avec [mêlée][skill-melee-fr-id]{title="Melee"} T5 recrute un paysan.  
Les deux personnes ont chacune étudié environ 15 semaines (à savoir 1+2+3+4+5) avant de passer au niveau 5.  
Les paysans n'ont pas de compétence, on ajoute donc 0. La nouvelle unité a donc environ 30 semaines d'apprentissage.  
Cela correspond à 3 personnes avec mêlée T4 (1+2+3+4=10 semaines par personne).  
La nouvelle unité est donc de niveau 4.

Pour le calcul des semaines d'apprentissage, tout comme pour l'apprentissage, ce sont les valeurs de compétences "brutes" qui comptent, auxquelles sont d'abord soustraits tous les bonus et malus tels que les bonus raciaux.

Expérience de jeu (Solthar):

En fait, la question est plus compliquée.  
Cependant, vous pouvez ignorer cette étape si vous lisez ce guide pour la première fois.  
Chaque fois qu'une unité avance d'un niveau, un dé est lancé pour déterminer combien de semaines il lui faudra pour passer au niveau suivant.  
Cela donne une valeur comprise entre 1 et (2 x nouveau niveau − 1).  
Une unité peut donc avoir un niveau compris entre (6,1) -cette notation signifie niveau 6 et encore une semaine avant la promotion -et (6,13).  
Cette valeur est prise en compte lors du mélange.  
Par exemple, si vous mélangez une personne avec (5,6) et une personne avec (1,2) – qui correspondent toutes deux exactement à la moyenne – elles auront un total de 16 semaines d’apprentissage.  
Cependant, deux personnes avec (3,4) ne correspondent qu’à 12 semaines d’apprentissage.  
La différence de deux semaines par personne sera « créditée » à la nouvelle unité.  
Il a donc (3,2) - un peu mieux que la moyenne.  

Si vous mélangez (5,1) et (1,1), c'est-à-dire des personnes qui ont presque atteint le prochain niveau, vous obtiendrez même (4,4).  
Cependant, le mélange de (5,11) et (1,3) donne (3,5) comme nouvelle valeur.  
Il n’est donc pas possible de prédire avec précision la valeur des compétences d’une unité mixte.  
Seules une valeur minimale et maximale peut être spécifiée.

## Utilisation des compétences

Les compétences permettent aux unités de faire certaines choses.  

Parfois, c'est le niveau de compétence de l'unité qui rend possible une activité donnée.  
Parfois, le niveau de compétence total (nombre de personnes x niveau de compétence) de l'unité joue également un rôle.  

Les compétences peuvent être divisées en plusieurs groupes.

### Compétences de production

Il s'agit du plus grand groupe de compétences.  
Ces compétences permettent de fabriquer des objets, des bâtiments, des bateaux ou des routes.  
Les compétences de production sont les suivantes :

- [Alchimie][alchimie]{title="Alchemy"} (fabrication de potions)
- [Apprivoisement][apprivoisement]{title="Taming"}  (obtention de chevaux)
- [Construction navale][construction-navale]{title="Shipcraft"}
- [Construction de routes][construction-de-routes]{title="Roadwork"}
- [Extraction de pierres][extraction-de-pierres]{title="Quarrying"}
- [Extraction minière][extraction-miniere]{title="Mining"} (production de fer, de laen ou d'adamantium)
- [Fabrication d'armes][fabrication-darmes]{title="Weaponsmithing"}
- [Fabrication d'armures][fabrication-darmures]{title="Armoursmithing"}
- [Fabrication de chariots et de catapultes][fabrication-de-chariots]{title="Cartmaking"}
- [Herboristerie][herboristerie]{title="Herbalism"} (récolte de plantes)
- [Maçonnerie][maconnerie]{title="Masonry"}
- [Sylviculture][sylviculture]{title="Forestry"} (production de bois et de mallorn)

Plus d'information :

- [Production][production-fr-id]
- [L'alchimie][alchimie-id]

### Compétences de gain d'argent

Le [commerce][commerce]{title="Trade"}, la [taxation][skill-taxation-fr-id]{title="Taxation"}, et le [divertissement][skill-divertissement-id]{title="Entertainment"} permettent de gagner de l'argent (des silvers).

Plus d'information : [l'argent][argent].

### Dissimulation

[espionnage][skill-espionnage-id]{title="Espionage"}, [discrétion][skill-discretion-id]{title="Stealth"} et [perception][skill-perception-fr-id]{title="Perception"} sont centrés sur la dissimulation.

Plus d'information: [la discrétion][discretion].

### Compétences de déplacements

La [voile][voile]{title="Sailing"} et l'[équitation][equitation]{title="Riding"} sont des compétences expliquées dans le chapitre sur les [déplacements][deplacements].  

L'équitation est également abordée dans le chapitre des [combats][tableaux-relatifs-a-la-guerre].

### La magie

La [magie][magie-fr-id] est une compétence aux pouvoirs particulièrement puissants.

### Compétences de combat

Les compétences de maniement des armes sont les suivantes :

- [combat à l'arme d'hast][combat-a-larme-dhast]{title="Polearm"}
- [combat à mains nues][combat-a-mains-nues]{title="Unarmed combat"}
- [mêlée][skill-melee-fr-id]{title="Melee"} (combat à l'arme coupante)
- [tir à l'arc][tir-a-larc]{title="Bow"}
- [tir à l'arbalète][tir-a-larbalete]{title="Crossbow"}
- [tir à la catapulte][tir-a-la-catapulte]{title="Catapult"}

Les autres compétences essentielles au combat sont :

- [endurance][skill-endurance-fr-id]{title="Endurance"}
- [équitation][equitation]{title="Riding"}
- [tactique][tactique]{title="Tactics"}

Toutes ces compétences sont particulièrement importantes dans les [batailles][guerre], que ce soit contre d'autres factions ou des [monstres][monstres].

Poursuivre la lecture : [liste des compétences][liste-des-competences].

<!-- From [https://wiki.eressea.de/index.php?title=Talente/fr&oldid=16177] -->

[cmd-teach-fr]: [[cmd-teach-fr]]
[cmd-unit-fr]: [[cmd-unit-fr]]
[cmd-learn-fr]: [[cmd-learn-fr]]
[cmd-forget-fr]: [[cmd-forget-fr]]
[cmd-learn-auto-fr]: [[cmd-learn-auto-fr]]
