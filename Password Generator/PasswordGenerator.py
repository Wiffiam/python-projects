#Password generator
#October 23, 2021
#William Wu

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to my password generator!")

letterCount = int(input("How many letters would you like? \n"))
numberCount = int(input("How many numbers would you like? \n"))
symbolCount = int(input("How many symbols would you like? \n"))

print("Your random password is:")

password = ''

for char in range(1, letterCount + 1):
    password += random.choice(letters)
for char in range(1, numberCount + 1):
    password += random.choice(numbers)
for char in range(1, symbolCount + 1):
    password += random.choice(symbols)

listPassword = list(password)
random.shuffle(listPassword)
passwordOutput = ''.join(listPassword)

passwordList = open("passwords.txt", "w")

print(passwordOutput)
print(passwordOutput, file = passwordList)
passwordList.close()
print("Your password has been saved to passwords.txt.")
