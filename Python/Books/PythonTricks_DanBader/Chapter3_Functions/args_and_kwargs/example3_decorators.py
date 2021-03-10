import functools


def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(func, args, kwargs)
        result = func(*args, **kwargs)
        print(result)

    return wrapper


@trace
def greet(greeting, name):
    return '{}, {}!'.format(greeting, name)


greet('Hello', 'Bob')
