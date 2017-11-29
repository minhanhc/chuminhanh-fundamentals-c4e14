size = [5,7,300,90,24,50,75]
print("Hello, my name is Anh and here is my sheep size: ")
print(size)
count = 0
while count < 5:
    count += 1
    print("MONTH",count)
    for i in range(len(size)):
        size[i]+=50
    print("One month has passed, now here is my flock")
    print(size)

    print("Now my biggest sheep has size", max(size), "let's sheer it")
    maxsize = max(size)
    for i in range(len(size)):
        if size[i] == maxsize:
            size[i] = 8
            print("After shearing, here is my flock:")
            print(size)
sum = sum(size)
print("My flock has size in total:", sum)
print("I would get", sum, "*2 =", sum*2)
