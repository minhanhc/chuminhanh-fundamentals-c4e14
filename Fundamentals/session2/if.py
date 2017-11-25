yob = int(input("Your year of birth?"))
age = 2017 - yob

print("Your age:", age)

if age < 10:
    print("Baby")
elif age < 20:
    print("Teenager")
elif age < 30:
    print("Pre-Adult")
else:
    print("Adult")
