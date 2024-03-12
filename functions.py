def result(result_check):
    if result_check == 1:
        print(bcolors.DEFAULT + bcolors.GREEN + f"Du vann")
    elif result_check == 2:
        print(bcolors.DEFAULT + bcolors.RED + f"Du förlora")


def play_screen(tie, win, loss, rounds):
    print(bcolors.DEFAULT + bcolors.YELLOW +  f"Rounds: {rounds} {bcolors.GREEN} Wins: {win} {bcolors.RED} Losses: {loss} {bcolors.DEFAULT} Ties: {tie}")
    print(f"{bcolors.RED}Rock=\'R\' {bcolors.GREEN}Paper=\'P\' {bcolors.BLUE}Scissors=\'S\' {bcolors.PURPLE}Quit=\'Q\' {bcolors.YELLOW + bcolors.UNDERLINE}Fusk=\'F\'{bcolors.DEFAULT} {bcolors.BOLD + bcolors.YELLOW}Reset=\'Z\'" + bcolors.DEFAULT)


def start_screen():
    print(bcolors.YELLOW + f"Välkommen till {bcolors.RED}Rock {bcolors.GREEN}Paper {bcolors.BLUE}Scissors!")
    
    print("""
         
 /$$$$$$$  /$$$$$$$   /$$$$$$  /$$
| $$__  $$| $$__  $$ /$$__  $$| $$
| $$  \ $$| $$  \ $$| $$  \__/| $$
| $$$$$$$/| $$$$$$$/|  $$$$$$ | $$
| $$__  $$| $$____/  \____  $$|__/
| $$  \ $$| $$       /$$  \ $$    
| $$  | $$| $$      |  $$$$$$/ /$$
|__/  |__/|__/       \______/ |__/
          """
          )
def check(move_list,Player, Ai):
    global result_check #gör variabeln till en global.
    if move_list[Player]==1:
        if Ai==2:
            
            result_check=1
            result(result_check)
            
            
        else:
           
            result_check=2
            result(result_check)
            
            
    elif move_list[Player]==2:
        if Ai==3:
           
            result_check=1
            result(result_check)
            
        else:
            result_check=2
            result(result_check)
           
     
    elif move_list[Player]==3:
        if Ai==1:
        
            result_check=1
            result(result_check)
            
        
        else:
            result_check=2
            result(result_check)

            

class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    DEFAULT = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'