#!/bin/bash

# Définir les informations de connexion à la base de données
user="USER"
password="MDP"
database="BDD"

# Définir le répertoire de sauvegarde
backup_dir="/mon/chemin"

# Utiliser une variable pour stocker le numéro d'incrément
increment=1

# Construire le nom du fichier de sauvegarde avec l'incrément
backup_file="$backup_dir/$database"_"$increment.sql"

# Vérifier si le fichier de sauvegarde existe déjà
while [ -e "$backup_file" ]; do
    # Incrémenter la variable d'incrément si le fichier existe déjà
    increment=$((increment + 1))
    backup_file="$backup_dir/BugSafari_DEV_$increment.sql"
done

# Exécuter la commande mysqldump avec les informations de connexion
mysqldump -u "$user" -p"$password" "$database" > "$backup_file"

# Vérifier si la commande mysqldump s'est exécutée avec succès
if [ $? -eq 0 ]; then
    echo "La sauvegarde a été créée avec succès dans le fichier $backup_file"
else
    echo "Erreur lors de la création de la sauvegarde."
fi