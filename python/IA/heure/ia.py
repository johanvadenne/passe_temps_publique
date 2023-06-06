    # ======================================= import ======================================= #

import re
from datetime import datetime
from pprint import pprint
from time import gmtime, strftime, time

while 1:
    # ======================================= import ======================================= #

    # ======================================= variable ======================================= #

    
    motReference = []
    compteur = 0
    trouver = False
    donneeQuestion = 0

    # ======================================= variable ======================================= #

    # ======================================= fonction ======================================= #

    # affiche l'heure
    def afficheHeure():
        return strftime("%H:%M:%S", gmtime())

    # espacement entre les mot
    def espacement(phrase):
        phrase = phrase.replace("-", " ")
        phrase = phrase.replace("'", " ")
        phrase = phrase.lower()
        return phrase

    # extrait tout les caractère non alphabétique et les acsents
    def extraitAlphabet(sentence):
        return re.sub(r'[^a-zA-Z\s]', '', sentence)

    # ======================================= fonction ======================================= #

    # ======================================= programme ======================================= #

    # question
    question = input("question: ")
    temps = time()
    # ouvre fichier reference
    fichier = open("reference.txt", "r+", encoding="utf-8")
    reference = (fichier.read().split("\n"))
    fichier.close()

    # pour chaque reference
    for phrase in reference:
        # sépare les mots
        phrase = espacement(phrase)
        phrase = phrase.split(" ")
        
        # pour chaque phrase
        for mot in phrase:
            # retire les caractère indésirable
            mot = extraitAlphabet(mot)
            
            # si il n'y à pas de mot continuer
            if mot == "":
                continue
            else:
                # calcule tout les mots dans un tableau [nom du mot, nombre de répétition]
                for i in range(len(motReference)):
                    # initialisation
                    trouver = False
                    if mot == motReference[i][0]:
                        trouver = True
                        break
                    else:
                        continue
                    
                if trouver:
                    motReference[i][1] += 1
                else:
                    motReference.append([mot, 1])
                
        compteur+=1

    pprint(sorted(motReference, key=lambda student: student[1], reverse=True))


    # analyse qestion
    for phrase in reference:
        texte1 = extraitAlphabet(question)
        texte2 = extraitAlphabet(phrase)
        # si la question est la même que nos données de référence alors afficher l'heure
        if texte1 == texte2:
            print(afficheHeure())
            break
        
        else:
            # sépare les mots dans une table
            phraseQuestion = espacement(question)
            phraseQuestion = phraseQuestion.split(" ")
            for motQuestion in phraseQuestion:
                # initialisation
                trouver = False
                # retire les caractère indésirable
                motQuestion = extraitAlphabet(motQuestion)
                
                # si il n'y à pas de mot continuer
                if motQuestion == "":
                    continue
                
                # cherche si il y a les même mot dans la question et référence
                for motRef, nbOccurrences in motReference:
                    if motQuestion == motRef:
                        trouver = True
                        break
                    else:
                        continue
                    
                if trouver:
                    donneeQuestion += nbOccurrences
                    
            break

    # calcule des résulats
    donneeReference = len(phraseQuestion) * (len(reference) / 2)
    print(str(donneeQuestion) + ' | ' + str(donneeReference))

    # affichichage 
    if donneeQuestion >= donneeReference:
        print("voici l'heure actuelle: " + afficheHeure())
    else:
        print("Désolé je ne peux pas répondre à votre question")

    trouver = False
    phraseQuestion = extraitAlphabet(question).replace(" ", "")
    for phrase in reference:
        phrase = extraitAlphabet(phrase).replace(" ", "")
        if phraseQuestion == phrase:
            trouver = True
            break
    print(temps - time())

    if not trouver:
        reponse = input("Dois-je utiliser cette questions comme référence? [o/n]: ")

        if reponse == "o":
            fichier = fichier = open("reference.txt", "a+", encoding="utf-8")
            fichier.write("\n"+question)
            fichier.close()
            
# ======================================= programme ======================================= #