import os
from rich.console import Console
from fonction import *
import shutil
import aspose.words as aw
import time

def rechercheDevoir():
    dossierNAS = ["COURSPT","COURSNC","COURSDF"]
    
    fichierNAS = [r"{}:\COURSPT\01-AP\[SLAM1] AP CahierDeTexte.md",
                  r"{}:\COURSPT\02-B1\[SLAM1] B1 CahierDeTexte.md",
                  r"{}:\COURSPT\03-B2\[SLAM1] B2 CahierDeTexte.md",
                  r"{}:\COURSPT\04-B3\[SLAM1] B3 CahierDeTexte.md",
                  r"{}:\COURSNC\02 - B1 - PHP\CahierDeTexte.md",
                  r"{}:\COURSDF\Cahier de texte SLAM1 2022-2023.doc"
                  ]
    
    lettreLecteur = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lettre = str
    console = Console()
    cheminNAS = []
    connection = bool
    fichierLocal = str
    dossierLocal = "devoir prof local"
    dossierLocalWord = "devoir prof local word"
    dossierLocalNouveauDevoir = "nouveau devoir"
    fichierLocalmd = str
    
    
#======================================================================= fonction =======================================================================#     
    
    #connection echoué
    def connectionEchoue():
        console.print("[red]Connection echoué[/red]")
    
    #renvoie le texte d'un fichier
    def lectureFichier(nomFichierNAS, dossierLocal = "", fichierLocal = ""):
        
        if nomFichierNAS[-4:] == ".doc":
            
            # chemin de destination pour la copie du fichier
            cheminLocal = dossierLocal
            # chemin du fichier à copier
            cheminNAS = nomFichierNAS
            # copie le fichier à la destination spécifiée
            shutil.copy2(cheminNAS, cheminLocal)
            
            #sauvegarde fichier NAS en .md
            doc = aw.Document(fichierLocal)
            nomFichierNAS = fichierLocal.replace(".doc", ".md")
            doc.save(nomFichierNAS)
        
        fichier = open(nomFichierNAS, "r", encoding="utf-8")
        lecture = fichier.read()
        fichier.close()
            
        return lecture
    
    #vérifie si les devoirs sont à jour
    def verifieMiseAJour(texteLocal, texteNAS, nomFichier, cheminFichierLocal, cheminFichierNAS):
        
        dateDeModification = os.path.getmtime(cheminFichierNAS)
        dateDeModification = time.strftime("%d/%m/%Y-%H:%M:%S",time.gmtime(dateDeModification))
        
        #si le texte est identique
        if texteLocal == texteNAS:
            console.print("[cyan]Le fichier[/cyan] [dark_red]{}[/dark_red] [green4]est à jour[/green4]: {}".format(nomFichier, dateDeModification))
            #sinon j'affiche les modification et je met à jour le fichier
        else:
            console.print("[cyan]Le fichier[/cyan] [dark_red]{}[/dark_red] [blue_violet]à été modifié[/blue_violet]: {}".format(nomFichier, dateDeModification))
            texteModifier = texteModifie(texteLocal, texteNAS)
            console.print("[light_salmon3]partie qui à été modifié:[/light_salmon3]\n\n")
            print(texteModifier)
            ecriture(cheminFichierLocal, texteNAS)
            
            #récupère le nombre de fichier dans le dossier "nouveau devoir"
            for chemin ,dossier, fichier in os.walk(dossierLocalNouveauDevoir):
                num = len(fichier)
                
            #créer le nom du fichier
            numFichier = str(num).zfill(4)
            dateDeModification = dateDeModification.replace("/", "_")
            dateDeModification = dateDeModification.replace(":", "_")
            nomNouveauFichier = "/nouveauDevoir{}-{}.md".format(numFichier, dateDeModification)
            ecriture(dossierLocalNouveauDevoir+nomNouveauFichier, texteModifier)
                    
    
    #renvoie le texte que le prof à rajouter
    def texteModifie(texteLocal, texteNAS):
        lentexteLocal = len(texteLocal) - 1
        lentexteNAS = len(texteNAS) - 1
        x = 0
        
        #test si le début du texte à été modifier
        for i in range(lentexteLocal):
            if texteLocal[i] != texteNAS[i]:
                    x = i
                    break
                
        #test si la fin du texte à été modifier
        y = lentexteNAS
        for i in range(lentexteLocal):
            if texteLocal[lentexteLocal - i] == texteNAS[lentexteNAS - i]:
                y -= 1
            else:
                break
            
        y += 1
        texte1 = texteNAS[x:y]
        return texte1
    
    #Pour les fichier .doc
    def verifieMiseAJourDoc(cheminLocal, cheminNAS, fichier, nomFichier):
        
            # copie le fichier à la destination spécifiée
            shutil.copy2(cheminNAS, cheminLocal)
            shutil.copy2(cheminNAS, dossierLocal)
            
            #sauvegarde fichier NAS en .md
            doc = aw.Document(fichier)
            cheminLocal = fichier.replace(".doc", ".md")
            doc.save(cheminLocal)
            
            nomFichier = nomFichier.replace(".doc", ".md")
            fichierLocal = dossierLocal + r"\\" + nomFichier
            texteLocal = lectureFichier(fichierLocal)
            texteNAS = lectureFichier(cheminLocal)
            verifieMiseAJour(texteLocal, texteNAS, nomFichier, fichierLocal, cheminNAS)
            
