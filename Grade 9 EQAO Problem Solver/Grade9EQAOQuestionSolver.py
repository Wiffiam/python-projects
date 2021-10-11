"""
Grade 9 EQAO Math Problem Solver with enhancements
William Wu
October 7, 2021
2016 Question 3
"""

#Import operating system dependency.
import os

#Import program logo (in separate file for ease of readabiltiy.)
import Grade9EQAOQuestionSolverGraphics

#Defining screen clearing function
def clear():
  #NT = Windows (If OS = Windows, run cls)
  if os.name == "nt":
    os.system("cls")
  #POSIX = Linux / macOS (If OS = Linux based, run clear)
  elif os.name == "posix":
    os.system("clear")

"""
The program will be set to continue solving by default to ensure the user may solve at least one math problem, before being asked whether they would like to continue.
"""

continue_solving = True

#Loop allows the program to continue solving until continue_solving = False (when the user chooses to end the program.)
while continue_solving:
  #Printing EQAO graphics
  print(Grade9EQAOQuestionSolverGraphics.logo)

  #Getting user's input for all car wash parameters including the money that needs to be raised, amount of car wash teams, the cars each team will wash per hour, the car wash duration in hours, the number of breaks, and the duration for each break.
  moneyRaised = float(input("Input the amount of money needed to be raised: \n"))
  carWashTeams = int(input("Input the amount of car washing teams there will be: \n"))
  carsWashedPerHour = float(input("Input how many cars each team will wash per hour: \n"))
  carWashDuration = float(input("Input the amount of hours the car wash will last: \n"))
  numberOfBreaks = int(input("Input number of breaks each team will take: \n"))
  breakDuration = float(input("Input how long each break will be in minutes: \n"))

  #Calculating the amount of money to charge each car to raise the user specified amount of money, given the car wash parameters set by user.
  moneyCharged = moneyRaised / ((carWashTeams*carsWashedPerHour)*(carWashDuration - numberOfBreaks * (breakDuration/60)))

  #Clearing the screen and reprinting the logo to make space for the answers.
  clear()
  print(Grade9EQAOQuestionSolverGraphics.logo)

  #Printing the amount of money needed to be raised, followed by the amount of money needed to be charged per car, with all values being displayed to 2 decimal points and the money charged being rounded to 2 decimals.
  print("The amount of money you will need to charge per car to raise $" +  str("%0.2f" % moneyRaised) + " is $" + str("%0.2f" % round(moneyCharged, 2)) + ".")

  #Asking the user whether they would like to continue using the program.
  user_continue = input("Would you like to continue? Type yes or no: \n")
  if user_continue.lower() == "yes":
    continue_solving = True
    clear()
  elif user_continue.lower() == "no":
    continue_solving = False
    clear()

#Giving the user a goodbye message if they choose to end the program.
print(Grade9EQAOQuestionSolverGraphics.goodbye)