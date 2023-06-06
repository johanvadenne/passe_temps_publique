from random import *
import os
from math import *
from nomPrenom import *
from nombrePremier import *
from rich.console import Console

console = Console()

############################################### Fonction


def utilisateurs():
    
    nombreUtilisateur = "str"


    #saisie
    while nombreUtilisateur.isdigit() == False:
        nombreUtilisateur = console.input("\n[sky_blue3]nombre d'utilisateur à générer: [/sky_blue3]")
    nombreUtilisateur = int(nombreUtilisateur)
    
    #taille des tableau -1
    nbrNom = len(noms) - 1
    nbrPrenomGarcon = len(prenomGarcons) - 1
    nbrPrenomFille = len(prenomFilles) - 1

    #tableau
    mesUtilisateurs = []

    #créer les utilisateurs
    for i in range(nombreUtilisateur):

        #nombre aleatoire entre 0 et 1
        gf = randint(0,1)

        #si 0 garçon si 1 fille
        if gf == 0:
            #récupère le prénom et le nom dans le tableau
            mesUtilisateurs.append(prenomGarcons[randint(0,nbrPrenomGarcon)] + " " + noms[randint(0, nbrNom)])
        elif gf == 1:
            #récupère le prénom et le nom dans le tableau
            mesUtilisateurs.append(prenomFilles[randint(0,nbrPrenomFille)] + " " + noms[randint(0, nbrNom)])

    #j'écris les utilisateur créer
    console.print("\n[chartreuse3]" + "\n".join(mesUtilisateurs) + "[/chartreuse3]")

    #j'ouvre le fichier mesUtilisateurs.txt
    fichier = open("mesUtilisateurs.txt", "w+", encoding="utf-8")

    #j'écris tout les utilisateurs que j'ai dans mon tableau
    for i in mesUtilisateurs:
        fichier.write(i + "\n")
    fichier.close()



accents = [["é","e"],["è","e"],["ê","e"],["ë","e"],["à","a"],["â","a"],["ä","a"],["ù","u"],["û","u"],["ü","u"],["ô","o"],["ö","o"],["î","i"],["ï","i"],["ÿ","y"]]

def genererMail():
    
    #vérifie si fichier existe
    if os.path.exists("mesUtilisateurs.txt"):

        #ouvre fichier en lecture
        fichier = open("mesUtilisateurs.txt", "r+", encoding="utf-8")
        texte1 = fichier.readlines()
        
        #si fichier vide
        if len(texte1) > 0:
            
            tableauGmail = []
            
            #créer l'adresse mail
            for i in texte1:
                for j in accents:
                    i = i.replace(j[0], j[1])
                i = i.lower()
                i = i.replace("-", ".")
                i = i.replace(" ", ".")
                i = i.replace("\n", "")
                tableauGmail.append(i+str(randint(1000, 9999))+"@gmail.com")
            
            #écrie les adresse mail
            fichier = open("mesUtilisateursMail.txt", "w+", encoding="utf-8")
            for i in tableauGmail:
                fichier.write(i + "\n")
                console.print("[chartreuse3]"+i+"[/chartreuse3]")
                
        else:
            console.print("[red]Vous n'avez pas créer d'utilisateur[/red]")

    else:
        fichier = open("mesUtilisateurs.txt", "w+", encoding="utf-8")
        console.print("[red]Vous n'avez pas créer d'utilisateur[/red]")

    fichier.close()


