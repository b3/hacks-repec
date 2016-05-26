# Virtuoso

Virtuoso est une solution de gestion de données de tous types (Relationnel, sémantique, etc.). Nous l'utilisons pour sa vocation de dépôt de triplets RDF.

Il permet de configurer précisement : 

 - le mot de passe administrateur
 - l'emplacement de la base de données
 - la mémoire allouée
 - les logs d'accès au serveur
 - le déploiement sur le port 80
 - l'accès au téléchargement des dumps

La plupart de la documentation correspond aux commandes utilisable en shell (bash) sous Unix. C'est donc compliqué de travailler avec Windows.


## Démarrage de virtuoso

```
virtuoso-t -f -c [chemin/vers/virtuoso.ini]
```

L'option `-c` permet de spécifier le fichier de configuration. Pour tester, il peut être instéressant d'ajouter l'option `-f` qui permet de garder la sortie dans la console (foreground).

Les logs d'exécution sont enregistrés dans le fichier `virtuoso.log` (voir entrée `ErrorLogFile` de `virtuoso.ini`).


## Accès à la console SQL de Virtuoso

Suivant l'installation choisie, exécuter la commande `isql-v`, `/usr/local/virtuoso/bin/isql-v` ou `/usr/bin/virtuoso/bin/isql-v`.


## Accès à la page d'administration web de Virtuoso

Si le module **conductor** a été installé, l'interface d'administration est accessible à l'adresse `http://localhost:[port]/conductor`.

Source : http://fr.dbpedia.org/wiki/D%C3%A9ploiement_de_Virtuoso#D.C3.A9marrage_de_virtuoso

## Accès

Dans l'outil [Conductor](http://dev.repec.fr:8890/conductor/), une fois identifié (via l'identifiant/mot de passe), nous pouvons accéder à l'interface iSQL (Interactive SQL) pour exécuter des commandes sur la base de données, à l'aide des commandes SQL prise en charge par Virtuoso.

ISQL est accessible via l'onglet *Database*, puis *Interactive SQL*.

## Prise en main de la base de données

Nous trouverons ci-dessous quelques commandes qui permettent d'importer les données en base et de vérifier le bon fonctionnement des commandes exécutées.


### Afficher les informations sur le serveur

```
status();
```


### Vider un graphe nommé

```
SPARQL CLEAR GRAPH <repec-per>;
```


###  Pré-charger les données

```
ld_dir('/home/repec/data', 'n-triples-*.nt', 'repec-per');
```


### Lister les fichiers qui sont dans la file d'attente

```
SELECT * FROM DB.DBA.load_list;
```

NB: une fois le chargement effectué, si tout c'est bien passé, la valeur ll_state doit être égale à 2


### Vider la mémoire tampon pour le pré-chargement

```
DELETE FROM DB.DBA.load_list;
```


### Importer les données qui sont dans la file d'attente

``` 
set isolation='uncommitted';
rdf_loader_run();
```

### Retourner le nom de fichiers qui ont été correctement chargés

```
SELECT COUNT(1) FROM load_list WHERE ll_state=2;
```
