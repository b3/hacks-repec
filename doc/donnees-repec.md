Notes concernant les données RePEc
==================================


Concernant les données auteurs
------------------------------

La base IDEAS (https://ideas.repec.org/), mise en place par la Banque Fédérale de Saint Louis (Etats-Unis), propose une interface web d'accès aux données de RePEc.
Concernant les données auteurs, on y trouve différentes sections parmi les quelles :

- la liste des auteurs pour lesquels il existe des homonymes. 418 homonymes sont répertoriés, soit 900 personnes en tout (en admettant les doublons).
	https://ideas.repec.org/homonyms.html. dRemarque: Il s'agit d'une liste non exhaustive. Un outil comme [OpenRefine](http://openrefine.org/) pourrait être utilisé pour éventuellement en déceler d'autres.
- la liste des auteurs qui ne donnent plus signe de vie; c'est-à-dire dont les informations ne sont potentiellement plus à jour. 783 auteurs sont listés dans cette catégorie.
	https://ideas.repec.org/i/elost.html

A noter que l'on trouvera des données statistiques d'accès aux données RePEc à l'adresse suivante: http://logec.repec.org/.


Le service "RePEc Author Service"
---------------------------------

"RePEc Author Service" est une interface réservée aux chercheurs en économie qui leur permet de garder à jour une page profil. Spécificités :

 - Les détails de contact sont historisés et peuvent être retracés.
 - Ce service donne lieu à la création d'un profil public qui liste tous
   les travaux de recherche (à la manière de ce que propose Google
   Scholar). Le profil en question est ensuite visible depuis le site
   [IDEAS](https://ideas.repec.org/i/e.html).
 - Le profil d'un auteur peut être rattaché à tout travail dont il   
   prétend être l'auteur.
 - Un identifiant unique est créé pour chaque auteur (RePEc Short-ID).
 - Cela permet de distinguer les travaux d'homonymes.
 - L'auteur a accès à des données statistiques concernant
   ces travaux et les citations associés.
 - Les données collectées sont utilisées pour des travaux en économie et
   en finance, incluant les auteurs et les institutions auxquels ils
   sont affiliés.

Ce service n'est pas conçu pour l'analyse de données, il n'y a aucun accès prévu à cet effet. Il faut passer par les dépôts (voir ci-dessous) ou la site IDEAS.


Accès aux données RePEc via API
-------------------------------

Depuis quelques mois (septembre 2015), le site IDEAS a mis en place [une API qui permet d'interroger la base RePEc](https://ideas.repec.org/api.html). Pour le moment, l'accès a cet API n'est pas public. Il faut faire une demande justifiée aux près des administrateurs pour pouvoir l'utiliser. La liste des méthodes qui peuvent être appelées n'est pas communiquée sur le site. Par contre, nous savons que les métadonnées sont retournées au format JSON.


Accès aux données RePEc via les dépôts
--------------------------------------

RePEc est un projet pensé de manière décentralisé qui recouvrent des données issues de différents sources. Certaines données ne sont accessibles que sur demande, en particulier celles liées à la vie privée (tels que des adresses emails par exemple). Pour un usage commercial des données, il est demandé de prendre contact d'abord avec les personnes en charge de RePEc.

Une [documentation est fournie](https://ideas.repec.org/stepbystep.html) pour qui souhaite mettre en place un serveur RePEc.

Les métadonnées principales ("core metadata") sont communiquées par les éditeurs. Certains services RePEc viennent par la suite enrichir ces données.
Chaque éditeur met à disposition ces métadonnées via le web ou un serveur FTP anonyme (c'est à dire qui ne nécessite pas d'identifiant). Les adresses qui donnent accès à ces données sont disponibles dans les modèles d'archive qui sont eux même référencés dans l'archive intitulé [RePEc:all](ftp://all.repec.org/RePEc/all/).
La manière standard pour acquérir les données de base est donc de passer par les archives des éditeurs. Pour ce faire deux outils en ligne de commande (développés en PERL), sont mis à disposition :

- remi: Mirror RePEc data. Ce programme permet de récupérer les données RePEc sur les différentes archives participantes. La version la plus récente est téléchargeable à l'adresse suivante : ftp://repec.oru.se/RePEc/cpd/soft/remi/remi_latest.zip
- ReDIF-perl: Il s'agit d'un programme pour parser les fichiers au format REDIF (.rdf) et vérifier leur syntaxe.  La version actuelle (2.70) est téléchargeable à l'adresse suivante : http://hubec.repec.org/ReDIF-perl/ReDIF-perl-2.70.tar.gz

L'outil [RePEc Data Check](http://econpapers.repec.org/check/) donne accès à des données statistiques sur les erreurs rencontrés lors du moissonnage des différentes dépôts.

Si il est possible d'accéder à toutes les données depuis un même dépôt (grâce à la réplication des archives au sein des institutions participantes), cela ne garanti en rien que les données ainsi récoltées soient correctes et à jour. La seule manière de s'assurer d'avoir les bonnes données est d'interroger le dépôt archives de chaque éditeur.

Sur le plan technique, les standards utilisés sont :

 - le format [REDIF](http://openlib.org/acmes/root/docu/redif_1.html) [Research Documents Information Format] (syntaxe de type clé/valeur);
 - le format [AMF](http://amf.openlib.org/doc/ebisu.html) [Academic Metadata Format] (syntaxe de type XML);
 - le protocole [OAI/PMH](https://www.openarchives.org/pmh/) [Open Archives Initiative - Protocol for Metadata Harvesting] pour l'échange et le moissonage de données.

Les données relatives aux auteurs sont accessibles via l'archive "RePEc:per". Il s'agit d'un répertoire qui se situe au même niveau que les autres dans les dépôts RePEc. Dans notre cas, la copie est disponible à cette adresse : http://test.boulgour.com/repec/remo/per/. A noter qu'il existe un [script PERL](ftp://repec.oru.se/RePEc/cpd/conf/migrate.cfg) qui met à jour les handles suite à la migration de certains identifiants de différentes institutions.


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

>Qu'est-ce qu'un working paper (WP) ? Particulièrement important en sciences économiques, le working paper est un document qui fournit les résultats détaillés d'une recherche. Dans le monde académique, il est considéré comme une prepublication, ou preprint, c'est-à-dire un projet d'article en attente de parution dans une revue scientifique. Le réseau RePEc est l'acteur majeur de la diffusion de la littérature grise en économie, et notamment des working papers. [Source: [site de l'Université de Rennes 1](http://focus.univ-rennes1.fr/content.php?pid=467792&sid=5722677)]

La liste de tous les templates est disponible à cette adresse : https://ideas.repec.org/templates.html

Econpapers met à disposition sur son site un outil pour vérifier la bonne syntaxe des documents créés par les utilisateurs. Des emails sont envoyés tous les mois aux auteurs pour leur signalité des problèmes si des erreurs sont identifés dans les documents qui ont été soumis.


Identifant unique pour les auteurs
----------------------------------

Chaque auteur se voit attribué un identifiant (Short-ID) qui est composé de trois lettres et d'un identifiant numérique :
- 1er caractère: p (pour "person")
- 2ème et 3èmes caractères: deux premières lettres du nom de famille de l'auteur
- caractères suivants: valeur numérique (auto-incrémentée ??)

Exemple : https://ideas.repec.org/e/pyu16.html 


Le site RePEc propose un service [Author Short-ID Lookup](https://ideas.repec.org/cgi-bin/shortid.cgi) qui permet de retrouver les publications d'un auteur.
Si l'on interroger l'outil avec le nom d'un auteur, l'application nous renvoie la liste des auteurs avec ce nom, accompagné du Short-ID associé.


Encodage des données
--------------------

RePEc supporte les standards [Unicode](https://fr.wikipedia.org/wiki/Unicode) UTF-8 et, depuis peu, UTF-16. Par conséquent, les fichiers au format ASCII, ISO-LATIN-1 et Windows-1252 sont pris en charge. Néanmoins, cela n'exclus en rien des problèmes d'encodage.


*Remarque: Une bonne partie des informations ci-dessus sont issues de [cette page](https://ideas.repec.org/getdata.html) sur le site IDEAS.*