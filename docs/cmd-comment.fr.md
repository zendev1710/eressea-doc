---
# cSpell:locale fr, en
alias: cmd-comment-fr
---
# Commentaire (;)

Le point-virgule « ; » est utilisé dans les commandes Eressea pour marquer les commentaires (temporaires).
Certains de ces commentaires sont insérés « automatiquement ».
Par exemple, le [[ordres|modèle d'ordres]] standard contient toujours les noms des régions et des unités, le nombre de personnes et leur réserve d'argent en guise de commentaire.
De plus, les commentaires sont également utilisés pour fournir au programme [[echeck]] certaines informations, comme les salaires dans une région.

```text
ERESSEA abcd "Entrez le mot de passe ici"

; ECHECK -l -w4 -r90 -v4.01

REGION 85,-48 ; Darkland
; ECheck Salaire 15

UNIT ub2;    Handyman [3,30$]
    LEARN forestry
    // LEARN Shipbuilding AT T2 or T3
```

Si vous utilisez le programme [[vorlage]] pour créer un modèle d'ordres, diverses informations sont transmises au joueur via ces commentaires :

```text
REGION 85,-48 ; Darkland (Plain, 290 people, $4270 Silver)
; ECheck Salary 15
;  . .  |Farms: 8534 +9|Silver: 47588297 +48400|Upkeep: 2379414 +2420|
; . E w |Recruits: 213 +0|Horses: 2532 -8|Profit: 51204 +54|
;  . .  |pl. free: 1466 -9|                       |                        |
;       |Spice: 125 +0|Jewel: 175 +0|Myrrh: 125 +0|
;       |Oil: 75 +0|Silk: 150 +0|Incense: 100 +0|
; Prod.: Balm: -4 +0 max. tradeable: 85
; Street (100%) to the east
; Region income: 2660 Silver
; Food costs:    2900 Silver
; Material pool: 4270 Silver, 1 Speer

; -   -   -   -   -   -   -   -   -   -   -   -
; Dans un champ ouvert:

UNIT ub2;  Handyman [3,0$] flieht
; Weight: 60.00GE Walking: 32.40GE/32.40GE
; Forestry 2
    LEARN Forestry
    // LEARN Forestry On T3
```

Le joueur lui-même peut également insérer des commentaires après un point-virgule.
Cependant, comme ces commentaires ne sont pas inclus dans le modèle de la semaine suivante, les commentaires permanents après [[comment-with-slashes|`//`]] ont généralement plus de sens.

Pour économiser la capacité de transmission, les commentaires temporaires peuvent être supprimés avant l'envoi des ordres.
Certains outils font cela, comme [[magellan]] ou VPP.

## Liens externes

- [Vorlage et VPP sur Gulrak.de]

<!-- From [https://wiki.eressea.de/index.php?title=;&oldid=16702] -->

[Vorlage et VPP sur Gulrak.de]: http://www.gulrak.de/eressea/tools.html
