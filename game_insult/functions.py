from perso import Player
from data import *
import random 
player1 = Player(1)
player2 = Player(2)


# Fonction pour lancer le debut du jeux et permet de definir qui commence en premier
def start_game():
    first = [player1.name,player2.name]
    random.choice(first)
    rad = random.choice(first)
    if rad == player1.name:
        player1.turn += 1
        tour_de_jeu()
    elif rad == player2.name:
        player2.turn += 1
        tour_de_jeu()

# Fonction choix des personnages
def game():
    while True:
        print("Choisir un personnage\n")
        choix = int(input("1 : Red 2 : Blue\n"))
        if choix == 1:
            player1 = Player(1)
            player2 = Player(2)
            break
        elif choix == 2:
             player1 = Player(1)
             player2 = Player(2)
             break
        else:
            print("choisis 1 ou 2\n")
    start_game()

# Tour de jeu
def tour_de_jeu():
    if player1.turn == 1:
        player1.turn -= 1
        player2.turn +=1 
        print("C'est à toi")
        print(player1.name,":",player1.hp)
        print("Insulte de Red :",p1_list,"\n")
        
    elif player2.turn == 1:
        player1.turn += 1
        player2.turn -=1 
        print("C'est à toi")
        print(player2.name,":",player2.hp)
        print("Insulte de Blue:",p2_list,"\n")
              
    link()

# affichage
def link():
    random_sujet = random.choice(sujet)
    random_verbe = random.choice(verbe)
    random_complement = random.choice(complement)
    random_fin = random.choice(fin)
    slime = [random_sujet,random_verbe,random_complement,random_fin]
    print("1:",slime[0])
    print("2:",slime[1])
    print("3:",slime[2])
    print("4:",slime[3])
    print("5: Insulter","\n")

    repons = int(input("choisir\n"))
    if player1.turn == 1:
        player1.rep = repons
    
    if player2.turn == 1:
        player2.rep = repons

    if player1.rep == 1:
        p2_list.append(random_sujet)
    elif player1.rep == 2: 
        p2_list.append(random_verbe)
    elif player1.rep == 3: 
        p2_list.append(random_complement)
    elif player1.rep == 4: 
        p2_list.append(random_fin)
    elif player1.rep == 5:
        player2.setInsult(True)
        finisher()
    player1.rep = 0

    if player2.rep == 1:
        p1_list.append(random_sujet)
    elif player2.rep == 2: 
        p1_list.append(random_verbe)
    elif player2.rep == 3: 
        p1_list.append(random_complement)
    elif player2.rep == 4: 
        p1_list.append(random_fin)
    elif player2.rep == 5:
        player1.setInsult(True)
        finisher()
    player2.rep = 0
    
    tour_de_jeu()

# INSULTER
def finisher():
    if player1.insult == True:        
        # print(-(len(p1_list) * 2))
        player2.setHp(player2.hp - (len(p1_list) * 2))
        # print(p1_list)
        i=0
        while(i < len(p1_list)):
            p1_list.pop(i)    
        # print(p1_list)     
        player1.setInsult(False) 
        player1.rep = 0 
        if player2.getHp() <= 0 :
            print("vous avez perdu",player2.name)
            exit()

    if player2.insult == True:
        # print(-(len(p2_list) * 2))
        player1.setHp(player1.hp - (len(p2_list) * 2))
        # print(p2_list)
        i=0
        while(i < len(p2_list)):
            p2_list.pop(i)  
        # print(p2_list)         
        player2.setInsult(False)
        player2.rep = 0 
        if player1.getHp() <= 0 :
            print("vous avez perdu",player1.name)
            exit()
