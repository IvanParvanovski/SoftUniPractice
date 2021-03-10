groceries = input().split("!")

user_input = input()
while user_input != "Go Shopping!":
    user_input = user_input.split()
    command = user_input[0]
    if command == "Urgent":
        item = user_input[1]
        if item not in groceries:
            groceries.insert(0, item)

    elif command == "Unnecessary":
        item = user_input[1]
        if item in groceries:
            groceries.remove(item)
    elif command == "Correct":
        old_item = user_input[1]
        new_item = user_input[2]
        if old_item in groceries:
            for index in range(len(groceries)):
                if groceries[index] == old_item:
                    groceries[index] = new_item
    elif command == "Rearrange":
        item = user_input[1]
        if item in groceries:
            index_of_old_item = groceries.index(item)
            old_item = groceries.pop(index_of_old_item)
            groceries.append(old_item)
    user_input = input()
print(", ".join(groceries))