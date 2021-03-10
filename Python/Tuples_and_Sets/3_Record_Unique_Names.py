def unique_names(names_count):
    names_set = set()
    for _ in range(names_count):
        user_name = input()
        names_set.add(user_name)

    return names_set


names = unique_names(int(input()))
for name in names:
    print(name)