import functools


def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result

    return wrapper


def greet():
    """ Return a friendly greeting."""
    return 'Hello!'


decorated_greet = uppercase(greet)

print(greet.__name__)
print(greet.__doc__)

print()

print(decorated_greet.__name__)
print(decorated_greet.__doc__)

