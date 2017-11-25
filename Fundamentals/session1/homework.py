# How to check a varible's type?
# - Type(value)
# In what case will you get syntax error?
# - Varible doesn't begin with a letter or underscore: 7days = "1 week"
# - contains illegal character: ineed$ ="I need money"
# - be Python's keyword: in = "notout"

response = input("Radius?")
r = float(response)
area = 3.14 * r**2
print("Area =", area)

Cs = input("Enter the temperature in Celsius?")
t = float(Cs)
Ft = 32 + 1.8 * t
print(Cs,"(C) =",Ft,"(F)")
