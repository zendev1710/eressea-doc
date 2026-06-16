---
# cSpell:locale fr
alias: envoi-des-ordres
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# Envoi des ordres

## Ce dont vous avez besoin pour jouer à Eressea

En plus de votre propre accès à la messagerie électronique, vous n'avez pas besoin de grand-chose pour jouer à Eressea.  

Pour éditer les [[ordres]], un simple éditeur de texte suffit.  
Sous UNIX/Linux par ex. VI ou EMACS, sous Windows Notepad fonctionne également.  
L'important, c'est que l'éditeur n'ajoute des sauts de lignes que là où vous en saisissez.  
En aucun cas l'éditeur ne doit effectuer de renvoi à la ligne automatique pour des lignes trop longues, sinon les ordres pourraient ne pas être exécutés correctement.  

[Notepad++] est un bon éditeur pour Windows.

### Exemples

La plupart des nouveaux joueurs utilisent l'outil [[magellan]].  
Eressea dispose également de divers autres outils qui facilitent la vie du joueur.  
Voici une liste des plus utilisés :

- [CSMap][csmap-fr-id]
- [ECheck][echeck-fr-id]
- [[ehmv]]
- [[magellan]]
  - [[extended-commands]]
  - [[fftools]]
- [[vorlage]]

## Comment soumettre des ordres et ce que vous obtenez en retour

Vous pouvez envoyer vos ordres jusqu'à 20 fois à chaque tour.  
La transmission d'ordres provisoires est donc possible et recommandée.  

Vous devez vous assurer que l'heure correcte est réglée sur votre ordinateur.  
Le serveur utilise l'heure d'envoi comme base pour écraser les anciens ordres, et non l'heure de réception.  

Attention : les ordres doivent apparaître sous forme de texte normal (texte brut) dans le corps de l'e-mail.  
Alternativement, ils peuvent être dans un fichier `.txt` envoyé en pièce jointe, mais l'e-mail doit alors être vide (pas de texte dans le corps de l'e-mail).  
Dans le cas contraire, les ordres ne seront pas reconnus par le serveur de jeu et seront ignorés !  
Il existe divers [outils][comment-soumettre-des-ordres-et-ce-que-vous-obtenez-en-retour] qui facilitent la saisie des ordres, en particulier pour les grandes factions.  

Soyez prudent lorsque vous utilisez des interfaces web telles que GMX ou GMail !  
Ceux-ci se sont avérés problématiques dans le passé car les e-mails étaient mal formatés.  

Les utilisateurs de [[magellan]] peuvent très facilement [envoyer des ordres directement depuis le programme][envoi-des-ordres-depuis-magellan], sans avoir à passer par des programmes de messagerie ou des outils de messagerie web.

Les ordres doivent toujours être envoyés à [eressea-server@kn-bremen.de], avec, en objet, l'intitulé **ERESSEA ORDERS 2**.
Si l'objet de l'email est différent, les emails ne seront pas reconnus par le serveur de jeu et seront ignorés.  
Les ordres qui arrivent correctement sont automatiquement vérifiés avec le vérificateur de syntaxe ECheck et le résultat de la vérification est envoyé au joueur.  

Un exemple :

```text
ECHECK (Version 3.4.2, Jun 12 2000), Zug-Checker für Eressea - Freeware!

Process file `[faroul@beyond.kn-bremen.de](mailto:faroul@beyond.kn-bremen.de)'2'.
Recruitment cost set to 75 Silver, Warning Level 0.
Silver pool activated.

