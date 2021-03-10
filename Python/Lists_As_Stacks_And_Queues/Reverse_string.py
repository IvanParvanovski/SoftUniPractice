def reversed_string(text):
    stack = list()
    for char in text:
        stack.append(char)

    reversed_text_characters = list()

    while stack:
        char = stack.pop()
        reversed_text_characters.append(char)

    return ''.join(reversed_text_characters)

text = input()

# print(text[::-1], )
# print(''.join(element for element in reversed(text)))
# print(''.join(reversed(text)))
print(reversed_string(text))