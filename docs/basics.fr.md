---
# cSpell:locale fr, en
alias: bases
---
# Bases

Ce n’est pas parce qu’il n’y a pas de gagnant à Eressea que vous ne pouvez pas perdre.
Nous voyons souvent des erreurs évitables chez les débutants qui conduisent à l'élimination précoce d'une faction du jeu parce qu'une règle n'a pas été entièrement comprise ou que le joueur rencontre des problèmes sans être préparé.

Les éléments de base suivants que chaque joueur doit comprendre.

## Rapport

Il y a deux rapports chaque semaine contenant les mêmes données.
Le rapport normal (NR) est un fichier texte lisible avec n'importe quel éditeur.
Le rapport informatique (CR) est un fichier compris par des outils tels que [[magellan]] et [[csmap]].

Nous recommandons aux débutants de faire leurs premiers pas avec le rapport normal et un éditeur de texte.
Les premières commandes font rarement plus d'une douzaine de lignes et vous n'avez pas besoin d'un outil comme Magellan pour les créer.
Au contraire, étant donné que ces outils sont conçus pour gérer de grands partis comptant des centaines d’entités, ils comportent de nombreuses fonctionnalités qui ont tendance à prêter à confusion au début, détournant l’attention des informations importantes qui sont plus faciles à voir dans le rapport normal.

## Ordres longs et courts

Les unités ne peuvent effectuer qu'une seule action [Action] longue par semaine, mais peuvent en effectuer un nombre illimité d'actions courtes.

DANGER! Le combat peut être une action longue, même si vous ne vous êtes pas attaqué.

## Bataille

Les combats dans des régions que vous ne [[cmd-guard|guardez]] sont toujours longs, même si toute votre faction est attaquée par un seul éclaireur, il empêche TOUTES les unités qu'il [[cmd-attack|attaqué]] d'exécuter leur ordre long.
Vous devez donc vous assurer que vous gardez vos régions au plus tard dès la première semaine au cours de laquelle votre faction peut être attaquée.

## Famine

Évitez [la famine] à tout prix. Les effets sont catastrophiques.
Chaque personne a besoin de 10 pièces d'argent par semaine pour ne pas avoir faim

## Finance

Les divertissements et les impôts s'apprennent plus rapidement que le commerce, ne TRAVAILLEZ qu'en cas d'urgence pour éviter la famine.

## Mage

Chaque zone magique possède un sort de niveau 1 qui produit 50 pièces d'argent par niveau de lanceur de sorts.
Si votre race n'a pas de pénalité en magie, former des magiciens tôt peut être intéressant comme source alternative de revenus. Mais attention, tous les sorts ne fonctionnent pas.

## Utilisation des objets et de l'argent

`GIVE` et `RESERVE` déclare et que `GIVE` réserve les articles auprès du destinataire.
Quand quelque chose est utilisé, par exemple pour fabriquer un objet ou pour recruter, qui l'utilise et dans quel ordre ?

## Capacité de chargement

Expliquez les poids et le nombre de personnes.
Indiquez à nouveau où se trouve `MOVE` dans la séquence des ordres.
`ENTERTAIN` vient en premier ; vous pouvez l'utiliser pour surcharger un bateau ou une unité `TRANSPORTING`.

## Nouvelles unités

Les unités qui ont de l'argent ou qui reçoivent de l'argent utilisent toujours cet argent en premier avant d'accéder à la [[items-pool]].
Si vous créez une nouvelle unité, recrutez un chat (coûte 90 argent) et le laissez courir dans la région voisine (10 argent d'entretien) afin de lui permettre d'y apprendre le divertissement la semaine suivante (encore 10 argent d'entretien) puis de le divertir (à partir de là il prend soin de lui-même) il ne suffit pas de lui donner 20 argent pour le temps de trajet et la semaine d'apprentissage, il faut aussi lui donner les 90 argent pour votre propre recrutement.
Sinon, l'unité arrivera dans la région voisine affamée.

## Scout

Sont un investissement stratégique.
Sécurisez les régions voisines importantes, mais seulement si vous en avez les moyens.
En règle générale, il ne suffit pas de placer une unité de divertissement dans la montagne voisine si elle ne peut pas la garder.

<!-- From [https://wiki.eressea.de/index.php?title=Grundlagen&oldid=17000] -->

[Action]:./commands.md#ordres-courts-et-longs
[starvation]: ./silver.md#famine
