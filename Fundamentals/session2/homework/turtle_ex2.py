from turtle import *

n = int(input("Enter an integer number that > 3: "))

for i in range(3, n+1):
    if i%2 ==1:
        color("blue")
    else:
        color("red")
    for j in range(i):
        forward(100)
        left(360/i)
mainloop()
