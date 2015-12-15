makefile := $(lastword $(MAKEFILE_LIST))

all:
	@echo "Choisir une cible"
	@egrep -B1 '^[^.: ]+:' $(makefile) | grep -ve '--' | sed -e 1,2d -e 's/:.*$$//'

.PHONY: push
# pousser les modifications vers les dépôts git
push:
	git push boulgour master
	git push github master
