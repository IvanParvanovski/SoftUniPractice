from copy import deepcopy

from ol_2019.ex5.down import Down
from ol_2019.ex5.left import Left
from ol_2019.ex5.right import Right
from ol_2019.ex5.up import Up


number = int(input())
field = [[0] * number for _ in range(number)]

assert len(field) == number, 'Field Length is not equal to the given number!'
if number > 0:
    assert len(field[0]) == number, 'Field Width is not equal to the given number!'

hero_col, hero_row = map(int, input().split())

directions = {
    'left': Left,
    'right': Right,
    'down': Down,
    'up': Up,
}

while True:
    data = input()

    if data == 'eastern odyssey':
        break

    divided_data = data.split()

    wanted_destination_col = int(divided_data[0])
    wanted_destination_row = int(divided_data[1])
    direction = divided_data[2]
    hero_stamina = int(divided_data[3])

    rests = 0
    impossible = False
    while True:
        is_achieved = hero_row == wanted_destination_row and \
                      hero_col == wanted_destination_col

        if is_achieved:
            break

        for _ in range(hero_stamina):
            pass


    while True:
        with Move() as m:
            hero_col, hero_row = m

    #     if rests != 0:
    #         direction = Destination(hero_col,
    #                                 hero_row,
    #                                 wanted_destination_col,
    #                                 wanted_destination_row,
    #                                 len(field[0]),
    #                                 len(field),
    #                                 direction,).change_direction()
    #
    #     new_field = deepcopy(field)
    #     should_change = True
    #     while stamina > 0 and \
    #             (hero_col != wanted_destination_col or hero_row != wanted_destination_row):
    #         hero_col, hero_row = directions.get(direction)(hero_col, hero_row)
    #         try:
    #             new_field[hero_row][hero_col] = 1
    #         except IndexError:
    #             should_change = False
    #             break
    #         stamina -= 1
    #
    #     if should_change:
    #         field = new_field
    #     else:
    #         impossible = True
    #         break
    #
    #     stamina = hero_stamina
    #     rests += 1
    #
    # if impossible:
    #     print('Voyage impossible')
    # else:
    #     print(rests - 1)

for f in field:
    print(' '.join(map(str, f)))
