---
# cSpell:locale fr
alias: bases
---

# Bases

Ce n’est pas parce qu’il n’y a pas de gagnant à Eressea que vous ne pouvez pas perdre.  

Nous voyons souvent des erreurs évitables chez les débutants, qui conduisent à l'élimination précoce d'une [faction][faction] du jeu parce qu'une règle n'a pas été entièrement comprise, ou que le joueur rencontre des problèmes sans être préparé.  

Pour bien débuter, chaque joueur devrait prendre connaissance des éléments de base qui suivent.  

## Rapport

Chaque semaine deux rapports contenant les mêmes données sont envoyés.  
Le rapport normal (NR) est un fichier texte lisible avec n'importe quel éditeur.  
Le rapport informatique (CR) est un fichier compris par des outils tels que [Magellan][magellan-fr-id] et [CSMap][csmap-fr-id].  

Nous recommandons aux débutants de faire leurs premiers pas avec le rapport normal et un éditeur de texte.  
Les premières commandes font rarement plus d'une douzaine de lignes et vous n'avez pas besoin d'un outil comme Magellan pour les créer.  

Au contraire, étant donné que ces outils sont conçus pour gérer de grandes factions comptant des centaines d'[unités][unites], ils comportent de nombreuses fonctionnalités qui ont tendance à prêter à confusion au début.  
Cela peut détourner l’attention des informations importantes, qui sont plus faciles à identifier dans le rapport normal.  

## Les ordres longs et courts

Chaque unité ne peut effectuer qu'un seul [ordre long][ordres-courts-et-longs] par semaine, mais peut effectuer un nombre illimité d'ordres courts.  

!!! warning "Danger"
    Le [combat][le-combat] peut être une action longue, même si vous n'avez pas vous-même attaqué.  

## La bataille

Les combats dans des régions que vous ne [gardez pas][cmd-guard-fr]{title="GUARD"} sont toujours longs, même si toute votre faction est attaquée par un seul éclaireur, il empêche **TOUTES** les unités qu'il [attaque][cmd-attack-fr]{title="ATTACK"} d'exécuter leur ordre long.  
Vous devez donc vous assurer que vous gardez vos régions au plus tôt, dès que votre faction est susceptible d'être attaquée.  

## La famine

Évitez la [famine][famine] à tout prix. Les effets sont catastrophiques.  
Chaque personne a besoin de 10 silver par semaine pour ne pas avoir faim.

## Les finances

Le [divertissement][skill-divertissement-id]{title="Entertainment"} et la [collecte d'impôts][skill-taxation-fr-id]{title="Taxation"} s'apprennent plus rapidement que le commerce, ne [travaillez][cmd-work-fr]{title="WORK"} **qu'en cas d'urgence** pour éviter la famine.  

## Mage

Chaque [École de Magie][ecoles-de-magie] possède un sort de niveau 1 qui produit 50 silver par niveau de lanceur de sorts.  
Si votre peuple n'a pas de pénalité en magie, former des mages tôt peut être intéressant comme source alternative de revenus.  
Mais attention, parfois les sorts échouent.  

<!-- TODO:
## Les objets et l'argent

`GIVE` et `RESERVE` déclare et que `GIVE` réserve les articles auprès du destinataire.
Quand quelque chose est utilisé, par exemple pour fabriquer un objet ou pour recruter, qui l'utilise et dans quel ordre ?
-->

## Capacité de chargement

Un [déplacement][deplacements] échouera si la [capacité de chargement][capacite-de-transport] du transporteur est inférieure au poids total des personnes, des objets, des équipements etc.  

N'hésitez pas à vérifier l'emplacement de l'ordre `MOVE` dans la [séquence des ordres][sequence-des-ordres].  

Par exemple, l'ordre `ENTERTAIN` s'exécute avant; avec l'argent potentiellement gagné, un bateau ou une unité pourrait être surchargé.  

## Nouvelles unités

Les unités qui ont de l'argent ou qui reçoivent de l'argent utilisent toujours cet argent en premier avant d'accéder à la [réserve d'objets][reserve-d-objets-id].  

<!-- TODO: add orders example otherwise it"s unclear  -->
Par exemple, vous créez une nouvelle unité, recrutez un [Chat][chats]{"title=Cat"} (coûte 90 silver).  
Vous le laissez courir dans la région voisine (10 silver d'entretien) afin de lui permettre d'y [apprendre][cmd-learn-fr]{title="LEARN"} le [divertissement][skill-divertissement-id]{title="Entertainment"} la semaine suivante (coûtera 10 silver de plus d'entretien).  

Dans cette situation, il ne suffit pas de lui donner 20 silver pour le temps de trajet et la semaine d'apprentissage.  
Il faudra en fait lui donner en plus 90 silver pour votre propre recrutement, sinon, l'unité arrivera [affamée][famine] dans la région voisine.  

## Scout

Les scouts (éclaireurs) sont un investissement stratégique.  
Sécurisez les régions voisines importantes, mais seulement si vous en avez les moyens.  
En règle générale, il ne suffit pas de placer un artiste (unité de divertissement) dans la montagne voisine si elle ne peut pas la garder.  

<!-- From [https://wiki.eressea.de/index.php?title=Grundlagen&oldid=17000] -->

[cmd-attack-fr]: [[cmd-attack-fr]]
[cmd-guard-fr]: [[cmd-guard-fr]]
[cmd-learn-fr]: [[cmd-learn-fr]]
[cmd-work-fr]: [[cmd-work-fr]]
