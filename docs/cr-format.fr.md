---
# cSpell:locale fr
alias: format-cr
---
# Format CR

Le CR se compose de blocs, d'attributs et d'entrées de liste.  
Un bloc correspond généralement à un objet, un attribut à une variable de l'objet.  
Les blocs peuvent avoir des sous-blocs.

## Blocs

Les noms et le nombre de blocs ne sont pas prédéfinis.  
Selon le jeu et la version, différents blocs peuvent être contenus dans un fichier.  
Il est tout à fait légitime de créer un sous-ensemble de blocs, par exemple pour transformer un rapport complet en « juste » une carte.  

Les blocs sont désignés par un seul mot en majuscule composé uniquement des lettres A à Z.  
Les blocs peuvent avoir un identifiant composé d'un ou plusieurs entiers signés de 32 bits.  
Les identifiants sont uniques, chacun ne peut donc apparaître qu'une seule fois par bloc dans un CR.  
L'identifiant peut être suivi de ';' Un commentaire distinct suivra, mais cela doit être évité.

Les blocs sans identifiant sont toujours des sous-blocs du dernier bloc précédent avec identifiant.  
Un bloc de ce type peut apparaître plusieurs fois, mais une seule fois par bloc parent (ils sont, pour ainsi dire, uniques par rapport à l'identifiant du bloc parent).  

Exzmples :

```text
VERSION 16
REGION -3 -7
REGIONSMESSAGES
```

## Attributs

Les noms et le nombre d'attributs ne sont pas prédéfinis.  
Un attribut se compose de deux éléments : la valeur et la balise.  
La balise doit être composée de lettres et de chiffres, mais ne doit pas contenir d'espaces.  
La valeur est soit une liste d'un ou plusieurs entiers, soit une chaîne écrite entre guillemets.  
La valeur et la balise sont séparés l'un de l'autre par un point-virgule.  

Depuis la version 35, un attribut ne peut apparaître qu'une seule fois au sein d'un bloc.  
Dans les versions CR antérieures à 35, certains blocs violaient cette règle, comme le bloc `ADDRESSES`.  

Exemples :

```text
0 0;Bergbau
"Xandaryl";Insel
172;Turn
```

## Entrées de liste

Les attributs sans balise doivent être traités séparément.  
Il s'agit d'entrées dans une liste d'ordres, de messages, etc.  
En termes de structure, ils sont équivalents aux attributs de chaîne, mais n'ont pas de point-virgule ni de balise en fin de ligne.  

Exemple :

```text
"MAKE Horse"
"Thorin; a warrior"
"Thorin (thor) couldn't earn silver"
```

## Astuces d'implémentation

Il est préférable d'analyser le CR ligne par ligne.  
Après avoir lu une ligne, on vérifie d'abord s'il s'agit d'un bloc : les blocs sont les seuls qui commencent par une lettre.  
S'il ne s'agit pas d'un attribut mais qu'il commence par un `-` ou un nombre, il s'agit alors d'un attribut entier.  
Si cela commence par un `"`, il s'agit d'une entrée de chaîne ou de liste.  

### À propos des blocs

Vous analysez les blocs en lisant le nom du bloc (jusqu'au premier espace) puis les identifiants séparés par des espaces.  
Faites attention aux éventuels commentaires (pour les CR Eressea antérieurs à la version 36) !  

### Attributs de type Integer

Identifiez le nombre en recherchant jusqu'à trouver un `;`.  
Lisez ensuite le nom de la balise jusqu'à la fin de la ligne.  
Veuillez noter qu'il peut encore y avoir des espaces à la fin de la ligne ou autour du `;` pourrait rester là.  

### À propos des entrées de liste

Lisez jusqu'au prochain `"`.  
Attention, il peut certainement y avoir des points-virgules dans la chaîne.  
Si le `"` n'est plus suivi d'un point-virgule, c'est un élément de liste, sinon c'est un attribut de chaîne.  

### Attributs de type String

La chaîne a déjà été lue donc sautez le `;` , et trouvez le nom de la balise.  
Encore une fois, faites attention aux espaces autour du point-virgule ou en fin de ligne.  

### Pièges à éviter

- Un attribut de type entier peut être constitué de plusieurs nombres, comme des niveaux de compétences.
  Le nombre d'entiers n'est pas nécessairement le même pour les attributs portant le même nom, et il n'est pas toujours égal à 2 (c'est actuellement le cas, mais cela reste ouvert pour une expansion future).
- Lignes vides : il ne devrait pas y avoir de lignes vides dans un CR.
  Mais un bon analyseur devrait être capable de le gérer.
- Lignes invalides : les CR sont souvent tronqués car un outil de messagerie ou un éditeur a renvoyé à la ligne des lignes considérées trop longues.
  Dans ce cas, un avertissement doit absolument être émis et l'attribut doit être ignoré.
- CR/LF : Mac, Unix et Windows stockent chacun différemment la fin d'une ligne.
  L'analyseur doit être capable de reconnaître tous les formats.
- L'orthographe des balises doit être unique, c'est-à-dire ni adaptée ni convertie.
  Un bon analyseur reconnaîtra toujours deux balises comme identiques si elles diffèrent uniquement par leur capitale.
- Trémas : les chaînes et les balises peuvent contenir des trémas.
  Un bon analyseur reconnaît la translittération courante des trémas (notamment en allemand)
- Fin de fichier : il peut arriver qu'il n'y ait pas de saut de ligne après la dernière ligne du CR

## Blocs réservés et tags

- `VERSION` est le premier bloc du CR.
  Un bon analyseur doit traiter plusieurs blocs `VERSION` dans son entrée, et traiter ce cas comme si un deuxième rapport est à traiter (exemple : cat 1.cr 2.cr 3.cr | analyseur)
- `Turn` est une balise contenant l'âge (dans le jeu) du bloc.
  Les blocs au sein d'un CR peuvent être datés différemment, si, par exemple, un rapport a été compilé à partir d'informations collectées sur plusieurs cycles.
  L'attribut `Turn` doit indiquer la date des informations les plus récentes sur le bloc.
  Il est hérité entre les sous-blocs, donc si ces blocs représentent des versions plus récentes ou plus anciennes, ils doivent avoir leur propre attribut `Turn`.
  Les CR sans informations sur le tour sont mieux traités comme provenant du tour 0.
- `Konfiguration` est une balise dans le bloc `VERSION`.
  Il peut être utilisé pour décrire le contenu du CR, par exemple. avec le nom de l'outil qui l'a créé ou une description, par exemple « EMap-export ».
  La valeur `standard` est réservée au serveur Eressea.

## Voir aussi

- [Format d'un CR en détail] (site web en allemand), données recueillies et préparées par *The White Wolf* (tww)

<!-- From [https://wiki.eressea.de/index.php?title=CR\_Format&oldid=5847] -->

[Format d'un CR en détail]: http://dose.0wnz.at/thewhitewolf/cr-format
