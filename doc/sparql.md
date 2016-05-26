#SPARQL - Infos et données

[SPARQL](https://www.w3.org/TR/rdf-sparql-query) est le standard permettant d'interroger une base de données de triplets RDF. Il est au web sémantique ce que SQL est aux bases de données relationnelles.  Il a été conçu et recommandé par le W3C (World Wide Web Consortium) en 2008. Il est l'acronyme de Simple Protocol And RDF Query Language.
 
Construire une requête SPARQL se fait par appariemment de graphes (*graph-matching* en anglais) : on recherche tous les éléments correspondants au graphe que l'on a spécifié comme patron dans la question.
 
La forme la plus classique d'une requête SPARQL est, comme en SQL, le `SELECT WHERE`. SPARQL possède de toutes manières plusieurs points communs avec SQL.
 
Pour écrire une requête, nous allons :

1. définir les espaces de noms utilisés (les URI que l'on a spécifié dans les triplets RDF).
 
2. identifier les variables dont on veut recevoir les valeurs résultat (clause `SELECT`).
 
Voici une requête SPARQL classique : 

```
prefix p1: <...>
prefix p2: <...>
...
SELECT ...
WHERE {
  ...
}
OFFSET ...
LIMIT ...
ORDER BY...
``` 
