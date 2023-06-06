import os
from rich.console import Console

console = Console

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

def creationNomFichierAutomatique(nomDossier, nomFichier, texte):
    while 1:
        reponse = input("voulez vous donner un nom à votre fichier? [o/n]: ")
        if reponse == "o":
            nomFichier = input("nom fichier ex:(fichier.txt): ")
            try:
                break
            except:
                print("le nom du fichier n'est pas valide")
        elif reponse == "n":
            for chemin ,dossier, fichier in os.walk(nomDossier):
                num = len(fichier)

            nomFichier = str(num).zfill(4) + nomFichier
            break
    chemin = nomDossier + "/" + nomFichier
    creationFichier(chemin)
    ecriture(chemin, texte)

def saisieInt(phrase):
    
    reponseInt = ""
    while not reponseInt.isdigit():
        reponseInt = input(phrase)
    return int(reponseInt)

def saisieFloat(phrase):
    
    reponseFloat = ""
    while 1:
        reponseFloat = input(phrase)
        try:
            float(reponseFloat)
            break
        except:
            None
    return float(reponseFloat)

#vérifie l'existance du chememin
def existe(repertoire):
    return (os.path.exists(repertoire))
    
#connection echoué
def connectionEchoue(texte):
    console.print("{}[red]Connection echoué[/red]".format(texte))