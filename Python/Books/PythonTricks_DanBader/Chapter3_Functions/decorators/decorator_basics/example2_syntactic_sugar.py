def null_decorator(func):
    return func


@null_decorator
def greet():
    return 'Hello!'



print(greet())