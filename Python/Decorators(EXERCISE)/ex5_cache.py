def cache(func):
    def wrapper(num):
        result = func(num)
        wrapper.log[num] = result
        return wrapper.log[num]

    wrapper.log = dict()
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n-1) + fibonacci(n-2)


fibonacci(3)
print(fibonacci.log)
