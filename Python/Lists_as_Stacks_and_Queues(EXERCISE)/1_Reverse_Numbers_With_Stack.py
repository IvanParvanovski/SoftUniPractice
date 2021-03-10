def reverse_numbers(numbers):
    numbers_list = list()
    for num in numbers:
        numbers_list.append(num)

    reversed_numbers_list = list()
    while numbers_list:
        reversed_numbers_list.append(numbers_list.pop())

    return ' '.join(reversed_numbers_list)


print(reverse_numbers(input().split()))
