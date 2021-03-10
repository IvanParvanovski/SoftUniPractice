message = input()

user_input = input()
while user_input != "Finish":
    user_input = user_input.split()
    command = user_input[0]

    if command == "Replace":
        current_char = user_input[1]
        new_char = user_input[2]

        while current_char in message:
            message = message.replace(current_char, new_char)
        print(message)

    elif command == "Cut":
        start_index = int(user_input[1])
        end_index = int(user_input[2])

        if -1 < end_index < len(message) and -1 < start_index < len(message):
            index_difference = end_index - start_index
            message = list(message)
            for _ in range(index_difference + 1):
                message.pop(start_index)
            print(''.join(message))
        else:
            print("Invalid indexes!")

    elif command == "Make":
        upper_or_lower = user_input[1]

        if upper_or_lower == "Upper":
            message = message.upper()
        elif upper_or_lower == "Lower":
            message = message.lower()

        print(message)

    elif command == "Check":
        substring = user_input[1]
        if substring in message:
            print(f"Message contains {substring}")
        else:
            print(f"Message doesn't contain {substring}")

    elif command == "Sum":
        start_index = int(user_input[1])
        end_index = int(user_input[2])

        if -1 < start_index < len(message) and -1 < end_index < len(message):
            sum = 0
            for index in range(start_index, end_index + 1):
                sum += ord(message[index])
            print(sum)
        else:
            print("Invalid indexes!")

    user_input = input()
