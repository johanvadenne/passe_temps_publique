from pprint import pprint

# après avoir récupérer les données de la table
# les données seront plus lisible si (ils sont en minuscule (lower()), les accents sont retirer (re), tout les verbes à l'infinitif (créer une base de donnée exprès), et autre si nécessaire, récupéré le morceau de phrase le plus interressant "," et j' en je, n' en ne, etc...)

#table temporaire remplace table donnée
tablePhraseDonnee=[
["donner le heure", 1, "", "donner le", "donner,le heure"],
["donner moi le heure", 1, "", "donner moi le", "donner,le heure"],
["ne donner pas le heure", 0, "ne,pas,ne donner pas", "donner,le", "donner,le heure"],
["ne me donner pas le heure", 0, "ne,pas,ne me donner pas", "me donner,le", "donner,le heure"]
]

# question temporaire
question = "je ne avoir pas besoin de le heure"

# question format liste
questionTable = question.split(" ")


############### vraiable ###############

point = 0
pointMaxBis = 0
pointMax = 0
pointMaxQuestion = 0
tableNegationCopy = []
vraissemblance1 = []
vraissemblance2 = []
petitevraissemblance1 = []
petitevraissemblance2 = []
vraissemblance1Bis = []
vraissemblance2Bis = []
vraissemblanceNegation = []
vraissemblanceNegationBis = []
moyenneVraissemblanceNegation = []
donneeMot = []
phraseTable = []
bon = bool
vraissemblanceNegationTrouver = bool

############### vraiable ###############


# calcule des points max pour la vraissemnlance de la question
for i in range(len(questionTable)):
    for j in range(len(questionTable)):
        if i+j+1 <= len(questionTable):
            pointMaxQuestion += 1

## test de vraissemblance
for donnee in tablePhraseDonnee:
    point = 0
    pointMax = 0
    phrase = donnee[0].split(" ")
    for indMotPhrase in range(len(phrase)):
        for indMotPhraseBis in range(len(donnee[0].split(" "))):
            indMot = indMotPhrase+indMotPhraseBis+1
            if len(phrase)+1 > indMot:
                mot = " ".join(phrase[indMotPhraseBis:indMot])
                if indMotPhrase < 1:
                    if mot in questionTable:
                        point+=1
                else:
                    if mot in question:
                        point += 1
                pointMax +=1
    pointMaxBis = pointMax 
    if pointMax < pointMaxQuestion:
        pointMax = pointMaxQuestion
    if donnee[1]:
        vraissemblance1.append((point * 100) / pointMax)
        vraissemblance1Bis.append((point * 100) / pointMaxBis)
    else:
        vraissemblance2.append((point * 100) / pointMax)
        vraissemblance2Bis.append((point * 100) / pointMaxBis)

# calcule et affichage des moyennes et vraissemblance
print("vraissemblance vrai grand: "+str(vraissemblance1Bis))
print("vraissemblance faux grand: "+str(vraissemblance2Bis))
print("vraissemblance vrai petit: "+str(vraissemblance1))
print("vraissemblance faux petit: "+str(vraissemblance2))
moyenneVraissemblance1 = sum(vraissemblance1)/ len(vraissemblance1)
moyenneVraissemblance2 = sum(vraissemblance2)/ len(vraissemblance2)
moyenneVraissemblance1Bis = sum(vraissemblance1Bis)/ len(vraissemblance1Bis)
moyenneVraissemblance2Bis = sum(vraissemblance2Bis)/ len(vraissemblance2Bis)
print("probabilité vrai grand: "+str(moyenneVraissemblance1))
print("probabilité faux grand: "+str(moyenneVraissemblance2))
print("probabilité vrai petit: "+str(moyenneVraissemblance1Bis))
print("probabilité faux petit: "+str(moyenneVraissemblance2Bis))

# afficher l'heure si...
if max(vraissemblance1) == 100 or max(vraissemblance1Bis) == 100 or  max(vraissemblance1) - max(vraissemblance2) >= 50 or max(vraissemblance1Bis) - max(vraissemblance2Bis) >= 30:
    print("il est midi")
elif max(vraissemblance2) == 100 or max(vraissemblance2Bis) == 100 or max(vraissemblance2) - max(vraissemblance1) >= 50 or max(vraissemblance2Bis) - max(vraissemblance1Bis) >= 30:
    print("négation comfirmer")
