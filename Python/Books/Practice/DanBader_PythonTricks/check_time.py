import functools
import time


def calculate_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f'{func.__name__}: {end_time - start_time}')
        return func

    return wrapper
