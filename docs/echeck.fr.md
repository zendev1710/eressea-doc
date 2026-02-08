---
# cSpell:locale fr
alias: echeck-fr
---
# ECheck

 **EVérifiez** est le vérificateur d'ordres, qui fonctionne également sur le serveur d'Eressea.  

ECheck n’est ni parfait ni complet.  
Ses résultats peuvent contenir des faux-négatifs et des faux-positifs.  
Ainsi, si ECheck ne signale aucune erreur, cela ne signifie pas nécessairement que les ordres sont tous corrects.  
Si ECheck signale des erreurs, cela ne signifie pas non plus nécessairement que les ordres ne sont pas valides.  

Surtout lorsqu'il y a des changements de règles ou des objets rares, ECheck ne le sait pas toujours immédiatement.  
ECheck est davantage destiné à aider à vérifier à nouveau les ordres si nécessaire.  

ECheck est accessible de différentes manières :

- Lors de l'envoi des ordres, ECheck est automatiquement appelé et l'email de réponse du serveur contient le résultat.
  Dans ce contexte, nous vérifions uniquement avec un niveau d'avertissement à 1 (voir ci-dessous)
- Dans Magellan : ici, vous pouvez définir les options comme vous le souhaitez.
  Magellan peut également ajouter automatiquement les "méta-ordres".
  Ce sont des commentaires qui aident ECheck, par exemple, à vérifier la consommation d'argent.
  Cependant, il n'y a en réalité aucune raison d'utiliser ECheck de Magellan, puisque les mécanismes propres de Magellan (vérification de syntaxe et "problèmes ouverts") sont plus fiables et peuvent faire plus.
- Sur la ligne de commande (invite de commande « cmd » sous Windows, dans n'importe quel terminal sous Linux).
  Là, vous devez spécifier les paramètres répertoriés ci-dessous.

Il existe différents niveaux d'avertissement contrôlés par les paramètres de ligne de commande.  
Avec `-w1`, seules les erreurs de syntaxe sont affichées.  
Les niveaux d'avertissement `w2` à `w4` émettent des avertissements supplémentaires, concernant par exemple la consommation d'argent, les enseignants ou les itinéraires.  
Le paramètre `noxxx` peut également supprimer certains avertissements.  
ECheck suppose normalement que vous renseignez des ordres en allemand pour Eressea.  
Les ordres en anglais peuvent être vérifiés avec le paramètre `-Len`.  

## Utilisation

```console
Usage: ./echeck [options] <orders file>

  -Ppfad  Path information for the additional files; the locale de is appended
  -Rgame  Read additional files from the game subdirectory; Default setting: e2
  -       Uses stdin instead of an input file.
  -b      suppresses warnings and errors (letter)
  -q      does not expect any information on people/silver in [] at UNIT
  -rnnn   Sets recruitment cost to nnn silver
  -c      writes the warnings and errors in a compiler-like form
  -m      writes the warnings and errors for Magellan
  -e      writes the checked file to stdout, error to stderr
  -E      writes the checked file to stdout, error to stdout
  -ofile  writes the checked file to the file 'file'
  -Ofile  writes errors to file 'file'
  -h      shows this little help
  -hs     shows list of keywords for tokens.txt
  -hb     shows list of orders for orders.txt
  -hp     shows list of parameters for parameter.txt
  -hr     shows list of directions for directions.txt
  -hm     shows list of messages for messages.txt
  -hf     shows list of files that ECheck is trying to read
  -s      uses stderr for warnings, errors etc., not stdout
  -p      shortens some expenses for piping
  -l      simuliert Silberpool-Funktion
  -n      Does not count NameMe comments (;;) as a line
  -noxxx  No xxx warnings. xxx can be:
    ship  Unit controls ship and may not have command
    route no check for cyclic ROUTE
    lost  Unit loses silver and items
  -w[n]   Level n warnings (default: 4)
     1    mainly syntax errors
     4    almost all warnings
     5    teacher/student
  -x      Line countingab PARTEI instead of the beginning of the file
  -Lloc   Sets locale loc
  -vm.l   Mainversion.Level - für Test, ob richtige ECheck-Version
  -Q      Quiet
  -C      Compact edition
```

## Voir aussi

- [[envoi-des-ordres]]

## Liens externes et téléchargements

- [Téléchargement pour Windows (echeck.exe) et Linux (echeck)]
- [Code source d'ECheck]
- [Une version obsolète d'ECheck pour Windows]

<!-- From [https://wiki.eressea.de/index.php?title=ECheck&oldid=7268] -->

[Téléchargement pour Windows (echeck.exe) et Linux (echeck)]: https://www.eressea.kn-bremen.de/downloads
[Code source d'ECheck]: https://github.com/eressea/echeck
[Une version obsolète d'ECheck pour Windows]: https://www.eressea.de/files/echeck.zip
