letter_counts = {}
for letter in "This is String with Upper and lower case Letters":
    letter_counts[letter] = letter_counts.get(letter, 0) + 1
letter_items = list(letter_counts.items())
letter_items.sort()
print(*letter_items, sep = ' \n')
