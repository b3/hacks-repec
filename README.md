# Hacks RePEc

On trouve ici quelques scripts et autres documents utilisés pour *jouer* avec
la base [RePEc](http://repec.org).

Le but final est de pouvoir construire un service de visualisation/étude du
réseau de co-auteurs en économie sur des *snapshots* complet des données de la
base à des moments différents.

Dans un premier temps on essaie :

1. de mettre au point de simples scripts permettant de disposer d'un *dump*
   (le plus complet possible) des données bibliographiques publiques
   disponibles dans [RePEc](http://repec.org) ;

2. de générer un graphe des liens entre co-auteurs à partir des données
   bibliographiques récupérées.

Pour cela il est nécessaire de comprendre et documenter le fonctionnement
technique de cette base.

L'état d'avancement de la tentative de récupération des notices
bibliographiques de la base est accessible en ligne sur
<http://dev.repec.fr>.


# Contenu

* [`bin`](bin) contient les scripts et programmes créées
* [`doc`](doc) contient des documentations (synthèse, listes de références, conventions de nommage, CR de réunions, etc.)
* [`ext`](ext) contient les archives d'outils extérieurs récupérés

ATTENTION: installer gnu-sed sous OS X (par exemple: brew install gnu-sed --with-default-names) car 
sinon l'option -r ne sera pas reconnue avec le sed installé par défaut par Apple.

ATTENTION: base64 -D (sous OS X) et -d (sous Linux)

# Droits

Copyright (C) 2015-2016 Bruno BEAUFILS.

Les scripts distribués ici le sont sous les termes de la *licence général
publique GPL, version 2*, disponible dans le fichier [GNU-GPL](GNU-GPL).

Les autres documents distribués ici sont mis à disposition selon les termes de
la *licence Creative Commons Attribution - Pas d’Utilisation Commerciale -
Partage dans les Mêmes Conditions 4.0 International* (CC-BY-NC-SA), disponible
dans le fichier [CC-BY-NC-SA](CC-BY-NC-SA).
