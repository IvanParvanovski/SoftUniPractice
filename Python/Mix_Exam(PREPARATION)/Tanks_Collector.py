tom_tanks = input().split(", ")
number_of_commands = int(input())


def command_add():
    tank_name = user_input[1]

    if tank_name not in tom_tanks:
        tom_tanks.append(tank_name)
        output = "Tank successfully bought"
    else:
        output = "Tank is already bought"

    return output


def command_remove():
    tank_name = user_input[1]
    if tank_name in tom_tanks:
        tom_tanks.remove(tank_name)
        output = "Tank successfully sold"
    else:
        output = "Tank not found"

    return output


def command_remove_at():
    given_index = int(user_input[1])

    if 0 <= given_index < len(tom_tanks):
        tom_tanks.pop(given_index)
        output = "Tank successfully sold"
    else:
        output = "Index out of range"

    return output


def command_insert():
    given_index = int(user_input[1])
    tank_name = user_input[2]

    if 0 <= given_index < len(tom_tanks):

        if tank_name not in tom_tanks:
            tom_tanks.insert(given_index, tank_name)
            output = "Tank successfully bought"
        else:
            output = "Tank is already bought"
    else:
        output = "Index out of range"
    return output


for counter in range(number_of_commands):
    user_input = input().split(", ")
    command = user_input[0]
    if command == "Add":
        print(command_add())

    elif command == "Remove":
        print(command_remove())

    elif command == "Remove At":
        print(command_remove_at())

    elif command == "Insert":
        print(command_insert())

print(", ".join(tom_tanks))
