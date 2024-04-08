#!/bin/bash

# Définir les informations de connexion à la base de données
user="sauvegarde"
password="pwd"
declare -a tableau_BDD=("BugSafari_PROD" "BugSafari_DEV" "BugSafari_TEST")
nbrBDD=${#tableau_BDD[@]}
indBoucle=0

# faire ceci pour toute les bases de données
while [ $indBoucle -le $nbrBDD ]
do

    # récupère la date et l'heure du jour
    heure=$(date +%H%M)
    jour=$(date +%Y%m%d)

    # récupère le nom de la BDD
    nomBDD=${tableau_BDD[$indBoucle]}

    # Définir le répertoire de sauvegarde et log
    repertoireSauvegarde="/home/johan/sauvegardeTest/$nomBDD/$nomBDD"_"$jour$heure.sql"
    repertoireLogSuccees="/var/log/bdd/sauvegarde.log"
    repertoireLogErrreur="/var/log/bdd/erreur.log"

    # Exécuter la commande mysqldump avec les informations de connexion
    mysqldump -u "$user" -p"$password" "$nomBDD" > "$repertoireSauvegarde"

    # Vérifier si la commande mysqldump s'est exécutée avec succès
    if [ $? -eq 0 ]; then
        echo "La sauvegarde a été créée avec succès $nomBDD." > $repertoireLogSuccees
    else
        echo "Erreur lors de la création de la sauvegarde $nomBDD." > $repertoireLogErrreur
    fi

    ((indBoucle++))
done