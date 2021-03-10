from collections import defaultdict
words = input().split()
characters_dict = defaultdict(int)

for word in words:
    for element in word:
        characters_dict[element] += 1

for element in characters_dict:
    print(f"{element} -> {int(characters_dict[element])}")