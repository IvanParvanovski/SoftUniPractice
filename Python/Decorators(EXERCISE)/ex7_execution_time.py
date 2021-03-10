from timeit import default_timer as timer


def exec_time(func):
    def wrapper(*args, **kwargs):
        start = timer()
        func(*args, **kwargs)
        end = timer()
        result = end - start
        return result

    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 10000000))
