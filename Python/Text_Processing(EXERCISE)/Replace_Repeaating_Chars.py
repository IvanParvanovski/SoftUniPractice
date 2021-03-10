user_input = input()
output = ""

for index in range (len(user_input)):
    first_char = user_input[index]
    if index + 1 < len(user_input):
        second_char = user_input[index + 1]

        if first_char != second_char:
            output += first_char
    else:
        output += first_char
print(output)