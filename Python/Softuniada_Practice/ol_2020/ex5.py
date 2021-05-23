from copy import copy


def star_func(directions_, combinations_):
    for direction in directions_:
        for combination in combinations_:
            current_comb = copy(combination)
            current_comb.append(direction)
            yield current_comb


card = input()
combinations = [[]]
directions = ('S', 'L', 'R')

for symbol in card:
    if symbol == '*':
        combinations = tuple(star_func(directions, combinations))
    else:
        for comb in combinations:
            comb.append(symbol)

print(len(combinations))
sorted_combinations = sorted(combinations)

for comb in combinations:
    print(''.join(comb))
