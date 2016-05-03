all: help

help:
	@eval $$(sed -r -n 's/^([a-zA-Z0-9_-]+):.*?## (.*)$$/printf "%-20s %s\\n" "\1" "\2";/ ;	ta; b; :a p' $(MAKEFILE_LIST))

sinclude makefile.$(shell uname -n)

.PHONY: check
check:							## vérifier la présence des outils nécessaires
	bin/check-tools

.PHONY: push
push:							## pousser les modifications vers les dépôts git
	git push boulgour master
	git push github master

.PHONY: github
github:							## récupérer les modifications depuis github et synchroniser
	git pull github master
	git push boulgour master

.PHONY: boulgour
boulgour:						## récupérer les modifications depuis boulgour et synchroniser
	git pull boulgour master
	git push github master
