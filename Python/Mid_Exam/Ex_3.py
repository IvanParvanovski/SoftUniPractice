neighborhood = input().split("@")
start_index = 0
output = ""
fail_counter = 0
cycle = 1

user_input = input()
while user_input != "Love!":
    user_input = user_input.split()
    command = user_input[0]

    if command == "Jump":
        length = int(user_input[1])

        for counter in range(1, length + 1):
            start_index += 1

            if start_index == len(neighborhood):
                start_index = 0
                break

        if 0 <= start_index < len(neighborhood):
            if int(neighborhood[start_index]) == 0 and start_index != -1:
                output = f"Place {start_index} already had Valentine's day."
                print(output)

            elif int(neighborhood[start_index]) >= 2 and start_index != -1:
                neighborhood[start_index] = str(int(neighborhood[start_index]) - 2)

                if int(neighborhood[start_index]) == 0:
                    output = f"Place {start_index} has Valentine's day."
                    print(output)
    user_input = input()

print(f"Cupid's last position was {start_index}.")
if neighborhood.count("0") == len(neighborhood):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(neighborhood) - neighborhood.count('0')} places.")