else:
    # si rien n'est détecté, chercher partie négatif
    for i in tablePhraseDonnee:
        if not i[1]:
            point = 0
            pointBis = 0
            tableNegation = []
            pointMax = 0
            pointMaxBis = 0
            i = str(i[2]).split(",")
            for j in i:
                if len(str(j).split(" ")) > 1:
                    if j in question:
                        point += len(j.split(" "))
                    pointMax += len(j.split(" "))
                else:
                    if j in questionTable:
                        point += 1
                        pointBis += 1
                        tableNegation.append(j)
                    pointMax += 1
                    pointMaxBis += 1
            vraissemblanceNegation.append((point*100)/pointMax)
            resutat = (pointBis*100)/pointMaxBis
            if resutat == 100:
                vraissemblanceNegationTrouver = True
                tableNegationCopy.append(tableNegation)
            else:
                vraissemblanceNegationTrouver = False
    print("vraissemblance négation: "+str(vraissemblanceNegation))
    for i in range(len(vraissemblanceNegation)):
        moyenneVraissemblanceNegation.append((vraissemblanceNegation[i]+vraissemblance2[i])/2)
        pobaNegation = sum(moyenneVraissemblanceNegation)/len(moyenneVraissemblanceNegation)
    print("moyenne négation: "+str(moyenneVraissemblanceNegation))
    print("probabilité négation: "+str(pobaNegation))
    if max(moyenneVraissemblanceNegation) >= 80:
        print("négation comfirmer")
        # si la probabilité n'est pas assé elevé
    else:
        # chercher les mots de la 4ème colonne
        for i in tablePhraseDonnee:
            point = 0
            pointMax = 0
            mot = str(i[3]).split(",")
            for j in mot:
                if len(str(j).split(" ")) > 1:
                    if j in question:
                        point += len(j.split(" "))
                    pointMax += len(j.split(" "))
                    for k in str(j).split(" "):
                        if k in questionTable:
                            point += 1
                        pointMax += 1
                else:
                    if j in questionTable:
                        point += 1
                    pointMax += 1
            if i[1]:
                petitevraissemblance1.append((point * 100) / pointMax)
            else:
                petitevraissemblance2.append((point * 100) / pointMax)
                
                
print("petite ressemblance vrai: "+str(petitevraissemblance1))
print("petite ressemblance faux: "+str(petitevraissemblance2))
moyennePetiteRessemblance1 = sum(petitevraissemblance1)/len(petitevraissemblance1)
moyennePetiteRessemblance2 = sum(petitevraissemblance2)/len(petitevraissemblance2)
print("petite probabilité vrai: "+str(moyennePetiteRessemblance1))
print("petite probabilité faux: "+str(moyennePetiteRessemblance2))
moyenneGeneral1 = (moyenneVraissemblance1 + moyenneVraissemblance1Bis + moyennePetiteRessemblance1) / 3
moyenneGeneral2 = (moyenneVraissemblance2 + moyenneVraissemblance2Bis + moyennePetiteRessemblance2) / 3
print(f"({moyenneVraissemblance1} + {moyenneVraissemblance1Bis} + {moyennePetiteRessemblance1}) / 3")
print(f"({moyenneVraissemblance2} + {moyenneVraissemblance2Bis} + {moyennePetiteRessemblance2}) / 3")
print("moyenne générale vrai: "+str(moyenneGeneral1))
print("moyenne générale faux: "+str(moyenneGeneral2))
if moyenneGeneral1 > moyenneGeneral2:
    print("c'est l'heure")
    vraiQuestion = 1
else:
    print("désolé je n'ai pas de montre sur moi")
    vraiQuestion = 0



#################### partie fin ####################


#################### recupère référence base ####################

trouver = False
for i in tablePhraseDonnee:
    phraseTable = str(i[0]).split(" ")
    for j in range(len(phraseTable)):
        if len(donneeMot) <= j:
                donneeMot.append([])
        for k in range(len(phraseTable)):
            indPhrase = j+k+1
            if len(phraseTable)+1 > indPhrase:
                for l in range(len(donneeMot[j])):
                    if " ".join(phraseTable[k:indPhrase]) == donneeMot[j][l][0]:
                        trouver = True
                        break
                # rajoute un au nombre d'occurence
                if trouver:    
                    donneeMot[j][l][1] += 1
                # sinon créer le mot
                else:
                    donneeMot[j].append([" ".join(phraseTable[k:indPhrase]), 1])
                trouver = False

referanceTable = []
for i in donneeMot:
    for j in i:
        if j[1] == len(tablePhraseDonnee):
            referanceTable.append(j[0])
referenceBase = ",".join(referanceTable)
phrase = question

#################### recupère référence base ####################

reponse =""
#reponse = input("ai-je bien répondu à votre question")
#if reponse == "n":
#    if vraiQuestion == 1:
#        vraiQuestion = 0
#    else:
#        vraiQuestion == 1

