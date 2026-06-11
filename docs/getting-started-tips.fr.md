---
# cSpell:locale fr
alias: conseils-pour-debutants
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# Conseils pour débutants

Lorsque vous renseignez les ordres, assurez-vous d'avoir utilisé l'identifiant de faction et les identifiants d'unité corrects.  

[Définissez un mot de passe][cmd-password] et n'oubliez pas de le mémoriser.  

C'est plus intéressant pour tout le monde si vous donnes des noms originaux à votre faction et à toutes vos unités.  
N'oubliez pas qu'Eressea est un jeu de rôle fantastique : des noms comme « Les tortionnaires télécommandés de Barney » (oui, ça a vraiment existé !) ne correspondent pas à l'ambiance d'Eressea.  

Si vous avez le moindre doute ou la moindre question, le mieux est de contacter le [serveur Discord d'Eressea].  
Vous pouvez y accéder via un navigateur, un programme installé ou une application.  
On vous y donnera sans aucun doute des conseils pour vos premiers pas et vous aurez les réponses à vos questions.  
Vous pouvez également poser vos questions sur le [forum des Jeux PbEm].  
Eressea y possède son propre sous-forum.  

La plupart des joueurs utilisent [[magellan]], un programme client qui lit le CR (« Computer Report »), l'affiche clairement, aide à créer des ordres et montre de nombreuses erreurs.  

Il existe aussi [ECheck][echeck-fr-id], un programme qui vous permet de vérifier la validité de vos ordres.  
ECheck est exécuté automatiquement par le serveur lors de la réception des ordres et le résultat est renvoyé.  
Utilisez ECheck avec l'option `-e` pour vérifier si vos ordres sont interprétés comme prévu.  
ECheck vérifie uniquement la syntaxe des ordres.  
ECheck n'analyse pas la sémantique (c'est-à-dire le sens et la logique des ordres), mais il peut effectuer divers tests concernant l'argent lorsque le [[ordres|modèle d'ordres]] du serveur est utilisé.  

Fixez-vousi plusieurs objectifs.  
L'un de tes premiers objectifs devrait être d'explorer les environs.  
C'est le seul moyen de découvrir les régions montagneuses et forestières importantes où vous pourrez extraire du minerai et récolter du bois.  
Envoiez donc quelques unités composées d'un seul soldat et donnez-leur suffisamment d'argent pour subvenir à leurs besoins pendant un certain temps.  

!!! note "Remarque"
    N'oubliez pas de prendre en compte l'argent nécessaire au recrutement !  

Créez davantage d'unités et apprenez certaines compétences dont vous pensez avoir besoin lors des trois ou quatre prochains tours.  

Le [divertissement][cmd-entertain] est essentiel pour gagner de l'argent.  
Sans suffisamment d'argent, ta faction ne pourra pas se développer.  
Les [collecteurs d'impôts][cmd-tax] constituent également une bonne source de revenus;  
pour cela, il te faut, par exemple, des métaux ([exploitation minière][ressources-minieres]) ou du bois ([exploitation forestière][ressources-forestieres]) pour fabriquer des armes comme des épées ou des lances;  
et bien sûr, les collecteurs d'impôts doivent posséder les compétences d'armes appropriées ([collecte d'impôts][collecter-les-impots], [compétences d'armes][competences-de-combat]).  

La [perception][skill-perception-fr-id]{title="Perception"} est une compétence essentielle, souvent sous-estimée par les débutants.  
Seuls les [percepteurs][cmd-tax] peuvent repérer les unités camouflées et les empêcher de [piller][le-vol-la-methode-malhonnete] !  
Il est donc judicieux de recruter et d'entraîner au moins un percepteur par région dès le début.  
Il est également conseillé de construire des [châteaux][chateaux]{title="Castle"} rapidement, au moins au niveau 2, ainsi que des comptoirs commerciaux (compétences requises : [maconnerie][maconnerie]{title="Masonry"} et [extraction minière][extraction-miniere]{title="Mining"} pour la pierre et [[batiments|la construction des châteaux]]) afin de pouvoir [commercer][le-commerce].  
Bien sûr, il est également indispensable de former les marchands et les transports nécessaires (généralement de la cavalerie) et de les équiper [de chevaux et de chariots][chevaux-et-chariots].  
Comprendre le commerce n'est pas chose aisée pour les débutants, mais l'effort en vaut la peine.  

Les unités aux compétences coûteuses, comme [[tactique|les Tacticiens]], [[liste-des-competences|les Alchimistes]], etc., ne devraient être entraînées que plus tard, car leur entraînement consomme beaucoup d'argent (200 silver par tour).  
Entraîner des [[magie|Mages]] coûte encore plus cher, mais un mage maîtrisant des sorts de combat peut apporter un avantage considérable en combat.  
De plus, les mages de toutes les écoles de magie peuvent lancer un sort pour gagner de l'argent très tôt dans le jeu, ce qui rend un investissement initial rentable (surtout pour les races bénéficiant d'un bonus de +1 en Magie).  

Il serait également conseillé de prendre certaines précautions au cas où les voisins ne seraient pas très paisibles.  
En d'autres termes, un plan pour protéger ta faction contre les attaques une fois la période d'immunité initiale terminée.  

Ajoute de nombreux commentaires à tes fichiers d'ordres afin de bien comprendre le but de chaque action lors des tours suivants.  
Il est conseillé de regrouper les ordres par région, en prévoyant quelques lignes de commentaires pour chaque région.  
Un bon point de départ pour votre nouveau fichier d'ordres est le [[ordres|modèle d'évaluation]] ajouté à l'évaluation du tour suivant.  
Pour chaque unité, vous pouvez également indiquer ce qu'elle produit, pour qui, sa destination ou le type d'échange commercial qu'elle effectue.  

