example = "ThiS is String with Upper and lower case Letters"
letter_counts = {}
for letter in example:
    if letter != " ":
        letter_counts[letter] = letter_counts.get(letter, 0)+1
letter_items = list(letter_counts.items())
print(letter_items)
for x, y in letter_items:
    print (x, y)