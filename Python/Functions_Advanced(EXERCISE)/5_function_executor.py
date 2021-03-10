def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    result = list()
    for element in args:
        func = element[0]
        arguments = element[1]
        result.append(func(*arguments))
    return result


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
