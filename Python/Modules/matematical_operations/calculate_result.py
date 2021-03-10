from matematical_operations import divide_numbers, multiply_numbers, subtract_numbers, sum_numbers, raise_numbers

# def calculate_two_numbers(x, y, sign):
#     if sign == "/":
#         return x / y
#
#     elif sign == "*":
#         return x * y
#
#     elif sign == "-":
#         return x - y
#
#     elif sign == "+":
#         return x + y
#
#     elif sign == "^":
#         return x ^ y


def calculate_two_numbers(x, y, sign):
    arguments = (x, y)
    if sign == "/":
        return divide_numbers(*arguments)

    elif sign == "*":
        return multiply_numbers(*arguments)

    elif sign == "-":
        return subtract_numbers(*arguments)

    elif sign == "+":
        return sum_numbers(*arguments)

    elif sign == "^":
        return raise_numbers(*arguments)
