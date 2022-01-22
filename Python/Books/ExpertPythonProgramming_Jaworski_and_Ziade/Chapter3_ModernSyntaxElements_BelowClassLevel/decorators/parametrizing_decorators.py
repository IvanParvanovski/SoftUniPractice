def repeat(number=3):
    """
    Cause decorated function to be repeated a number of times.
    Last value of original function call is returned as a result.
    :param number: number of repetitions, 3 if not specified
    """

    def actual_decorator(function):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(number):
                result = function(*args, **kwargs)
            return result
        return wrapper
    return actual_decorator


@repeat(2)
def print_my_call():
    print('Hello, Ivan')


@repeat()
def print_my_name():
    print('Ivan Parvanovski')


# print_my_call()
print_my_name()