def motDePasse():
    lettresMinuscules = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lettresMajuscules = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    lettresSpeciaux = ["é","è","à","ù","ô","î","ö","ï","û","ü","â","ê","ë","ÿ"]
    chiffres = ["0", "1", "2", "3", "4", "5", "3", "7", "8", "9"]
    caracteresSpeciaux = [",",".","'",'"',"#","&","~","{","}","[","]","-","|","`","_","\\","@","°","(",")","/",";","!",":","?","*","+"]
    niveau = int
    longueur = int
    x = int
    motDePasse = ""

    #saisie
    while True:
        nbrMotDePasse = console.input("[sky_blue3]\nCombien de mot de passe voulez vous?[/sky_blue3]\n")
        if nbrMotDePasse.isdigit():
            if int(nbrMotDePasse) > 0:
                break
    nbrMotDePasse = int(nbrMotDePasse)
    while True:
        niveau = console.input("[sky_blue3]Quel est le niveau de sécurité de votre mot de passe?\n[1] très faible: lettre minuscule\n[2] faible: lettre minuscule + lettre majuscule\n[3] moyen: lettre minuscule + lettre majuscule + chiffre\n[4] fort: lettre minuscule + lettre majuscule + chiffre + lettre spéciale\n[5] très fort: lettre minuscule + lettre majuscule + chiffre + lettre spéciale + caractère spéciale\n[/sky_blue3]")
        if niveau.isdigit():
            if int(niveau) >= 1  and int(niveau) <= 5:
                break
    niveau = int(niveau)
    while True:
        longueur = console.input("[sky_blue3]Quel est la longueur de votre mot de passe (plus de 8)?\n[/sky_blue3]")
        if longueur.isdigit():
            if int(longueur) > 8:
                break
    longueur = int(longueur)

    #créer mot de passe
    for i in range(nbrMotDePasse):
        motDePasse = ""
        for i in range(longueur):
            x = randint(1,niveau)

            if x == 1:
                motDePasse += lettresMinuscules[randint(0, len(lettresMinuscules)-1)]

            elif x == 2:
                motDePasse += lettresMajuscules[randint(0, len(lettresMajuscules)-1)]

            elif x == 3:
                motDePasse += chiffres[randint(0, len(chiffres)-1)]

            elif x == 4:
                motDePasse += lettresSpeciaux[randint(0, len(lettresSpeciaux)-1)]

            else:
                motDePasse += caracteresSpeciaux[randint(0, len(caracteresSpeciaux)-1)]

        console.print("[dodger_blue1]" + motDePasse + "[/dodger_blue1]")


def genererNombrePremier():
    
    a = 1
    x = 0
    y = 0
    z = 0
    tableauNombrePremier = [2, 3]
    nombrePremier = True
    
    #saisie
    while True:
        b = console.input("[sky_blue3]Sasissé le chiffre maximal(Attention: au dessus de 1 000 000 cela peut prendre plus de 10sec)\n[/sky_blue3]")
        if b.isdigit():
            if int(b) > 0:
                break
    b = int(b)

    for i in range(4, b):
        x = sqrt(i)
        y = 1
        a = 0
        nombrePremier = True

        while y < x:
            y += 1
            z = i % tableauNombrePremier[a]
            a += 1
            if a > len(tableauNombrePremier) - 1:
                break
            
            
            if z == 0:
                nombrePremier = False
                break
        if nombrePremier:
            tableauNombrePremier.append(i)

    console.print("[pale_green3]" + str(tableauNombrePremier) + "[/pale_green3]")
    fichier = open("nombrePremier.txt", "w+", encoding="utf-8")
    fichier.write(str(tableauNombrePremier))
    fichier.close()

# =====================================================================================


