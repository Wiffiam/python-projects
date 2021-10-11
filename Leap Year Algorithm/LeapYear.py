#Leap year calculator
#September 11, 2021
#William Wu

print("Welcome to the leap year calculator.")
year = int(input("What year would you like to calculate? \n"))

if year % 4 > 0:
    print("The year " + str(year) + " is a common year.")
elif year % 100 > 0:
    print("The year " + str(year) + " is a leap year.")
elif year % 400 > 0:
    print("The year " + str(year) + " is a common year.")
else:
    print("The year " + str(year) + " is a leap year.")