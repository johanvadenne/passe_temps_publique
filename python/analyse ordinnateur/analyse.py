# FR: enregistre dans un fichier python sous forme de tableau, le nom de tous les fichiers et leurs dates de modification
# EN: saves in a python file as an array, the name of all files and their modification dates

import os
import time

# FR: crée un fichier python
# EN: creates a python file
fichier_python = open("cheminDate_001.py", "w+", encoding="utf-8")
fichier_python.write("cheminFichier = ")

# FR: parcours le dossier
# EN: browse the file
for chemins ,dossiers, fichiers in os.walk(r"D:"):
    
    # FR: parcours les fichier
    # EN: browse the files
    for fichier in fichiers:
        
        # FR: récupère le chemen du fichier
        # EN: retrieves the chemen from the file
        chemin = str(chemins)+"\\"+str(fichier)
        
        # FR: récupère la date de la dernière modification du fichier
        # EN: retrieves the date of the last modification of the file
        dateHeure = os.path.getmtime(chemin)
        dateHeure = time.strftime("%d/%m/%Y-%H:%M:%S",time.gmtime(dateHeure))
        
        print(str(chemin) + " : " + str(dateHeure))
        
        # FR: écrie le chemin + date
        # EN: write the path + date
        fichier_python.write("(\""+chemin + "\", \"" + str(dateHeure)+"\"),\n")

# FR: ferme le fichier
# EN: close the file
fichier_python.close()