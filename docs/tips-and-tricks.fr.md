---
alias: trucs-et-astuces
---
# Trucs et astuces

## Il n'est pas toujours nécessaire de savoir monter à cheval

Le commerce et le transport deviennent rentables dès le début de la partie.
Même sans savoir monter à cheval, on peut emmener un cheval par personne, ce qui augmente la capacité de l'unité de 5,4 à 25,4 kg.
4 [trolls] peuvent même transporter un chariot et, avec 4 chevaux, atteindre une capacité de 223,2 kg.

Cela permet même à un petit groupe de transporter des pierres, des marchandises et autres objets lourds.

## Comment équiper mes troupes

La meilleure armure est composée d'une [armure de plaques] et d'un bouclier.
Un calcul rapide montre qu'un guerrier équipé d'un bouclier, d'une armure et d'une épée pèse 6 kg et est immobilisé.
C'est pourquoi, autrefois, les chevaliers avaient des écuyers – et dans Eressea, des chevaux.

Pour chaque tranche de 20 kg de poids excédentaire, on équipe l'unité d'un cheval, et les troupes peuvent à nouveau se déplacer.
Comme mentionné [ici](#il-nest-pas-toujours-nécessaire-de-savoir-monter-à-cheval), il n'est même pas nécessaire de savoir monter à cheval.
On peut également équiper 100 hommes de 70 armure de plaques et de 30 [cotte de mailles]; l'équipement de l'unité pèse alors exactement 540 kg, soit sa capacité de charge maximale.

> Si l'adversaire inflige des dégâts très élevés par coup, il peut être préférable de remplacer l'armure de plates par une cotte de mailles, voire de l'omettre complètement, car sinon la probabilité de coup plus élevée n'est pas compensée par la protection de l'armure.

## Que doivent apprendre mes troupes ?

*Les troupes apprennent [l'endurance] et la [maîtrise des armes].
Selon la race, il arrive un moment où il est plus avantageux d'apprendre l'endurance que la Maîtrise des armes.
Finalement, chaque nouveau niveau de maîtrise des armes coûte autant de temps d'apprentissage que plusieurs niveaux d'endurance.
Tu peux calculer quand ce point est atteint, ou te baser sur la maîtrise des armes de tes ennemis – car il est absolument crucial de ne pas prendre beaucoup de retard sur eux.

L'avantage de maîtriser deux compétences réside aussi dans le fait qu'il est plus facile d'avoir toujours des *instructeurs* (*teachers*) disponibles, pour enseigner l'une ou l'autre compétence.

## De quoi ai-je absolument besoin au premier tour ?

Peu importe la race et le besoin qui en découle en artistes ou collecteurs d'impôts par exemple, tu dois absolument former au moins un percepteur et peut-être une unité en [camouflage] dès le premier tour pour éviter d'être distancé, car les races particulièrement douées en camouflage exploitent souvent leur capacité à voler lorsqu'elles en ont l'occasion.

## Acheter de la marchandise

Bien que l'achat excessif augmente temporairement le prix d'une marchandise, il est conseillé d'en acheter davantage tant que ce prix reste inférieur au prix de vente.
En général, une marchandise peut être vendue dans bien plus de régions que tu ne peux l'acheter, et les marchands peuvent vendre plusieurs marchandises différentes par tour.
Il existe même des situations où il est judicieux d'acheter des marchandises à un prix supérieur au prix de vente maximal, mais c'est probablement aller trop loin.

Le commerce te permet de gagner d'importantes sommes d'argent créées « à partir de rien », c'est-à-dire sans puiser dans les ressources régionales des agriculteurs ; c'est une opportunité à ne surtout pas manquer.

## Nombre maximal d'unités dans une faction

**Une faction peut compter au plus 2 500 unités** (250 dans E3). Pour en créer de nouvelles lorsque la limite est atteinte, il faut d’abord dissoudre certaines unités en fusionnant plusieurs unités (les laisser mourir de faim, perdre des batailles ou utiliser l'ordre `GIVE 0` sont également possibles). Cependant, comme les unités vides ne sont dissoutes que peu de temps avant la fin de la séquence de commandes, il est impossible de créer de nouvelles unités de cette manière avant la semaine suivante.

Parfois, avec une petite astuce, on peut faire les deux en un seul tour : l’unité A transfère tout son personnel à l’unité B. L’unité A, désormais vide, peut recruter immédiatement (après l’ordre `GIVE`). La condition préalable est bien sûr de disposer de deux unités dans la région où l’on souhaite recruter et de pouvoir les combiner.

## Les agriculteurs comme éclaireurs

Les [paysans nomades] apportent des informations précieuses des régions voisines.
Si le nombre de paysans dans une région augmente soudainement et bien plus vite que ne le permettrait la croissance naturelle de la population agricole, la cause est la [migration de paysans] venus des régions voisines.
Souvent, des monstres ayant élu domicile dans les environs et chassant les paysans en sont responsables.
Une autre possibilité est que certains paysans ne trouvent pas de travail dans leur région d'origine.

Conclusion : Quiconque s'intéresse aux tendances démographiques jette également un œil aux régions voisines.

## Entrepôt

Dans une région, un entrepôt est géré par une unité prioritaire (par exemple, le seigneur du plus ancien château) qui reçoit les marchandises excédentaires.
Si une autre unité a besoin de ces marchandises, elle peut les récupérer (avec la réserve de ressources activée) grâce à l'ordre [[cmd-reserve]].
Il est important que l'entrepôt soit prioritaire car [[cmd-reserve]] parcourt les unités de la région et prélève les objets nécessaires auprès de la première unité disponible qui les possède. De plus, cela permet de visualiser en un coup d'œil les objets disponibles.

!!! tip
     Si l'entrepôt adopte un camouflage permanent, le stock devrait échapper à un espion peu compétent, errant ou nageant, appartenant à une faction hostile. Une autre théorie suggère un niveau de perception élevé pour rendre l'entrepôt difficile à piller ; toutefois, un bon observateur de la même faction, en plus de la présence de l'entrepôt lui-même, suffirait également à empêcher le vol.

## Échapper à la mort par famine

L'ordre d'affichage des unités d'une faction dans un rapport définit la priorité à s'accapparer la nourriture.
Les mages, les percepteurs, les tacticiens et autres unités importantes doivent donc être placés le plus haut possible.
L'argent est presque toujours distribué du haut vers le bas (bien que cela ne soit pas garanti par le Maître de Jeu !).

Si une région manque d'argent pour nourrir tout le monde, par négligence ou vol, les unités de rang supérieur s'accapareront la nourriture en premier, laissant les suivantes  mourir de faim.

Si un seul membre d'une unité souffre de la faim, l'unité entière subit le désavantage de voir ses compétences réduites de moitié.
Par conséquent, placer une unité de 100 collecteurs d'impôts tout en bas d'une région n'est peut-être pas la meilleure stratégie.

Les unités peuvent être triées dans l'ordre souhaité à l'aide de l'ordre' [[cmd-sort]].

## Routes maritimes sûres

Avec de grandes factions, il est facile de perdre le fil dans la gestin de sa flotte.
Un oubli d'ordre ROUTE (ou NMR) peut facilement entraîner la poursuite du trajet d'un bateau déjà arrivé à destination, et qui finira par s'écraser contre une montagne au tour suivant. Pour éviter cela, termine les ordres ROUTE par une double PAUSE, par exemple :

ROUTE NE NE NE NE E E E E E E NW NW NW SE PAUSE PAUSE

Cela a pour effet de définir l'ordre par défaut pour le tour suivant sur ROUTE PAUSE NE NE NE NE E E E E E E NW NW NW SE PAUSE lorsque le dernier ordre PAUSE est atteint.
Un message d'erreur s'affiche alors, mais le vaisseau ne bouge plus.

## Unités TEMP

Avec les unités TEMP, tu peux faire toutes sortes de choses et contourner les restrictions que le jeu impose par excès de prudence.
Par exemple, tu peux quitter un bâtiment ou un bateau et tu ne sais pas ce qui va se passer ? C'est très simple.

     GIVE TEMP 123 ALL
     GIVE TEMP 123 ALL PERSONS
     MAKE TEMP 123
          ; ... NAME et autres nouveaux ordres de l'unité
     END
     GIVE neu COMMAND

L'unité vide transmet fidèlement la commande à l'unité appropriée et la nouvelle unité TEMP prend le relais de l'ancienne (avec un nouveau numéro).

## Mon bateau échoue à prendre la mer alors qu'il n'est pas surchargé

Il arrive parfois qu'un message indique qu'un bateau n'a pas pu partir en raison d'une surcharge.
Cependant, après vérification, il s'avère que le bateau n'est en réalité pas surchargé.

Il ne s'agit généralement pas d'un bug, mais plutôt d'une surcharge du bateau liée à un volume trop important d'argent, ensuite dépensé.
Comme l'ordre `MOVE` précède la maintenance des unités dans la [séquence des ordres], le bateau était encore surchargé lors de sa tentative de départ.
Parfois, l'erreur est également due à des unités exécutant l'ordre `WORK`.
Tout semble normal dans le rapport, mais l'unité surcharge le bateau en argent, qu'elle consomme ensuite après la phase de déplacement.

## Voir aussi

- [Conseils]

<!-- From [https://wiki.eressea.de/index.php?title=Tipps\_und\_Tricks&oldid=6990] -->

[trolls]: ./races.md#trolls "Trolls"
[paysans nomades]: ./farmers-hike.md "Bauernwanderung"
[migration de paysans]: ./farmers-proliferation.md "Prolifération des paysans"
[RESERVE]: ./cmd-reserve.md "RESERVE"
[SORT]: ./cmd-sort.md "SORT"
[séquence des ordres]: ./commands-sequence.md "Séquence des ordres"
[Conseils]: ./hints.md "Conseils"
