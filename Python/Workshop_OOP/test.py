l = [1, 2, 3, 4]
my_dict = {}
for index in range(0, len(l), 2):
    if index % 2 == 0:
        try:
            my_dict[l[index]] = l[index + 1]
        except IndexError:
            my_dict[l[index]] = ' '

print(my_dict)