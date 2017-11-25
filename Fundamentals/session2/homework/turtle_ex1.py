from turtle import *

right(30)
forward(100)
for n in range(15):
    if n % 4 == 3:
        right(150)
        forward(100)
    elif n % 4 == 1:
        left(120)
        forward(100)
    else:
        left(60)
        forward(100)
mainloop()
