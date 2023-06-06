import os
from rich.console import Console

def nouveauFichier():
    dossier = [
    r"{}:\COURSPT",
    r"{}:\COURSNC",
    r"{}:\COURSDF",
    r"{}:\COURSMT",
    #r"{}:\PARTAGE",
    #r"{}:\COMPTE",
    #r"{}:\_Documentation Générale"
    ]

    cheminLocal = []
    dossierAnalyse = "dossier analyse"
    nomFichier = "nom dossier et fichier.txt"
    console = Console()
    lettreLecteur = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lettre = str
    NouveauFichier = []
    NouveauDossier = []
    texte = ""

#======================================================================= fonction =======================================================================#

    #vérifie l'existance du chememin
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

#======================================================================= fonction =======================================================================#

#======================================================================= connection NAS =======================================================================#

    #Cherche le lecteur NAS
    for i in lettreLecteur:
        cheminNAS = []
        connection = False
        for j in dossier:
            cheminNAS.append(j.format(i))

        #vérifie si les dossier son accecible
        for j in cheminNAS:
            if existe(j):
                connection = True
            else:
                connection = False
                break
            
        #si tous les dossiers sont accecible j'enregistre la lettre du lecteur et je sors de la boucle
        if connection:
            lettre = i
            break
        else:
            continue

        
#======================================================================= connection NAS =======================================================================#

#======================================================================= analyse des fichiers local =======================================================================#

    if not existe(dossierAnalyse):
        creationDossier(dossierAnalyse)

    for i in cheminNAS:

        cheminFichierLocal = str(i).split("\\")
        cheminFichierLocal = dossierAnalyse + "/" + cheminFichierLocal[-1] + ".txt"
        if not existe(cheminFichierLocal):
            creationFichier(cheminFichierLocal)
        cheminLocal.append(cheminFichierLocal)

#======================================================================= analyse des fichiers local =======================================================================#

#======================================================================= analyse fichier =======================================================================#


    if connection:
        for i in cheminNAS:
            console.print("{} connection [green]réussie[/green]".format(i))

        for i in range(len(cheminLocal)):
            fichierLocal = cheminLocal[i]
            listeDossierFichier = lectureFichier(fichierLocal)
            texte = ""
            for chemin ,dossier, fichier in os.walk(cheminNAS[i]):

                for j in dossier:
                    texte += "\n\n" + j

                    
                    #si il est déja enregistré affiché OUI
                    if j in listeDossierFichier:
                        print("\n\n")
                        console.print("[cyan]dossier[/cyan] [white]{}[/white] [chartreuse3]OUI[/chartreuse3]".format(j))
                        #sinon afficher NON
                    else:
                        console.print("[cyan]dossier[/cyan] [white]{}[/white] [red3]NON[/red3]".format(j))
                        NouveauFichier.append(j)
                        
                    print("\n")

                for k in fichier:

                    texte += "\n" + k

                    #si il est déja enregistré affiché OUI
                    if k in listeDossierFichier: 
                        console.print("[yellow]fichier [/yellow][white]{}[/white] [chartreuse3]OUI[/chartreuse3]".format(k))
                        #sinon afficher NON
                    else:
                        console.print("[yellow]fichier [/yellow][white]{}[/white] [red3]NON[/red3]".format(k))
                        NouveauFichier.append(k)
            ecriture(fichierLocal, texte)   


    ecriture(cheminFichierLocal, texte)
    print("\n\nnouveau dossier:{}\n".format("\n".join(NouveauDossier)))
    print("\n\nnouveau fichier:{}\n".format("\n".join(NouveauFichier)))

#======================================================================= analyse fichier =======================================================================#