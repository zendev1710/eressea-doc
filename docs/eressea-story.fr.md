---
# cSpell:locale fr
alias: histoire-d-eressea
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# Eressea depuis ses débuts

Selon [Wikipedia], Eressea a été lancé le 27 août 1996.
Il a été développé en tant que spin-off d'[[atlantis]].
La popularité était sujette à des fluctuations relativement fortes.
Le record était de plus de 2 000 factions début 2002.
Fin 2005, il y avait pour la première fois moins de 1 000 factions.
Fin 2008, les nouvelles inscriptions ont été temporairement fermées.
À cette époque, il y avait moins de 700 factions.
Mais le jeu continue.

## Développeurs

- Russel Wallace
  Développeur d'Atlantis 1.0
- Alex Schröder
  Développeur de l'Atlantide version allemande.
  Le code Atlantis 1.0 et celui de la version allemande sont disponibles gratuitement, contrairement au code Eressea basé sur celui-ci.
- Christian Schlittchen ([Corwin][corwin])
  a développé Eressea et fait tourner le jeu pendant longtemps (jusqu'au tour 289, vers mi-2002).
- Katja Zedel ([Katze (Designerin)][katja-zedel-fr-id])
  était la développeuse et directrice du jeu d'Eressea avec Corwin.
  Le plus grand projet de Katja a été le développement d'une nouvelle magie.
- [Enno Rehling][enno-fr-id]
  est là depuis le tour 39 et a pris en charge le développement et la gestion du jeu après le départ des deux autres directeurs du jeu.
- Henning Peters ([Faroul][faroul-fr-id])
  Développeur, entre autres, du vérificateur d'ordres [[echeck]].
- Benjamin Bärmann, Ingo Wilken
  Co-développeur dans les premières années, notamment sur l'alchimie

## Évolution des règles

De nombreux changements mineurs et majeurs ont été apportés aux règles au fil du temps, généralement pour améliorer l'équilibre du jeu.  
En voici une liste, loin d'être complète.

## Premier Âge

Un jour

- Les races sont introduites dans le jeu
- Seuls les humains peuvent désormais recevoir des migrants, les migrants des autres races sont convertis dans la race du propriétaire, tout en conservant leur niveau de compétence
- Elves lose their +1 bonuses in entertainment and lumbering

27.08.1996

- La première évaluation

04.12.1998

- L'ordre `FIND` disparaît (que faisait-il ?)
- L'option `ADDRESSES` est introduite dans le jeu

05.12.1998

- La soumission d'ordres partiels est désormais possible sans supprimer les ordres précédemment reçus pour d'autres unités

13.12.1998

- Les bateaux à la dérive en mer sans équipage suffisant ont 33 % de chances de couler
- Les monuments sans dirigeant s’effondrent lentement

18.12.1998

- Les combattants reçoivent 10 jours d'apprentissage en [endurance][skill-endurance-fr-id] en plus des jours d'apprentissage de leur compétence d'arme respective, et 10 jours d'équitation s'ils sont montés et impliqués dans le combat

08.01.1999

- La compétence `SCHIFFSBAU` est renommée en `SCHIFFBAU` (en langue allemande)

14.01.1999

- Le format du rapport informatique (CR) évolue

23.02.1999

- Les unités peuvent désormais être contactées directement, même si elles sont déguisées en faction et que leur adresse ne peut donc pas être vue.

28.02.1999

- L'ordre `ADDRESS` est aboli et sera ensuite remplacé par les ordres `EMAIL`et`BANNER`

08.04.1999

- L'ordre `OPINION` est introduit pour pouvoir saisir des enquêtes et des opinions directement sous forme d'ordre

27.04.1999

- Enno crée la base d'un grand désespoir 9 ans plus tard.
  Les unités déguisées en faction qui participent aux batailles sont désormais affichées comme une armée distincte.
  Lors du dépannage de grandes batailles, y compris celles impliquant des groupes (qui n'existent pas encore au moment du changement), ce changement rend la compréhension presque impossible.

09.04.1999

- Si une unité a une valeur de compétence supérieure à celle de son adversaire, les dégâts qu'elle inflige en cas de coup augmentent de la différence de compétence

30.04.1999

- Une limite unitaire est introduite; à partir de 2000, il sera réduit de 200 chaque mois jusqu'à atteindre 1 000.
- Au moment de l'activation de la fonctionnalité, 9 factions dépassent la limite

09.05.1999

- L'entrée dans les bâtiments nécessite l'ordre `HELP GUARD` ou `CONTACT`, mais désormais pas `HELP GIVE`

17.05.1999

- La potion de créativité double la capacité des alchimistes

31.05.1999

- `DELIVER` et `GIVE` peuvent maintenant utiliser le paramètre `EVERYTHING`

06.06.1999

- Les champs carrés existants sont remplacés par des champs hexadécimaux, même si, lors d'une enquête auprès des joueurs, la majorité s'y opposait
  Ce changement suscite beaucoup de colère parmi les joueurs.
  Aujourd’hui, cependant, presque personne ne doute de la justesse de ce changement, qui signifie que chaque région a 6 régions voisines au lieu de 4.
  Les sentiers deviennent également plus courts car on peut désormais marcher en diagonale.
  Cela signifie qu’il se passe beaucoup de choses en termes de portée.
- Les chevaux ne doublent plus leur déplaement, mais donnent à la place un +1 à la portée.
  Cela signifie qu'un passager sur route ne parcourt plus 4 régions, mais seulement 3 régions.
- Tous les bateaux perdent un point de portée
- Le bonus des Aquariens sur la vitesse du bateau est réduit de moitié à +1
- Les bateaux ne peuvent partir que dans la direction d'où ils viennent et dans les deux directions voisines, sauf s'il existe un port allié dans la région
- Les bateaux peuvent désormais subir des dégâts et ne couleront plus simplement s'ils manquent d'équipage
- Les bateaux endommagés perdent de leur capacité et éventuellement de leur vitesse
- Les salaires des non-orques sont réduits au niveau actuel (salaire du fermier -1 ?)

06.06.1999

- L'ordre `ROUTE` est modifié et le paramètre `BREAK` enrichi

12.09.1999

- Les identifiants d'unité sont convertis en identifiants Base36 à quatre chiffres
- L'ordre `NUMBER [wish ID]` est introduit dans le jeu
- Le paramètre `PEASANTS` est éliminé et remplacé par `0` parce que `GIB BAUERN` pouvait être confondu avec l'identifiant en Base36 `baue`

19.12.1999

- Le Père Noël distribue des cadeaux pour la première fois

16.01.2000

- Tous les migrants humains dotés de compétences coûteuses deviennent des humains, ce changement n'est en fait qu'une correction de bug

13.01.2000

- `OPTION BZIP2` est introduit pour réduire la taille des rapports envoyés

01.02.2000

- La carte Merian (une représentation cartographique ASCII du monde connu faisant partie du rapport) est supprimée car elle est rarement utilisée

20.02.2000

- `FOLLOW` n'est un ordre long que si l'unité bouge réellement

28.02.2000

- Vous ne gagnez plus d'expérience au combat. Ce changement est le résultat d'abus massifs

12.03.2000

- Seules les unités armées capables de manier l'arme peuvent garder

## Deuxième Âge

« Nous écrivons la première semaine du mois des bénédictions des champs, dans la première année du Deuxième Âge. » (tour 184)  

Avec ces mots commence le 8 avril. 2000 le Deuxième Âge.  
Cela s’accompagne d’un grand nombre de changements de règles révolutionnaires, résumés sous le terme générique de réforme magique.  
Cependant, ce ne sont pas seulement des changements qui affectent la magie.  
La grande majorité de ces changements concerne les races et les règles de combat.  

### Début du 6ème Monde

<!--- TODO: clarify RdU -->
- L'unité de départ de chaque course reçoit désormais un cadeau de départ
  - Les Elfes reçoivent des bottes de fée
  - Les Nains reçoivent une hache, une cotte de mailles et 30 jours d'apprentissage des armes coupantes
  - Les Orcs obtiennent T4 dans toutes les compétences d'armes
  - Les Chats reçoivent un RdU
  - Les Gobelins reçoivent une unité de départ de 10 personnes et pas seulement une, ainsi qu'un RdU
  - Les Insectes reçoivent neuf potions de nest warming, suffisamment pour recruter pour un hiver
  - Les Aquariens reçoivent un bateau et 30 jours d'apprentissage de la voile
  - Les Humains obtiennent une fortification (à cette époque elle n'était composée que de 2 pierres)
  - Les halfelins reçoivent 1 chariot, 2 chevaux, 5 objets de luxe de chaque type et un cheval T1
  - Les trolls reçoivent 10 pierres et Perception T3
  - Les démons obtiennent une [endurance][skill-endurance-fr-id] T15
- Les Murs de Feu (*Firewall*) sont introduits en tant que nouveau type de région

### La "Réforme Magique" 08.04.2000 (Tour 184)

- L'école de magie jusqu'ici universelle Lirpa (le nom vient à l'origine d'un poisson d'avril, mais après l'introduction des nouvelles Écoles de Mahie, il est rapidement devenu un nom commun pour « l'ancienne magie ») est remplacée par Draig, Illaun, Tybied, Gwyrrd et Cerddor.
  La Réforme implique un affaiblissement drastique de la magie, notamment en supprimant le sort Feu du Solzil, dont l'effet ne peut être comparé à aucun sort de combat connu aujourd'hui.
- `RESEARCH` selon la rumeur est supprimé. Un mage peut lancer tous les sorts de son école de magie d'un niveau inférieur ou égal à son niveau en magie.
- L'apprentissage de la magie devient nettement plus coûteux (50 + 50 * (1 + niveau) * Niveau / 2), surtout à des niveaux élevés. Auparavant, cela coûtait toujours 200 silver
- Au lieu d'un sort par tour, l'aura est introduit. Cela signifie qu'il est désormais possible de lancer plusieurs sorts en une semaine, avec une augmentation significative des coûts d'aura
- Seuls les mages du même domaine magique peuvent s'enseigner entre eux
- Lorsque vous apprenez la magie pour la première fois, vous devez choisir une école de magie avec `LEARN MAGIC "<Magic School>"`
- Les points de vie de toutes les unités sont doublés
- Les dégâts des armes normales sont augmentés d'environ 25 %.
  Les armes à plusieurs composants et celles fabriquées à partir de matières premières rares augmentent davantage les dégâts
- Les effets d'armure sont également augmentés d'environ 25 %
- Les combattants à distance ont une probabilité de 33 % de trouver une cible dans les première et deuxième lignes, et une probabilité de 67 % de trouver uniquement une cible dans la première rangée. Autrefois, seul la première ligne était attaquée
- Les monstres peuvent avoir plusieurs attaques par tour de combat, c'est-à-dire qu'ils peuvent lancer des sorts plusieurs fois ou attaquer de manière conventionnelle plusieurs fois
- En plus des sorts, les monstres peuvent également avoir d'autres attaques spéciales
- Le souffle du dragon ne peut plus être arrêté par des sorts d'antimagie, car les dragons ne représentent autrement que peu de menace
- Les coûts de recrutement des Elfes, des Démons et des Insectes sont augmentés à 130, 150 et 80
- Les unités affamées ne meurent plus avec 2/3 de chances mais subissent à la place des dégâts de famine; La même chose s'applique aux Démons qui ne peuvent pas manger d'agriculteurs
- Une seule herbe pousse par région, qui doit repousser et n'est plus disponible indéfiniment
- L'ordre `GROW HERBS` est introduit, alternativement l'ordre `GROW FLOWERS` fonctionne également
- L'université est rebaptisée Académie
- Der Kalender wird verändert. Statt in Monaten wird nun in Wochen gerechnet. Ein Jahr besteht aus 9 Monaten mit je 3 Wochen. Die Monate sind: Eiswind, Schneebann, Blütenregen, Mond der milden Winde, Sonnenfeuer, Feldsegen, Nebeltage, Sturmmond und Herdfeuer. Als Winter (für die Insektenrekrutierung wichtig) gelten Herdfeuer, Eiswind und Schneebann. In den Monaten Schneebann, Nebeltage und Sturmmond toben die Stürme auf See besonders heftig. Die Auswirkung von Stürmen wird verändert: ein Schiff, welches in einen Sturm gerät, steht jetzt vor größeren Problemen als bisher.
- Les ordres `DELIVER`, `RESERVE` et `//` sont désormais exécutés jusqu'à ce que des ordres contraires soient reçus pour une unité. Par exemple, si le joueur provoque un NMR, ces ordres seront toujours exécutés
- Le sang de paysans affecte 100 démons dans une région, et non plus une seule unité
- Les Familiers et l'Astral sont introduits dans le jeu

### "Réforme des matières premières" - Date et tour inconnus

La Réforme des matières premières, certainement le plus grand ensemble de changements de grande envergure après la Réforme Magique, est intervenu après l'arrêt du développement d'Eressea annoncé publiquement.  
Annoncé comme le tout dernier changement de règle (si vous pensez au fromage maintenant, c’est que vosu faites partie des vrais anciens d’Eressea 😃).  
Cependant, de nombreux autres changements, plus ou moins importants, ont prouvé par la suite le contraire.  

- Le lissage des agriculteurs est une tentative de répartir plus équitablement les matières premières importantes entre les agriculteurs.
  Les régions comptant de nombreux agriculteurs ont été supprimées et les régions qui en comptaient peu ont été comblées.
  Le nombre d'agriculteurs dans Eressea est resté le même. Non seulement les agriculteurs mais aussi les acteurs de la région ont joué un rôle important dans la distribution.
  Ainsi les gens qui avaient rassemblé 10 000 soldats dans une région centrale se retrouvaient, après lissage, dans une région vide d'agriculteurs, tout comme quand une armée d'invasion venait de débarquer sur une île.
  D’un autre côté, si vous aviez votre armée sur l’océan, tout allait bien.
  Le lissage des paysans a été annoncé dans un bref délai, mais la formule exacte ne l’a pas été.
  Ce changement provoque également beaucoup d'émoi parmi les joueurs, car beaucoup se sentent traités injustement (à cause de tous les paysans perdus)
- Parallèlement au lissage des paysans, les Orcs ont perdu leur taux de reproduction de 5 %
  Toutes les unités Orc existantes ont été converties en Snootlings; ils ne peuvent apprendre que des compétences pertinentes pour le combat jusqu'au niveau T7.
  Depuis le changement, les Orcs ne sont soustraits aux agriculteurs que 1 contre 2 lors du recrutement et remis aux agriculteurs 2 contre 1, les Snootlings n'apportent aucun paysan lorsqu'ils sont remis à 0 (est-ce vrai ?).
  La remise des anciens Orcs aux agriculteurs a eu lieu dans la séquence des ordres AVANT le lissage des paysans afin d'empêcher les Orcs de tricher pour obtenir un avantage.
  Bien sûr, de nombreux joueurs ont ignoré cette annonce et il y a eu ici aussi beaucoup de controverses.
  Les plaintes persistantes des joueurs concernant ces changements de règles sont généralement considérées comme la raison du départ de Corwin d'Eressea et de l'annonce du gel du développement, qui n'a jamais été respecté.
  Afin de maintenir un petit degré de dilution des compétences, ce qui était le cas avec l'augmentation des Orcs, à partir de ce moment, les Orcs n'apprennent tout simplement plus de compétence non liée au combat avec une probabilité de 5 %.
  Le bonus tactique de +1 pour les Orcs demeure malgré l'absence de dilution (à mon avis, un oubli majeur de la part de la direction du jeu, mais personne ne me l'a demandé à l'époque [Xolgrim])
- Les jours d'apprentissage sont remplacés par des probabilités d'apprentissage, l'édulcoration des compétences a désormais un effet nettement pire sur les compétences des unités (cette partie doit être écrite beaucoup plus en détail, mais je n'ai pas le temps pour [Xolgrim] pour le moment)
- La croissance du bois est complètement renversée et considérablement réduite.
  Au lieu d'une augmentation hebdomadaire des arbres de 5 % (soit au moins 30 bois dans une forêt de 600 mètres, avec une scierie 60 bois par semaine pouvant être abattus toute l'année), les arbres sont divisés en graines, jeunes arbres (pousses) et arbres.
  Les arbres jettent des graines au printemps et en été, celles-ci se transforment en jeunes arbres au printemps de l'année suivante, puis en arbres au printemps suivant.
- La pierre, le fer et le laen peuvent désormais apparaître dans tous les types de région, et non plus seulement dans les montagnes et les glaciers
- Les pierres doivent être extraites en couches; le niveau de la couche pouvant être extraite correspond au niveau de compétence en extraction de pierre de l'unité exploitant la carrière
  La première couche commence toujours au niveau 1 dans les montagnes et les glaciers, mais dans d'autres régions, elle peut être plus élevée.
  Avant, les pierres ne s'accumulaient pas, vous pouviez en extraire 100 par niveau dans une montagne (avec une carrière 200, les trolls, plus) par niveau, si vous ne le faisiez pas, les pierres étaient perdues.
  Il était donc plus intéressant de produire sans carrière que d'attendre qu'une soit construite.
- Le fer doit être extrait en couches; le niveau de la couche exploitable correspond à la compétence de l'unité mineur.
  En montagne, la première couche commence toujours au niveau 1, dans d'autres régions, cela peut être plus élevé.
  Le fer ne s'accumulait pas dans le passé, on pouvait en extraire 50 par niveau dans une montagne (avec des mines 100, les nains, plus).
  Si vous ne le faisiez pas, le fer s'accumulait dans la montagne et vous pouviez l'exploiter plus tard.
- Le laen doit être exploité par « couches », le niveau de la couche pouvant être exploitée correspond au niveau de compétence de l'unité minière.
  Le premier niveau commence toujours au niveau 7 en montagne, mais dans d'autres régions, il peut être plus élevé.
  Le laen ne s'accumulait pas dans le passé, une petite quantité soumise à de fortes fluctuations pouvait être extraite dans les montagnes.
  Si cela n’avait pas été fait, les laen se seraient accumulé et pourraient être exploités plus tard.
- `GUARD` empêche l'extraction de toutes les matières premières par des unités visibles

### Autres évolutions

Mars 2002 - BRAVO Screenfun

Le BRAVO Screenfun comporte un article de deux pages, qui a momentanément provoqué une ruée de très jeunes joueurs.  
Dans les première et troisième semaines suivant la sortie, 100 joueurs supplémentaires s'inscrivent, et 200 la deuxième semaine.  
Cela porte le nombre de joueurs à un niveau record de plus de 2 000.  
Cependant, la plupart des nouveaux joueurs, qualifiés de manière désobligeante de "BRAVO les enfants" par les joueurs expérimentés, ne restent dans le 10ème monde que quelques semaines.  

05.05.2002

<!-- TODO translated from english -->
- Guarding units prevent recruitment and the extraction of all limited resources from the region.
  In this context there is a small additional change: In the future, `GUARD` will no longer work if the person guarding does not see the producer.
  As a special case, for an empty `TEMP` unit, the creating unit is used as the visibility reference.
  In other words: What is crucial in this case is whether the unit that created the `TEMP` unit is seen.
- The available amount of resources is initially halved.
  This is an adjustment to the lower number of farmers and the expected significantly smaller faction sizes.
  For renewable resources, the growth rate has simply been reduced;
  for non-renewable resources, such as iron, fewer new resources are now added when a new 'mining stage' is reached.
- The proportion of farmers that can be recruited per turn is reduced from 20% to 5% of the farmer population.
  This makes the driver ant strategy less attractive.
- Catapults now only have 6 attacks instead of the previous 10.
  In addition, her skill penalty is now 4 instead of 1.
  Its weight is reduced from 120 to 100 lbs.
- Catapult ammunition can be produced (the change on June 2nd, 2002).
  Until the evaluation on June 2nd, all catapults still fire without ammunition, with the evaluation on June 2nd, catapults must be supplied with ammunition!

02.06.2002

- Les munitions pour catapulte sont introduites.
- Ceci peut être produit à partir de pierres en utilisant `MAKE CATAPULT AMMUNITION` par un constructeur de pierre de niveau 3 et pèse 10 unités de poids.
  Une unité de munition correspond à une volée de 6 coups.
- Les unités dans l'Astral coûtent une maintenance normale (auparavant, il n'y avait pas de maintenance dans l'Astral)

Date unknown.

- Les coordonnées ne sont plus absolues mais relatives à la région de départ du joueur.
  Chaque joueur commence désormais aux coordonnées (0,0)
- Les combats ne durent plus 10 rounds, mais seulement 5 rounds ou 6 avec le round du tacticien
- Les migrants ne peuvent plus acquérir de compétences coûteuses.
  Les unités existantes avec des compétences coûteuses ne peuvent pas être transférées
- Au bout d'un moment, les morts-vivants se transforment en super morts-vivants au taux de 10 pour 1.
  Un peu plus tard, le taux de conversion est fixé à 2 pour 1.
- Les tacticiens reçoivent désormais un bonus aléatoire à leur compétence
- Les coûts de recrutement des Nains ont augmenté de 90 à 110
- Les volcans sont introduits comme de nouveaux types de régions
- Le niveau maximum de compétence passera de 32 à 64 à mesure que les unités du vieux monde franchiront ce seuil pour la première fois.
  Les programmeurs ne s'attendaient pas à ce qu'une unité atteigne un jour un niveau aussi élevé.
- Les barrières glaciaires des anciens mondes (d’abord 1 à 3 puis 4 et 5) commencent à fondre.
  Les icebergs se libèrent des barrières glaciaires et flottent jusqu'à ce qu'ils fondent.
- Le nombre de morts-vivants sera ajusté en fonction de l'âge de la région
- Les unités qui se trouvent dans l'Astral consomment à nouveau 10 silver par semaine pour la maintenance

Octobre 2003 - Inscription clôturée

- Dans un premier temps, les nouvelles inscriptions à Eressea ne sont plus possibles pour les joueurs germanophones.
La raison pour laquelle Enno fait cela est qu'il s'amuse moins avec la communauté et travaille de plus en plus avec de nouveaux joueurs.
Peu de temps après, les inscriptions seront à nouveau possibles contre un don (pour une bonne cause).

11.7.2004 - Réforme des règles de combat (à partir du tour 390 environ)

- Les effets des différences de compétences sont divisés par deux (chance de toucher +-5 % au lieu de +-10 %, +1 point de dégâts au lieu de +2)
- Le coût de certaines armes puissantes sera augmenté.
  Les arcs elfiques coûtent désormais 2 mallorn au lieu de 1, les hallebardes 2 bois et 1 fer au lieu de 1 bois et 1 fer
- Les démons meurent désormais de faim comme les autres races (réduction des compétences et points de vie)
- La première ligne devient plus facile à déborder en combat.
  Cela se produit désormais selon un rapport de 3/1 (au lieu de 10/1 auparavant).
- La régénération des points de vie est ralentie
- Les Aquariens nageurs ne peuvent plus transporter d'autres races
- Les héros sont introduits dans le jeu.
  Une unité peut utiliser l'ordre `TRANSPORTATION` pour devenir une unité de héros.
  Les Héros infligent 10 fois plus de coups au combat, mais se comportent autrement normalement et ne se distinguent pas des unités normales du point de vue de l'ennemi.
  Le nombre de Héros qu'un groupe peut avoir est sévèrement limité et suit la même formule que les migrants (log10 (taille du groupe ÷ 50) × 20).

17.04.2005 - RESTART, poids, etc.

04.05.2005 -Le [[xontormia-express]] réapparaît après une pause sous un nouvel éditeur

05.06.2005 - Réforme de l'Astral (à partir du tour 430) etc.

- Les unités traversant un vortex du chaos perdent les 3/4 de leur santé
- Pierres, chevaux, chars et catapultes s'effondrent en poussière dans l'Astral
- Les monstres deviennent plus agressifs (en fait, il s'agit plutôt d'une correction de bug)
- Les bateaux peuvent à nouveau être surchargés

27.07.2005 - Mouvements après combat

- Les unités ne peuvent exécuter un ordre long après le combat que si chaque unité dans leur armée est autorisée à le faire

10.09.2005 - Double jeu, passation de faction

- Les joueurs des factions datant d'au moins 150 tours sont autorisés à créer une deuxième faction
- Les transferts de faction sont interdits.
  Il s'agit d'une réaction au fait qu'après la capitulation d'une faction, il y avait souvent des problèmes (en raison du jeu multiple ou de la prise de contrôle des factions dans une alliance par l'ennemi), ce qui impliquait du travail et de la frustration pour la direction du jeu.
- Les factions mourantes remettent leurs objets à des factions amies (`HELP ALL`)

13.09.2005 - Mouvements après combat

- Ordres longs possibles après de courts combats; `MOVE`, `ROUTE` etc. seulement si aucune des unités de la faction n'a un long combat

31.01.2007 -> 14.02.2007 - Règles de combat (tour 513)

- Les batailles sur les océans sont toujours courtes
- Les batailles dans d'autres régions sont courtes si une unité amie garde la région
- Les bateaux subissent des dégâts dès le 2ème tour de combat si au moins une personne à bord subit des dégâts
- Les unités en fuite restent dans la région et ne perdent aucun objet
- Les ynités avec `COMBAT FLEE` peuvent encore bouger
- Avant, les règles étaient : un combat était long s’il durait plus d’un tour (de combat).
  Les unités en fuite jetaient presque tous leurs objets et fuyaient vers une région voisine au hasard.

15.11.2007 - Unicode

- Les rapports sont convertis en encodage UTF-8 (anciennement ISO-8895-15)

11.02.2008 - Réserves dobjet et d'argent

- Les réserves dobjet et d'argent sont actives pour toutes les factions (auparavant, elles étaient facultatives)

02.03.2008 - Xontormia Express

- Après que les articles n'aient été publiés que de manière très irrégulière ces derniers mois, le dernier numéro de [[xontormia-express]] est en cours de publication.

28.04.2008 - Un identifiant est associé à chaque région

15.05.2008 - Magie et monstres

- Les sorts « Voile de confusion » et « Brouillard de confusion » seront supprimés sans remplacement
- La faction des monstres a pour identifiant (ii)

03.06.2008 - Portails du monde, adamantium, Astral

- Des îles avec des portails apparaissent soudainement dans le monde d'Eressea
- L'adamantium est introduit dans le jeu
- La vitesse de déplacement dans l'Astral n'est plus que de 1 (en fait, une correction de bug)

Décembre 2008 - Inscriptions (enfin) clôturées

- En raison de sérieux problèmes de serveur, les inscriptions seront fermées pour tout le monde

10.05.2009

- Le développement d'Eressea 1.5 est reporté.  À sa place vient le projet E3A.
  L'objectif est de développer rapidement une version jouable incluant des changements majeurs pouvant être implémentés avec le moins de codage possible.

02.12.2017 - La liste d'attente est à nouveau traitée pour la première fois

- L'inscription de nouveaux joueurs est suspendue à partir du 24 décembre 2017 (dernière semaine du mois de Tempête lune en An 33 du Deuxième Âge - 1056)
- Le 18ème monde émerge

## Eressea Le Troisième Àge

Eressea 2 est prévu depuis des années, mais Enno est désormais sûr que cette version d'Eressea sera un jeu web.  
Cependant, cela nécessite des changements fondamentaux dans le code et la jouabilité, qui doivent être testés au préalable dans Eressea 1.5.  

Afin d'apporter enfin quelque chose de nouveau aux joueurs et d'acquérir une première expérience avec une version simplifiée d'Eressea, le développement du titre provisoire Eressea 1.1 E2K9 débutera le 10 mai 2009.  
La version 1.5 n'a pas été choisie car la E1.1 est censée se passer de beaucoup d'efforts de programmation en supprimant un certain nombre d'ordres et en modifiant les paramètres existants.  
Il s’agissait à l’origine d’une étape intermédiaire plus petite vers E1.5.

En raison des changements massifs de règles, l'E1.1 démarrera dans un nouveau monde.  
Afin de contrecarrer les problèmes du jeu sans fin et de maintenir la charge de travail du jeu en cours aussi faible que possible, il ne sera pas possible de démarrer le jeu plus tard.  

Le programmeur de ce projet est [Enno][enno-fr-id], l'équipe de conception à ce stade n'est composée que de Xolgrim.  
Quelques jours plus tard, elle a été agrandie à sa taille actuelle avec Eon, qui avait remarqué Enno via une liste de diffusion, et Phygon, qui, comme Xolgrim, avait déjà travaillé sur divers projets inachevés d'Eressea.  

Le titre provisoire, qui est l'abréviation de « Eressea 2009 », illustre le peu de temps qui reste pour le développement, la conception, la programmation et les tests.
Le 24 juin 2009 est la première date de début prévue, mais celle-ci ne put être respectée pour plusieurs raisons.  
Avant toute autre raison, essentiellement privée, le nombre de nouvelles inscriptions est crucial.  
L’espoir était de plus de 50 joueurs, le rêve était d’environ 100.  
Pourtant, trois jours avant la date limite d'inscription, près de 400 joueurs s'étaient déjà inscrits.
Au moins les fonctionnalités de base de l’algorithme de suspension ont été achevées à temps pour le 24 juin.
La construction du monde a pu alors commencer.

Personne ne croit qu'Eressea Le Troisième Âge, E3 en abrégé, puisse se passer de beaucoup de reprogrammation.  
La liste des petits et grands changements est longue, et la liste des choses à faire de toute urgence après le lancement est encore plus longue.  
Par exemple, de nombreux sorts, dont certains sont déjà de niveau 2, n’ont pas encore été entièrement revus.  
Comme ceux-ci ne peuvent être évoqués qu'au plus tôt au deuxième tour du jeu, il reste encore beaucoup de temps pour ces petites choses et d'autres...  

<!-- From [https://wiki.eressea.de/index.php?title=Geschichte\_von\_Eressea&oldid=7324] -->

[Wikipedia]: http://de.wikipedia.org/wiki/Eressea_PbeM
[Xolgrim]: https://wiki.eressea.de./cmd-use.mdr:Xolgrim#XE-Artikel_von_Xolgrim "Benutzer:Xolgrim (wiki)"
