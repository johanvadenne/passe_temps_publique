import random
import re
import mysql.connector
from time import strftime

#Connection et authentification à la base de donnée
conect = mysql.connector.connect(host="",user="",password="", database="time")

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

def CommandeSQL():
    #Connection
    SQLLite = conect.cursor()
    #Execute commande SQL
    SQLLite.execute("SELECT * FROM t_time;")
    #Récupèrre le résultat de la commande
    donnee = SQLLite.fetchall()
    #Se déconnect
    SQLLite.close()
    return donnee

def CommandeSQLInsert(phrase, bon, morceau):
    #Connection
    SQLLite = conect.cursor()
    #Execute commande SQL
    SQLLite.execute("INSERT INTO t_time VALUES('{}', {}, '{}')".format(phrase, bon, morceau))
    #Récupèrre le résultat de la commande
    donnee = SQLLite.fetchall()
    #Se déconnect
    SQLLite.close()
    return donnee

# retourne l'heure
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



question = input("question: ")
question = supprimeCaractereSpeciaux(question)

fichier = open("bon.txt", "r+", encoding="utf-8")
reference = (fichier.read().split("\n"))
fichier.close()

donneeTable = CommandeSQL()
print(donneeTable)

for i in donneeTable:
    if i[2] in question.split(" "):
        heure()
        morceau = i[2]

reponse = input("est-ce que j'ai bien répondu?\n")

if reponse == "oui":
    for i in donneeTable:
        if question == i[0]:
            quit()
    else:
        CommandeSQLInsert(question, 1, morceau)