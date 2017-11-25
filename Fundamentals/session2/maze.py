from turtle import *

# for i in range(5):
#     color("black")
#     forward(50)
#     color("white")
#     forward(50)
#     color("red")
#     forward(50)
#     color("white")
#     forward(50)
n = int(input("Enter a number: "))

speed(-1)
for i in range(n):
    circle(500/n,180)
    right(180 * (n-2) / n)
mainloop()
