import os

#répertoire et nom fichier
monRepertoire = str
repertoireDevoir = str
repertoireDevoirAP = str
repertoireDevoirBLOC1 = str
repertoireDevoirBLOC3 = str
repertoireCopieFichierProf = str
copieFichierProfAP = str
copieFichierProfBLOC1 = str
copieFichierProfBLOC3 = str
copieTexteFichierProfAP = str
copieTexteFichierProfBLOC1 = str
copieTexteFichierProfBLOC3 = str
NASfichierDevoirAP = str
NASfichierDevoirBLOC1 = str
NASfichierDevoirBLOC3 = str
NAStexteDevoirAP = str
NAStexteDevoirBLOC1 = str
NAStexteDevoirBLOC3 = str
nouveauDevoir = str
lettreLecteur = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#numéro
num1 = int
num2 = int
num3 = int
numFichier = str
#texte
texte1 = str
modification = bool


#################### fonction

#fonction renvoie si dossier ou fichier existant
def exist(repertoire):

    #renvoie un booléen
    return (os.path.exists(repertoire))


#fonction créer dossier
def creationDossier(dossier):
    
    #créer dossier
    os.mkdir(dossier)


#fonction créer fichier
def creationFichier(fichier):
    
    #créer fichier
    nomFichier = open(fichier, "w+", encoding="utf-8")
    nomFichier.close()


#fonction récupère le texte d'un fichier
def recupTexteFichier(fichier):
    
    #lit le fichier et récupère le texte
    nomFichier = open(fichier, "r", encoding="utf-8")
    texteFichier = nomFichier.read()
    nomFichier.close()
    
    return texteFichier


#fonction copie le fichier du prof en en local et créer un nouveau fichier si il y a eu des modification
def copieFichier(texteLocal, texteNAS, cheminDuFichierLocal, cheminFichierNouveauDevoir, nomDuFichierVerifie):
    
    if (texteLocal == texteNAS):
        print("\033[93mLe fichier\033[96m {}\033[92m est à jour".format(nomDuFichierVerifie))
    else:
        print("\033[93mLe fichier\033[96m {}\033[94m à été modifié\n\nVoicie le contenue midifié\n\n\n{}".format(cheminFichierNouveauDevoir, nomDuFichierVerifie))
        texte1 = texteNAS.replace(texteLocal, "")
        
        creationNouveauFichierDevoir(texte1, cheminFichierNouveauDevoir)
        
        nomFichier = open(cheminDuFichierLocal, "w+", encoding="utf-8")
        nomFichier.write(texteNAS)
        nomFichier.close()


#nouveau fichier
def creationNouveauFichierDevoir(texte, chemin):
    
    num1 = 0
    num2 = 0
    num3 = 1
    numFichier = str(num1) + str(num2) + str(num3)
    nouveauDevoir = chemin+"/nouveauDevoir{}.md".format(numFichier)
    
    while (exist(nouveauDevoir)):
        num3 +=1
        if (num3 == 10):
            num3 = 0
            num2 += 1
        if (num2 == 10):
            num2 = 0
            num1 += 1
        numFichier = str(num1) + str(num2) + str(num3)
        nouveauDevoir = chemin+"/nouveauDevoir{}.md".format(numFichier)
    
    fichier = open(nouveauDevoir, "w+", encoding="utf-8")
    fichier.write(texte)
    fichier.close()
    modification = True
    return modification

#################### fonction

#################### remplie variable

# récupérer le chemin du répertoire courant
monRepertoire = os.getcwd()
monRepertoire = "/".join(monRepertoire.split("\\") [:-1])

#répertoire des fichiers devoir
repertoireDevoir = monRepertoire+"/devoir"
repertoireDevoirAP = repertoireDevoir+"/devoir AP"
repertoireDevoirBLOC1 = repertoireDevoir+"/devoir BLOC1"
repertoireDevoirBLOC3 = repertoireDevoir+"/devoir BLOC3"

#repertoire des fichiers copié
repertoireCopieFichierProf = monRepertoire+"/copy fichier prof"
copieFichierProfAP = repertoireCopieFichierProf+"/[SLAM1] AP CahierDeTexte.md"
copieFichierProfBLOC1 = repertoireCopieFichierProf+"/[SLAM1] B3 CahierDeTexte.md"
copieFichierProfBLOC3 = repertoireCopieFichierProf+"/[SLAM1] B1 CahierDeTexte.md"

