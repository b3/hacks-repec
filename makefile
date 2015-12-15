all:
	@echo "Tâches disponibles"
	@egrep -hB1 '^[^.: ]+:' $(MAKEFILE_LIST) | sed '1d;s/--//;s/:.*$$//;s/^/  /'

sinclude makefile.$(shell uname -n)

.PHONY: check
# vérifier la présence des outils nécessaires
check:
	bin/check-tools

.PHONY: push
# pousser les modifications vers les dépôts git
push:
	git push boulgour master
	git push github master
