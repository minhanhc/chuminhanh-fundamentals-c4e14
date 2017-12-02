bac = int(input("How many B bacterias are there? "))
time = int(input("How much time in minute will we wait? "))

period = time // 2
bacs = bac * 2 **period

print("After {0} minutes, we would have {1} bacteria".format(time, bacs))
