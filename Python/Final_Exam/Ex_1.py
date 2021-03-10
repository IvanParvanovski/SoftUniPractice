activation_key = input()
user_input = input()
while user_input != "Generate":
    user_input = user_input.split(">>>")
    command = user_input[0]

    if command == "Contains":
        substring = user_input[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif command == "Flip":
        upper_or_lower = user_input[1]
        flip_start_index = int(user_input[2])
        flip_end_index = int(user_input[3])

        if upper_or_lower == "Upper":
            activation_key = list(activation_key)
            for index in range(flip_start_index, flip_end_index):
                if index != len(activation_key) - 1:
                    activation_key[index] = activation_key[index].upper()

        elif upper_or_lower == "Lower":
            activation_key = list(activation_key)
            for index in range(flip_start_index, flip_end_index):
                if index != len(activation_key) - 1:
                    activation_key[index] = activation_key[index].lower()
        activation_key = ''.join(activation_key)
        print(activation_key)

    elif command == "Slice":
        slice_start_index = int(user_input[1])
        slice_end_index = int(user_input[2])
        activation_key = list(activation_key)
        for index in range(slice_end_index - slice_start_index):
            activation_key.pop(slice_start_index)
        activation_key = ''.join(activation_key)
        print(activation_key)

    user_input = input()

print(f"Your activation key is: {activation_key}")