# Concepts et principes

RePEc est avant tout une base de données bibliographiques
"*décentralisée*". Son fonctionnement est basé sur un "*protocole*" [^1]
appelé le protocole de [Guilford] et un format de fichier appelé
[Redif] pour *REsearch Documents Information Format*. Ce format est un
simple format texte.

[^1]: Les guillemets sont là à dessein comme on le verra plus bas.

[Guilford]: ftp://all.repec.org/RePEc/all/root/docu/guilp.html
[Redif]: ftp://all.repec.org/RePEc/all/root/docu/redif_1.html

A priori ce protocole ne sert pas qu'à diffuser les données
bibliographiques mais également des informations sur des sites, des
logiciels ou de la documentation (en fait diffuser des fichiers
Redif). C'est très récursif en fait.

Le principe est que des sites (au sens géographico-institutionnel[^2])
mettent **publiquement** à disposition des informations sur un site
(au sens interneto-informatique) qu'ils contrôlent. Cette mise à
disposition est faite en respectant certaines conventions qui
permettent à tous les membres d'un réseau de copier ces données chez
eux.

[^2]: Ça va du département d'économie d'une Université jusqu'à des éditeurs

De cette manière chaque membre du réseau a le contrôle de ses données
et une copie des données des autres membres du réseau. C'est l'aspect
"*décentralisé*" : le mec qui met a disposition les données est le
seul maître de celles-ci mais tout les membres du réseau en ont une
copie.

Pour participer à ce réseau il faut avoir un code (3 lettres
latines). Un ensemble d'individus (l'autorité du réseau) contrôle
l'attribution de ce code (histoire de ne pas avoir de doublon et de
s'assurer de la cohérence sémantique du réseau).

Une fois qu'on s'est vu attribué un code, en suivant une petite
procédure, on peut mettre en place un site (au sens informatique) qui
diffuse les informations voulues et qui récupère les données de tous
les autres (ou d'une partie des autres) sites du réseau grâce à un
logiciel ad-hoc. Ce site fait alors parti intégrante du "*réseau*". Un
tel site est appelée une *archive*.

Les données diffusées par un site sont organisées en groupe d'intérêt
commun (un journal, une équipe, etc.). Un groupe est appelée une
*série*. Une série est identifiée par un code de 6 lettres choisi par
l'administrateur de ce site.

# Conventions pratiques

Concrêtement, une archive, de code `aaa` par exemple, est juste un
répertoire accessible **publiquement** et anonymement via FTP ou
HTTP. Ce répertoire contient au moins 2 sous-répertoires :

  - `aaa` qui contient les fichiers Redif qu'il diffuse ;
  - `remo` (pour *remote*) qui contient une copie mirroir des autres
    sites du réseau, un répertoire par archive, chacun étant nommé par
    son code.

Le répertoire d'une archive, toujours de code `aaa`, contient des
fichiers Redif sous la forme suivante :

~~~~
RePEc
|
+-- aaa
|   |
|   +-- aaaarch.rdf
|   +-- aaaseri.rdf
|   +-- ...
|   +-- abcdef
|   |   |
|   |   +-- tata.rdf
|   |   +-- titi.rdf
|   |   +-- ...
|   +-- conf
|   |   |
|   |   +-- ..
|   +-- docu
|   |   |
|   |   +-- ..
|   +-- soft
|       |
|       +-- ..
|
+-- remo
    |
    +-- aab
    |   |
    |   +-- ...
    +-- xyz
    |   |
    |   +-- ...
    |
    +-- ...
~~~~

Les fichiers `aaaarch.rdf` et `aaaseri.rdf` sont des fichiers
Redif, appelés des *templates* d'archives, qui décrivent l'archive
elle même (son adresse ftp, son institution, etc.) ou les séries
(sémantique de la série, etc.) qu'elle gère. Chaque série contient les
données diffusées organisées comme on veut mais uniquement dans des
fichiers Redif.

Les répertoires `soft` et `conf` d'une archive contiennent des
logiciels et leur fichier de configuration. Ce sont soit des logiciels
utiles pour la gestion de l'archive elle-même ou plus généraux
permettant de manipuler les données pour offrir un service en
particulier.

Le répertoire `docu` contient des documentations diverses (des
logiciels diffusés par exemple).

Techniquement une archive particulière (le *core* du réseau, celle de
code `all`) diffuse comme seule information des fichiers Redif qui
décrivent les archives et les séries de chaque membre (site) du
réseau. En fait cette archive contient une copie des fichiers
`???arch.rdf` et `???seri.rdf` de toutes les archives membres. De
ce que j'en ai compris de la lecture du code des scripts disponible,
son adresse est <ftp://all.repec.org/RePEc>.

La plupart des sites d'un réseau diffuse des fichiers Redif qui ne
sont que des notices bibliographiques. Le format de ce fichier est
facile à analyser (*parser*) parce que c'est du texte. Il existe par
ailleurs une bibliothèque Perl, [redif-perl], qui permet de simplifier
ce travail.

[redif-perl]: http://openlib.org/acmes/root/docu/redif-perl.html

# Les *services* RePEc

RePEc est normalement une instance parmi d'autre d'un réseau utilisant
ce jeu de conventions. AMHA c'est le seul.

Un service offert par RePEc (comme [Ideas], [Econpapers][^3], [NEP],
etc.) est simplement une archive particulère qui permet de faire un
certain nombre de trucs à partir des données du réseau. Comme exemple
on peut citer : affichage en HTML des données redif, recherche dans
l'ensemble des données disponibles, classement, etc.

[^3]: Ce sont deux services quasi-identique mais à l'interface différente

[Ideas]: http://ideas.repec.org
[Econpapers]: econpapers.repec.org
[NEP]: http://nep.repec.org

Un service sort un peu du lot c'est **RePEc [Author] service**. Il
permet à des auteurs de s'enregistrer, de tenir à jour son profil
(institution de rattachement, email, etc.), de garder l'historique de
son profil, de s'attacher des publications (pour lever les ambiguités
sur les homonymies par exemple), d'être notifié régulièrement de
modification sur ses publications, etc.

