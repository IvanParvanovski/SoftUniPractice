wagons = int(input())
train = [0] * wagons

command = input()

while command != "End":
    command_list = command.split()

    if "add" in command:
        people = int(command_list[1])
        train[len(train) - 1] += people

    elif "insert" in command:
        index = int(command_list[1])
        people = int(command_list[2])
        train[index] += people

    elif "leave" in command:
        index = int(command_list[1])
        people = int(command_list[2])

        train[index] -= people
    command = input()
print(train)