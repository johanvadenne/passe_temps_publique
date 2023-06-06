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
# -- faire les modifications nécessaire dans la bases (difficile (pas encore réfléchie)