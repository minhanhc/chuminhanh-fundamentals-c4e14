from turtle import *

color("orange")
speed(-1)
circle_count = int(input("Enter the number of circle to draw:"))
for i in range(circle_count):
    circle(100)
    right(360/circle_count)


mainloop()
