def target_change_remove(replicator, skill):
    while substring in skill:
        skill = skill.replace(substring, replicator)
    return skill


skill = input()

user_input = input()
while user_input != "For Azeroth":
    user_input = user_input.split()
    command = user_input[0]

    if command == "GladiatorStance":
        skill = skill.upper()
        print(skill)

    elif command == "DefensiveStance":
        skill = skill.lower()
        print(skill)

    elif command == "Dispel":
        index = int(user_input[1])
        letter = user_input[2]

        if -1 < index < len(skill):
            skill = list(skill)
            skill[index] = letter
            skill = ''.join(skill)
            print("Success!")
        else:
            print("Dispel too weak.")

    elif command == "Target":
        second_command = user_input[1]
        substring = user_input[2]

        if second_command == "Change":
            second_substring = user_input[3]
            skill = target_change_remove(second_substring, skill)
            print(skill)

        elif second_command == "Remove":
            skill = target_change_remove("", skill)
            print(skill)

        else:
            print("Command doesn't exist!")

    else:
        print("Command doesn't exist!")
    user_input = input()