#################### recupère créer petite ref ####################

######## si pas bonne question ########

x = 0
petiteRefTable = questionTable.copy()
if not vraiQuestion:
    for i in questionTable:
        if i in referanceTable:
            petiteRefTable[x] = ","
        x+=1
    petiteRef = " ".join(petiteRefTable)
while ", ," in petiteRef:
    petiteRef = petiteRef.replace(", ,",",")
while "," == list(petiteRef[0]):
    petiteRef = list(petiteRef)
    petiteRef.pop(0)
    petiteRef.pop(0)
    petiteRef = "".join(petiteRef)
while "," == petiteRef[len(petiteRef)-1]:
    petiteRef = list(petiteRef)
    petiteRef.pop(len(petiteRef)-1)
    petiteRef.pop(len(petiteRef)-1)
    petiteRef = "".join(petiteRef)

for i in tablePhraseDonnee:
    if not i[1]:
        mot = str(i[2]).split(",")
        petiteRefTable = petiteRef.split(" ")
        for j in mot:
            x = 0
            if len(j.split(" ")) < 2:
                for k in petiteRefTable:
                    if k == j:
                        petiteRefTable[x] = ","
                    x+=1
                
petiteRef = " ".join(petiteRefTable)

while " , " in petiteRef or ", " in petiteRef or " ," in petiteRef:
    petiteRef = petiteRef.replace(" , ", ",")
    petiteRef = petiteRef.replace(", ", ",")
    petiteRef = petiteRef.replace(" ,", ",")
    
print(petiteRef)
######## si pas bonne question ########

#################### recupère créer petite ref ####################

tableOccurence = []
x = 0
trouver = False
if vraissemblanceNegationTrouver:
    for i in tableNegationCopy:
        for j in i:
            if j in tableOccurence:
                continue
            else:
                tableOccurence.append(j)
    nbr = len(tableOccurence)
    if nbr > 1:
        for i in questionTable:
            if i in tableOccurence:
                print(x)
                x = 0
                trouver = True
            elif trouver:
                x+=1
                
            
            
            
print(tableOccurence)

################## à refaire (au propre)!!! partie sur la bonne voie
# recapitulatif:

###### fait ######

# créer une table avec (la phrase, le type de question, les négations, les second référence, les première références, le nombre de mot entre les négations)
# -- les phrases seront enregistrer en miniscule

###### fait ######

# -- touts les caractères indésirables retirer ou remplacer par des espace ou leurs lettres d'origine, tous les verbes seront à l'infinitif, voir plus tard => determinant et pluriel singulier
# -- lorsque la question est posé on vérifie si la première référence est dedans (si oui on lance l'analyse)
# -- une fois le programme lancer on vas recupérer la partie de la phrase qui à la référence (séparer la phrase lorsque qu'il y à une virgule ou d'autre ponctuation)
# -- faire 2 analyse de vraissemblance, une pour les petites phrase et une autre pour les grange phrase
# -- je définie la la meilleurs condition pour afficher le résultat, la condition que j'ai créer, voir si l'on peut pas la définir la le programme lui-même:
# ---- if max(vraissemblance1) == 100 or max(vraissemblance1Bis) == 100 or max(vraissemblance1) - max(vraissemblance2) >= 50 or max(vraissemblance1Bis) - max(vraissemblance2Bis) >= 30:
# ---- elif max(vraissemblance2) == 100 or max(vraissemblance2Bis) == 100 or max(vraissemblance2) - max(vraissemblance1) >= 50 or max(vraissemblance2Bis) - max(vraissemblance1Bis) >= 30:
# -- si aucun résultat après cet deux conditions, détecter si il y a des négations, si tout les négations d'une phrase on été trouvé ne pas dire l'heure
# -- si touts les petit mot négatif on été tout saisir une variable en vrai
# -- si toujours aucun résutat, faire un test de vrassemblance avec les secondes références
# -- (pas encore fait) touts les petit mot négatif on été tout, vérifier la distance des petit mot négatif si il y en à plusieurs par rapport à nos données
# -- selon la distance des mots négatifs créer une condition
# -- si toujours aucun résultat faire la moyenne de toutes nos moyennes calculé
# -- puis afficher par rapport au résultat
# -- poser la question si la question si bien répondu
# -- récupérer les donnée à insére dans la base
# -- la phrase (facile)
# -- le type de phrase (facile)
# -- ce qui fais de la phrase une négation (difficile)
# -- les second référence ( après avoir trouver les négation, facile)
# -- les première référence (facile) petit hic
# -- le nombre de mot entre les négations (facile)
# -- faire les modifications nécessaire dans la bases (difficile (pas encore réfléchie))