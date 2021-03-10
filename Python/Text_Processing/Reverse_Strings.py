user_input = input()
reversed_strings = dict()
while user_input != "end":
    reversed_strings[user_input] = "".join(list(user_input[index] for index in range(len(user_input)-1, -1, -1)))
    user_input = input()
    
for key, value in reversed_strings.items():
    print(f"{key} = {value}")