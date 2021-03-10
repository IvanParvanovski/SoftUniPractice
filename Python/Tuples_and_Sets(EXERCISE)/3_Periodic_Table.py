def read_input(elements_lines_count):
    return [input().split() for _ in range(elements_lines_count)]


def periodic_elements_set(elements):
    unique_elements = set()
    for periodic_elements in elements:
        for element in periodic_elements:
            unique_elements.add(element)
    return unique_elements


def print_result(result):
    return [print(symbol) for symbol in result]


def periodic_table(elements_lines_count):
    print_result(periodic_elements_set(read_input(elements_lines_count)))


periodic_table(int(input()))
