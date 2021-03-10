def count_numbers(user_input):
    numbers_dict = dict()

    for num in list(map(float, user_input)):
        if num in numbers_dict:
            numbers_dict[num] += 1
        else:
            numbers_dict[num] = 1

    print_numbers_count(numbers_dict)


def print_numbers_count(numbers_dict):
    for num in numbers_dict:
        print(f"{num} - {numbers_dict[num]} times")


count_numbers(input().split())
