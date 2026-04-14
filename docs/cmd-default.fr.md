---
# cSpell:locale fr
alias: cmd-default-fr
---
<!-- disable MD052 because of mkdocs autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# DEFAULT

**`DEFAULT`**`"`*`order`*`"`  

L'ordre `DEFAULT` définit [[ordres|l'ordre]] par défaut qu'une unité exécutera **la semaine suivante**.  

## Modèle d'ordres et ordres par défaut

Une fois que vous avez envoyé vos ordres et que le serveur a créé l'évaluation, des ordres spécifiques sont définis pour chaque unité.  
Ce sont les ordres par défaut.
Ils seront exécutés la semaine suivantes si vous n'envoyez pas d'ordre **pour une unité donnée**.  
<!-- TODO: clarify (bad from german translation) -->
Vous recevrez les ordres par défaut avec le rapport sous forme de fichier texte (également appelé modèle d'ordres), si vous ne les utilisez pas avec l'ordre [[cmd-option|`OPTION ZUGVORLAGE NOT`]] désactivé.  
Ils sont également inclus dans le rapport informatique (CR).
Le rapport normal (NR) ne contient toujours que le premier ordre long par défaut.  
Vous ne pouvez donc pas y voir tous les ordres par défaut.

Tous les [ordres longs][ordres-courts-et-longs] sont normalement inclus dans les ordres par défaut d'une unité.
Les exceptions sont `ATTACK`, `FOLLOW` et `MOVE`.  

De plus, tous les [[comment-with-slashes|`//`]] et tous les ordres commençant par `@` sont adoptés.
L'orthographe peut être standardisée.  

Ordres envoyés :

```text
UNIT abc
    ; seulement 10 cette semaine
    BUY 10 Balm
    SELL 100 Oil
    // acheter plus de baume la semaine prochaine
    @GIVE xyz ALL Balm ; transporteur
    GIVE abc 100 Silver
    RECRUIT 1
```

Ordres par défaut pour la semaine suivante :

```text
UNIT abc
    BUY 10 Balm
    SELL 100 Oil
    // acheter plus de baume la semaine prochaine
    @GIVE xyz ALL Balm ; Transporter
```

D'ailleurs, si l'unité passe à tort plusieurs ordres longs (par exemple `LEARN` et `WORK`), il est difficile de prévoir ce qui en résultera.  
Il en va de même pour les autres ordres invalides.

## L'ordre DEFAULT

L'ordre `DEFAULT` change ce comportement en modifiant les ordres par défaut transmis par le serveur.  
Si l'unité a reçu un ordre `DEFAULT`, ses ordres **longs** ne seront pas inclus dans le modèle d'ordres.  
Les [ordres longs][ordres-courts-et-longs] avec `//` et ordres court avec `@` sont acceptés.
Les ordres donnés sont validés dans une certaine mesure.
Les ordres invalides ne sont donc pas acceptés.  
Cependant, ce test a des limites, il vaut mieux ne pas s’y fier.

Vous pouvez également insérer des ordres courts en utilisant l'ordre `DEFAULT`.

Ordres envoyés :

```text
UNIT abc
    ; cette semaine seulement 10
    BUY 10 Balm
    SELL 100 Öl
    // apprendre la semaine prochaine
    @GIVE xyz ALL Balm ; Transporter
    GIVE abc 100 Silver
    RECRUIT 1
    DEFAULT "GIVE 123 50 Silver; ne pas oublier"
    DEFAULT "LEARN Trade" ; Supprime BUY et SELL
    DEFAULT "XXX" ; aucun ordre, ce ne sera pas accepté
```

Ordres par défaut pour la semaine suivante :

```text
UNIT abc
    GIVE 123 50 Silver; don't forget
    LEARN Trade
    // apprendre la semaine prochaine
    @GIVE xyz ALL Balm ; Transporter
```

Si vos ordres par défaut doivent contenir des guillemets, il existe actuellement plusieurs façons d'y parvenir :

```text
DEFAULT "CAST 'Create a Ring of Invisibility'"
DEFAULT 'CAST "Create a Ring of Invisibility"'
DEFAULT "NAME UNIT \"Bob's Builders\""
DEFAULT "MAKE 1 'Water of life'"
```

## L'ordre `MOVE`

L'ordre `MOVE` joue un rôle particulier : il n'est pas inclus dans le modèle.  
Au lieu de cela, les ordres longs que l'unité avait dans le modèle la semaine précédente sont adoptés (mais uniquement les ordres longs).

Ordres par défaut :

```text
LEARN Ride
@GIVE 0 10 Silver
// pas de commentaire
```

Ordres envoyés :

```text
MOVE e
```

Ordres par défaut pour la semaine suivante :

```text
LEARN Ride
```

Que se passe-t-il si les deux ordres `MOVE` et `DEFAULT` sont en jeu ?

Modèle :

```text
WORK
// maintenant à l'ouest
```

Ordres envoyés :

```text
DEFAULT "LEARN Endurance"
// maintenant, apprendre
MOVE w
```

Ordres par défaut pour la semaine suivante :

```text
LEARN Endurance
// now learn
```

`DEFAULT` supprime aussi les ordres **longs** par défaut (ici `WORK`) et les réinitialise.

Il est possible de définir `MOVE` avec `DEFAULT`.

Modèle :

```text
WORK
@GIVE 0 1 Silver
```

Orders envoyés :

```text
DEFAULT "MOVE o"
WORK
@GIVE 0 2 Silver
```

Ordres par défaut pour la semaine suivante :

```text
MOVE e
@GIVE 0 2 Silver
```

Les ordres par défaut pour la semaine encore d'après, si aucun autre ordre n'est envoyé pour l'unité :

```text
@GIVE 0 2 Silver
```

Ici aussi, l'unité n'effectuerait pas d'ordre long.

!!! note
    Le nombre maximal d'ordres autorisé pour une unité est de 128, ce qui devrait suffire dans la plupart des cas.

Expérience de jeu (Solthar) :

`DEFAULT DEFAULT` ???

Est-il possible d'imbriquer des ordres `DEFAULT` pour passer des ordres plusieurs semaines à l'avance ?

Eh bien, quelque chose comme `DEFAULT "DEFAULT 'LEARN Endurance'"` fonctionne apparemment comme prévu, mais la Direction du Jeu préfère ne donner aucune garantie à ce sujet.  
Veuillez ne pas soumettre de rapports de bogues si quelque chose comme ceci ne fonctionne pas comme prévu.
Les langages de script tels que [[vorlage]], [[extended-commands]] ou [[fftools]] sont plus adaptés à de tels projets.

## Voir aussi

- [[orders]]
- [[sending-orders]]

<!-- From [https://wiki.eressea.de/index.php?title=DEFAULT&oldid=16788] -->
