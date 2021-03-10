curses = input().split(", ")
text = input()
for element in curses:
    while element in text:
        text = text.replace(element, "*" * len(element))
print(text)