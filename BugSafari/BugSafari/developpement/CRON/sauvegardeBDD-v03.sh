#!/bin/bash

# Définir les informations de connexion à la base de données
source .env
declare -a tableau_BDD=("BugSafari_PROD" "BugSafari_DEV" "BugSafari_TEST")
nbrBDD=${#tableau_BDD[@]}
indBoucle=0

# faire ceci pour toute les bases de données
while [ $indBoucle -ne $nbrBDD ]
do

    # récupère la date et l'heure du jour
    heure=$(date +%H%M)
    jour=$(date +%Y%m%d)
    dateHeure=$(date +"%Y/%m/%d %H:%M:%S") # Obtenir la date actuelle au format YYYY/MM/JJ hh:mm:ss
    milliseconds=$(date +"%N" | cut -c1-6) # Obtenir les millisecondes
    dateHeureMillisecondes="${dateHeure}.${milliseconds}"

    # récupère le nom de la BDD
    nomBDD=${tableau_BDD[$indBoucle]}

    # Définir le répertoire de sauvegarde et log
    repertoireSauvegarde="$CHEMINSAUVEGARDEBDD/$nomBDD/$nomBDD"_"$jour$heure.sql"

    # Exécuter la commande mysqldump avec les informations de connexion
    mysqldump -u "$USER" -p"$PASSWORD" "$nomBDD" > "$repertoireSauvegarde"

    # Vérifier si la commande mysqldump s'est exécutée avec succès
    if [ $? -eq 0 ]; then
        echo "$dateHeureMillisecondes : La sauvegarde a été créée avec succès $nomBDD." >> $LOGSAUVEGARDE
    else
        echo "$dateHeureMillisecondes : Erreur lors de la création de la sauvegarde $nomBDD." >> $LOGERREUR
    fi

    ((indBoucle++))
done