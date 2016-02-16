# coding: utf8
# Handle data from RePEc:per
# Input file format : Redif [.rdf]
# Output file format : N-Triples [.nt]

# Auteurs: Christophe Willaert, Nahid Oulmi

import sys
import urllib2

# Flag utilisé lorsque l'utilisateur appelle la commande avec le paramètre -b ou --base-url
url_as_input = False


def affiche_aide():

	aide = """Produit des triplets RDF à partir d'un fichier ReDIF de l'archive per

usage: repec-person2nt [OPTIONS] FILE

FILE est un fichier ReDIF qui contient un seul enregistrement de type 'Template-Type: ReDIF-Person 1.0' tel qu'on les trouve dans l'archive 'per' de la base RePEc.

Les triplets RDF sont affichés au format \"Canonical N-Triple\" [1] sur la sortie standard.

Ces triplets mettent en relation :

 - un auteur à son nom
 - un auteur à ses articles
 - un auteur à sa date de dernière connection sur http://authors.repec.org
 - un auteur à une URL permettant d'accéder à une source ReDIF le définissant dans une copie de l'archive 'per'.

   Par défaut on utilise la copie de ce fichier dans l'archive de test (d'URL de base http://test.boulgour.com/repec/remo/per/pers).

L'auteur est identifié par son 'Short-Id' RePEc. Les articles sont identifiés par leur 'Handle' RePEc.

[1]: https://www.w3.org/TR/n-triples/

OPTIONS possibles :
    -h, --help          affiche ce message
    -b, --base-url      URL de base pour le lien source
""";

	print(aide)


def create_triple(subject, predicate, object):
    return '"' + subject + '" ' + predicate + ' "' + object + '" .' + '\n'


def parse_file(content, base_url):
	author   = ''
	name	 = ''
	articles = []
	papers   = []
	last_login = ''
	handle = ''
	creator_uri = '<http://purl.org/dc/elements/1.1/creator>'
	name_uri = '<http://xmlns.com/foaf/spec/#term_name>'
	modified_uri = '<http://purl.org/dc/terms/modified>'
	identifier_uri = '<http://purl.org/dc/terms/identifier>'
	source_uri = '<http://purl.org/dc/elements/1.1/source>'

	# On parcours chaque ligne du fichier à analyser
	for line in content:
		# Ici, on extrait les lignes contenants des clés/valeurs séparées par le caractère ':'
		key, value = line.partition(":")[::2]
		# Par sécurité, on passe la clé en minuscule
		key = key.lower()
		# On supprime les caractères espaces éventuels en début et fin de ligne
		value = value.strip()

		# Si la ligne contient le nom de l'auteur, on stocke la valeur dans la variable name
		if key == 'name-full':
			name = value

		# Si la ligne contient le Short-ID, on stocke la valeur dans la variable author
		if key == 'short-id':
		    author = value

		# Si il s'agit d'un working paper, on ajoute le handle de ce document à la liste 'papers'
		if key == 'author-paper':
		    papers.append(value)

		# Si il s'agit d'un article, on ajoute le handle de ce document à la liste 'articles'
		if key == 'author-article':
		    articles.append(value)

 		# Si il y a la date de dernière connexion (key), on la rajoute à la variable "last_login" (value) définie en haut
		if key == 'last-login-date':
			last_login = value

		if key == 'handle':
			handle = value
			

	nt_output = ''

	# On ajoute le triplet RDF qui fait le lien entre le Short-ID et le nom de l'auteur
	if name != '':
		nt_output += create_triple(author, name_uri, name)

	# On ajoute le triplet RDF qui fait le lien entre le Short-ID et la date de dernière connexion de l'auteur
	if last_login != '':
		nt_output += create_triple(author, modified_uri, last_login)

	# On ajoute le triplet RDF avec la source de l'auteur
	if handle != '':
		nt_output += create_triple(author, identifier_uri, '<' + handle + '>')

	# On ajoute le triplet RDF vers le fichier source utilisée
	nt_output += create_triple(author, source_uri, base_url)

	# On créé les triplets RDF pour chacun des working papers, que l'on stocke dans la variable 'nt_output' de type string
	for paper in papers:
		nt_output += create_triple('<' + paper + '>', creator_uri, author)

	# On créé les triplets RDF pour chacun des articles, que l'on stocke dans la variable 'nt_output' de type string
	for article in articles:
		nt_output += create_triple('<' + article + '>', creator_uri, author)

	# On envoi le tout à la sortie standard
	sys.stdout.write(nt_output)

	
# On supprime le premier argument qui retourne le nom du fichier appelé
del sys.argv[0]

# On boucle sur tous les arguments passés en paramètres (sauf le premier qui a été supprimé plus haut)
for arg in sys.argv:
	# Cas où l'utilisateur souhaite avoir l'aide
	if arg == '-h' or arg == '--help':
		affiche_aide()
		exit(0)
	# Cas où l'utilisateur passe en paramètre le chemin du fichier à parser
	elif arg == '-b' or arg == '--base-url':
		url_as_input = True
	else:
		# Si on a pas trouvé l'argument qui passe le chemin en paramètre, on affiche l'aide et on arrête le programme
		if url_as_input == False:
			affiche_aide()
			exit(0)
		else:
			# Sinon: il nous reste à récupérer l'url en argument (qui est passé en second paramètre, après -b/--base-url)
			base_url = arg

			# On tente d'ouvrir le fichier
			try:
				data = urllib2.urlopen(base_url)
				parse_file(data, base_url)
			# Si on ne parvient pas à ouvrir le fichier, on redirige l'erreur sur la sortie des erreurs (stderr)
			except IOError, err:
				sys.stderr.write(str(err) + '\n')