#======================================================================= fonction =======================================================================# 
    
#======================================================================= connection NAS =======================================================================#
    
    #Cherche le lecteur NAS
    for i in lettreLecteur:
        cheminNAS = []
        connection = False
        for j in dossierNAS:
            cheminNAS.append("{}:/{}".format(i, j))
        
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
    
    #si tous les dossiers sont accecible 
    if connection:
        for i in cheminNAS:
            console.print("{} connection [green]réussie[/green]".format(i))
        
        #si dossier local exist
        if not existe(dossierLocalNouveauDevoir):
            creationDossier(dossierLocalNouveauDevoir)
        
        #si dossier local exist
        if not existe(dossierLocalWord):
            creationDossier(dossierLocalWord)
        
        #si dossier local exist
        if existe(dossierLocal):
            
            #vérifie si chaque fichier local existe
            for i in fichierNAS:
                fichierLocal = i.split("\\")
                fichierLocal = dossierLocal + r"\\" + fichierLocal[-1]
                
                #si fichier est un .doc
                if fichierLocal[-4:] == ".doc":
                    fichierLocalmd = fichierLocal.replace(".doc", ".md")
                else:
                    fichierLocalmd = fichierLocal
                
                #si ces fichier exist
                if existe(fichierLocal) and existe(fichierLocalmd):
                    continue
                #sinon créer fichier
                else:
                    print("fichier manquant")
                    ecriture(fichierLocal ,lectureFichier(i.format(lettre), dossierLocal, fichierLocal))
            
        else:
            print("dossier manquant")
            #créer dossier local
            creationDossier(dossierLocal)
            #créer tous le fichier local
            for i in fichierNAS:
                
                fichierLocal = i.split("\\")
                fichierLocal = dossierLocal + r"\\" + fichierLocal[-1]
                ecriture(fichierLocal ,lectureFichier(i.format(lettre), dossierLocal, fichierLocal))
        
#======================================================================= analyse des fichiers local =======================================================================# 
    
        for i in fichierNAS:
            
            if i[-4:] == ".doc":
                fichierLocal = i.split("\\")
                nomFichier = fichierLocal[-1]
                fichierLocal = dossierLocalWord + r"\\" + nomFichier
                verifieMiseAJourDoc(dossierLocalWord, i.format(lettre), fichierLocal, nomFichier)
            else:
                fichierLocal = i.split("\\")
                nomFichier = fichierLocal[-1].replace(".doc", ".md")
                fichierLocal = dossierLocal + r"\\" + nomFichier
                texteLocal = lectureFichier(fichierLocal)
                texteNAS = lectureFichier(i.format(lettre))
                verifieMiseAJour(texteLocal, texteNAS, nomFichier, fichierLocal, i.format(lettre))
            
    else:
        connectionEchoue()