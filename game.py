import sys                                 #Libraries
import random
from enum import Enum

print("GAME".center(30,'*'))
print("*".center(30,'*')) 
print("STONE".ljust(29,"."))
print("PAPER".ljust(29,"."))
print("SCISSOR".ljust(29,"."))
print("*".center(30,'*')) 

print("ENTER YOUR CHOICE: \n 1 - For Stone \n 2 - For Paper \n 3 - For Scissor ")

player_choice = input("Enter Player choice: ")
player = int(player_choice)

if player < 1 or player > 3:                #Use the given choices.
    sys.exit("Enter The Given Choices")

computer_choice = random.choice("123")  
computer = int(computer_choice)             #Computer generate random values between 1 and 3.

class game(Enum):
    STONE = 1
    PAPER = 2                               #Asign string to numerical value.
    SCISSOR = 3
print('')
print("Your choice " + str(game(player)).replace('game.','')) 
print("computer choice " + str(game(computer)).replace('game.','')) 

if player == 1 and computer == 3:
    print("You win 🏆")
elif player == 2 and computer == 1:
    print("You win 🏆")
elif player == 3 and computer == 2:
    print("You win 🏆")
elif player == computer:
    print(" The Game is Tie 🤝")
else:
    print(" 🤖 Computer Win the Game")
