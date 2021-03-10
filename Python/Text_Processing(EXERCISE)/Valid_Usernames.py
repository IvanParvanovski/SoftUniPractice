user_names = input().split(", ")
valid_user_names = list()

for element in user_names:
    check = False
    if 15 > len(element) > 3:
        for char in element:
            if char.isdigit() or char.isalpha() or ord(char) == 95 or ord(char) == 45:
                check = True
            else:
                check = False
                break
        if check:
            valid_user_names.append(element)
for element in valid_user_names:
    print(element)