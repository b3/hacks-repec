#SPARQL - Infos et données

 SPARQL est le standard permettant d'interroger une base de données de triplets RDF. 
 Il est au web sémantique ce que SQL est au bases de données relationnelles.
 Il a été conçu et recommandé par le W3C (World Wide Web Consortium) en 2008.
 Il est l'acronyme de Simple Protocol and RDF Query Language.
 
 Construire une requête SPARQL se fait par appariemment de graphes (graph-matching en anglais):
 on recherche tous les éléments correspondants au graphe que l'on a spécifié comme patron dans la question.
 
 La forme la plus classique d'une requête SPARQL est, comme en SQL, le SELECT WHERE. Le SPARQL possède de toutes manières 
 plusieurs points communs avec le SQL.
 
 Pour écrire une requête, nous en 1er allons définir les espaces de noms utilisés 
 (Ce sont les URI que l'on a spécifié dansles triplets RDF.)
 
 Puis, on identifie les variables dont on veut recevoir les valeurs résultat (clause SELECT).
 
 Voici une requête SPARQL classique : 
  prefix p1: <...>
  prefix p2: <...>
  ...
  select ...
  where {
	...
	}
  OFFSET ...
  LIMIT ...
  ORDER BY...
 
