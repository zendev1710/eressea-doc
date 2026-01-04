---
# cSpell:locale fr, en
alias: cmd-password-fr
---
# PASSWORD

**`PASSWORD`**`["new-password"]`  

Cela réinitialise le mot de passe.  
Vous devez toujours l'utiliser en donnant l'ordre [[cmd-eressea]] dans le fichier d'ordres suivant.  
Seuls des lettres et des chiffres sont autorisés dans le mot de passe.  
Si le mot de passe contient des caractères illégaux, ceux-ci seront remplacés par des caractères autorisés aléatoires.  
L'ordre `PASSWORD` sans paramètres définit un mot de passe généré aléatoirement.  

Au début, chaque faction se voit attribuer un mot de passe aléatoire.  

Exemple :

```text
; la deuxième semaine du mois hearth fire
ERESSEA 11 "OldPassword"
PASSWORD "Incorrect" ; no effect
UNIT 75
    PASSWORD "MoftZga" ; s'applique à partir du prochain tour !
    [...]
        
; la dernière semaine du mois hearth fire
ERESSEA 11 "MoftZga"
[...]
```

<!-- TODO: clarify... what is a train !? an evaluation !? -->
Quelques précisions :

- Le mot de passe est le seul élément du fichier d'ordres qui soit sensible à la casse
- Le mot de passe doit être défini par une unité
- Le mot de passe qui était valide lors du dernier tour ou celui qui a été défini lors du dernier tour s'applique toujours au fichier d'ordres respectif.
  Le mot de passe des envois d'ordre précédents reste valable même si plusieurs fichiers d'ordre ont été envoyés pour le train d'ordres actuel dans lequel des mots de passe différents ont été définis
- Le mot de passe n'a été réinitialisé avec succès que si le message "The password was changed to ..." a été inclus dans l'évaluation

<!-- From [https://wiki.eressea.de/index.php?title=PASSWORD&oldid=6276] -->
