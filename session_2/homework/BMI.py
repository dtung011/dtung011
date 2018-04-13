m = int(input("you weight: "))
h = int(input("your height: "))

BMI = m/(h**2)

if BMI > 30:
    print ("Obese")
elif BMI > 25:
    print ("Overweight")
elif BMI > 18.5:
    print ("Normal")
elif BMI > 16:
    print ("Underweight")
else:
    print ("Severely underweight")