Orders were read for 1 faction and 100 units.
The orders seem fine.
```

Cette confirmation intervient généralement en quelques minutes.  
Étant donné que le serveur ne peut malheureusement envoyer qu'une seule confirmation des ordres toutes les 2 minutes (pour des raisons techniques), les temps d'attente peuvent être plus longs, notamment peu avant l'évaluation.  
Ainsi, envoyer fréquemment des ordres identiques pour obtenir une confirmation plus rapidement n’aide personne, cela ne fait qu’aggraver le problème.  

Cependant, si les ordres ont été envoyés correctement au serveur, ils sont généralement traités, même si aucune confirmation des ordres n'a été reçue avant évaluation.  
Pour des raisons techniques, aucune confirmation ne sera envoyée le samedi entre 20h45 et minuit.  
<!-- TODO: traduction ZAT ? -->
**Il est donc conseillé d'envoyer les ordres le plus tôt possible avant le ZAT de 21h00.**  

Si l'évaluation est retardée et finalement envoyée après 11h00 le dimanche matin (en raison de problèmes techniques ou d'erreurs dans le jeu), l'évaluation de la semaine suivante sera annulée.  

Si aucun ordre n'est reçu par le meneur du jeu au cours de cinq tours consécutifs (appelé "NMR", pour *`No Move Received`*), la faction est automatiquement dissoute !  

ECheck sur le serveur effectue uniquement des tests de syntaxe de base.  
Vous pouvez également télécharger ECheck sur votre ordinateur et utiliser ses options pour des tests plus avancés.  
Magellan a également intégré des tests approfondis qui rendent ECheck pratiquement inutile.  

## Demande

### Demander le rapport

Parfois, il peut arriver que l'e-mail contenant le rapport soit perdu quelque part en raison de pannes techniques.  
Si vous n'avez toujours pas reçu de rapport le lundi soir, et qu'il n'y a eu aucune annonce dans la liste d'annonces d'Eressea, vous pouvez demander à nouveau l'évaluation en cours.

Pour cela, envoyez un email à [eressea-server@kn-bremen.de] (car c'est le seul endroit où les données sont disponibles), avec l'objet suivant :

```text
ERESSEA 2 REPORT <faction-id> "<mot de passe>"
```

Cela signifie que tous les fichiers envoyés après l'évaluation régulière sont renvoyés à l'adresse requérante (qui peut être différente de l'adresse à laquelle le rapport est normalement envoyé), y compris le rapport informatique.

!!! warning
    Les factions avec des caractères spéciaux dans le mot de passe ne peuvent pas demander de rapport !

Ne demandez pas le rapport "rapidement" parce que vous ne l'avez pas sous la main pour le moment.  
De telles demandes génèrent un trafic inutile.  

*emails Eressea.*

| Concernant                                      | Avis                                        |
|-------------------------------------------------|---------------------------------------------|
| ERESSEA 2 ORDERS                                | Contient les ordres d'Eressea dans le texte |
| ERESSEA 2 REPORT <identifiant> "<mot de passe>" | Demande le rapport pour la faction          |

## Ce que vous devez considérer lors de la saisie des ordres

Chaque tour d'ordres doit commencer par la ligne [`ERESSEA xxx "<mot de passe>"`][cmd-eressea-fr]. *xxx* est l'identifiant de votre faction, et *mot de passe* est le mot de passe de la faction.  
Chaque tour doit se terminer avec le mot-clé [`NEXT`][cmd-next-fr].  

Tous les ordres sont émis par unité, même s'il s'agit d'ordres qui affectent la faction dans son ensemble; quelqu'un doit le faire.  

Si l'option a été activée, un modèle pour le prochain fichier d'ordres est toujours envoyé dans un fichier séparé.  
Voici un exemple d’un tel tour d'ordres :

```text
ERESSEA 2 "GrofxMoftzg"
; ECHECK -z -w4 -r100
REGION 4,2;     Handan
; ECHECK WAGE 12
UNIT 5;         Horde de Trolls [5,100$]
    LEARN mining
UNIT 36;        Danseur de la Mort [10,630$]
    ENTERTAIN
REGION 4,3;     Carcavelos
; ECHECK WAGE 11
UNIT 35;        Esclaves zombies [10,110$]
    WORK
REGION 5,3;     Grandola
; ECHECK WAGE 11
UNIT 32;        Reiter der Verdammnis [5,30$]
    LEARN Entertainment
