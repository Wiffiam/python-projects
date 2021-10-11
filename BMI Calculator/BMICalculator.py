#BMI calculator
#September 11, 2021
#William Wu

print("Welcome to the BMI calculator.")
weight = float(input("What is your weight in kg? \n"))
height = float(input("What is your height in metres? \n"))
bmi = round(weight/(height ** 2), 1)

underweight = 18.5
normal = 25
slightlyOverweight = 30
obese = 35

if bmi <= underweight:
    print("Your BMI is " + str(bmi) + ", you are underweight.")
elif bmi <= normal:
    print("Your BMI is " + str(bmi) + ", you are normal weight.")
elif bmi <=slightlyOverweight:
    print("Your BMI is " + str(bmi) + ", you are slightly overweight.")
elif bmi <= obese:
    print("Your BMI is " + str(bmi) + ", you are obese.")
else:
    print("Your BMI is " + str(bmi) + ", you are clinically obese.")