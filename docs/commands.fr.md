---
# cSpell:locale fr
alias: ordres
---
# Ordres

## Conventions d'écriture

```text
GIVE unit-id [number|ALL] [item]
```

Les conventions suivantes s'appliquent dans les règles de cette documentation :

- Des mots-clés comme `GIVE`, `MAKE`, `NOT` sont en majuscules.
  Ce n'est pas obligatoire, mais nous le recommandons. Le reste est en lettres minuscules.
  Les éléments en minuscules ne doivent pas être adoptés littéralement, mais doivent être remplacés par des valeurs concrètes, par exemple unit-id par le numéro de l'unité souhaitée.
  Parfois, nous écrirons également ceci sous la forme &lt;unit-id&gt;, auquel cas les symboles `<` et `>` ne sont **PAS* à inclure.
- Les éléments entre crochets sont facultatifs
  Ils peuvent donc être omis, mais ils changent le sens de l'ordre.
  Les alternatives sont définis avec le caractère `|`.

L'exemple ci-dessus permet `GIVE 123 ALL` ou `GIVE abc 4 sword`.  

## Syntaxe

À l'exception du mot de passe et des identifiants, l'évaluation par le serveur n'est pas sensible à la casse.  
`learN croSSBow` est tout à fait correct (mais déconseillé car difficile à lire).  

Les items doivent toujours être renseignés **au singulier**, ainsi il faut écrire `GIVE xyz 100 Sword` ou `MAKE 15 Stone`.  
Les items apparaissent souvent en majorité dans le rapport et sont pour la plupart compris dans les ordres, mais sachez que le serveur ne comprend pas le langage naturel, même si les ordres s'en approchent.  

De nombreux ordres peuvent être raccourcis, mais il ne faut pas en faire un usage conséquent car cela est sujet aux erreurs.  
Par exemple le raccourci `LEA` est ambigü car il peut correspondre à  `LEARN` ou `LEAVE`, ce qui produit une erreur à l'évaluation.  
Ici, vous devrez donc utiliser au moins 4 lettres.  

De plus, les abréviations trop énigmatiques ne sont pas particulièrement lisibles lorsque vous parcourez vos ordres plus tard...  
Il est toujours plus sûr de ne pas abréger vos ordres, d'autant plus qu'il peut y avoir des ordres, des objets ou des compétences qui ne figurent pas intentionnellement dans les instructions, mais qui commencent comme d'autres ordres, objets et compétences bien connus.  

Les textes contenant des espaces doivent être mis entre guillemets (""), ou les espaces doivent être remplacés par le caractère `~` (tilde):

```text
NAME Ship "Big Blue Bird"
GIVE unit 5 Water~of~life
COMBAT REAR
```

