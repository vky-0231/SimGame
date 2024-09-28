import sys                                 # Importing the sys module to exit the program.
import random                              # Importing the random module to generate random choices for the computer.
from enum import Enum                      # Importing Enum to define a set of symbolic names bound to unique, constant values.

# Displaying the game banner
print(" ")
print("GAME".center(30,'*'))
print("*".center(30,'*')) 
print("STONE".ljust(29,"."))
print("PAPER".ljust(29,"."))
print("SCISSOR".ljust(29,"."))
print("*".center(30,'*')) 

# Defining the choices as an Enum with corresponding values for Stone, Paper, and Scissor
class Game(Enum):
        STONE = 1
        PAPER = 2                              
        SCISSOR = 3

# Initializing game count to track the number of rounds played
Game_count = 0

# Main function to handle the game logic
def Game_SPS():

    print("ENTER YOUR CHOICE: \n 1 - For Stone \n 2 - For Paper \n 3 - For Scissor ",'\n')
   
    # Handling invalid input with try-except block
    try:
        player_choice = int(input("Enter Your choice: "))  # Getting player input and converting it to integer
        
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 3.")  # Error message for non-integer input
        return Game_SPS()

    # Ensuring that the player enters a valid choice between 1 and 3
    if player_choice not in ([1,2,3]):
        print("You must enter choice between 1 and 3.")  # Error message for out-of-range input
        return Game_SPS()

    # Computer generates a random choice between 1 and 3 (STONE, PAPER, SCISSOR)
    computer_choice = int(random.choice([1,2,3]))             
    
    # Displaying the player's and computer's choices
    print('')
    print("Your choice " + str(Game(player_choice)).replace('Game.',''))  # Removing the Enum prefix for better readability
    print("computer choice " + str(Game(computer_choice)).replace('Game.',''),'\n') 

    # Function to determine the winner based on the rules of the game
    def Game_work(player, computer):

        # Player wins scenarios
        if (player == 1 and computer == 3) or \
            (player == 2 and computer == 1) or \
            (player == 3 and computer == 2):
            print("You win 🏆")
        # Tie condition
        elif player == computer:
            print("The Game is a Tie 🤝")
        # Computer wins scenarios
        else:
            print("🤖 Computer Wins the game")

    # Calling the function to determine the winner
    Game_result = Game_work(player_choice, computer_choice)
    
    # If there is any result to print (optional, here Game_result is None)
    if Game_result is not None:
        print(Game_result)
    
    # Incrementing the game count
    global Game_count
    Game_count += 1
    print("You have played "+ str(Game_count) +" Times",'\n')

    # Asking the user if they want to play again
    while True:
        Play_again = input("Play Again? 'Y' or 'N': ")  # Input to decide whether to restart the game
        if Play_again.lower() not in ['y','n']:
            print("Please enter 'Y' for Yes or 'N' for No.")  # Handling invalid input for 'Play Again' prompt
            continue
        else:
            break
  
    # If the player chooses to play again, the game restarts
    if Play_again.lower() == 'y':
        return Game_SPS()
    else:
        print("Thank you for playing! ❤️")  # Ending message
        sys.exit("Goodbye!!!")  # Exiting the program

# Starting the game
Game_SPS()

