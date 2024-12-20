# option1="rock"
# option2="paper"
# option3="scissors"
import time
import random

def intro():
    # Clear the screen
    print("\033c", end="")  # For Windows, use: os.system('cls') (import os)

    # ASCII Art and Title
    print("""
   
 
 ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓██████████████▓▒░░▒▓████████▓▒░      ░▒▓████████▓▒░▒▓█▓▒░▒▓██████████████▓▒░░▒▓████████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░                ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░                ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒▒▓███▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░           ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░   
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░                ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░                ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
 ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░ 
                                                                                                                        
                                                                                                                        
                                                                                                     

    """)

    # Wait for a few seconds for effect
    time.sleep(2)

    # Welcome Message
    print("\nWelcome to the Rock, Paper, Scissors Game!\n")
    time.sleep(1)

    # Instructions
    print("Please choose one of the following options:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    print("\nMake your choice and let's play!\n")

    print("Type Here and Click Enter:\n")



# DEFINE FUNSTIONS THAT HAVE THE PLAYER AND CPU MAKING DECISIONS
# CPU decision definition
def cpudecision():
  cpuguess=random.randint(1,3)
  if cpuguess==1:
    print("CPU: ROCK!!")
  elif cpuguess==2:
    print("CPU: PAPER!!")
  elif cpuguess==3:
    print("CPU: SCISSORS!!")
    time.sleep(2)
    intro()


# PLayer decision definition
def playerdecision():
  playerguess=int(input())
  if playerguess==1:
    print("PLayer: ROCK!!")
    cpudecision()
  elif playerguess==2:
    print("PLayer: PAPER!!")
    cpudecision()
  elif playerguess==3:
    print("PLayer: SCISSORS!!")
    cpudecision()
  else:
    print("WRONG CHOICE, PLAY AGAIN!!")
    print("IN 2 Seconds!!")
    time.sleep(2)
    intro()


# FUNCTION TO COMPARE AND DECIDE WINNER
def winnerdecider():
  if playerguess==1 and cpudecision==1:
    print("MATCH DRAW")
  # elif playerguess==2 and cpudecision





# Call the intro function to display the interface
intro()
playerdecision()





