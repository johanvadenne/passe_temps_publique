import random

file = open(r"D:\Johan\GitHub\mes repertoire\BugSafari\developpemnt\BDD\fiche.txt", "r+", encoding="UTF-8")

texte = file.readlines()
file.close()

x = 0
value = ""

def biomaalea():
    nombre_aleatoire = random.randint(5, 29)
    return nombre_aleatoire



def insectalea():
    nombre_aleatoire = random.randint(724, 1442)
    return nombre_aleatoire


def nbrBiome():
    nombre_aleatoire = random.randint(1,3)
    return nombre_aleatoire

tab = []
for i in range(724, 1443):
    
    for j in range(nbrBiome()):
        idbiome = biomaalea()
        idinsect = i
        if idbiome in tab:
            continue
        tab.append(idbiome)
        value+="""
        ({0},{1})""".format(idbiome, idinsect)
    tab = []
    
    

print(value)


file = open(r"D:\Johan\GitHub\mes repertoire\BugSafari\developpemnt\BDD\fich.txt", "w+", encoding="UTF-8")
file.write(value)
file.close()