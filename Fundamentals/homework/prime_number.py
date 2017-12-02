n = int(input("Enter a number: "))

prime = False

for i in range(2,n):
    if n % i == 0:
        prime =True
        
if not prime:
    print("{0} is a prime number".format(n))
else:
    print("{0} is not a prime number".format(n))
