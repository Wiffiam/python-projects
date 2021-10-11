#Rock paper scissors
#September 11, 2021
#William Wu

import random

print("Welcome to Rock Paper Scissors.")

# Grabbing player input and converting to integer
while True:
    playerMove = input("Please choose rock, paper, or scissors. \n")

    if playerMove.lower() == "rock":
        playerMoveInt = 1
    elif playerMove.lower() == "paper":
        playerMoveInt = 2
    elif playerMove.lower() == "scissors":
        playerMoveInt = 3
    else:
        print("You have entered an invalid input. Please try again.")

# Converting random integer to rock, paper, or scissors
    aiMoveInt = random.randint(1, 3)

    if aiMoveInt == 1:
        aiMove = "rock"
    elif aiMoveInt == 2:
        aiMove = "paper"
    elif aiMoveInt == 3:
        aiMove = "scissors"

# Determining winner
    if aiMoveInt == playerMoveInt:
        print("You have both selected " + playerMove.lower() + "! It's a draw.")
    elif aiMoveInt == 1:
        if playerMoveInt == 2:
            print("You won! You selected " + playerMove.lower() + " and the computer selected " + aiMove + ".")
        else:
            print("You have lost! You selected " + playerMove.lower() + " and the computer selected " + aiMove + ".")
    elif aiMoveInt == 2:
        if playerMoveInt == 1:
            print("You have lost! You selected " + playerMove.lower() + " and the computer selected " + aiMove + ".")
        else:
            print("You won! You selected " + playerMove.lower() + " and the computer selected " + aiMove + ".")
    elif aiMoveInt == 3:
        if playerMoveInt == 1:
            print("You won! You selected " + playerMove.lower() + " and the computer selected " + aiMove + ".")
        else:
            print("You have lost! You selected " + playerMove.lower() + " and the computer selected " + aiMove + ".")

#Ending the game
    play_again = input("Play again? \n")
    if play_again.lower() == "no":
        break