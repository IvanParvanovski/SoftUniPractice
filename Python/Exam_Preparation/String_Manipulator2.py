import re
string = input()

user_input = input()
while user_input != "Done":
    user_input = user_input.split()
    command = user_input[0]

    if command == "Change":
        char = user_input[1]
        replacement = user_input[2]
        string = string.replace(char, replacement)
        print(string)

    elif command == "Includes":
        include_substring = user_input[1]
        print(True if include_substring in string else False)

    elif command == "End":
        end_substring = user_input[1]
        pattern = rf"{end_substring}$"
        result = re.search(pattern, string)
        print(True if result is not None else False)

    elif command == "Uppercase":
        string = string.upper()
        print(string)

    elif command == "FindIndex":
        char = user_input[1]
        print(string.index(char))

    elif command == "Cut":
        start_index = int(user_input[1])
        length = int(user_input[2])
        string = list(string)
        for _ in range(length):
            print(string.pop(start_index), end="")
        string = ''.join(string)

    user_input = input()
