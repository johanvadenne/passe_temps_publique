from rich.console import Console #permet afficher des textes en couleurs
from RechercheDevoir import *
from analyseNouveauFichier import *
from scanPort import *
import os

console = Console()



while True:
    
    os.system("cls")

    #affiche logo
    console.print("\n\n\n[dark_slate_gray2]\
\
                        ██╗    ██╗ ██████╗ ██╗     ███████╗    ███████╗██╗██████╗ ███████╗\n\
                        ██║    ██║██╔═══██╗██║     ██╔════╝    ██╔════╝██║██╔══██╗██╔════╝\n\
                        ██║ █╗ ██║██║   ██║██║     █████╗      █████╗  ██║██████╔╝█████╗  \n\
                        ██║███╗██║██║   ██║██║     ██╔══╝      ██╔══╝  ██║██╔══██╗██╔══╝  \n\
                        ╚███╔███╔╝╚██████╔╝███████╗██║         ██║     ██║██║  ██║███████╗\n\
                         ╚══╝╚══╝  ╚═════╝ ╚══════╝╚═╝         ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝\
\
        [/dark_slate_gray2]\n\n\n")
    

    #séparation avec des signes "="
    console.print("[deep_sky_blue2]="*100+"[/deep_sky_blue2]")
    

    #affiche les outils à disposition
    console.print("\n[deep_sky_blue2]\
\
        [1] - recherche nouveau devoir\n\
        [2] - recherche nouveau fichier et dossier\n\
        [3] - scanne port\n\
        [4] - [/deep_sky_blue2][light_coral]quitté\
\
        [/light_coral]")


    #séparation avec des signes "=" + demande de selection d'un programme
    option = console.input("[deep_sky_blue2]\n\
\
"+"="*100+"\n\n\
\
    Selctionnez le programme que vous voulez utiliser: \
\
[/deep_sky_blue2]")


    #option 1: recherche nouveau devoir
    if option == "1":
        rechercheDevoir()
    #option 2: recherche nouveau fichier et dossier
    elif option == "2":
        nouveauFichier()
    #option 3: quitté
    elif option == "3":
        analysePort()
    #option 3: quitté
    elif option == "4":
        break
    
    console.input("[yellow]\nEnter pour continuer[/yellow]")



console.input("[light_coral]\nentrée pour quitté: [/light_coral]")