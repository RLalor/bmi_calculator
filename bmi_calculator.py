height = float(input("Enter your height in M > "))

weight = int(input("Enter your weight in KG > "))

bmi = weight / (height * height)
if bmi < 18.5:
    statement = ", you are underweight."
elif bmi >= 18.5 and bmi < 25:
    statement = ", you have a normal weight."
elif bmi >= 25 and bmi < 30:
    statement = ", you are slightly overweight."
elif bmi >= 30 and bmi < 35:
    statement = ", you are obese."
elif bmi >= 35:
    statement = ", you are clinically obese."
print(f"Your BMI is {bmi}{statement}")
