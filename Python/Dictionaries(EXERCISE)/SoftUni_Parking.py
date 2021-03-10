commands_count = int(input())
car_plate_dict = dict()

for _ in range(commands_count):
    output = ""
    args = input().split()
    command = args[0]
    username = args[1]

    if command == "register":
        license_plate_number = args[2]

        if username in car_plate_dict:
            output = f"ERROR: already registered with plate number {car_plate_dict[username]}"
        else:
            car_plate_dict[username] = license_plate_number
            output = f"{username} registered {license_plate_number} successfully"

    elif command == "unregister":
        if username not in car_plate_dict:
            output = f"ERROR: user {username} not found"
        else:
            car_plate_dict.pop(username)
            output = f"{username} unregistered successfully"

    print(output)

for element in car_plate_dict:
    print(f"{element} => {car_plate_dict[element]}")