from nombrePremier import *
from random import *

a = 0
texte1 = ""
texte2 = ""
tableLettre = [["", ""]]

while texte1 == "" or texte1 == " ":
    texte1 = input("Saisissé le texte que vous voulez crypté: \n")

for i in texte1:
    existe = False
    for j in tableLettre:
        if i == j[0]:
            existe = True
            texte2 += str(j[1]) + " "
            break
    if existe:
        continue
    else:
        a += 1
        tableLettre.append([])
        tableLettre[a].append(i)
        tableLettre[a].append(nombrePremier.pop(randint(0, len(nombrePremier) - 1)))
        texte2 += str(tableLettre[a][1]) + " "

print(texte2)