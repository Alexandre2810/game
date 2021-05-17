import random

sujet = ["Il parait que tu", "Ton corps","T'es con tu","Tu ressemble","Ton père"]#1
verbe = ["on dirait","t'es","ressemble","le grand pecheur","pue"]#2
complement = ["gravement","tellement","un chien","le charbonneur","qui","une quille","à","à"]#3
fin = ["chier dessus","enculé","sans ame","petasse"," la catin"]#4

dictionary = {
    "sujet" : sujet,
    "verbe" : verbe,
    "complement" : complement,
    "fin" : fin
}
p1_list = []
p2_list = []
arrayFinal = []
randomBonus = random.choice(list(dictionary.keys()))
randomMalus = random.choice(list(dictionary.keys()))

while randomBonus == randomMalus :
      randomBonus = random.choice(list(dictionary.keys()))
      
for i in dictionary:
    currentWord = random.choice(dictionary[i])
    if i == randomBonus:
        dictionary[i].pop(dictionary[i].index(currentWord))
        arrayFinal.append(currentWord)
        
    currentWord = random.choice(dictionary[i])
    dictionary[i].pop(dictionary[i].index(currentWord))
    arrayFinal.append(currentWord)

   



