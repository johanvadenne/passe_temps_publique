import random
from pprint import pprint
import re
import mysql.connector
from time import strftime

#Connection et authentification à la base de donnée
conect = mysql.connector.connect(host="",user="",password="", database="time")


#Connection
SQLLite = conect.cursor()
#Execute commande SQL
SQLLite.execute("SELECT Ortho, lemme, cgram FROM t_dico WHERE cgram = 'VER';")
#Récupèrre le résultat de la commande
donnee = SQLLite.fetchall()
#Se déconnect
SQLLite.close()

table = []
for i in donnee:
    x = 0
    trouver = False
    for j in table:
        if i[1] == j[0]:
            trouver = True
            break
        x+=1
    if not trouver:
        table.append([i[1]])
    
    table[x].append(i[0])
    print(x)
pprint(table)
fichier = open("verbeConjuguer1.txt", "w+", encoding="utf-8")
fichier.write(str(table))