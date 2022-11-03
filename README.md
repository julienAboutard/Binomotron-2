# Binomotron Enhanced

Équipe : Julien et Vincent

## Contexte du projet

Ce brief est la suite de https://simplonline.co/briefs/ee7ef768-a817-49bb-9c80-05a828744007

On veut désormais pouvoir créer des groupes de plus de 2 apprenants (des "n-ômes", les assigner à des briefs et stocker les résultats.

➡ La base de données doit être adaptée pour respecter ce besoin avec

* une table 'brief' contenant le nom du brief, son lien sur Simplonline et le nombre d'élèves par groupe.

➡ Le programme doit pouvoir prendre 2 paramètres :

* L'identifiant du brief auquel assigner les groupes
* Un "flag" au choix :
    * --list : Si présent, liste simplement les groupes du brief, sinon les crée
    * --create : Si présent, crée les groupes pour le brief, sinon les liste

➡ Les groupes créés peuvent être stockés en base, ou d'une autre manière, par exemple en JSON. Ce choix ainsi que son implémentation est laissé libre.

⚠️ Le programme ne doit PAS écraser une liste de n-ômes déjà créée

⚠️ Le programme doit gérer les cas où ses paramètres sont mal passés

## Liste des fichiers

binomotron.py  
binomotron-script-data.py  
"Binomotron MCD".jpg  

## Détails techniques

Environnement : Python 3.10.7  
Installation : MariaDB + MariaDB Connector/MySQL Connector  
Développé via VS Code
