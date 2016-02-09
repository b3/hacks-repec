Virtuoso est une solution de gestion de données de tous types (Relationnel, sémantique, etc..). Nous l'utiliserons
pour sa vocation de dépôt de triplets RDF.
Il permet de configurer précisement : 
 - le mot de passe administrateur
 - l'emplacement de la base de données
 - la mémoire allouée
 - les logs d'accès au serveur
 - le déploiement sur le port 80
 - l'accès au téléchargement des dumps

La plupart de la doc est en Bash (Unix). C'est donc compliqué de travailler avec Windows.

###Démarrage de virtuoso
virtuoso-t -f -c [chemin/vers/virtuoso.ini]
L'option -c permet de spécifier le fichier de configuration. Pour tester, il peut être instéressant d'ajouter l'option -f 
qui permet de garder al sortie dans la console (foreground).

Les logs d'exécution sont enregistrés dans le fichier virtuoso.log, (voir entrée ErrorLogFile de virtuoso.ini).


Accès à la console SQL de Virtuoso
Suivant l'installation choisie, exécuter la commande isql-v, /usr/local/virtuoso/bin/isql-v ou /usr/bin/virtuoso/bin/isql-v.


Accès à la page d'administration web de Virtuoso
Si le module conductor a été installé, l'interface d'administration est accessible 
à l'adresse http://localhost:[port]/conductor. 

_ Source : http://fr.dbpedia.org/wiki/D%C3%A9ploiement_de_Virtuoso#D.C3.A9marrage_de_virtuoso _

### Accès

Après installation, pour accéder à Virtuoso sur le dump REPEC de Bruno il suffit d'utiliser : http://test.boulgour.com:8890/. 

Voici le code utilisé pour tenter des requêtes SPARQL sur la base :

` ld_dir ('/home/repec/data/', '*.nt', 'repec-per');
set isolation='uncommitted';
rdf_loader_run(); `

Toutefois, le moteur retourne : "The statement execution did not return a result set".


