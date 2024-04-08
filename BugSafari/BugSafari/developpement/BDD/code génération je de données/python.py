import random

file = open(r"D:\Johan\GitHub\mes repertoire\BugSafari\developpemnt\BDD\fiche.txt", "r+", encoding="UTF-8")

texte = file.readlines()
file.close()

x = 0
value = ""

def poidalea():
    nombre_aleatoire = random.randint(1, 350)
    return nombre_aleatoire



def joursalea():
    nombre_aleatoire = random.randint(1, 1000)
    return nombre_aleatoire


def menaceAlea():
    nombre_aleatoire = random.randint(0, 8)
    return nombre_aleatoire

def saisAlea():
    nombre_aleatoire = random.randint(0, 10)
    return nombre_aleatoire

def typealea():
    nombre_aleatoire = random.randint(1,16)
    return nombre_aleatoire


tabMenace = [
    "Éteinte (EX)", 
    "Éteinte à l’état sauvage (EW)", 
    "danger critique (CR)", 
    "En danger (EN)", 
    "Vulnérable (VU)", 
    "Quasi menacée (NT)", 
    "Préoccupation mineure (LC)", 
    "Données insuffisantes (DD)", 
    "Non évaluée (NE)"
]


tabSaison = [
    "Été",
    "Printemps",
    "Automne",
    "Hiver",
    "Été/Printemps",
    "Été/Automne",
    "Été/Hiver",
    "Printemps/Automne",
    "Printemps/Hiver",
    "Automne/Hiver",
    "Toute les saisons"
]

for i in texte:
    if x == 0:
        x+=1
        continue
    print(i)
    texte2 = i.split(",")
    if texte2[8] == '' or texte2[8] == '-':
        continue
    print(texte2[5])
    print(texte2[8])
    
    poid = poidalea()
    taille = poidalea()
    menace = tabMenace[menaceAlea()]
    saison = tabSaison[saisAlea()]
    jour = joursalea()
    idtype = typealea()
    
    value += """('{0}','Descrition ...',{1},'g',{2},'mm','{3}','5/10','{4}', {5},{6}),
    """.format(texte2[8], poid, taille, menace, saison, jour,idtype)
    

print(value)


file = open(r"D:\Johan\GitHub\mes repertoire\BugSafari\developpemnt\BDD\fich.txt", "w+", encoding="UTF-8")
file.write(value)
file.close()