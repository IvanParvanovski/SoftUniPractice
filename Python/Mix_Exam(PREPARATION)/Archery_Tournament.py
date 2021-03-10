targets = list(map(int, input().split("|")))
points = 0


def calculating_points(index, inside_points):
    if targets[index] >= 5:
        inside_points += 5
        targets[index] -= 5
    elif targets[index] < 5:
        inside_points += targets[index]
        targets[index] -= targets[index]
    return inside_points


user_input = input()
while user_input != "Game over":
    split_user_input = user_input.split("@")
    command = split_user_input[0]

    if "Shoot Left" == command:
        # Check the range of the index.
        left_start_index = int(split_user_input[1])
        if left_start_index > len(targets) - 1 or left_start_index < 0:
            user_input = input()
            continue
        else:
            left_length = int(split_user_input[2])

            # Go threw the user length.
            for left_counter in range(left_length):
                left_start_index -= 1
                if left_start_index < 0:
                    left_start_index = len(targets) - 1

            # Calculating the points.
            points += calculating_points(left_start_index, 0)

    elif "Shoot Right" == command:
        # Check the range of the index.
        right_start_index = int(split_user_input[1])
        if right_start_index > len(targets) - 1 or right_start_index < 0:
            user_input = input()
            continue
        else:
            right_length = int(split_user_input[2])

            # Go threw the user length.
            for right_counter in range(right_length):
                right_start_index += 1
                if right_start_index > len(targets) - 1:
                    right_start_index = 0

            # Calculating the points.
            points += calculating_points(right_start_index, 0)

    elif "Reverse" == command:
        targets = list(reversed(targets))

    user_input = input()

print(' - '.join(list(map(str, targets))))
print(f"Iskren finished the archery tournament with {points} points!")
filter()
