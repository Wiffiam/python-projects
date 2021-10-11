#Tip calculator
#September 11, 2021
#William Wu

print("Welcome to the bill calculator.")

billTotal = int(input("What was the total bill? \n"))
amountOfPeople = int(input("How many people to split the bill by? \n"))
percentageTip = int(input("What percentage tip would you like to give? \n"))
decimalTip = percentageTip / 100 + 1

billPerPerson = billTotal / amountOfPeople * decimalTip
print("Your total per person is $" + str(billPerPerson))