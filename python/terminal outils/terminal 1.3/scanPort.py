import socket
from datetime import datetime
from ipwhois import IPWhois
from pprint import pprint
from fonction import *

def analysePort():


    portDebut = ""
    portFin = ""
    portOuvert = 0
    portFermer = 0
    nomDossier = "analyse port"


#======================================================================= saisie =======================================================================#

    try:
        hote = input("\nsaisissez une adresse IP à scanner ou un nom de domaine ex:(127.0.0.1) ou (google.fr): ")
        hoteIP = socket.gethostbyname(hote)
        portDebut = saisieInt("\nport de début: ")
        portFin = saisieInt("\nport de fin: ")
        delai = saisieFloat("\ndélai en chaque scan de port en seconde ex:(1s ou 0.5s): ")
    except KeyboardInterrupt or ValueError:
        print("\nquitté")

#======================================================================= saisie =======================================================================#

#======================================================================= analyse port =======================================================================#

    print("\nscan {} en cour".format(hoteIP))
    temps1 = datetime.now()
    texte = "IP: " + hote + "\nhote: " + hoteIP + "\n"

    for port in range(portDebut,portFin):
        tempsAnalyse = datetime.now()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(delai)
        result = sock.connect_ex((hoteIP, port))
        temps = datetime.now() - tempsAnalyse
        if result == 0:
            portOuvert += 1
            texte += "\n" + "Port {}: \t Ouvert \t {}".format(port, temps)
            print ("Port {}: \t Ouvert \t {}".format(port, temps))
        else:
            portFermer += 1
            texte += "\n" + "Port {}: \t Fermé \t {}".format(port, temps)
            print ("Port {}: \t Fermé \t {}".format(port, temps))
        sock.close()

#======================================================================= analyse port =======================================================================#

#======================================================================= fin =======================================================================#

    fin = datetime.now() - temps1
    texte += "\n" + "\nscan {} teminé\n\
    duréé d'analyse {}\n\
    port ouvert {}\n\
    port fermer {}".format(hote, fin, portOuvert, portFermer)

    print("\nscan {} teminé\n\
    duréé d'analyse {}\n\
    port ouvert {}\n\
    port fermer {}".format(hote, fin, portOuvert, portFermer))

#======================================================================= fin =======================================================================#

#======================================================================= récupère d'autre donnée concernat hote =======================================================================#

    try:
        obj = IPWhois(hoteIP)
        results = obj.lookup_whois(get_referral=True)
        texte += "\n" + result
        pprint(results)
    except:
        None

    if not existe(nomDossier):
        creationDossier(nomDossier)

#======================================================================= récupère d'autre donnée concernat hote =======================================================================#

#======================================================================= enregistre dans un fichier =======================================================================#

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

            nomFichier = str(num).zfill(4) + "_analyse.txt"
            break
    chemin = nomDossier + "/" + nomFichier
    creationFichier(chemin)
    ecriture(chemin, texte)
    
#======================================================================= enregistre dans un fichier =======================================================================#