def two_digits_result(number):
    result = 0
    if number < 10:
        result = number
    elif number > 25:
        first_digit = number // 10 - 1
        index = number % 10
        index_final = index if index < 5 else index - 6
        result = range(1, 6)[index_final] + first_digit
    elif number > 10:
        first_digit = number // 10 - 1
        index = number % 10
        result = range(1, 11)[index] + first_digit
    print('My Result ', result)
    return result


def get_coins(number):
    while number > 0:
        yield two_digits_result(number % 100)
        number //= 100


def answer(number):
    numbers_results = list(range(100))

    for i in range(10, 100):
        numbers_results[i] = min(numbers_results[i - 10] + 1, numbers_results[i])

    for i in range(25, 100):
        numbers_results[i] = min(numbers_results[i - 25] + 1, numbers_results[i])

    count = 0
    while number > 0:
        an = numbers_results[int(number % 100)]
        if an != 0:
            print('Answer: ', an)

        count += an
        number /= 100

    return count


number = int(input())
print(answer(number))
print(sum(get_coins(number)))
