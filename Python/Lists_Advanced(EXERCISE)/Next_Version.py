user_version = input().split(".")
check = False
index = len(user_version) - 1

while check is False:
    element = int(user_version[index])
    element += 1

    if element > 9:
        element = 0
        user_version[index] = str(element)
        index -= 1
    else:
        user_version[index] = str(element)
        check = True

print(".".join(user_version))