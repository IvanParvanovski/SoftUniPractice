def even_numbers(function):
    def is_even(number):
        return number % 2 == 0

    def wrapper(numbers):
        result = function(numbers)
        return list(filter(is_even, result))

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