#repertoire des fichier NAS
NASrepertoireCoursPT = "{}:/COURSPT".format(lettreLecteur[0])
NASrepertoireDevoirAP = NASrepertoireCoursPT+"/01-AP/[SLAM1] AP CahierDeTexte.md"
NASrepertoireDevoirBLOC1 = NASrepertoireCoursPT+"/02-B1/[SLAM1] B1 CahierDeTexte.md"
NASrepertoireDevoirBLOC3 = NASrepertoireCoursPT+"/04-B3/[SLAM1] B3 CahierDeTexte.md"

#nom des nouveaux fichiers
nouveauDevoir = "/nouveauDevoir{}.md".format(numFichier)

#################### remplie variable

#################### vérification de fichier et repertoires existant

#créer les dossiers et fichiers si il n'existe pas
if (exist(repertoireDevoir) == False):
    creationDossier(repertoireDevoir)

if (exist(repertoireDevoirAP) == False):
    creationDossier(repertoireDevoirAP)

if (exist(repertoireDevoirBLOC1) == False):
    creationDossier(repertoireDevoirBLOC1)

if (exist(repertoireDevoirBLOC3) == False):
    creationDossier(repertoireDevoirBLOC3)


if (exist(repertoireCopieFichierProf) == False):
    creationDossier(repertoireCopieFichierProf)

if (exist(copieFichierProfAP) == False):
    creationFichier(copieFichierProfAP)

if (exist(copieFichierProfBLOC1) == False):
    creationFichier(copieFichierProfBLOC1)

if (exist(copieFichierProfBLOC3) == False):
    creationFichier(copieFichierProfBLOC3)

#connection au serveur NAS
for i in range(0, 26):
    NASrepertoireCoursPT = "{}:/COURSPT".format(lettreLecteur[i])
    if exist(NASrepertoireCoursPT):
        print("\033[95mconnection\033[96m serveur NAS\033[92m réussie")
        NASfichierDevoirAP = NASrepertoireCoursPT+"/01-AP/[SLAM1] AP CahierDeTexte.md"
        NASfichierDevoirBLOC1 = NASrepertoireCoursPT+"/02-B1/[SLAM1] B1 CahierDeTexte.md"
        NASfichierDevoirBLOC3 = NASrepertoireCoursPT+"/04-B3/[SLAM1] B3 CahierDeTexte.md"
        break

#################### vérification des fichier et repertoires existant



if (exist(NASrepertoireCoursPT)):

    if(exist(NASfichierDevoirAP)):
        print("\033[95mconnection\033[96m dossier AP\033[92m réussie")
    if(exist(NASfichierDevoirBLOC1)):
        print("\033[95mconnection\033[96m dossier BLOC 1\033[92m réussie")
    if(exist(NASfichierDevoirBLOC3)):
        print("\033[95mconnection\033[96m dossier BLOC 3\033[92m réussie")

    NAStexteDevoirAP = recupTexteFichier(NASfichierDevoirAP)
    copieTexteFichierProfAP = recupTexteFichier(copieFichierProfAP)
    copieFichier(copieTexteFichierProfAP, NAStexteDevoirAP, copieFichierProfAP, repertoireDevoirAP, "[SLAM1] AP CahierDeTexte.md")

    NAStexteDevoirBLOC1 = recupTexteFichier(NASfichierDevoirBLOC1)
    copieTexteFichierProfBLOC1 = recupTexteFichier(copieFichierProfBLOC1)
    copieFichier(copieTexteFichierProfBLOC1, NAStexteDevoirBLOC1, copieFichierProfBLOC1, repertoireDevoirBLOC1, "[SLAM1] B1 CahierDeTexte.md")

    NAStexteDevoirBLOC3 = recupTexteFichier(NASfichierDevoirBLOC3)
    copieTexteFichierProfBLOC3 = recupTexteFichier(copieFichierProfBLOC3)
    copieFichier(copieTexteFichierProfBLOC3, NAStexteDevoirBLOC3, copieFichierProfBLOC3, repertoireDevoirBLOC3, "[SLAM1] B3 CahierDeTexte.md")
    
    input("\033[90m Pour fermer cette fenêtre appuyé sur entrer:")
else:
    print("\033[95mconnection\033[96m serveur NAS\033[91m échoué")
    input("\033[90m Pour fermer cette fenêtre appuyé sur entrer:")

print("\033[97m")