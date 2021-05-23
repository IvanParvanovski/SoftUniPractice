from copy import copy


def remove_and_sum_elements(sequence, start, end):
    current_sequence = copy(sequence)
    for i in range(start, end + 1):
        current_sequence.pop(start)
    return current_sequence


def increase_numbers(sequence, value):
    return [x + value for x in sequence]


first_sequence = list(map(int, input().split()))
second_sequence = list(map(int, input().split()))

while True:
    data = input()
    if data == 'nexus':
        break

    connection = tuple(x.split(':') for x in data.split('|'))

    first_part = connection[0]
    second_part = connection[1]

    first_part_start = int(first_part[0])
    first_part_end = int(first_part[1])

    second_part_start = int(second_part[0])
    second_part_end = int(second_part[1])

    if first_part_start < second_part_start and first_part_end > second_part_end:
        total = first_sequence[first_part_start] + first_sequence[second_part_start] + \
                second_sequence[first_part_end] + second_sequence[second_part_end]

        starts = (first_part_start, second_part_start)
        ends = (second_part_end, first_part_end)
        first_sequence = remove_and_sum_elements(first_sequence, min(starts), max(starts))
        second_sequence = remove_and_sum_elements(second_sequence, min(ends), max(ends))

        first_sequence = increase_numbers(first_sequence, total)
        second_sequence = increase_numbers(second_sequence, total)

print(', '.join(map(str, first_sequence)))
print(', '.join(map(str, second_sequence)))
