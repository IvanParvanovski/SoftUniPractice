def find_strongest_eggs(eggs, step):
    sub_lists = list()
    for index in range(step):
        new_eggs = list()
        while index < len(eggs):
            new_eggs.append(int(eggs[index]))
            index += step
        sub_lists.append(new_eggs)

    strongest_eggs = list()
    for sub_list in sub_lists:
        n = len(sub_list) // 2
        mid_egg = sub_list[n]
        next_egg = sub_list[n + 1]
        previous_egg = sub_list[n - 1]
        if previous_egg < mid_egg > next_egg > previous_egg:
            strongest_eggs.append(mid_egg)

    return strongest_eggs


test = ([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
print(find_strongest_eggs(*test))
test = ([-1, 7, 3, 15, 2, 12], 2)
print(find_strongest_eggs(*test))
test = ([-1, 0, 2, 5, 2, 3], 2)
print(find_strongest_eggs(*test))
test = ([51, 21, 83, 52, 55], 1)
print(find_strongest_eggs(*test))
test = ([8, -30, 13, -10, 12, -20, 50, 50, 17, 80, 16, 60], 2)
print(find_strongest_eggs(*test))


