from random import randint

luck = randint(0,2)
agi = randint(0,2)
dmg = randint(1,6)
n = luck + agi
print(n)
if dmg < agi + luck:
    print("dodge")
else:
    print("hit")
