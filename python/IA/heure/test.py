ponctuations = [".", "!", "?",]


questionMinuscule = input("quest: ")
phraseQuestion = questionMinuscule
for ponctuation in ponctuations:
                while ponctuation in phraseQuestion:
                    positionPonctuation = questionMinuscule.index(ponctuation)
                    if positionPonctuation > questionMinuscule.index("heure"):
                        phraseQuestion = phraseQuestion[0:positionPonctuation]
                    else:
                        phraseQuestion = phraseQuestion[positionPonctuation+1:-1]
                        
                    print(phraseQuestion)
