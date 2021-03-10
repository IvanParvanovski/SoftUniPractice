electrons = int(input())
place_counter = 0
digits_counter = 0
electron_list = list()

while electrons > 0:
    place_counter += 1
    add_electrons = 0
    border = 2 * place_counter ** 2
    for counter in range(border):
        add_electrons += 1
        electrons -= 1
        if electrons <= 0:
            break
    electron_list.append(add_electrons)
print(electron_list)
