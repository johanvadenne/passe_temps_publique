# ========================================= import ========================================= #

import re
from pprint import pprint
from time import strftime

# ========================================= import ========================================= #

# ========================================= fonction ========================================= #

# retourne que des caractères alphabétique et simplifie des nom de verbe
def supprimeCaractereSpeciaux(texte):
    # créer les espaces
    phrase = texte.replace("-", " ")
    phrase = phrase.replace("'", " ")
    # réduit le texte un minuscule
    phrase = phrase.lower()
    
    nouvelleChaine = ""
    
    for caractere in phrase:
        # remplace la lettre accentué par sa lettre alphabéthique d'origine
        nouvelleChaine += accents.get(caractere, caractere)
    nouvelleChaine = re.sub(r'[^a-z0-9\s]', '', nouvelleChaine)
    
    nouvelleChaineTable = []
    
    # remplace le verbe conjugué par son verbe indicatif
    for mot in nouvelleChaine.split(" "):
        nouvelleChaineTable.append(verbe.get(mot, mot))
    nouvelleChaine = " ".join(nouvelleChaineTable)
    return nouvelleChaine

# retourne l'heure
def heure():
    print("il est "+ strftime("%H:%M:%S"))

# ========================================= fonction ========================================= #

# ========================================= objet ========================================= #

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

formalite = [
    "s'il vous plaît",
    "s'il te plaît",
]

# ========================================= objet ========================================= #

# ========================================= variable ========================================= #

donneeMot = []
meilleurReference = []
trouver = False
ind = 0
pointQuestion1 = 0
pointQuestion2 = 0
gagnerPoint = False
pointReference = 0
tableRefPoint = []

# ========================================= variable ========================================= #

# ========================================= programme ========================================= #

# ================== simplification des phrases ================== #

# ouverture fichier "reference2.txt"
fichier = open("reference.txt", "r+", encoding="utf-8")
reference = (fichier.read().split("\n"))
fichier.close()

# pour chaque phrase référence "supprimeCaractereSpeciaux()"
for ind in range(len(reference)):
    reference[ind] = supprimeCaractereSpeciaux(reference[ind])


# pour chaque formalité "supprimeCaractereSpeciaux()"
for ind in range(len(formalite)):
    formalite[ind] = supprimeCaractereSpeciaux(formalite[ind])

## supprime les formalité
# pour chaque phrase référence
for ind in range(len(reference)):
    # pour chaque phrase de formalité
    for phraseFor in formalite:
        #supprime les formalités
        phraseRef = reference[ind].replace(phraseFor, "")
        reference[ind] = phraseRef.strip()


## pour la question "supprimeCaractereSpeciaux()" et supprime les formalités
question = input("question: ")
question = supprimeCaractereSpeciaux(question)
for phraseFor in formalite:
    question = question.replace(phraseFor, "")
    question = question.strip()

# ================== simplification des phrases ================== #

# ================== calcul et enregistrement des données ================== #

## enregistre toutes les combinaisons de suite de mot d'une phrase (ex:"je suis là" enregistre: "je","suis","là","je suis","là suis","je suis là")
# pour chaque référence
for indRef in range(len(reference)):
    
    # pour chaque mot référence
    for indMotRef in range(len(reference[indRef].split(" "))):
        
        # ajoute une table pour chaque mot
        if len(donneeMot) <= indMotRef:
            donneeMot.append([])
            
        # pour chaque mot référence
        for indMotRefBis in range(len(reference[indRef].split(" "))):
            # convertie la phrase référence en tableau
            phrase = reference[indRef].split(" ")
            
            indPhrase = indMotRef+indMotRefBis+1
            
            ## pour évité de sortir du tableau
            # si le nombre de mot est plus grand que l'index
            if len(phrase)+1 > indPhrase:
                for l in range(len(donneeMot[indMotRef])):
                    
                    # si la combinaisons de mot existe déjà dans mes données j'ai trouver et je casse la boucle
                    if " ".join(phrase[indMotRefBis:indPhrase]) == donneeMot[indMotRef][l][0]:
                        trouver = True
                        break
                    
                # rajoute un au nombre d'occurence
                if trouver:    
                    donneeMot[indMotRef][l][1] += 1
                # sinon créer le mot
                else:
                    donneeMot[indMotRef].append([" ".join(phrase[indMotRefBis:indPhrase]), 1])
                trouver = False
                
## trie de chaque table de donnee
for IndMot in range(len(donneeMot)):
    donneeMot[IndMot] = sorted(donneeMot[IndMot], key=lambda x: x[1], reverse=True)

## récupère 25% des meilleurs référence pour chaque nombre de mot
ind = 0

for IndMot in donneeMot:
    nombreDonneeRef = (len(IndMot)*25)//100
    if nombreDonneeRef == 0:
        continue
    meilleurReference.append([])
    
    for donnee in range(nombreDonneeRef):
        meilleurReference[ind].append(IndMot[donnee])
    ind+=1

## selon les meilleurs références trouvé, différents points sont attribué
## pour pointQuestion1: les point sont attribué selon la référence trouver et son nombre occurence 
## pour pointQuestion2: les point sont attribué son la taille de la référence trouver (1 mot: 1, 2 mot: 2, ...) 
x = 0

for MRef in meilleurReference:
    x+=1
    
    for motMRef in MRef:
        
        # si une référence est trouver dans la qestion
        if motMRef[0] in question:
            # rajoute le nombre d'occurence
            pointQuestion1 += motMRef[1]
            gagnerPoint = True
            
    if gagnerPoint:
        gagnerPoint = False
        pointQuestion2 += x
            
# calcul de la moyenne
pointQuestion1 = pointQuestion1/len(question.split(" "))

## pour chaque référence, selon les meilleurs références trouvé, différents points sont attribué
for phraseRef in reference:
    
    for typeMRef in meilleurReference:
        
        for donneMRef in typeMRef:
            
            # si une référence est trouver dans notre phrase
            if donneMRef[0] in phraseRef:
                # rajoute le nombre d'occurence
                pointReference += donneMRef[1]
    # calcul de la moyenne
    pointReference = pointReference/len(phraseRef.split(" "))
    tableRefPoint.append(pointReference)
    pointReference = 0

# calcul de la moyenne de la table
moyenne = sum(tableRefPoint) / len(tableRefPoint)

# calcul de la probabilité
probabilite = (100 * (pointQuestion1 - min(tableRefPoint))) / (max(tableRefPoint) - min(tableRefPoint))

# affiche des résultat
print("la moyenne: "+str(moyenne))
print("point: "+str(pointQuestion1))
print("la probabilité: "+str(probabilite))
print("la probabilité 2: "+str((50*pointQuestion2) / 6))
if probabilite >= 50 or pointQuestion2 >= 6:
    heure()
    
# ================== calcul et enregistrement des données ================== #

# ========================================= programme ========================================= #
