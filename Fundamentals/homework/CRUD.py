shop = ['T-shirt', 'Sweater']

while True:
    n = input("Welcome to our shop, what do you want (C,R,U,D): ")
    if n == "R" or n == "r":
        print("Our item:", end =' ')
        print(*shop, sep = ', ')
    elif n == "C" or n == "c":
        new = input("Enter new item: ")
        shop.append(new)
        print("Our item:", end =' ')
        print(*shop, sep = ', ')
    elif n == "U" or n == "u":
        while True:
            position = int(input("Update position? "))
            if 0 < position < len(shop) + 1:
                rep = input("New item? ")
                shop[position -1] = rep
                print("Our item:", end =' ')
                print(*shop, sep = ', ')
                break
            else:
                print("Out of range")
    elif n == "D" or n == "d":
        while True:
            position = int(input("Delete position?"))
            if 0 < position < len(shop)+1:
                del shop[position - 1]
                print("Our item:", end =' ')
                print(*shop, sep = ', ')
                break
            else:
                print("Out of range")
    else:
        print("Invalid letter")
