def read_first_set_elements(first_set_count):
    return set([int(input()) for _ in range(first_set_count)])


def read_second_set_elements(second_set_count):
    return set([int(input()) for _ in range(second_set_count)])


def unique_elements_between_both_sets(first_set, second_set):
    return first_set.intersection(second_set)


def print_result(result):
    return [print(element) for element in result]


def elements_set(elements_count):
    (first_set_count, second_set_count) = list(map(int, elements_count))
    first_set = read_first_set_elements(first_set_count)
    second_set = read_second_set_elements(second_set_count)
    print_result(unique_elements_between_both_sets(first_set, second_set))


elements_set(input().split())
