numbers = [1,6,8,1,2,1,5,6]

num = int(input("Enter a number? "))
count = 0
for index, number in enumerate(numbers):
    if num == number:
        count += 1

if count < 2:
    print("{0} appears {1} time in my list".format(num, count))
else:
    print("{0} appears {1} times in my list".format(num, count))
