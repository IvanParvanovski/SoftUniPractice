from collections import defaultdict
user_input = input().split(" | ")
word_dict = defaultdict(list)

for element in user_input:
    element = element.split(": ")

    for word in element[1::]:
        word_dict[element[0]].append(word)
