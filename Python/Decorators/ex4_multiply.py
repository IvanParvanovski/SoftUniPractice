from functools import wraps


def multiply(times):
    def decorator(function):

        @wraps(function)
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs) * times
            return result

        return wrapper

    return decorator


@multiply(5)
def add_ten(number):
    return number + 10


print(add_ten(5))

test = multiply(5)
test_1 = test(add_ten)
test_2 = test_1(5)

# print(add_ten(3))
#
#
# @multiply(5)
# def add_ten(number):
#     return number + 10
#
# print(add_ten(6))
