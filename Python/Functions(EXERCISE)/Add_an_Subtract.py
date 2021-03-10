def sum_numbers(first_num, second_num):
    sum = first_num + second_num
    return sum


def subtract(sum, last_num):
    subtraction = sum - last_num
    return subtraction


def add_and_subtract():
    first_num = int(input())
    second_num = int(input())
    last_num = int(input())

    sum = sum_numbers(first_num, second_num)
    subtracted_number = subtract(sum, last_num)
    return subtracted_number


print(add_and_subtract())