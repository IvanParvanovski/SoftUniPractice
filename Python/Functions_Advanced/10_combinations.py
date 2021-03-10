def permutations(text, index):
    if index >= len(text):
        print("".join(text))
        return

    for i in range(index, len(text)):
        text[index], text[i] = text[i], text[index]
        permutations(text, index + 1)
        text[index], text[i] = text[i], text[index]


permutations(list(input()), 0)