Il est possible d'utiliser et de combiner des guillemets simples (`'`).  
Il est préférable d'essayer ce qui ressort exactement, car le comportement exact peut toujours évoluer.  

```text
MESSAGE REGION 'Say "Friend" and enter'
NAME CASTLE xyz "Helm's Deep"
DEFAULT 'MAKE 1 "Water of Life"'
```

L'*escaping* au moyen du caractère d'échappement `\` est aussi possible, mais pas forcément recommandé :

```text
MESSAGE REGION "Say \"Friend\" and enter"
NAME CASTLE xyz 'Helm\'s Deep'
DEFAULT 'MAKE 1 Water\~of\~Life'
```

D'ailleurs, il n'est pas nécessaire de se limiter à l'alphabet latin.  
Le jeu de caractères Unicode complet est utilisable dans les noms et les descriptions :

```text
NAME UNIT "Σωκράτης"
MESSAGE REGION "🨀 شاه مات"
```

Bien entendu, vous devez vous assurer que vous êtes compris des autres.  

## Modèle d'ordres

Le plus simple est d’utiliser le modèle de commandes à la fin de l’évaluation.  
Toutes les unités y sont répertoriées pour que vous n'oubliiez personne.  
Si vous n'envoyez aucun ordre, les ordres du modèle d'ordres seront quand même exécutés automatiquement.  
Même si vous n'envoyez des ordres que pour certaines de vos unités, les ordres du modèle d'ordres seront exécutés pour les unités restantes.  
Si votre évaluation ne contient pas de modèle d'ordres (d'extension `.txt`), vous pouvez le réactiver avec l'ordre [[cmd-option|`OPTION ZUGVORLAGE`]].

## Ordres courts et longs

Il existe des ordres courts et des ordres longs dans Eressea.  

Les ordres **longs** sont les suivants :

- [[cmd-work]],
- [[cmd-attack]],
- [[cmd-steal]],
- [[cmd-ride]],
- [[cmd-follow]],
- [[cmd-research]],
- [[cmd-buy]],
- [[cmd-teach]],
- [[cmd-learn]],
- [[cmd-make]] (exception: `MAKE TEMP`),
- [[cmd-move]],
- [[cmd-plant]],
- [[cmd-piracy]],
- [[cmd-route]],
- [[cmd-spy]],
- [[cmd-tax]],
- [[cmd-entertain]],
- [[cmd-sell]],
- [[cmd-cast]],
- [[cmd-destroy]],
- [[cmd-grow]].

Tous les autres ordres sont des ordres courts ([brève description] de tous les ordres).  

Vous pouvez passer **autant d'ordres courts que vous le souhaitez par unité**.  
Une unité ne peut généralement avoir **qu’un seul ordre long**.  

Il existe quelques exceptions, appelées ordres pseudo-longs (`ATTACK`, `FOLLOW`, `BUY`, `SELL`, `CAST`), dont plusieurs peuvent être donnés dans certaines circonstances.  
De plus amples informations peuvent être trouvées dans la description des différents ordres.  

Si une unité reçoit un ordre long, elle l'adoptera comme ordre par défaut, remplaçant l'ordre par défaut précédent.  
L'ordre par défaut est toujours dans le [modèle d'ordres] comme suggestion pour un ordre long.  
Il vous suffit donc de donner à un éleveur de chevaux l'ordre `MAKE Horse` une seule fois, et cet ordre apparaîtra dans le modèle d'ordres jusqu'à ce qu'il reçoive un autre ordre long (par exemple `LEARN Tazming`).  
Il est logique que tous les ordres longs ne soient pas adoptés comme ordres par défaut.  
Par exemple, les ordres longs `MOVE`, `ATTACK` et `FOLLOW` ne sont pas exécutés comme ordres par défaut.  
Pour plus d'informations sur les ordres par défaut : [[cmd-default]].  

Une unité qui a travaillé un tour, s'est déplacée vers le nord le tour suivant, et qui n'a ensuite plus reçu d'ordres, se stabilisera et travaillera à nouveau le tour suivant (à moins, bien sûr, qu'elle reçoive un autre ordre long ce tour-là).  

Veuillez noter qu'un seul ordre par unité sera affiché dans le rapport normal (NR).  
Les ordres par défaut restants sont affichés dans le modèle d'ordres (NR) et dans le rapport informatique (CR).  

## Exécuter des ordres courts de manière permanente

Parfois, il est judicieux d'exécuter un ordre court à chaque tour, comme l'ordre `GIVE`.  
Par exemple, les mineurs doivent constamment livrer le fer extrait à un forgeron pour la fabrication d'armes.  

Pour ce faire, vous pouvez préfixer chaque ordre court avec un `@` (arobase).  
Ces ordres sont simplement copiés dans le modèle d'ordres pour le tour suivant et - à moins que vous ne les supprimiez à nouveau - exécutés à nouveau.  

 **Exemple** :

```text
UNIT berg;               mineurs [5,400$,U500]
    MAKE iron
    @GIVE schm ALL Iron; livraison permanente au forgeron
UNIT schm;               forgeron [3,1343$,U250]
    MAKE Sword
```

!!! note
    Le **nombre maximal d'ordres** autorisés pour une unité est de **128**, ce qui devrait suffire dans la plupart des cas.

## Supprimer les messages d'erreur

Il peut arriver que vous acceptiez consciemment des erreurs lors de l'exécution d'un ordre.  
En le préfixant d'un point d'exclamation (`!`), vous pouvez forcer la suppression des messages d'erreur normalement produits par le serveur identifiant un problème sur l'ordre concerné.  

**Un exemple** :

```text
UNIT berg;         Miners
    MAKE iron
    !@GIVE tran ALL iron;  le transporteur n'est pas là; on veut éviter tout message d'erreur à ce sujet
UNIT tran;   Transporteur
    ROUTE w PAUSE e PAUSE; nous faisons la navette entre deux régions
    !@GIVE schm ALL iron;  à l'ouest on remet le fer aux forgerons
```

Bien entendu, cela comporte le risque que vous manquiez des erreurs auxquelles vous ne vous attendiez pas.  

## Voir aussi

- [[sequence-des-ordres]]
- [[orders-list]]
- [[cmd-default]]

Poursuivre la lecture : [[sequence-des-ordres]].

<!-- From [https://wiki.eressea.de/index.php?title=Befehl&oldid=16787] -->
