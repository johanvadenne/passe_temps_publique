# ========================================= import ========================================= #

import re
from pprint import pprint
from time import strftime
from Objet import *
import mysql.connector

# ========================================= import ========================================= #

# ================= connection à la base de donné ================= #

conect = mysql.connector.connect(host="localhost",user="root",password="", database="time")

# ================= connection à la base de donné ================= #


# ========================================= fonction ========================================= #

# ========================================= fonction ========================================= #

# ========================================= variable ========================================= #

ponctuations = [".", "!", "?",]

# ========================================= variable ========================================= #


# retourne que des caractères alphabétique et simplifie des nom de verbe
def purificationPhrase(texte):
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
        nouvelleChaineTable.append(verbeInfinitif.get(mot, mot))
    nouvelleChaine = " ".join(nouvelleChaineTable)
    nouvelleChaine = nouvelleChaine.strip()
    return nouvelleChaine

    ##### voir plus tard => determinant (j', l') et pluriels


def executeRequete(requete):
    #Connection
    SQLLite = conect.cursor()
    #Execute commande SQL
    SQLLite.execute(requete)
    #Récupèrre le résultat de la commande
    donnee = SQLLite.fetchall()
    #Se déconnect
    SQLLite.close()
    
    return donnee


def texteFormatSQL(liste):
    table = []
    for i in liste:
        table.append(f"'{i}'")
    texte = ",".join(table)
    return texte


# ========================================= fonction ========================================= #

###### étape 1 ######
### récupére la phrase et la purifié

questionBrut = input("question: ")
questionMinuscule = questionBrut.lower()
questionNettoyer = purificationPhrase(questionBrut)
questionTable = questionNettoyer.split(" ")

print(questionBrut)
print(questionNettoyer)
print(questionTable)

###### étape 2 ######
### rechercher les mots clés pour connaitre le type d'action

req = texteFormatSQL(questionTable)
print(req)

reqSQL = f"SELECT * FROM t_tableref WHERE MotRef IN ({req})"
print(reqSQL)

donneCle = executeRequete(reqSQL)
print(donneCle)

###### étape 3 ######
### vérifier si un mot clé est trouvé
### si trouver executer le type d'action et récupérer les données nécessaires
print(len(donneCle))
if len(donneCle) > 0:
    for Cle in donneCle:
        if Cle[2] == 1:
            # créer une fonction
            reqSQL = f"SELECT * FROM {Cle[3]}"
            print(reqSQL)
            donneRef = executeRequete(reqSQL)
            
            ###### étape 4 ######
            ### réduire la phrase
            phraseQuestion = questionMinuscule
            for ponctuation in ponctuations:
                while ponctuation in phraseQuestion:
                    positionPonctuation = phraseQuestion.index(ponctuation)
                    if positionPonctuation > phraseQuestion.index(Cle[1]):
                        phraseQuestion = phraseQuestion[0:positionPonctuation]
                    else:
                        phraseQuestion = phraseQuestion[positionPonctuation+1:-1]
                        
                    print(phraseQuestion)
                    
            phraseNettoyer = purificationPhrase(phraseQuestion)
            phraseTable = phraseNettoyer.split(" ")