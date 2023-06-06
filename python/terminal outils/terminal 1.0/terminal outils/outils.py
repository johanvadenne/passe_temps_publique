from fonction import *
from programmeRecherDevoir import *
from rich.console import Console
import os

console = Console()

def outils():
    
    while True:
        console.print("\n\n\n[dark_slate_gray2]                         ██╗    ██╗ ██████╗ ██╗     ███████╗    ███████╗██╗██████╗ ███████╗\n                         ██║    ██║██╔═══██╗██║     ██╔════╝    ██╔════╝██║██╔══██╗██╔════╝\n                         ██║ █╗ ██║██║   ██║██║     █████╗      █████╗  ██║██████╔╝█████╗  \n                         ██║███╗██║██║   ██║██║     ██╔══╝      ██╔══╝  ██║██╔══██╗██╔══╝  \n                         ╚███╔███╔╝╚██████╔╝███████╗██║         ██║     ██║██║  ██║███████╗\n                          ╚══╝╚══╝  ╚═════╝ ╚══════╝╚═╝         ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝[/dark_slate_gray2]\n\n\n")
    
        console.print("[deep_sky_blue2]="*100+"[/deep_sky_blue2]")
        
        console.print("\n[deep_sky_blue2]   [1] - créer utilisatteur\n   [2] - créer gmail\n   [3] - générer mot de passe\n   [4] - générer nombre premier\n   [5] - recherche nouveau devoir\n   [6] - recherche nouveau fichier et dossier\n   [7] - [/deep_sky_blue2][light_coral]quitté[/light_coral]")
        option = console.input("[deep_sky_blue2]\n"+"="*20+"\n\nSelction le programme que tu veux utiliser: [/deep_sky_blue2]")

        if option == "1":
            utilisateurs()
        elif option == "2":
            genererMail()
        elif option == "3":
            motDePasse()
        elif option == "4":
            genererNombrePremier()
        elif option == "5":
            rechercheDevoir()
        elif option == "6":
            analyseDossierNas()
        elif option == "7":
            break
        
        console.input("[yellow]\nEnter pour continuer[/yellow]")

outils()

console.input("[light_coral]\nentrée pour quitté: [/light_coral]")