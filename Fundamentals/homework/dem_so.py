numbers = [1,6,8,1,2,1,5,6]

num = int(input("Enter a number? "))
x = numbers.count(num)

if x < 2:
    print("{0} appears {1} time in my list".format(num,x))
else:
    print("{0} appears {1} times in my list".format(num,x))
