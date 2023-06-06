from random import randint

while True:
    outils = ("pierre", "papier", "ciseaux")
    reponse = True

    while reponse:
        joueur = input("pierre, papier, ciseaux:\n")

        for i in [0, 2]:
            if joueur == outils[i]:
                reponse = False
                break

    ordi = outils[randint(0,2)]

    print("ordi " + ordi + "\n" + "toi " + joueur + "\n")

    if joueur == ordi:
        resultat = "égalité"
    elif joueur == "pierre" and ordi == "papier":
        resultat = "perdu"
    elif joueur == "papier" and ordi == "ciseaux":
        resultat = "perdu"
    elif joueur == "ciseaux" and ordi == "pierre":
        resultat = "perdu"
    elif joueur == "pierre" and ordi == "ciseaux":
        resultat = "gagné"
    elif joueur == "papier" and ordi == "pierre":
        resultat = "gagné"
    elif joueur == "ciseaux" and ordi == "papier":
        resultat = "gagné"

    if resultat == "égalité":
        print("Il y a égalité\n")
    elif resultat == "perdu":
        print("Tu as perdu\n")
    elif resultat == "gagné":
        print("Tu as gagné\n")
    else:
        print("rien\n")

    while True:
        rejouer = input("voulez vous rejouer? oui ou non\n")
        if rejouer == "non":
            quit()
        elif rejouer == "oui":
            break