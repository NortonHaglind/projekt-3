# skapare = Norton Haglind Hilbers
# datum = 2024/03/12
# namn på proj. = Sten, Sax & Påse
from msvcrt import getwch
import functions, os, random
from functions import bcolors
win = 0
loss = 0
tie = 0
rounds = -1
active = True
os.system("cls")
move_list = {"R": 1, "P": 3, "S": 2, "F":4, "Q":0, "Z":5}  # visar vad bokstäverna är till koden
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

functions.start_screen()#skriver ut start skärm

while active:
    cheat = False
    start_check = True
    ai = random.randint(1, 3)
    rounds = rounds+1
    
    if cheat==True : #så inte den overflowar
        pass
    else:
        functions.play_screen(tie, win, loss, rounds)
    
 
    
    
    while True:
        
        
        player = getwch().upper() 
        if cheat==True: #så inte handen skrivs ut två gånger
            pass
        else:
            if player in move_list:
                os.system("cls")
            else:
                continue
        
        
        
        if player in move_list: # ser om man kan göra movet

            if move_list[player] > 0 and move_list[player] < 4:  # kollar om ditt "move" är en av 1-3

                print(bcolors.YELLOW + bcolors.UNDERLINE + f"Spelare hand ⬇⬇⬇: {move_hands[move_list[player]]}")  # skriver om bokstaven till handen

                if cheat == True:
                    pass
                else:
                   print(bcolors.UNDERLINE + bcolors.YELLOW + f"Ai hand ⬇⬇⬇: {move_hands[ai]}") 


                if move_list[player] == ai:
                    print(bcolors.DEFAULT + f"Det blev lika")
                elif ai or move_list[player] == 1:
                    functions.check(move_list, player, ai)
                elif ai or move_list[player] == 2:
                    functions.check(move_list, player, ai)
                break
            elif player == "Q":

                print(bcolors.PURPLE + f"GG next")

                active = False

                exit()
            elif player == "F" and cheat == False:
                cheat = True
                print(bcolors.YELLOW + bcolors.UNDERLINE + f"Ai hand:{bcolors.DEFAULT} {move_hands[ai]}")
                continue
            elif player == "Z":
                os.system("cls")
                tie = 0
                win = 0
                loss = 0
                rounds = 0
                functions.start_screen()
                functions.play_screen(tie, win, loss, rounds)
        else:
            continue

    if move_list[player] == ai:     #lägger till resultatet till poängräknaren
        tie = tie+1 
    elif functions.result_check == 2:
        loss = loss+1
    elif functions.result_check == 1: 
        win = win+1  
   