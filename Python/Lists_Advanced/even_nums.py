even_numbers = list(map(lambda x: int(x), input().split(", ")))
new_list = list()

for index in range(len(even_numbers)):
    if even_numbers[index] % 2 == 0:
        new_list.append(index)

print(new_list)