def analyseDossierNas():

    console = Console()
    nouveauFichier = []
    nouveauDossier = []

    chemin_dossierCOURSPT = r"Z:\COURSPT"
    chemin_dossierCOURSNC = r"Z:\COURSNC"
    chemin_dossierCOURSDF = r"Z:\COURSDF"

    #mes fichiers locals
    fichierLocalModificationCOURSPT = open("nom_dossier_et_fichier_NAS_COURSPT.txt", "a+", encoding="utf-8")
    fichierLocalModificationCOURSNC = open("nom_dossier_et_fichier_NAS_COURSNC.txt", "a+", encoding="utf-8")
    fichierLocalModificationCOURSDF = open("nom_dossier_et_fichier_NAS_COURSDF.txt", "a+", encoding="utf-8")
    fichierLocalLectureCOURSPT = open("nom_dossier_et_fichier_NAS_COURSPT.txt", "r+", encoding="utf-8")
    fichierLocalLectureCOURSNC = open("nom_dossier_et_fichier_NAS_COURSNC.txt", "r+", encoding="utf-8")
    fichierLocalLectureCOURSDF = open("nom_dossier_et_fichier_NAS_COURSDF.txt", "r+", encoding="utf-8")
    nomFichierDossierLocalCOURSPT = fichierLocalLectureCOURSPT.read().split("\n")
    nomFichierDossierLocalCOURSNC = fichierLocalLectureCOURSNC.read().split("\n")
    nomFichierDossierLocalCOURSDF = fichierLocalLectureCOURSDF.read().split("\n")




    #si chemin existe
    def existe(chemin):
        return os.path.exists(chemin)


    #analyse chaque dossier et fichier
    def analyse(cheminNAS, listeDossierFichier, nomDossierNAS):

        priveNouveauFichier = [nomDossierNAS]
        priveNouveauDossier = [nomDossierNAS]
        tablex = []

        for chemin ,dossier, fichier in os.walk(cheminNAS):
            for nomFichier in fichier:
                if nomFichier in listeDossierFichier: 
                    console.print("[white]{}[/white] [chartreuse3]OUI[/chartreuse3]".format(nomFichier))
                else:
                    console.print("[white]{}[/white] [red3]NON[/red3]".format(nomFichier))
                    priveNouveauFichier.append(nomFichier)
            for nomDossier in dossier:
                if nomDossier in listeDossierFichier: 
                    console.print("[white]{}[/white] [chartreuse3]OUI[/chartreuse3]".format(nomDossier))
                else:
                    console.print("[white]{}[/white] [red3]NON[/red3]".format(nomDossier))
                    priveNouveauDossier.append(nomDossier)

        tablex.append(priveNouveauFichier)
        tablex.append(priveNouveauDossier)
        return tablex

    def recupereDonnee(chemin_dossier, nomFichierDossierLocal, fichier, nomDossierNAS):

        table = []
        table = analyse(chemin_dossier, nomFichierDossierLocal, nomDossierNAS)
        fichier.write("\n" + "\n".join(table[0]))
        fichier.write("\n" + "\n".join(table[1]))
        nouveauFichier.append(table[0])
        nouveauDossier.append(table[1])


    #si ces trois chemin exist
    if existe(chemin_dossierCOURSPT) and existe(chemin_dossierCOURSNC) and existe(chemin_dossierCOURSDF):

        #COURSPT
        console.print("\n\n\n[blue]Dossier COURSPT[/blue]:\n\n")
        recupereDonnee(chemin_dossierCOURSPT, nomFichierDossierLocalCOURSPT, fichierLocalModificationCOURSPT, "COURSPT")

        #COURSNC
        console.print("\n\n\n[purpul]Dossier COURSNC[/purpul]:\n\n")
        recupereDonnee(chemin_dossierCOURSNC, nomFichierDossierLocalCOURSNC, fichierLocalModificationCOURSNC, "COURSNC")

        #COURSDF
        console.print("\n\n\n[cyan]Dossier COURSDF[/cyan]:\n\n")
        recupereDonnee(chemin_dossierCOURSDF, nomFichierDossierLocalCOURSDF, fichierLocalModificationCOURSDF, "COURSDF")


        
    for i in nouveauFichier:
        if len(i) == 1:
            console.print("\n\n[yellow]fichier {} RAS[/yellow]".format(i[0]))
        else:
            console.print("\n\n[blue]nouveau fichier {}[/blue]".format(i[0]))
            print("\n".join(i))
            
    print("\n\n")
    
    for i in nouveauDossier:
        if len(i) == 1:
            console.print("\n\n[yellow]Dossier {} RAS[/yellow]".format(i[0]))
        else:
            console.print("\n\n[blue]nouveau dossier {}[/blue]".format(i[0]))
            print("\n".join(i))
            
    else:
        console.print("[red]connexion échoué[/red]")


    fichierLocalLectureCOURSPT.close()
    fichierLocalLectureCOURSNC.close()
    fichierLocalLectureCOURSDF.close()

    fichierLocalModificationCOURSPT.close()
    fichierLocalModificationCOURSNC.close()
    fichierLocalModificationCOURSDF.close()

    # =====================================================================================