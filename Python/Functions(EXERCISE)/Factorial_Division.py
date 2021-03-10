def input_and_operation():
    first_num = int(input())
    second_num = int(input())
    total_one, total_two = multiply_factorial(first_num, second_num)
    result = divide(total_one, total_two)
    return result


def multiply_factorial(first_num, second_num):
    total_one = 1
    total_two = 1
    for first_counter in range(2, first_num + 1):
        total_one *= first_counter
    for second_counter in range(2, second_num + 1):
        total_two *= second_counter

    return total_one, total_two


def divide(total_one, total_two):
    local_divide = total_one / total_two
    return local_divide


print(f"{input_and_operation():.2f}")