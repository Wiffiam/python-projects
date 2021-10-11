#Treasure island game
#September 11, 2021
#William Wu

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure, and come out alive.")
choiceOne = input("Would you like to start off by going left or right? \n")
invalid = "Invalid choice, please try again."
death = '''
     888                888   888      
     888                888   888      
     888                888   888      
 .d88888 .d88b.  8888b. 88888888888b.  
d88" 888d8P  Y8b    "88b888   888 "88b 
888  88888888888.d888888888   888  888 
Y88b 888Y8b.    888  888Y88b. 888  888 
 "Y88888 "Y8888 "Y888888 "Y888888  888 

You have died. Please try again.
    '''
if choiceOne.lower() == "left":
    print(death)
elif choiceOne.lower() == "right":
    choiceTwo = input('''
            __ _.--..--._ _
     .-' _/   _/\_   \_'-.
    |__ /   _/\__/\_   \__|
       |___/\_\__/  \___|
              \__/
              \__/
               \__/
                \__/
             ____\__/___
       . - '             ' -.
      /                      \
~~~~~~~  ~~~~~ ~~~~~  ~~~ ~~~  ~~~~~
  ~~~   ~~~~~   ~!~~   ~~ ~  ~ ~ ~pjb

You have stumbled upon a coconut tree, where would you like to go next? Into the cave or to the beach? \n''')
    if choiceTwo.lower() == "cave":
        print(death)
    elif choiceTwo.lower() == "beach":
        choiceThree = input('''
            __________
           |  __  __  |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |__________|

You have found three doors, would you like to go in the red, blue, or yellow door? \n''')
        if choiceThree.lower() == "red":
            print(death)
        elif choiceThree.lower() == "blue":
            print(death)
        elif choiceThree.lower() == "yellow":
            print('''
        _______
      .'_/_|_\_'.
      \`\  |  /`/
       `\\ | //'
         `\|/`
           `
Congratulations, you have found the treasure and won!''')
    else:
        print(invalid)
else:
    print(invalid)

