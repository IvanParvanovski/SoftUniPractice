def sort_dict(dict):
    num = list()
    for name in dict:
        num.append(len(dict[name]))
    return num

user_input = input()
user_dict = dict()

while user_input != "Statistics":
    user_input = user_input.split("->")
    command = user_input[0]
    username = user_input[1]

    if command == "Add":
        if username in user_dict:
            print(f"{username} is already registered")
        else:
            user_dict[username] = list()

    elif command == "Send":
        email = user_input[2]
        user_dict[username].append(email)

    elif command == "Delete":
        if username in user_dict:
            user_dict.pop(username)
        else:
            print(f"{username} not found!")

    user_input = input()

print(f"Users count: {len(user_dict)}")
user_dict = dict(sorted(user_dict.items(), key=lambda user: (-len(user[1]), user[0])))
for user in user_dict:
    print(user)
    for massage in user_dict[user]:
        print(f" - {massage}")


