from verbeConjuguer import *
import mysql.connector

x = 1
texte = []
for i in table:
    x = 1
    for j in i:
        if x == 1:
            x = 2
            continue
        texte.append("INSERT INTO t_verbeinfinitif VALUES ('{}', '{}')".format(i[0].replace("'","\\'"), j.replace("'","\\'")))

#Connection et authentification à la base de donnée
conect = mysql.connector.connect(host="",user="",password="", database="time")

for i in texte:

    #Connection
    SQLLite = conect.cursor()
    #Execute commande SQL
    SQLLite.execute(i)
    #Récupèrre le résultat de la commande
    donnee = SQLLite.fetchall()
    #Se déconnect
    SQLLite.close()