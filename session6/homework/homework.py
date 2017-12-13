#1
def hello():
    for x in range(3):
        print("hello world")

hello()
#2
def add(x,y):
    print("x+y =", x + y)
x = int(input("x = "))
y = int(input("y = "))
add(x,y)
#3
from turtle import *
def draw_square(length,colo):
    color(colo)
    for i in range(4):
        forward(length)
        left(90)


for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

#4
def draw_star(x,y,length):
    penup()
    goto(x,y)
    pendown()
    for i in range(5):
        forward(length)
        right(144)

speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)


#5
def remove_dollar_sign(s):
    S = s.replace('$','')
    return S
string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
if string_with_no_dollars == "80% percent of life is to show up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")

#6
def get_even_list(l):
    for i in l:
        if i%2 == 1:
            l.remove(i)
    return l

even_list = get_even_list([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")

#7
def is_inside(l1,l2):
    if l2[0]+l2[3] > l1[0] > l2[0] and l2[1]+l2[2]>l1[1]>l2[1]:
        return True
    else:
        return False
is_inside([200, 120], [140, 60, 100, 200])
is_inside([100, 120], [140, 60, 100, 200])
