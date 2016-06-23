# Structure de la machine `dev.repec.fr`

La machine `dev.repec.fr` héberge le développement des outils et les données récupérées. Elle est accessible via ssh pour l'utilisateur `repec` dont le répertoire de base est `/home/repec`.

Le répertoire de base est un clone du dépôt git `hacks-repec`. Les fichiers de configurations utilisateurs classiques (`.bashrc`, etc.) ne sont pas suivis par git. Certains répertoires ne sont pas suivis par git et servent à stocker les données, récupérées ou calculées :

- `data`
- `RePEc` est le répertoire de base au sens de RePEc
- `tmp`
- `www`

## Structure du répertoire `RePEc`

Les logs des actions menées sont dans le répertoire `log`.

Les copies locales des archives sont dans le répertoire `remo`, un répertoire par archive comme le spécifie la convention RePEc.

Les copies datées des archives de RePEc sont dans des répertoires de `snapshots`. Chacun des répertoires de `snapshots` correspond à la date de la copie et contient une copie intégrale du répertoire `remo` et du répertoire `log`. Les copies sont créées via des liens physiques sauf pour les fichiers différents.

`remo` est un lien symbolique vers le répertoire de `snapshots` qui correspond à la date de sa mise à jour.

## Création d'un mirroir

Quelques notes en vrac pour ne pas oublier

```shell
STAMP=$(date '+%F')
cd $HOME/RePEc
mkdir snasphots/$STAMP
cp -rl remo snasphots/$STAMP
cp -rl log snasphots/$STAMP
screen $HOME/bin/repec-mirror &
watch -n 5 "$HOME/bin/repec-trace ; $HOME/bin/repec-trace -w > $HOME/www/index.html"
```
