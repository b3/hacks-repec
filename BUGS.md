# Les bugs identifiés

## dump

Les archives suivantes posent problème :

* `ntu` : on a une boucle infinie lors du téléchargement 

## robots.txt interdisant l'accès

Certaines archives virent tout le monde via un `robots.txt`. `dul` par exemple
exclut explicitement les *spiders*. Je ne comprends pas comment ils peuvent
partager leur données du coup.

J'ai ajouté `-e robots=off` mais ça n'est pas suffisant pour `dul` par exemple.

En attendant j'utilise [`bin/repec-mirror-quick`](bin/repec-mirror-quick) plutôt que le téléchargement archive par archive.
