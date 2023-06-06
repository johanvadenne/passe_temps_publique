from random import *


Pique = [("Pique", "1"),("Pique", "2"),("Pique", "3"),("Pique", "4"),("Pique", "5"),("Pique", "6"),("Pique", "7"),("Pique", "8"),("Pique", "9"),("Pique", "10"),("Pique", "Valet"),("Pique", "Dame"),("Pique", "Roi"),],
Coeur = [("Coeur", "1"),("Coeur", "2"),("Coeur", "3"),("Coeur", "4"),("Coeur", "5"),("Coeur", "6"),("Coeur", "7"),("Coeur", "8"),("Coeur", "9"),("Coeur", "10"),("Coeur", "Valet"),("Coeur", "Dame"),("Coeur", "Roi"),],
Carreaux = [("Careaux", "1"),("Careaux", "2"),("Careaux", "3"),("Careaux", "4"),("Careaux", "5"),("Careaux", "6"),("Careaux", "7"),("Careaux", "8"),("Careaux", "9"),("Careaux", "10"),("Careaux", "Valet"),("Careaux", "Dame"),("Careaux", "Roi"),],
Trefle = [("Trefle", "1"),("Trefle", "2"),("Trefle", "3"),("Trefle", "4"),("Trefle", "5"),("Trefle", "6"),("Trefle", "7"),("Trefle", "8"),("Trefle", "9"),("Trefle", "10"),("Trefle", "Valet"),("Trefle", "Dame"),("Trefle", "Roi"),]

joueur1 = []
nombreDeCarte = len(Pique) + len(Coeur) + len(Carreaux) + len(Trefle)

while (nombreDeCarte > 0):
    x = randint(1, 4)
    y = randint(0, nombreDeCarte - 1)
    
    if (x == 1):
        joueur1 = Pique.pop(y)
    elif (x == 2):
        joueur1 = Coeur.pop(y)
    elif (x == 3):
        joueur1 = Carreaux.pop(y)
    elif (x == 4):
        joueur1 = Trefle.pop(y)
    
    
    
    
    nombreDeCarte = len(Pique) + len(Coeur) + len(Carreaux) + len(Trefle)