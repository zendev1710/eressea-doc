---
# cSpell:locale fr
alias: cmd-password-fr
---

# `PASSWORD`

**`PASSWORD`**`["new-password"]`  

Cette instruction réinitialise le mot de passe de votre faction.  

!!! info "Rappel"
    L'ordre [`ERESSEA`][cmd-eressea-fr] doit être défini dans le lot d'ordres pour que l'instruction soit prise en compte.  

**Seuls des lettres et des chiffres sont autorisés dans le mot de passe**.  

Si le mot de passe contient des caractères illégaux, ceux-ci seront remplacés par des caractères autorisés aléatoires.  
L'ordre `PASSWORD` sans paramètres définit un mot de passe généré aléatoirement.  

Au premier tour après l'inscription, chaque faction se voit attribuer un mot de passe aléatoire, renseigné dans le rapport.  

Le mot de passe doit être défini **par une unité**, comme dans cet exemple :

```text
; la deuxième semaine du mois hearth fire
ERESSEA 11 "OldPassword"
PASSWORD "Incorrect" ; pas d'effet (l'ordre doit être passé par l'unité, comme ci-dessous)
UNIT 75
    PASSWORD "MoftZga" ; s'applique à partir du prochain tour !
    [...]
```

Le message `The password was changed to ...` est inclus dans le rapport suivant si le mot de passe a été réinitialisé avec succès.  

Le fichiers d'ordres suivants devront contenir le nouveau mot de passe :

```text
; la dernière semaine du mois hearth fire
ERESSEA 11 "MoftZga"
[...]
```

!!! note "Note"
    Lors de l'ouverture d'un rapport avec [Magellan][magellan-fr-id], le mot de passe renseigné dans le rapport est associé à la faction concernée, et mémorisé sur confirmation.  
    Magellan inscrit ensuite automatiquement les ordres `ERESSEA` et `PASSWORD` dans le fichier d'ordres à [envoyer][envoi-des-ordres-depuis-magellan].  

<!-- TODO: improve, remarks are not very clear -->
Remarques :

- le mot de passe est le seul élément du fichier d'ordres qui soit sensible à la casse
- le mot de passe qui était valide lors du dernier tour ou celui qui a été défini lors du dernier tour s'applique toujours aux fichiers d'ordres respectifs
- le mot de passe des envois d'ordre précédents reste valable même si plusieurs fichiers d'ordres ont été envoyés pour le lot d'ordres actuel dans lequel des mots de passe différents ont été définis

<!-- From [https://wiki.eressea.de/index.php?title=PASSWORD&oldid=6276] -->

[cmd-eressea-fr]: [[cmd-eressea-fr]]