NEXT
```

La première ligne avec ECHECK est destinée au vérificateur de syntaxe.  
Il reconnaît cette ligne et utilise les paramètres qui y sont spécifiés.  
Avec l'option `-z`, les personnes et leurs actifs en commentaire derrière l'ordre [`UNIT`][cmd-unit-fr] sont interprétés.  
Les revenus avec [`WORK`][cmd-work-fr] (généralement 11 silvers par personne), les [taxes][cmd-tax-fr] et le [divertissement][cmd-entertain-fr] (20 silver par personne) sont également pris en compte.  
Les compétences coûteuses telles que l'apprentissage de la magie avec l'ordre[`LEARN MAGIC`][cmd-learn-fr] et le déplacement d'unités transportant de l'argent (avec [`MOVE`][cmd-move-fr]) sont ensuite évalués et des avertissements sont émis s'il y a trop peu d'argent.  
`-w4` est le « niveau d'avertissement », 4 étant le niveau le plus verbeux.  
Et enfin, `-r100` indique que le coût de recrutement de cette faction est de 100 silver par personne.  

La ligne `; ECHECK WAGE 12` est également pour ECheck et fixe le salaire pour le travail dans cette région à 12 silver.  

On voit que les membres de l'unité 32 vont être affamés : 30 silver ne suffisent pas pour 5 personnes.  
Cependant, avec les paramètres ECheck `-z -w4` utilisés ci-dessus, ECheck le remarquera et émettra un avertissement.  
L'unité doit gagner de l'argent (par exemple avec [`ENTERTAIN`][cmd-entertain-fr] si elle possède déjà la compétence de divertissement, sinon avec [`WORK`][cmd-work-fr]).  
Une autre possibilité est qu'une autre unité avec suffisamment d'argent se déplace vers la région de coordonnées (5, 3).  

Tous les [[ordres]] peuvent être abrégés.  
L'ordinateur prend simplement le premier mot qui correspond à l'ordre saisi :

- `MO S` peut signifier soit `MOVE SOUTHEAST`, soit `MOVE SOUTHWEST`, auquel cas l'ordinateur ignore tous les autres ordres !
- `TE 5` signifie `TEMP 5`, mais `TE5` est un mot inconnu de l'ordinateur

En cas de doute, vous ne devez pas utiliser d'abréviations.  

Il ne peut y avoir qu'une seule commande par ligne.  
Si vous disposez d'un programme de messagerie qui renvoie à la ligne automatiquement les longues lignes de texte, vous pouvez répartir les ordres sur plusieurs lignes courtes;  
Mais il faut alors les « étendre » en ajoutant un `\` (antislash) :

```text
DESCRIBE unit "L'ancien guerrier existe depuis longtemps \
    mis au repos. Son visage marqué \
    témoigne d'une longue période de service au front."

Route Northwest West West Northwest Pause \
    Northwest Northeast Northwest Northeast Pause \
    Southwest Southeast Southwest Southeast Pause \
    Southeast East East Southeast Southeast Pause
```

Tous les ordres sont non sensibles à la casse.  
La seule exception à cette règle est le mot de passe, qui doit être **exactement** renseigné tel qu'il a été défini.  

Si des chaînes de caractères sont requises pour les ordres (par exemple pour un nom), elles doivent être placées entre guillemets si elles contiennent des espaces.  
Si nécessaire, ces chaînes de caractères peuvent être étendues sur plusieurs lignes, comme décrit précédemment.  
Entre les guillemets, plusieurs espaces, sauts de ligne et tabulations sont toujours compressés en un espace chacun.  

Tout texte qui suit un point-virgule (`;`) est considéré comme un [commentaire][cmd-comment-fr].  
Les commentaires peuvent faciliter la compréhension des ordres que vous effectuerez la prochaine fois.  
Si vous utiliser le [commentaire `//`][cmd-comment-with-slashes-fr], le commentaire sera automatiquement inclus dans le [modèle d'ordres][ordres] du tour suivant.  

Plusieurs ensembles d'ordres peuvent être envoyés.  
Vous pouvez certainement envoyer des ordres pour quelques unités seulement, et ainsi réduire le volume de transfert de données entre vous-même et le serveur.  
Les ordres des autres unités restent alors inchangés.  
La date de l'email (Date : en-tête) fait office d'ordre.  

## Voir aussi

- [Le Monde d'Eressea][world]
- [[first-round]]
- [[ordres]]

Poursuivre la lecture : [[remarques]].

<!-- From [https://wiki.eressea.de/index.php?title=Befehle\_einschicken&oldid=16786] -->

[eressea-server@kn-bremen.de]: mailto:eressea-server@kn-bremen.de

[Notepad++]: http://notepad-plus.sourceforge.net/
[Magellan]: http://magellan-client.sf.net

[cmd-comment-fr]: [[cmd-comment-fr]]
[cmd-comment-with-slashes-fr]: [[cmd-comment-with-slashes-fr]]
[cmd-entertain-fr]: [[cmd-entertain-fr]]
[cmd-eressea-fr]: [[cmd-eressea-fr]]
[cmd-learn-fr]: [[cmd-learn-fr]]
[cmd-tax-fr]: [[cmd-tax-fr]]
[cmd-move-fr]: [[cmd-move-fr]]
[cmd-work-fr]: [[cmd-work-fr]]
[cmd-next-fr]: [[cmd-next-fr]]
[cmd-unit-fr]: [[cmd-unit-fr]]
