from turtle import *

n = int(input("Enter a number: "))
width(10)


for i in range(n):
    if i % 6 < 3: #even
        color("green")
    else:
        color("pink")
    forward(20)
    penup()
    forward(20)
    pendown()

mainloop()
