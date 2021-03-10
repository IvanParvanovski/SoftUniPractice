user_operator = input()
user_first_num = int(input())
user_second_num = int(input())


def subtract(first_num, second_num):
    return first_num % second_num


def divide(first_num, second_num):
    return first_num / second_num


def add(first_num, second_num):
    return first_num + second_num


def multiply(first_num, second_num):
    return first_num * second_num


def calculation(main_operator, first_num, second_num):
    mapping = [
        ["subtract", subtract],
        ["divide", divide],
        ["add", add],
        ["multiply", multiply]
    ]

    for for_operator, function in mapping:
        if for_operator == main_operator:
            return function(first_num, second_num)


print(f"{calculation(user_operator, user_first_num, user_second_num):.0f}")