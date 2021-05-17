from functions import *

game_start = True

while game_start == True:
    start_menu = int(input("1 : Start 2: Quit\n"))
    if start_menu == 1:
        game_start = False
        new_game = game()
    elif start_menu == 2:
        quit()
        