Exemple de commentaires :

```text
REGION 4,4 ; Lochinver
; Prendre garde à la horde des ténèbres
; combattre ?

UNIT zbt;           Fabricant d'arc Jog'nabat et son clan [4;100$]
    MAKE Swords
    GIVE sjur 5 Swords; il ne donne probablement que les 4 qu'il
                        ; avait au dernier tour

UNIT sjur;          Fuhrmann Sjur [2;243$]
    // Capacité: 420 = 7 pierres; et des pièces d'argent !
    GIVE 7jht 7 Stones
    ROUTE SW W PAUSE E NE PAUSE
```

Le commentaire suivant l'ordre [[cmd-unit]] est inséré dans le modèle d'évaluation par le programme ;  
après le nom de l'unité, entre crochets, figurent le nombre de personnes qui la composent et la somme d'argent dont elle dispose (ici, 4 personnes avec 100 pièces d'argent et 2 personnes avec 243 pièces d'argent).  

Attention aux coûts d'entretien.  
Les grandes unités consomment beaucoup d'argent, et sans ressources, la population mourra de faim.  
Il suffit qu'une seule de tes unités dans une région dispose de suffisamment d'argent pour nourrir toutes les autres.  
N'oublie pas les unités qui quittent la région !  

Durant les premiers tours, vous pouvez vivre de votre capital de départ, mais **vous aurez rapidement besoin d'un revenu régulier**.  
Ce capital de départ est généralement épuisé après 4 à 6 tours.  
Le moyen le plus rapide de générer des revenus est de travailler comme percepteur d'impôts et artiste, et le [commerce][le-commerce] de produits de luxe promet des profits importants à long terme.  

Planifiez soigneusement les premières semaines.  
Vous pourrez ainsi calculer précisément le nombre d'artistes, de percepteurs d'impôts, d'armuriers, de bûcherons, etc., que ous pouvez et devez recruter.  

Au début de la partie, les unités de plusieurs factions sont parfois positionnées à proximité les unes des autres.  
Coordonnez-vous et répartissez les tâches afin d'optimiser votre expansion.  
Maintenez le contact avec de nombreuses factions; cela rend le jeu plus palpitant et vous sera utile par la suite.  
En cas de conflit, sachez que vous n'êtes pas seul.  
Les contacts vous permettent d'échanger des informations, comme des données cartographiques;  
ils vous permettent de partager vos expériences et vos astuces, et l'apprentissage mutuel est particulièrement précieux.  

Pour contacter d'autres factions, obtenez la liste de celles de votre région à l'aide de l'ordre [`OPTION ADDRESSES`][cmd-option] et contactez-les directement.  
Utilisez l'ordre [`MESSAGE REGION`][cmd-message] pour signaler votre présence aux autres factions.  

Pour atteindre vos objectifs, ne lésinez pas sur les dépenses.  
Le capital de départ est destiné à l'investissement.  
Le premier mineur produit du fer à grande échelle, le deuxième forge des épées et le troisième entraîne des guerriers.  
De plus, vous pouvez entreprendre diverses autres tâches : cartographier, former des mages, construire des navires, bâtir un château, fonder une guilde de voleurs, créer une petite caravane commerciale avec des chevaux et des chariots...  
Pour ces tâches, vous pouvez créer de nouvelles unités.  

Il faut éviter les guerres, surtout dans la phase initiale : les unités précieuses sont perdues trop rapidement, les revenus sont trop faibles ou les approvisionnements en matériaux s'épuisent.  

Si vous êtes en contact avec une faction puissante, essauez de lui vendre quelque chose.  
Essayez d'abattre des arbres, d'extraire des pierres ou du fer.  
Il est judicieux de localiser ou de construire deux châteaux pour commercer entre eux.  
Pour cela, vous aurez besoin de marchands et de chariots.  
Achetez un chariot et 2 chevaux au seigneur du château, ou construisez-en un vous-même.  

Il n'est pas nécessaire d'être allié à des partenaires commerciaux.  
Utilisez l'ordre [[cmd-contact]] pour échanger des marchandises et de l'argent avec d'autres factions sans être allié.  

L'un des tableaux les plus importants de ce guide est la [[sequence-des-ordres]], qui indique l'ordre de traitement des ordres par le serveur.  
Il illustre, par exemple, que vous pouvez tout à fait donner des matières premières à un forgeron la semaine précédant le début de sa production ([[cmd-give]] est en position 14, [[cmd-make]] en position 22), mais vous ne pouvez pas lui donner de potions ni les utiliser immédiatement ([[cmd-use]] est en position 7).

Il n'y a pas de gagnants dans ce jeu.  
La partie dure jusqu'à ce que vous perdiez espoir ou que vos ennemis vous aient anéantis.  
Ensuite, si les maîtres du jeu le permettent, vous pourrez recommencer avec une nouvelle faction.  

Et surtout, n'oubliez jamais : ce n'est qu'un jeu ! Il est fait pour que tout le monde s'amuse.  
Ne vous laissez pas agacer ni emporter par des décisions hâtives : le joueur qui incarne les orcs méchants est probablement quelqu'un de bien...  

## Voir aussi

- [[trucs-et-astuces]]
- [[remarques]]
- [[premier-tour]]
- [[bases|Les bases]]

Poursuivre la lecture : [[xontormia-express]].

<!-- From [https://wiki.eressea.de/index.php?title=Anfängertipps&oldid=17013] -->

[serveur Discord d'Eressea]: https://discord.gg/JyAeYJw%7CDiscord
[forum des Jeux PbEm]: http://www.pbem-spiele.de/
