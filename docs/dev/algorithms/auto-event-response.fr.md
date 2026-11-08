---
# cSpell:locale fr
alias: reponse-automatisee-a-un-evenement
---
# Réponse automatisée à un événement

De nombreux événements d'Eressea sont aléatoires ou influencés par d'autres joueurs.  
Pour ne pas les manquer, ou mieux encore, pour y réagir de manière appropriée, vous devez d'abord décider quels événements vous souhaitez découvrir et comment procéder.  

## Messages

De nombreux événements peuvent être facilement identifiés en consultant les messages : effets magiques déclenchés, apparition de monstres, combats, faim, etc.  

Dans la plupart des cas, il suffit de rechercher le type de message et d'utiliser ses attributs.  

## Comparaison

Malheureusement, tout le reste ne peut généralement être vérifié qu'en comparant l'état actuel aux conditions de l'événement.  
Cela inclut la présence de certaines unités ou peuples, le passage d'unités ou de vaisseaux inconnus, etc.  

## Priorité

En principe, il est conseillé d'attribuer une priorité aux événements et de les traiter ensuite en fonction de cette priorité.  

## Réaction

Une fois les événements hiérarchisés, l'étape suivante consiste à identifier les unités concernées afin qu'elles puissent potentiellement réagir.  
Malgré cette hiérarchisation, réagir à plusieurs événements est complexe, car des événements secondaires peuvent également influencer les ordres d'une unité.  

<!-- TODO: replace outdaed example, the current remains here until a suitable alternative example is created -->
***exemple obsolète***: la famine n’empêche plus l’exécution d'ordres longs.
Exemple :

Une unité est affamée et des morts-vivants apparaissent.  
La famine devrait être prioritaire, car elle force l’exécution de l'ordre long `WORK`.  
Cela limite naturellement les réactions possibles à l’apparition des morts-vivants.  
Il n’est plus possible de se déplacer vers la région adjacente.  

Cependant, il est possible de modifier l’état du combat.  
Selon que vous soyez en position de force ou non, différentes réactions sont nécessaires.  

<!-- From [https://wiki.eressea.de/index.php?title=Automatisierung\_Ereignissreaktion&oldid=6434] -->
