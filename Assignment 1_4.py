w = float(input("enter your weight (kg): "))
h = float(input("enter your height (m): "))
BMI = w / (h**2)

if BMI < 18.5:
    print("underweight")
if 18.5 <= BMI < 25:
    print("Normal Weight")
if 25 <= BMI < 30:
    print("Overweight")
if 30 <= BMI < 35:
    print("Obesity")
if 35 <= BMI < 39.9:
    print("Extreme obesity")
