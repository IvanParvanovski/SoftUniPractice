total = 0
while True:
    user_input = input()

    if user_input == 'stop':
        break

    name = user_input
    solved_problems = list(int(x) for x in input().split(', '))
    new_line = list()

    for i in range(len(solved_problems)):
        current_num = solved_problems.pop(0)
        multiplier = 1

        for n in solved_problems:
            multiplier *= n

        new_line.append(multiplier)
        solved_problems.append(current_num)

    bonus = sum(new_line)
    total += bonus
    print(f'{name} has a bonus of {bonus} lv.')

print(f'The amount of all bonuses is {total} lv.')
