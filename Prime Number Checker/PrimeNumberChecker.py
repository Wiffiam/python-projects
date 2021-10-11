#Prime number checker
#September 29, 2021
#William Wu

def prime_checker(number):
    prime = True
    for i in range(2, number):
        number % i
        if number % i == 0:
            prime = False
    if prime:
        print("It is a prime number.")
    else:
        print("It is not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)