[author]: https://authors.repec.org

Il me semble que c'est un service important pour ajouter de la
consistance à ce que l'on veut faire.

Malheureusement je n'ai pas trouvé la description technique de ce
service (qui n'est de toute façon pas automatique mais pas mal manuel
à ce que j'ai compris). Il me semble cependant que de toute façon les
données stockées là dedans ne sont pas toutes publiques ni
décentralisées.

# Remarques

Quelques trucs pas très clairement établis dans les docs et autres
critiques remarques sur l'ensemble sont listés ici :

  * le protocole de Guilford est a priori agnostique sur le contenu de
    ce qu'il diffuse et est annoncé comme tel. Malheureusement la
    documentation ne fait référence qu'à des trucs en économie et même
    explicitement lié à RePEc.
  
    Par ailleurs, aucun document diffusé ne semble définir
    explicitement les sites d'autorité (la copie de référence de
    `all`). Plus exactement les documents citent des emplacementes qui
    n'existent plus.
  
    Pour finir le document décrivant le *protocole* mélange concepts
    et *implémentation* et en fait l'implémentation est imposée.
  
    Tout ça n'aide pas à la compréhension du fonctionnement du bouzin.
  
  * le "protocole" de Guilford n'est pas un protocole au sens
    informatique. C'est une convention de nommage et de stockage.
  
  * le langage de prédilection de manipulation semble être Perl. C'est
    plutôt logique puisqu'il s'agit essentiellement de manipuler des
    fichiers textes et du web et que Perl est très bien adapté et
    rapide dans ce genre de situations. C'est la seule bonne nouvelle
    AMHA.
  
  * l'extension `.rdf` utilisées pour les fichiers Redif est
    particulièrement mal-venue dans le contexte de fichiers
    bibliographiques et de réseau ou on s'attendrait à du XML, ce qui
    n'est pas le cas.
  
  * tout ça est bien vieux et *complexe* à appréhender alors même que
    le principe de définition premier est annoncé comme la
    *simplicité*.
  
    Même à l'époque de la création du bouzin (années 1990) on avait des
    moyens de faire les choses plus *proprement* et efficacement. On
    voit bien que ça a manqué d'informaticiens (et que ça en manque
    encore quand on voit l'état des données de l'archive `all`).

# *Travail* en cours

Ce que je suis en train d'essayer de faire c'est un bon gros système
de mirroir bourrin automatique de toutes les données disponibles dans
le réseau RePEc. La première récupération risque d'être lente.

Construire un réseau de lien entre auteurs à partir des notices
bibliographiques récupérées devrait être faisable mais va surement
poser problème à cause des homonymies mais surtout des conventions de
nommage des auteurs qui ne sont pas les mêmes dans toutes les archives
AMHA.
