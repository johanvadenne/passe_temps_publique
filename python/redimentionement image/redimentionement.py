from PIL import Image
import os

# Définition de la nouvelle taille
nouvelle_taille = (300, 300)

for chemin ,dossier, fichiers in os.walk("D:/chemin"):
    for fichier in fichiers:
        print(str(chemin)+"/"+str(fichier))
        monchemin = str(chemin)+"/"+str(fichier)
        moncheminBis = monchemin.replace("/dossier/", "/dossierBis/")
        # Ouverture de l'image à redimensionner
        image = Image.open(monchemin)
        # Affichage des dimensions de l'image originale
        print("Dimensions de l'image originale:", image.size)
        # Redimensionnement de l'image
        image_redimensionnee = image.resize(nouvelle_taille)
        # Enregistrement de la nouvelle image
        image_redimensionnee.save(moncheminBis)
        # Affichage des dimensions de la nouvelle image
        print("Dimensions de la nouvelle image:", image_redimensionnee.size)
