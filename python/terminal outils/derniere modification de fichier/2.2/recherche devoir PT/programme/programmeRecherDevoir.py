import os
import time
from rich.console import Console


##################### variable

monRepertoire = str
RepertoireProf = str
monRepertoireDevoir = str
monRepertoireAP = str
monRepertoireBLOC1 = str
monRepertoireBLOC3 = str
monRepertoireCopieFichierProf = str
monFichierCopieProfAP = str
monFichierCopieProfBLOC1 = str
monFichierCopieProfBLOC3 = str
NASRepertoireProf = str
NASrepertoireDevoirAP = str
NASrepertoireDevoirBLOC1 = str
NASrepertoireDevoirBLOC3 = str
NAStexteDevoirAP = str
NAStexteDevoirBLOC1 = str
NAStexteDevoirBLOC3 = str
maCopieTexteFichierProfAP = str
maCopieTexteFichierProfBLOC1 = str
maCopieTexteFichierProfBLOC3 = str
texte1 = str
console = Console()
lettreLecteur = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
nomNouveauFichier = str
num = int
numFichier = str
dateDeModification = str

##################### variable

##################### fonction

#renvoie si dossier ou fichier existe
def exist(repertoire):
    return (os.path.exists(repertoire))


#créer dossier
def creationDossier(dossier):
    os.mkdir(dossier)


#créer fichier
def creationFichier(fichier):
    nomFichier = open(fichier, "w+", encoding="utf-8")
    nomFichier.close()


#récupère le texte d'un fichier
def recupTexteFichier(fichier):
    nomFichier = open(fichier, "r", encoding="utf-8")
    texteFichier = nomFichier.read()
    nomFichier.close()
    
    return texteFichier


#vérifie si le prof à rajouté un devoir
#si oui je met à jour mon fichier local et j'écrie dans un nouveau fichier juste la partie qui à changer
def modification(texteLocal, texteNAS, nomDuFichierVerifie, cheminFichier, cheminNouveauFichier, cheminFichierNAS):
    
    dateDeModification = os.path.getmtime(cheminFichierNAS)
    dateDeModification = time.strftime("%d/%m/%Y-%H:%M:%S",time.gmtime(dateDeModification))
    if (texteLocal == texteNAS):
        console.print("[cyan]Le fichier[/cyan] [dark_red]{}[/dark_red] [green4]est à jour[/green4]: {}".format(nomDuFichierVerifie, dateDeModification))
    else:
        console.print("[cyan]Le fichier[/cyan] [dark_red]{}[/dark_red] [blue_violet]à été modifié[/blue_violet]: {}".format(nomDuFichierVerifie, dateDeModification))
        texte1 = texteModifie(texteLocal, texteNAS)
        console.print("[light_salmon3]voici la partie qui à été modifié:[/light_salmon3]\n\n")
        print(texte1)
        ecriture(cheminFichier, texteNAS)
        
        num = 0
        while(True):
            
            num += 1
            numFichier = str(num).zfill(4)
            dateDeModification = dateDeModification.replace("/", "_")
            dateDeModification = dateDeModification.replace(":", "_")
            nomNouveauFichier = "/nouveauDevoir{}-{}.md".format(numFichier, dateDeModification)
            
            if not (exist(cheminNouveauFichier+nomNouveauFichier)):
                ecriture(cheminNouveauFichier+nomNouveauFichier, texte1)
                break
            

#renvoie le texte que le prof à rajouter
def texteModifie(texteLocal, texteNAS):
    lentexteLocal = len(texteLocal) - 1
    lentexteNAS = len(texteNAS) - 1

    for i in range(lentexteLocal):
        if texteLocal[i] != texteNAS[i]:
                x = i
                break
            
    y = lentexteNAS
        
    for i in range(lentexteLocal):
        
        if texteLocal[lentexteLocal - i] == texteNAS[lentexteNAS - i]:
            y -= 1
        else:
            break
    
    y += 1
    texte1 = texteNAS[x:y]
    
    return texte1


#ecrie dans un fichier
def ecriture(cheminFichier, texte):
    fichier = open(cheminFichier, "w+", encoding="utf-8")
    fichier.write(texte)

##################### fonction

#################### remplie variable

#mon repertoire
monRepertoire = os.getcwd()
monRepertoire = "/".join(monRepertoire.split("\\") [:-1])
console.print("[dark_slate_gray2]Mon repertoire:[/dark_slate_gray2] [dark_red]{}[/dark_red]".format(monRepertoire))

#mes fichiers devoir
monRepertoireDevoir = monRepertoire+"/devoir"
monRepertoireAP = monRepertoireDevoir+"/devoir AP"
monRepertoireBLOC1 = monRepertoireDevoir+"/devoir BLOC1"
monRepertoireBLOC3 = monRepertoireDevoir+"/devoir BLOC3"

#mes fichiers copié
monRepertoireCopieFichierProf = monRepertoire+"/copy fichier prof"
monFichierCopieProfAP = monRepertoireCopieFichierProf+"/[SLAM1] AP CahierDeTexte.md"
monFichierCopieProfBLOC1 = monRepertoireCopieFichierProf+"/[SLAM1] B1 CahierDeTexte.md"
monFichierCopieProfBLOC3 = monRepertoireCopieFichierProf+"/[SLAM1] B3 CahierDeTexte.md"

