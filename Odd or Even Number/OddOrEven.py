#Odd or even
#September 11, 2021
#William Wu

print("Welcome to the odd or even number calculator.")

number = int(input("What number would you like to check? \n"))

if number % 2 == 0:
    print(str(number) + " is even.")
else: 
    print (str(number) + " is odd.")