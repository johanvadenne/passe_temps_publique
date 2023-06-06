import socket
from datetime import datetime
from ipwhois import IPWhois
from pprint import pprint
from fonction import *
from rich.console import Console

console = Console()

def analysePort():





#======================================================================= fonction =======================================================================#



    
    def whois(hoteIP):
        texte = ""
        try:
            obj = IPWhois(hoteIP)
            results = obj.lookup_whois(get_referral=True)
            texte = "\n" + results
            pprint(results)
        except:
            None

        
        return texte
    
    def finScan(temps1, hote, portOuvert, portFermer):
        fin = datetime.now() - temps1
        texte = "\n" + "\nscan {} teminé\n\
        duréé d'analyse {}\n\
        port ouvert {}\n\
        port fermer {}".format(hote, fin, portOuvert, portFermer)

        print("\nscan {} teminé\n\
        duréé d'analyse {}\n\
        port ouvert {}\n\
        port fermer {}".format(hote, fin, portOuvert, portFermer))
        
        return texte
    
    def scanFourchette():
        
        nomDossier = "analyse port"
        portOuvert = 0
        portFermer = 0
        
        
        if not existe(nomDossier):
            creationDossier(nomDossier)
        
        try:
            hote = input("\nsaisissez une adresse IP à scanner ou un nom de domaine ex:(127.0.0.1) ou (google.fr): ")
            hoteIP = socket.gethostbyname(hote)
            portDebut = saisieInt("\nport de début: ")
            portFin = saisieInt("\nport de fin: ")
            delai = saisieFloat("\ndélai en chaque scan de port en seconde ex:(1s ou 0.5s): ")
        except KeyboardInterrupt or ValueError:
            print("\nquitté")
            
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

        texte += finScan(temps1, hote, portOuvert, portFermer)

        texte += whois(hoteIP)

        creationNomFichierAutomatique(nomDossier, "_analyse.txt", texte)

#======================================================================= fonction =======================================================================#
    while 1:
        console.print("\n[deep_sky_blue2]\
\
            [1] - saisir une fourchette\n\
            [2] - choisier une liste\n\
            [3] - créer une liste\n\
            [4] - [/deep_sky_blue2][light_coral]sortir\
\
            [/light_coral]")
        
        option = console.input("[deep_sky_blue2]\n\
\
"+"="*100+"\n\n\
\
    Selctionnez le programme que vous voulez utiliser: \
\
[/deep_sky_blue2]")

        #option 1: saisir une fourchette
        if option == "1":
            scanFourchette()
        #option 2: choisier une liste
        elif option == "2":
            None
        #option 3: créer une liste
        elif option == "3":
            None
        #option 3: quitté
        elif option == "4":
            break

#======================================================================= saisie =======================================================================#

    

