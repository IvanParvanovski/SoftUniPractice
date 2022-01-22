def my_decorator(func):
    def wrapped(*args, **kwargs):

        # do some stuff before the original
        # function gets called
        result = func(*args, **kwargs)

        # do some stuff after function call and
        # return the result
        return result

    # return wrapped function
    return wrapped