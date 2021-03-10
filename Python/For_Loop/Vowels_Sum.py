text = input()
text_lenght = len(text)
total = 0

for char_count in range(text_lenght):
    chars = text[char_count]

    if chars == "a":
        total += 1
    elif chars == "e":
        total += 2
    elif chars == "i":
        total += 3
    elif chars == "o":
        total += 4
    elif chars == "u":
        total += 5
    char_count += 1

print(total)
