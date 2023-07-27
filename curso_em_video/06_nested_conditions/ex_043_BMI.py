# Develop a logic that reads a person's weight and height, calculates their BMI(IMC)
# and displays their status, according to the table below:
# - Under 18.5 = Underweight
# - Between:
#   - 18.5 and 25 = Ideal weight
#   - 25 to 30 = Overweight
#   - 30 to 40 = Obesity
#   - Above 40 = Morbid obesity
weight = float(input("What's your weight? (Kg) "))
height = float(input("How tall are you? (m) "))
bmi = weight / (height**2)
print(f"The person's BMI is {bmi:.1f}")
if bmi < 18.5:
    print("You are UNDER normal weight")
elif 18.5 <= bmi < 25:
    print("CONGRATULATIONS, you are in the NORMAL WEIGHT range")
elif 25 <= bmi < 30:
    print("You are OVERWEIGHT")
elif 30 <= bmi < 40:
    print("You are in OBESITY")
elif bmi >= 40:
    print("You are in MORBID OBESITY, be careful!")
