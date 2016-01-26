# Synthèse de compréhension - RePEc

## Introduction

Le RePEc (pour Research Papers in Economic) est une importante base de données décentralisée de publication en recherche 
sur l'économie. La base de données regroupe 460,000 articles de recherche, 1,500 revues et 720,000 articles, 15,500 chapitres 
de livres, 12,000 livres et 2,700 composants logiciels. Au total, on aurait 1,800,000 items. Plus outils permettent d'accéder 
à cette base de données, les plus populaires étant [IDEAS](http://ideas.repec.org), [EconPapers](http://econpapers.repec.org), [Inomics](https://inomics.com/top/economics), et [Socionet](https://socionet.ru).

## Accéder aux données auteurs

On peut accéder à différentes données : institutions, revues, articles, etc. Mais ce sont les données auteurs (nom, prénom, etc.)
qui nous intéressent. Pour les retrouver, l'outil le plus intéressant semble être IDEAS. Ce site permet d'accéder à toute 
la base de données RePEc. Authors permet lui aux auteurs de s'enregistrer, de s'authentifier et au besoin de modifier les 
informations le concernant. 

## Comment accéder aux métadonnées RePEc

RePEc est un projet pensé de manière décentralisée qui recouvrent des données issues de différents sources. Certaines données ne sont accessibles que sur demande, en particulier celles liées à la vie privée (tels que des adresses emails par exemple). Pour un usage commercial des données, il est demandé de prendre contact d'abord avec les personnes en charge de RePEc.
On trouvera la documentation qui explique comment mettre en place un serveur RePEc à l'adresse suivante : https://ideas.repec.org/stepbystep.html.
 
Les métadonnées principales (*core metadata*) sont communiquées par les éditeurs. Certains services RePEc viennent par la suite enrichir ces données. 
Chaque éditeur met à disposition ces métadonnées via le web ou un serveur FTP anonyme (c'est à dire qui ne nécessite pas d'identifiant).
Les adresses qui donnent accès à ces données sont disponibles dans les modèles d'archive qui sont eux même référencés dans l'archive intitulé `RePEc:all` (accessible ici : ftp://all.repec.org/RePEc/all/). 
Pour résumer, la manière standard pour acquérir les données de base est de passer par les archives des éditeurs. Pour ce faire deux outils en ligne de commande (développés en PERL), sont mis à disposition : 
 
- `remi` : Mirror RePEc data. Ce programme permet de récupérer les données RePEc sur les différentes archives participantes. Version actuelle : 1.4a 
   Téléchargeable à l'adresse suivante : ftp://repec.oru.se/RePEc/cpd/soft/remi/remi_latest.zip 
 
- `ReDIF-perl`. Il s'agit d'un programme pour *parser* (analyser) les fichiers au format ReDIF (`.rdf`) et vérifier leur syntaxe. Version actuelle : 2.70 
   Téléchargeable à l'adresse suivante : http://hubec.repec.org/ReDIF-perl/ReDIF-perl-2.70.tar.gz 

L'outil [RePEc Data Check](http://econpapers.repec.org/check) donne accès à des données statistiques sur les erreurs rencontrés lors du moissonnage des différentes dépôts.
 
Si il est possible d'accéder à toutes les données depuis un même dépôt (grâce à la réplication des archives au sein des institutions participantes), cela ne garanti en rien que les données ainsi récoltées soient correctes et à jour. La seule manière de s'assurer d'avoir les bonnes données est d'interroger le dépôt archives de chaque éditeur. 

Techniquement parlant, les standards utilisés sont : 
- le format ReDIF [Research Documents Information Format] (syntaxe de type clé/valeur) ;
  http://openlib.org/acmes/root/docu/redif_1.html 

- le format AMF [Academic Metadata Format] (syntaxe de type XML) ;
  http://amf.openlib.org/doc/ebisu.html

- le protocole OAI/PMH [Open Archives Initiative - Protocol for Metadata Harvesting] pour l'échange et le moissonage de données. 
  https://www.openarchives.org/pmh/ 
 
Les données relatives aux personnes (auteurs, éditeurs, ...) sont accessible via l'archive `RePEc:per` (via ce lien : ??????). A noter que les données de citations ne son 

## Les fichiers ReDIF

Un fichier ReDIF (Research Document Information Format) est un fichier texte de métadonnées concernant une publication 
(nom, prénom, organisme de rattachement). Ces derniers se présentent sous des répertoires, dont les noms se composent de trois
lettres. A l'intérieur, on retrouve les fichiers ReDIF. Un répertoire peut contenir plusieurs fichiers ReDIF, et c'est souvent
le cas. 

## Le format d'un fichier ReDIF

Un ReDIF se présente sous la forme d'un template (c-a-d un modèle sur lequel l'on doit se greffer) pour décrire son document. 

Là encore, il y a plusieurs types de templates :

- `Template-Type: ReDIF-Archive 1.0` pour les archives
- `Template-Type: ReDIF-Series 1.0` pour *series* templates
- `Template-Type: ReDIF-Paper 1.0` pour *working paper* templates
- `Template-Type: ReDIF-Article 1.0` pour *journal article* templates
- `Template-Type: ReDIF-Book 1.0` pour *book* templates
- `Template-Type: ReDIF-Chapter 1.0` pour *book chapter* templates
- `Template-Type: ReDIF-Software 1.0` pour *software component* templates

Ce qui nous intéresse c'est : working paper, journal articles, books, book chapter. Nous allons détailler les différents types 
de templates et leur organisation.

## Working paper

 - `Template-Type:`
 - `Author-Name:`
 - `Title:` 
 - `Handle:`

4 champs obligatoires, le reste est non-obligatoire. Dans le reste on retrouve le détail de l'identité de l'auteur 
(nom de famille, prénom etc.) son email, sa date de création, etc. Utile pour déceler des homonymes. Mais ces champs ne sont 
pas obligatoires donc on ne peut pas être sûrs.

Template vide : https://ideas.repec.org/paper.rdf
Documentation : https://ideas.repec.org/t/papertemplate.html

### Journal articles

 - `Template-Type:`
 - `Author-Name:`
 - `Title:`
 - `Handle:`

Même constat.

Template vide : https://ideas.repec.org/article.rdf
Documentation : https://ideas.repec.org/t/articletemplate.html

### Books

 - `Template-Type:`
 - `Title :`
 - `Provider-Name:`
 - `Handle:` 
 - `Author-Name:`
 - `Editor-Name :`

Parmi `Author-Name` ou `Editor-Name`, seul un doit être présent. Parfois on se retrouve qu'avec l'éditeur, parfois l'auteur, 
parfois les deux.

Template vide : https://ideas.repec.org/book.rdf
Documentation : https://ideas.repec.org/t/booktemplate.html

### Books chapters

 - `Template-Type:`
 - `Author-Name:`
 - `Title:`
 - `Handle:`
 
Template vide : https://ideas.repec.org/chapter.rdf
Documentation : https://ideas.repec.org/t/chaptertemplate.html

Les différents auteurs peuvent être indexés sous un grand nombre de noms différents. Par exemple : `John Maynard Keynes`, 
`John M. Keynes`, `Keynes John Maynard`, etc. Il y a aussi les préfixes et suffixes (Dr, Mr, Mrs, etc.), les erreurs d'orthographe,
les homonymes, etc. Cependant, le système d'enregistrement sur RePEc permet aux auteurs de retrouver automatiquement l'index sous 
lequel ils sont enregistrés.
