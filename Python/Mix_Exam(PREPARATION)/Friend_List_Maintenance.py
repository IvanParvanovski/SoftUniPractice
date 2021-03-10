friends = input().split(", ")


def command_blacklist():
    # Variables.
    friend_name = list_of_attributes[1]

    # Logic of the function.
    if friend_name in friends:

        # Go threw the list and check if the person matches with the friend on the given index.
        for index in range(len(friends)):

            # Set the person to "Blacklisted".
            if friend_name == friends[index]:
                friends[index] = "Blacklisted"

        # Change the output and return it.
        output = f"{friend_name} was blacklisted."
    else:
        output = f"{friend_name} was not found."

    return output


def command_error():
    # Variables.
    given_index = int(list_of_attributes[1])
    name_on_the_given_index = friends[given_index]

    # Logic of the function.
    if name_on_the_given_index != "Blacklisted" and name_on_the_given_index != "Lost":
        friends[given_index] = "Lost"
        print(f"{name_on_the_given_index} was lost due to an error.")


def command_change():
    # Variables.
    given_index = int(list_of_attributes[1])
    new_name = list_of_attributes[2]

    # Logic of the function.
    if 0 <= given_index < len(friends):
        past_friend_name = friends[given_index]
        friends[given_index] = new_name
        print(f"{past_friend_name} changed his username to {new_name}.")


def print_output():
    # Calculate the "Blacklisted" names.
    blacklisted_names = sum(list(1 for element in friends if element == "Blacklisted"))

    # Calculate the "Lost" names.
    lost_names = sum(list(1 for element in friends if element == "Lost"))

    # Return the output.
    # return f"Blacklisted names: {blacklisted_names}\nLost names: {lost_names}\n{' '.join(friends)}"
    print(f"Blacklisted names: {blacklisted_names}")
    print(f"Lost names: {lost_names}")
    print(' '.join(friends))


# Main program.

user_input = input()
while user_input != "Report":
    list_of_attributes = user_input.split()
    command = list_of_attributes[0]

    if command == "Blacklist":
        print(command_blacklist())

    elif command == "Error":
        command_error()

    elif command == "Change":
        command_change()

    user_input = input()

print_output()
