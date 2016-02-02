# Question ouvertes

## Comment identifier les publications d'un auteur correspondant à un WP ?

Ce sont des notices de type `Template-Type: ReDIF-Paper 1.0`. Reste à voir si l'information est stockée dans les fichiers ReDIF de l'archive `per`.

## Est-ce que cette l'information de classification d'une publication est présente de manière **fiable** dans la base ?

Dans les fichiers ReDif, la classification de la publication n'est pas obligatoire. Donc elle ne peut pas être présente de manière fiable.

## Quel est le taux de publications sans information de classification accessible directement dans la base ?

J'ai trouvé un script Perl installable facilement sur un serveur qui permet de parcourir les champs de fichiers ReDif : https://ideas.repec.org/c/rpc/script/paperscript.html. Ca peut être un moyen d'obtenir le taux des publications sans classification.

# Questions fermées

## Est-ce qu'il y a un *Template-Type* réservé aux Working Papers (`Author-Paper`) ?

Oui les enregistrements de type `Template-Type: ReDIF-Paper 1.0`, cf http://openlib.org/acmes/root/docu/redif_1.html.
