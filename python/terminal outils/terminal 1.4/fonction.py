import os

def existe(repertoire):
    return (os.path.exists(repertoire))

#créer dossier
def creationDossier(dossier):
    os.mkdir(dossier)
    
#créer fichier
def creationFichier(chemin):
    fichier = open(chemin, "w+", encoding="utf-8")
    fichier.close()
    
#ecrie dans un fichier
def ecriture(chemin, texte):
    fichier = open(chemin, "w+", encoding="utf-8")
    fichier.write(texte)
    fichier.close()
    
#lecture fichier
def lectureFichier(cheminFichier):
    fichier = open(cheminFichier, "r+", encoding="utf-8")
    lecture = fichier.read()
    fichier.close()
    return lecture