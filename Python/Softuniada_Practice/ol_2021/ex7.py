numbers_count = int(input())
speed_commands = list(map(int, input().split()))
start_speed = int(input())
end_speed = int(input())
valid = True

for speed_command_index in range(len(speed_commands)):
    current_speed_command = speed_commands[speed_command_index]
    try:
        following = speed_commands[speed_command_index + 1]

        if following > start_speed + current_speed_command < end_speed:
            start_speed += current_speed_command
        else:
            if start_speed - current_speed_command >= 0:
                start_speed -= current_speed_command
            else:
                valid = False
                break
    except IndexError:
        if start_speed + current_speed_command <= end_speed:
            start_speed += current_speed_command
        elif start_speed - current_speed_command >= 0:
            start_speed -= current_speed_command
        else:
            valid = False
    print(start_speed)

if valid:
    print(start_speed)
else:
    print(-1)
