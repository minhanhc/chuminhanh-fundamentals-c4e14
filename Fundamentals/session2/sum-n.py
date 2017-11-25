n = int(input("Enter a number: "))
#
# S = n * (n + 1) / 2
# print(int(S))

# sum = 0
#
# for i in range(0,n+1):
#     sum += i
#
# print(sum)

sequence = range(n + 1)
s = sum(sequence)
print(s)
