#Python hangman
#September 28, 2021
#William Wu

import random

from HangmanArt import logo, stages

from HangmanWords import word_list

chosen_word = random.choice(word_list)

word_length = len(chosen_word)

display = []

lives = 6

print(logo)

for length in range(word_length):
    display += "_"

print(display)

end_game = False
lose_lives = True

guess_list = ""

while lives > 0 and not end_game:
    guess = input("Guess one letter in the word: \n").lower()
    lose_lives = True
    if guess in guess_list:
      print("You have already guessed", guess)
    else:
      guess_list += guess + " "
      for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess:
              display[position] = letter
              lose_lives = False
              print(display)
              if "_" not in display:
                  end_game = True
                  print("You win!")
      if lose_lives == True:
        lives = lives-1
        print(stages[lives])

if lives == 0:
    print("You lost!")
    print("The word was:", chosen_word)