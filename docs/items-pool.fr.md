---
# cSpell:locale fr
alias: reserve-d-objets
---

[](){ #reserve-d-objets-id }

# Réserve d'objets

En particulier avec les factions volumineuses, les joueurs peuvent perdre le fil dans certaines régions, d'autant plus que "distribuer de l'argent" est plutôt ennuyeux, compliqué et n'ajoute pas grand-chose au plaisir du jeu.

[](){ #reserve-d-argent-id }

## Réserve d'argent

La réserve d'argent prend en charge la distribution de l'argent lorsque vous jouez, de sorte que par exemple avec [`RECRUIT`][cmd-recruit-fr] l'unité obtienne automatiquement suffisamment d'argent (si disponible dans la région) ou permette l'apprentissage de compétences coûteuses.  
Néanmoins, il est précisé tout au long des instructions que les unités doivent avoir suffisamment d'argent sur elles.  
C'est juste pour éviter de l'oublier.

De même, les [bâtiments][batiments-id] sont approvisionnés depuis la réserve si l'argent est présent dans la région au début du tour.  
Si l’entité propriétaire du bâtiment ne peut pas le payer de sa poche ou de la réserve, le bâtiment ne peut pas fonctionner.  
À la fin du tour, l'unité tentera à nouveau de payer le bâtiment à partir de ses propres réserves d'argent ou de la cagnotte de son propre groupe.  

**Les unités `TEMP` ne peuvent pas réserver**.
Ils couvrent les frais de recrutement à partir de la réserve d'argent, si nécessaire, mais devraient recevoir de l'argent et des objets qu'ils devraient emporter avec eux dans une autre région ou traiter immédiatement avec [`GIVE`][cmd-give-fr].

!!! warning "Attention"
    Lorsque les unités `TEMP` obtiennent de l'argent, elles l'utilisent également pour recruter !  
    Donc, si vous souhaitez qu'ils emportent de l'argent avec eux dans une autre région, l'argent de recrutement doit également être remis.

Des règles particulières s'appliquent à l'entretien des unités : tout l'argent de la région est utilisé ici, quelles que soient les réservations antérieures.  
Les unités ne donnent pas l'argent dont elles ont besoin pour leur propre entretien aux unités (pour que celles-ci paient leur entretien).

## Réserve de matériel

La réserve de matériaux est la suite logique de la réserve d'argent : chaque unité qui a besoin de quelque chose, par exemple les pierres et le bois pour la construction des bâtiments, les obtiennent automatiquement des autres unités de la région.  

Les réserves ne sont valables que pour votre propre faction.  
Les objets doivent être explicitement remis à des unités étrangères.  

Les réserves ne fonctionnent pas seulement en production (essentiellement avec l'ordre [`MAKE`][cmd-make-fr]), mais globalement pour tout, notamment pour les ordres [`RESERVE`][cmd-reserve-fr], [`GIVE`][cmd-give-fr], [`USE`][cmd-use-fr], [`CAST`][cmd-cast-fr] et [`RECRUIT`][cmd-recruit-fr].  
Si l'unité ne dispose pas d'un item, elle le prélève dans la réseerve de matériaux pour le traiter, le remettre ou le réserver.  
Cependant, si une unité a besoin d'armes pour une attaque ou pour collecter des impôts, celles-ci doivent être explicitement remises ou réservées, car la réserve de matériel ne s'applique pas pour cet usage.  

**Les factions inexpérimentées doivent planifier soigneusement leur réserve de matériel**, car il peut facilement arriver de « voler » sans le vouloir des ressources à des unités;  
ces unités léséees ne pourront alors pas produire (ou pas assez), tandis que l'unité avec surplus d'items aura utilisé plus de ressources et probablement produit plus que prévu.  

### Exemple 1

```text
UNIT a ; mineur, possède 30 fer
    MAKE 20 iron
    @GIVE c ALL iron
;
UNIT b ; fabricant d'armes, n'a pas de fer
    RESERVE 10 iron
    MAKE 10 sword
;
UNIT c; pour stockage, n'a pas de fer
    LEARN Stealth
```

**Résultat de l'avaluation :**

- L'unité b reçoit d'abord 10 fer de la réserve d'objets de a
- L'unité a donne les 20 fer restants à c
- L'unité b fabrique 10 épées avec 10 fer
- L'unité a extrait 20 fer
- Donc l'unité b possède finalement 10 épées
- L'unité a possède finalement 20 fer
- L'unité c possède finalement 20 fer

## RESERVE et GIVE

Il y a quelques particularités à noter à propos de [`RESERVE`][cmd-reserve-fr] et [`GIVE`][cmd-give-fr], qui précèdent la plupart des autres ordres de la [[orders-sequence]].  
Celles-ci s'appliquent autant à la réserve d'argent qu'à la réserve de matériaux.

Premièrement, les items remis ou réservés ne sont plus disponibles dans la réserve.  
<!-- TODO: clarify -->
Elle ne peut donc utiliser que ce que l'unité a réservé ou reçu.  

Avec l'ordre `RESERVE`, l'unité procède de la façon suivante : lors d'un premier passage, chaque unité réserve d'abord ses propres items.  
Dès lors, tout ce qui a été réservé ne sera plus disponible depuis la réserve.  
Ce n’est qu’alors que les unités essaient d’obtenir des autres unités les objets de la réserve qu’elles n’avaient pas lors de la première étape.  
Tant le traitement des ordres `RESERVE` que la récupération des items sont effectués dans l'ordre dans lequel les unités apparaissent dans le rapport - à proprement parler, cela n'est pas garanti, mais c'est une pratique de longue date.  

Si une unité a plusieurs ordres `RESERVE` pour un item, **cela ne s'additionne pas**.
Au lieu de cela, tous les ordres sont exécutés en sequence.  
Cependant, ce comportement n'est pas garanti, il est donc préférable qu'une unité n'ait qu'un seul ordre `RESERVE` par item.  

Lorsque l'ordre `GIVE` est ensuite exécuté, les items sont également supprimés de la réserve si nécessaire.
Une fois encore, l'ordre du rapport est respecté.  
Les items réservés par n'importe quelle unité (y compris l'unité passant l'ordre `GIVE`) ne sont pas transmis.
Les items remis ne sont plus dans la réserve.  

!!! note
    L'ordre `GIVE xyz ALL` ne remet que les items non réservés à l'unité elle-même.

Tous les autres ordres utilisent d'abord vos propres items, réservés ou transférés, puis ensuite seulement utilisent les items non réservés de la réserve.  

### Exemple 2

```text
UNIT a; possède 10 Silver
    LEARN Melee
    RESERVE 20 Silver
;
UNIT b; ne possède pas de Silver
    LEARN Melee
    RESERVE 10 Silver
;
UNIT c; possède 10 Silver
    LEARN Melee
    RESERVE 10 Silver
```

**Résultat de l'avaluation :**

- L'unité a réserve ses propres 10 silver
- L'unité c réserve ses propres 10 silver
- Comme il n'y avait que 20 silver dans la région, les ordres RESERVE restants expirent
- L'unité a consomme ses propres 10 silver d'entretien
- L'unité c consomme ses propres 10 silver d'entretien
- L'unité b est affamé car il n'y a plus d'argent

Si une unité avait 10 silver de plus au départ, l’unité b ne serait pas affamée.

### Exemple 3

```text
UNIT a; possède 20 Silver
    RESERVE 20 Silver
    GIVE c 20 Silver
;
UNIT b; possède 20 Silver
    MOVE EAST
;
UNIT c; ne possède pas de Silver
    MOVE WEST
```

**Résultat de l'avaluation :**

- L'unité a réserve ses propres 20 silver
- L'unité a donne 20 silver de la réserve d'argent à c
  Ses 20 silver sont réservés, elle prend donc les 20 silver de b
- L'unité b va vers l'est et sera affamée s'il n'y a pas d'autre unité alliée avec de l'argent dans la région de destination
- L'unité c prend 20 silver et va vers l'ouest

### Exemple 4

```text
UNIT a ; possède 10 Silver, 20 bois, 10 fer
    LEARN Melee
    RESERVE 5 Iron; (1)
    GIVE d ALL Iron; (6)
;
UNIT b ; possède 10 Silver, 10 fer
    RESERVE 100 Silver ; (2), (4)
    RESERVE 10 Wood ; (5)
    GIVE c 100 Silver ; (7)
    GIVE d 9 Wood ; (8)
    LEARN Melee
;
UNIT c ; Melee 10, possède 100 Silver
    RESERVE 100 Silver ; (3)
    MAKE 10 Spear ; (9)
;
UNIT d ; possède 200 Silver
    LEARN Forestry
```

 **Version :**

- (1), (2), (3) : les unités a, b et c réservent initialement leurs propres 5 fer, 10 silver et 100 silver, respectivement
- (4) : ce n'est qu'alors que b récupère les 90 silver restants de la réserve, à savoir 10 de l'unité a et 80 de l'unité d, puisque ce sont les seules qui n'ont pas encore été réservées
- (5) : L'unité b prend 10 bois de la réserve de l'unité a
- (6) : L'unité a donne les 5 fer restants qui n'étaient pas réservés à l'unité d
- (7) : L'unité b essaie de donner 100 silver à c ; le seul argent qui n'est pas encore réservé qu'a l'unité d (120), donc 100 de celui-ci sont donnés à c
- (8) : L'unité b donne 9 bois de l'unité a à l'unité d
- (9) : L'unité c prend 1 bois de l'unité a depuis la réserve, bois qui n'a pas encore été réservé pour la production
  Elle ne peut donc construire qu'une seule lance
- (10) : Toutes les unités paient l'entretien (nous supposons ici 10 silver par personne)

**Résultat de l'avaluation :**

- L'unité a n'a finalement plus de silver, plus de bois, 5 fer
- L'unité b a finalement 10 bois, 80 silver (20 utilisés pour l'entretien de a et b), 10 fer
- L'unité c a finalement 190 silver (10 consommés) et 1 lance
- L'unité d a finalement 9 bois, 10 silver (10 consommés), 5 fer

## Note historique

Dans les anciennes versions, la réserve de matériaux était un paramètre facultatif que chaque joueur pouvait activer ou désactiver.  
Il y avait des réglages séparés pour l'argent et les autres objets.

!!! note
    Les **réserves** d'argent et de matériaux sont désormais **automatiquement actives pour toutes les factions**.
    Elles ne peuvent plus être désactivées.

## Voir aussi

- [`GIVE`][cmd-give-fr]
- [`RESERVE`][cmd-reserve-fr]
- [[orders-sequence]]

Poursuivre la lecture : la [guerre][guerre].

<!-- From [https://wiki.eressea.de/index.php?title=Materialpool&oldid=17006] -->

[cmd-cast-fr]: [[cmd-cast-fr]]
[cmd-give-fr]: [[cmd-give-fr]]
[cmd-make-fr]: [[cmd-make-fr]]
[cmd-recruit-fr]: [[cmd-recruit-fr]]
[cmd-reserve-fr]: [[cmd-reserve-fr]]
[cmd-use-fr]: [[cmd-use-fr]]
