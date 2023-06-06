from pprint import pprint

fichier = open("verbe.txt", "r+", encoding="utf-8")
tableVerbe = fichier.read()
fichier.close

tableVerbe = tableVerbe.split("\n")

Terminaison = [
    "e",
    "es",
    "e",
    "ez",
    "ons",
    "ent"
]

x = 0
verbeConjuguer = []

for verbe in tableVerbe:
    conjugaison = ""
    verbeConjuguer.append([])
    for i in Terminaison:
        conjugue =verbe[:-2] + i
        verbeConjuguer[x].append(conjugue)
    x += 1

pprint(verbeConjuguer)