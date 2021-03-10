def print_result(result):
    return [print(name) for name in result]


def read_input(input_count):
    return set([input() for _ in range(input_count)])


def unique_user_names(input_count):
    print_result(read_input(input_count))


unique_user_names(int(input()))
