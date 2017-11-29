from random import choice, randint

for k in range(10):
    wordlist = ["shadow fiend", "juggernaut", "queen of pain", "night stalker", "ember spirit", "slardar", "slark", "silencer", "batrider", "disruptor"]
    word = choice(wordlist)
    n = list(word)
    for i in range(len(n)):
        j = randint(0,len(n)-1)
        a = n[i]
        n[i] = n[j]
        n[j] = a

    print(*n, sep = ' ')


    guess = input("Your answer: ")
    if guess != word:
        print("Try it again")
    else:
        print("Hura, it is", word)
        
