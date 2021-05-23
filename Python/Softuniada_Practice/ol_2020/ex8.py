def generate_sticks(sticks_count):
    for _ in range(sticks_count):
        yield tuple(x for x in input().split())


def does_index_repeat(index_sequence):
    index_sequence_copy = list(index_sequence)
    while index_sequence_copy:
        element = index_sequence_copy.pop()
        if element in index_sequence_copy:
            return True
    return False


def increase_value(index_sequence):
    index_sequence_len = len(index_sequence)
    for index in range(1, index_sequence_len + 1):
        if index == 1:
            index_sequence[index_sequence_len - index] += 1

        if index_sequence_len - index == 0:
            break

        if index_sequence[index_sequence_len - index] == index_sequence_len:
            index_sequence[index_sequence_len - index] = 0
            index_sequence[index_sequence_len - index - 1] += 1

    return index_sequence


def convert_index_to_elements(indexes, elements):
    for index in indexes:
        yield elements[index]


def generate_combinations(index_sequence,
                                elements,
                          combinations):

    index_sequence = increase_value(index_sequence)

    if index_sequence[0] == len(index_sequence):
        return combinations

    if not does_index_repeat(index_sequence):
        combinations.append(list(convert_index_to_elements(index_sequence, elements)))

    return generate_combinations(index_sequence, elements, combinations)


def generate_indexes(seq):
    return [0] * len(seq)


sticks_count = int(input())
sticks = list(generate_sticks(sticks_count))
combinations = set()


for stick in sticks:
    stick_combinations = generate_combinations(generate_indexes(stick), stick, [])
    sticks_copy = list(sticks)
    sticks_copy.remove(stick)

    for stick_combination in stick_combinations:
        main_and_secondary_stick_combinations = [stick_combination]

        for secondary_stick in sticks_copy:
            secondary_stick_combinations = generate_combinations(generate_indexes(secondary_stick),
                                                                 secondary_stick,
                                                                 [])

            new_combinations = list()
            for marginal_combination in secondary_stick_combinations:

                for main_and_secondary_stick_combination in main_and_secondary_stick_combinations:
                    if main_and_secondary_stick_combination[0].__class__.__name__ == 'list':
                        new_combination = (*main_and_secondary_stick_combination,
                                           marginal_combination)
                    else:
                        new_combination = (main_and_secondary_stick_combination,
                                           marginal_combination)

                    new_combinations.append(new_combination)

            main_and_secondary_stick_combinations = new_combinations

        for combination in main_and_secondary_stick_combinations:
            combinations.add(tuple(tuple(x) for x in combination))

print(len(combinations))
combinations = sorted(combinations)
for combination in combinations:
    result = list()
    for inside_combination in combination:
        result.append(f"|{'-'.join(inside_combination)}|")
    print(' # '.join(result))
