import mysql.connector
from pprint import pprint
import re


#Connection et authentification à la base de donnée
conect = mysql.connector.connect(host="",user="",password="", database="ia.2.2")


compteurX = 0
compteurY = 0
phraseTable = []
phraseCorrect = False


# ======================================= fonction ======================================= #

# ============== verbe ============== #

def verbe(phraseTable, emplacement):
    phraseCorrect = False
    typeMot = "VER"
    
    if emplacement == 0:
        for resultatDuMot in phraseTable:
            if emplacement == 0:
                emplacement += 1
                continue
            
            else:
                for mot in resultatDuMot:
                    TypeMot = mot[1].split(":")
                    if typeMot == "VER":
                        if TypeMot[0] == "PRO" or TypeMot[0] == "ART":
                            phraseCorrect = True
                            break
                        else:
                            phraseCorrect = False
                    
                    elif typeMot == "PRO":
                        if TypeMot[0] == "ART" or TypeMot[0] == "NOM" or TypeMot[0] == "PRE" == TypeMot[0] == "PRO":
                            phraseCorrect = True
                            break
                        else:
                            phraseCorrect = False
                        
                    elif typeMot == "PRE":
                        if TypeMot[0] == "VER" or TypeMot[0] == "ART" or TypeMot[0] == "ADJ":
                            phraseCorrect = True
                            break
                        else:
                            phraseCorrect = False
                    
                    elif typeMot == "ART":
                        if TypeMot[0] == "NOM" or TypeMot[0] == "NOM":
                            phraseCorrect = True
                            break
                        else:
                            phraseCorrect = False
                    
                    elif typeMot == "NOM":
                        if TypeMot[0] == "NOM" or TypeMot[0] == "PRE" or TypeMot[0] == "ADJ":
                            phraseCorrect = True
                            break
                        else:
                            phraseCorrect = False
                    
                    elif typeMot == "ADJ":
                        if TypeMot[0] == "NOM" or TypeMot[0] == "PRE":
                            phraseCorrect = True
                            break
                        else:
                            phraseCorrect = False
                    
                if not phraseCorrect:
                    break
    
    return phraseCorrect
                        
# ============== verbe ============== #


# extrait tout les caractère non alphabétique et les acsents
def extraitAlphabet(texte):
    """Retourne une chaine de caractères sans les accents"""
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
    nouveauTexte = ""
    for caractere in texte:
        nouveauTexte += accents.get(caractere, caractere)
        
    texte = espacement(nouveauTexte)
    return re.sub(r'[^a-zA-Z\s]', '', texte)

# espacement entre les mot
def espacement(phrase):
        phrase = phrase.replace("-", " ")
        phrase = phrase.replace("'", " ")
        phrase = phrase.lower()
        return phrase

#requête SQL qui cherche le mot et le type de mot
def CommandeSQLRechercheMot(mot):
    #Connection
    SQLLite = conect.cursor()
    #Execute commande SQL
    SQLLite.execute("""
    SELECT Ortho, cgram FROM t_dico
    WHERE Ortho = '{}';
    """.format(mot))
    #Récupèrre le résultat de la commande
    donnee = SQLLite.fetchall()
    #Se déconnect
    SQLLite.close()
    return donnee

# ======================================= fonction ======================================= #

# ======================================= programme ======================================= #

questionOriginal = input("question: ")
questionEspacement = espacement(questionOriginal)
questionExtraitAlphabet = extraitAlphabet(questionOriginal)
questionTable = questionEspacement.split(" ")
for mot in questionTable:
    resultatSql = CommandeSQLRechercheMot(mot)
    phraseTable.append([])
    for j in resultatSql:
        if j[0] == mot:
            print(j)
            phraseTable[compteurX].append([j[0], j[1]])
    compteurX += 1

pprint(phraseTable)

for resultatDuMot in phraseTable:
    for mot in resultatDuMot:
        TypeMot = mot[1].split(":")
        if TypeMot[0] == "VER":
            phraseCorrect = verbe(phraseTable, compteurY)

if phraseCorrect:
    print("OK")
else:
    print("et non...")

# ======================================= programme ======================================= #