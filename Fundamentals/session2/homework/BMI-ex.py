h = int(input("Enter your height(cm): "))
m = int(input("Enter your weight(kg): "))

hm = h/100
BMI = m / (hm**2)
print(BMI)
if BMI < 16:
    print("Severly underweight")
elif BMI <18.5:
    print("Underweight")
elif BMI < 25:
    print("Normal")
elif BMI < 30:
    print("Overweight")
else:
    print("Obese")
