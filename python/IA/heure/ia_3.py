import re
from pprint import pprint
from time import strftime


def supprimeCaractereSpeciaux(texte):
    phrase = texte.replace("-", " ")
    phrase = phrase.replace("'", " ")
    phrase = phrase.lower()
    nouvelleChaine = ""
    for caractere in phrase:
        nouvelleChaine += accents.get(caractere, caractere)
    nouvelleChaine = re.sub(r'[^a-zA-Z0-9\s]', '', nouvelleChaine)
    nouvelleChaineTable = []
    for mot in nouvelleChaine.split(" "):
        nouvelleChaineTable.append(verbe.get(mot, mot))
    nouvelleChaine = " ".join(nouvelleChaineTable)
    return nouvelleChaine

def heure():
    print("il est "+ strftime("%H:%M:%S"))

accents = {
        'à': 'a', 'á': 'a', 'â': 'a', 'ã': 'a', 'ä': 'a', 'å': 'a',
        'è': 'e', 'é': 'e', 'ê': 'e', 'ë': 'e',
        'ì': 'i', 'í': 'i', 'î': 'i', 'ï': 'i',
        'ò': 'o', 'ó': 'o', 'ô': 'o', 'õ': 'o', 'ö': 'o', 'ø': 'o',
        'ù': 'u', 'ú': 'u', 'û': 'u', 'ü': 'u',
        'ý': 'y', 'ÿ': 'y',
        'ç': 'c',
        'ñ': 'n'
}

verbe ={
    "peux" : "pouvoir", "peut" : "pouvoir", "pouvez" : "pouvoir", "pouvons" : "pouvoir", "peuvent" : "pouvoir",
    "pourrais" : "pouvoir", "pourrait" : "pouvoir", "pourrez" : "pouvoir", "pourrons" : "pouvoir", "pourront" : "pouvoir",
    "pourrais" : "pouvoir", "pourrait" : "pouvoir", "pourrions" : "pouvoir", "pourriez" : "pouvoir", "pourraient" : "pouvoir",
    "donne" : "donner", "donnes" : "donner", "donnez" : "donner", "donnons" : "donner", "donnent" : "donner"
}

pronom ={
    "je": "1ps", "tu": "2ps", "il": "3ps", "elle": "3ps", "on": "3ps", "nous": "1pp", "vous": "2pp", "ils": "3pp", "elles": "3pp"
}

formalite = [
    "s'il vous plaît",
    "s'il te plaît",
]

fichier = open("reference.txt", "r+", encoding="utf-8")
reference = (fichier.read().split("\n"))
fichier.close()

for i in range(len(reference)):
    reference[i] = supprimeCaractereSpeciaux(reference[i])


for i in range(len(formalite)):
    formalite[i] = supprimeCaractereSpeciaux(formalite[i])

for i in range(len(reference)):
    for phraseFor in formalite:
        phraseRef = reference[i].replace(phraseFor, "")
        reference[i] = phraseRef.strip()


question = input("question: ")
question = supprimeCaractereSpeciaux(question)
for phraseFor in formalite:
    question = question.replace(phraseFor, "")
    question = question.strip()


#ind = 0
#for phrase in reference:
#    nouvelleChaine = ""
#    for mot in phrase.split(" "):
#        nouvelleChaine += pronom.get(mot, mot) + " "
#    reference[ind] = nouvelleChaine.strip()
#    ind += 1

donneeMot = []
trouver = False
# partie qui renvoie toutes les combinaisons de suite de mot d'une phrase
for i in range(len(reference)): #pour chaque référence
    for j in range(len(reference[i].split(" "))): #pour chaque nombre de mot
        if len(donneeMot) <= j:
            donneeMot.append([])
        for k in range(len(reference[i].split(" "))): #pour chaque mot
            phrase = reference[i].split(" ")
            if len(phrase)+1 > j+k+1:
                for l in range(len(donneeMot[j])):
                    #print(" ".join(phrase[k:j+k+1]))
                    #print(donneeMot[j][l][0])
                    if " ".join(phrase[k:j+k+1]) == donneeMot[j][l][0]:
                        trouver = True
                        break
                if trouver:    
                    donneeMot[j][l][1] += 1
                else:
                    donneeMot[j].append([" ".join(phrase[k:j+k+1]), 1])
                trouver = False
                

for i in range(len(donneeMot)):
    #for j in range(len(donneeMot[i])):
    donneeMot[i] = sorted(donneeMot[i], key=lambda x: x[1], reverse=True)



meilleurReference = []
for i in donneeMot:
    x = (len(i)*25)//100
    for j in range(x):
        meilleurReference.append(i[j])
        
pprint(meilleurReference)

pointQuestion = 0
for i in meilleurReference:
    if i[0] in question:
        pointQuestion += i[1]

pointQuestion = pointQuestion/len(question.split(" "))

point = 0
tablePoint = []
for j in reference:
    for i in meilleurReference:
        if i[0] in j:
            point += i[1]
    point = point/len(j.split(" "))
    tablePoint.append(point)
    print(str(j)+str(point))
    point = 0
print("la moyenne: "+str(sum(tablePoint)/len(reference)))
print("point: "+str(pointQuestion))
if pointQuestion >= min(tablePoint):
    heure()

probabilite = (100 * (pointQuestion-min(tablePoint))) / (max(tablePoint)-min(tablePoint))
print("la probabilité: "+str(probabilite))