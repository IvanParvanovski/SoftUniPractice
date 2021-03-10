text = input()
power = 0
i = 0

while i < len(text):
    ch = text[i]
    if ch == ">":
        power += int(text[i + 1])
    elif power > 0:
        text = text[:i] + text[i + 1:]
        power -= 1
        i -= 1
    i += 1
print(text)