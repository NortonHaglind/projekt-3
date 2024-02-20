# rock=1
# scissors=2
# paper=3
from msvcrt import getwch
import functions, os, random
from functions import bcolors
win = 0
loss = 0
tie = 0
rounds = -1
active = True
os.system("cls")
move_list = {"R": 1, "P": 3, "S": 2, "F":4, "Q":0}  # visar vad bokstäverna är till koden
move_hands = {1: bcolors.DEFAULT + bcolors.RED + """
   _________
  |   |  |  \__
  /¨¨¨¨===  |  |
 /    ___/__|__|
|    /         |
 \____ROCK_____/             
              """, 3: bcolors.DEFAULT + bcolors.GREEN + """
    __ __ __
   |  |  |  |__
   |¨¨|¨¨|¨¨|  |
__ |¨¨|¨¨|¨¨|¨¨|
\ \|  |  |  |¨¨|
|  \__         |
|              |
 \____PAPER____/
""", 2:  bcolors.DEFAULT + bcolors.BLUE + """
 __       __
 \  \   /  /
  \  \ /  /
   \  V  /__ __
  /¨¨¨¨===  |  |
 /    ___/__|__|
|    /         |
 \__SCISSORS___/
"""}  # skriver om siffrorna till händer.




while active:
    cheat = False
    ai = random.randint(1, 3)
    rounds = rounds+1
    

    
    
    os.system("cls")
    print(bcolors.DEFAULT + bcolors.YELLOW +  f"Rounds: {rounds} Wins: {win} Losses: {loss} Ties: {tie}")
    print(
    bcolors.YELLOW + f"Välkommen till {bcolors.RED}Rock {bcolors.GREEN}Paper {bcolors.BLUE}Scissors! {bcolors.RED}Rock=\'R\' {bcolors.GREEN}Paper=\'P\' {bcolors.BLUE}Scissors=\'S\' {bcolors.PURPLE}Quit=\'Q\' {bcolors.YELLOW + bcolors.UNDERLINE}Fusk=\'F\'" + bcolors.DEFAULT)

    while True:
        player = getwch().upper()

        if player not in move_list:
            continue
        elif move_list[player] > 0 and move_list[player] < 4:  # kollar om ditt "move" är en av 1-3
            
            print(bcolors.YELLOW + bcolors.UNDERLINE + f"Spelare hand: {move_hands[move_list[player]]}")  # skriver om bokstaven till handen
            if move_list[player] == ai:
                print(bcolors.DEFAULT + bcolors.YELLOW + f"Det blev lika")
            elif ai or move_list[player] == 1:
                functions.check(move_list, player, ai)
            elif ai or move_list[player] == 2:
                functions.check(move_list, player, ai)
            if cheat == True:
                break
            else:
               print(bcolors.UNDERLINE + bcolors.YELLOW + f"Ai hand: {move_hands[ai]}") 
               break
            
        elif player == "Q":
                    
            print(bcolors.PURPLE + bcolors.UNDERLINE + f"GG next")

            active = False

            exit()
        elif player == "F" and cheat == False:
            cheat = True
            print(bcolors.YELLOW + bcolors.UNDERLINE + f"Ai hand:{bcolors.DEFAULT} {move_hands[ai]}")
            continue
    if move_list[player] == ai:     #lägger till resultatet till poängräknaren 
        tie = tie+1 
    elif functions.result_check == 2:
        loss = loss+1
    elif functions.result_check == 1: 
        win = win+1  
    print("press anything to continue")
    round_end=getwch()
    