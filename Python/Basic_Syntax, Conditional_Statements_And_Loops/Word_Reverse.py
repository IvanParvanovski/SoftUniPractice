word = input()
reversed_string = ""

for i in range(len(word) - 1, -1, -1):
    reversed_string += word[i]
print(reversed_string, end="")