def symmetric_different_values(even_set, odd_set):
    return even_set.symmetric_difference(odd_set)


def different_values(even_set, odd_set):
    return odd_set.difference(even_set)


def union_values(even_set, odd_set):
    return even_set.union(odd_set)


def calculate_ascii_value(name):
    return sum([ord(char) for char in name])


def separate_input_to_odd_and_even(count):
    even_set = set()
    odd_set = set()
    for index in range(1, count + 1):
        name = input()
        name_value = calculate_ascii_value(name)
        name_divided_by_index = int(name_value / index)

        if name_divided_by_index % 2 == 0:
            even_set.add(name_divided_by_index)
        else:
            odd_set.add(name_divided_by_index)

    return even_set, odd_set


def solve(count):
    even_set, odd_set = separate_input_to_odd_and_even(count)
    even_set_sum = sum(even_set)
    odd_set_sum = sum(odd_set)
    output_set = set()

    if even_set_sum == odd_set_sum:
        output_set = union_values(even_set, odd_set)

    elif even_set_sum < odd_set_sum:
        output_set = different_values(even_set, odd_set)

    elif even_set_sum > odd_set_sum:
        output_set = symmetric_different_values(even_set, odd_set)

    return output_set


print(', '.join(map(str, solve(int(input())))))
