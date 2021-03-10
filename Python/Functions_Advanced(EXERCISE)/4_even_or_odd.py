def even_nums(numbers):
    return [x for x in numbers if x % 2 == 0]


def odd_nums(numbers):
    return [x for x in numbers if x % 2 != 0]


def even_odd(*args):
    command = args[-1]
    numbers_list = [int(args[i]) for i in range(len(args) - 1)]
    result = list()

    if command == "even":
        result = even_nums(numbers_list)
    elif command == "odd":
        result = odd_nums(numbers_list)

    return result

