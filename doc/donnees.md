Notes concernant les données RePEc
==================================

*Remarque: Une bonne partie des informations ci-dessus sont issues de [cette page](https://ideas.repec.org/getdata.html) sur le site IDEAS.*

Concernant les données auteurs
------------------------------

La base IDEAS (https://ideas.repec.org/), mise en place par la Banque Fédérale de Saint Louis (Etats-Unis), propose une interface web d'accès aux données de RePEc.
Concernant les données auteurs, on y trouve différentes sections parmi les quelles :

- https://ideas.repec.org/homonyms.html : la liste des auteurs pour lesquels il existe des homonymes. 418 homonymes sont répertoriés, soit 900 personnes en tout (en admettant les doublons).
  Remarque : Il s'agit d'une liste non exhaustive. Un outil comme [OpenRefine](http://openrefine.org/) pourrait être utilisé pour éventuellement en déceler d'autres.
- https://ideas.repec.org/i/elost.html : la liste des auteurs qui ne donnent plus signe de vie, c'est-à-dire dont les informations ne sont potentiellement plus à jour. 783 auteurs sont listés dans cette catégorie.

A noter que l'on trouvera des données statistiques d'accès aux données RePEc à l'adresse suivante: http://logec.repec.org/.


Le service *RePEc Author Service*
---------------------------------

*RePEc Author Service* est une interface réservée aux chercheurs en économie qui leur permet de garder à jour une page profil. Spécificités :

- Les détails de contact sont historisés et peuvent être retracés.
- Ce service donne lieu à la création d'un profil public qui liste tous les travaux de recherche (à la manière de ce que propose Google Scholar). Le profil en question est ensuite visible depuis le site [IDEAS](https://ideas.repec.org/i/e.html).
- Le profil d'un auteur peut être rattaché à tout travail dont il prétend être l'auteur.
- Un identifiant unique est créé pour chaque auteur (RePEc `Short-ID`).
- Cela permet de distinguer les travaux d'homonymes.
- L'auteur a accès à des données statistiques concernant ses travaux et les citations associés.
- Les données collectées sont utilisées pour des travaux en économie et en finance, incluant les auteurs et les institutions auxquels ils sont affiliés.

Ce service n'est pas conçu pour l'analyse de données, il n'y a aucun accès prévu à cet effet. Il faut passer par les dépôts (voir ci-dessous) ou le site IDEAS.


Accès aux données RePEc via API
-------------------------------

Depuis quelques mois (septembre 2015), le site IDEAS a mis en place [une API qui permet d'interroger la base RePEc](https://ideas.repec.org/api.html). Pour le moment, l'accès a cet API n'est pas public. Il faut faire une demande justifiée auprès des administrateurs pour pouvoir l'utiliser. La liste des méthodes qui peuvent être appelées n'est pas communiquée sur le site. Par contre, nous savons que les métadonnées sont retournées au format JSON.


Accès aux données RePEc via les dépôts
--------------------------------------

La [synthese-repec](synthese-repec.md) contient une section difinissant l'accès aux métadonnées RePEc.

Les données relatives aux auteurs sont accessibles via l'archive `RePEc:per`. Il s'agit d'un répertoire qui se situe au même niveau que les autres dans les dépôts RePEc. Dans notre cas, la copie est disponible à cette adresse : http://dev.repec.fr/remo/per/. A noter qu'il existe un [script Perl](ftp://repec.oru.se/RePEc/cpd/conf/migrate.cfg) qui met à jour les handles suite à la migration de certains identifiants de différentes institutions.


Les formats de données
----------------------

Dans le cadre de nos travaux, les formats de modèles qui nous intéressent sont les suivants :

- Working paper (paper)
    - template vide: https://ideas.repec.org/paper.rdf
	- documentation: https://ideas.repec.org/t/papertemplate.html
- Article (article)
	- template vide: https://ideas.repec.org/article.rdf
	- documentation: https://ideas.repec.org/t/articletemplate.html
- Chapitre (chapter)
	- template vide: https://ideas.repec.org/chapter.rdf
	- documentation: https://ideas.repec.org/t/chaptertemplate.html
- Livre (book)
	- template vide: https://ideas.repec.org/book.rdf
	- documentation: https://ideas.repec.org/t/booktemplate.html

La liste de tous les templates est disponible à cette adresse : https://ideas.repec.org/templates.html


### Qu'est-ce qu'un working paper (WP) ?

Particulièrement important en sciences économiques, le working paper est un document qui fournit les résultats détaillés d'une recherche. Dans le monde académique, il est considéré comme une *prepublication*, ou *preprint*, c'est-à-dire un projet d'article en attente de parution dans une revue scientifique. Le réseau RePEc est l'acteur majeur de la diffusion de la littérature grise en économie et notamment des working papers. [Source: [site de l'Université de Rennes 1](http://focus.univ-rennes1.fr/content.php?pid=467792&sid=5722677)]

[Econpapers](http://econpapers.repec.org) met à disposition sur son site un outil pour vérifier la bonne syntaxe des documents créés par les utilisateurs. Des emails sont envoyés tous les mois aux auteurs pour leur signaler des problèmes si des erreurs sont identifiées dans les documents qui ont été soumis.


Identifant unique pour les auteurs
----------------------------------

Chaque auteur se voit attribué un identifiant (`Short-ID`) qui est composé de trois lettres et d'un identifiant numérique :

- 1er caractère : p (pour *person*)
- 2ème et 3èmes caractères : deux premières lettres du nom de famille de l'auteur
- caractères suivants : valeur numérique (auto-incrémentée ?)

Exemple : https://ideas.repec.org/e/pfa122.html 

RePEc propose un service, [Author Short-ID Lookup](https://ideas.repec.org/cgi-bin/shortid.cgi), qui permet de retrouver les publications d'un auteur. Si l'on interroge l'outil avec le nom d'un auteur, l'application nous renvoie la liste des auteurs avec ce nom, accompagné du `Short-ID` associé.


Encodage des données
--------------------

RePEc supporte les standards [Unicode](https://fr.wikipedia.org/wiki/Unicode) UTF-8 et, depuis peu, UTF-16. Par conséquent, les fichiers au format ASCII, ISO-LATIN-1 et Windows-1252 sont pris en charge. Néanmoins, cela n'exclut en rien des problèmes d'encodage.
