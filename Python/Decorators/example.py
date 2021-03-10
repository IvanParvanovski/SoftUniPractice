def say_hi(function):
    return f"Hello {function()}!"


def uppercase(function):
    @say_hi
    def wrapper():
        result = function()
        uppercase_result = result.upper()
        return uppercase_result

    return wrapper


up = uppercase(lambda: 'kitty')
print(up)

