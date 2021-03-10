def create_number_set(raw_input, section_index):
    section = raw_input[section_index].split(',')
    section_start = int(section[0])
    section_end = int(section[1])
    range_set = set([index for index in range(section_start, section_end + 1)])
    return range_set


def solve(number_count):
    longest_set = set()
    for _ in range(number_count):
        raw_input = input().split('-')
        first_set = create_number_set(raw_input, 0)
        second_set = create_number_set(raw_input, 1)

        unique_numbers = first_set.intersection(second_set)
        if len(unique_numbers) > len(longest_set):
            longest_set = unique_numbers
    return longest_set


longest_number_set = solve(int(input()))
print(f"Longest intersection is [{', '.join(map(str, longest_number_set))}] with length {len(longest_number_set)}")