#repertoire prof
NASRepertoireProf = "{}:/COURSPT"
NASrepertoireDevoirAP = NASRepertoireProf+"/01-AP/[SLAM1] AP CahierDeTexte.md"
NASrepertoireDevoirBLOC1 = NASRepertoireProf+"/02-B1/[SLAM1] B1 CahierDeTexte.md"
NASrepertoireDevoirBLOC3 = NASRepertoireProf+"/04-B3/[SLAM1] B3 CahierDeTexte.md"

#################### remplie variable

#################### créer les dossiers et fichiers si il n'existe pas

#mes fichiers devoir
if (exist(monRepertoireDevoir) == False):
    creationDossier(monRepertoireDevoir)

if (exist(monRepertoireAP) == False):
    creationDossier(monRepertoireAP)

if (exist(monRepertoireBLOC1) == False):
    creationDossier(monRepertoireBLOC1)

if (exist(monRepertoireBLOC3) == False):
    creationDossier(monRepertoireBLOC3)

#mes fichiers copié
if (exist(monRepertoireCopieFichierProf) == False):
    creationDossier(monRepertoireCopieFichierProf)

if (exist(monFichierCopieProfAP) == False):
    creationFichier(monFichierCopieProfAP)
    ecriture(monFichierCopieProfAP, "AP")

if (exist(monFichierCopieProfBLOC1) == False):
    creationFichier(monFichierCopieProfBLOC1)
    ecriture(monFichierCopieProfBLOC1, "BLOC 1")

if (exist(monFichierCopieProfBLOC3) == False):
    creationFichier(monFichierCopieProfBLOC3)
    ecriture(monFichierCopieProfBLOC3, "BLOC 3")

#################### créer les dossiers et fichiers si il n'existe pas

#connection au serveur NAS
for i in range(0, 26):
    NASRepertoireProf = "{}:/COURSPT".format(lettreLecteur[i])
    if exist(NASRepertoireProf):
        console.print("[dark_violet]connection[/dark_violet] [cyan]serveur NAS[/cyan] [chartreuse3]réussie[/chartreuse3]")
        NASrepertoireDevoirAP = NASRepertoireProf+"/01-AP/[SLAM1] AP CahierDeTexte.md"
        NASrepertoireDevoirBLOC1 = NASRepertoireProf+"/02-B1/[SLAM1] B1 CahierDeTexte.md"
        NASrepertoireDevoirBLOC3 = NASRepertoireProf+"/04-B3/[SLAM1] B3 CahierDeTexte.md"
        break

if (exist(NASRepertoireProf)):
    
    if((exist(NASrepertoireDevoirAP)) and (exist(NASrepertoireDevoirBLOC1)) and (exist(NASrepertoireDevoirBLOC3))):
        console.print("[dark_violet]connection[/dark_violet] [cyan]dossier AP[/cyan] [chartreuse3]réussie[/chartreuse3]")
        console.print("[dark_violet]connection[/dark_violet] [cyan]dossier BLOC 1[/cyan] [chartreuse3]réussie[/chartreuse3]")
        console.print("[dark_violet]connection[/dark_violet] [cyan]dossier BLOC 3[/cyan] [chartreuse3]réussie[/chartreuse3]")

        NAStexteDevoirAP = recupTexteFichier(NASrepertoireDevoirAP)
        maCopieTexteFichierProfAP = recupTexteFichier(monFichierCopieProfAP)
        modification(maCopieTexteFichierProfAP, NAStexteDevoirAP, "[SLAM1] AP CahierDeTexte.md", monFichierCopieProfAP, monRepertoireAP, NASrepertoireDevoirAP)

        NAStexteDevoirBLOC1 = recupTexteFichier(NASrepertoireDevoirBLOC1)
        maCopieTexteFichierProfBLOC1 = recupTexteFichier(monFichierCopieProfBLOC1)
        modification(maCopieTexteFichierProfBLOC1, NAStexteDevoirBLOC1, "[SLAM1] B1 CahierDeTexte.md", monFichierCopieProfBLOC1, monRepertoireBLOC1, NASrepertoireDevoirBLOC1)

        NAStexteDevoirBLOC3 = recupTexteFichier(NASrepertoireDevoirBLOC3)
        maCopieTexteFichierProfBLOC3 = recupTexteFichier(monFichierCopieProfBLOC3)
        modification(maCopieTexteFichierProfBLOC3, NAStexteDevoirBLOC3, "[SLAM1] B3 CahierDeTexte.md", monFichierCopieProfBLOC3, monRepertoireBLOC3, NASrepertoireDevoirBLOC3)
    
    else:
        
        if(exist(NASrepertoireDevoirAP)):
            console.print("[dark_violet]connection[/dark_violet] [cyan]dossier AP[/cyan] [red]échoué[/red]")
        if(exist(NASrepertoireDevoirBLOC1)):
            console.print("[dark_violet]connection[/dark_violet] [cyan]dossier BLOC 1[/cyan] [red]échoué[/red]")
        if(exist(NASrepertoireDevoirBLOC3)):
            console.print("[dark_violet]connection[/dark_violet] [cyan]dossier BLOC 3[/cyan] [red]échoué[/red]")
        
        console.input("[light_goldenrod3]appuyer sur entée pour quitté l'invite de commande[/light_goldenrod3]")
        
else:
    console.print("[dark_violet]connection[/dark_violet] [cyan]serveur NAS[/cyan] [red]échoué[/red]")
    console.input("[light_goldenrod3]appuyer sur entée pour quitté l'invite de commande[/light_goldenrod3]")


console.input("[light_goldenrod3]appuyer sur entée pour quitté l'invite de commande[/light_goldenrod3]")