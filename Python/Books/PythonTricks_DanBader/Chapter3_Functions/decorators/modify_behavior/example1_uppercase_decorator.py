from Chapter3_Functions.decorators.decorator_basics.example1_simple_decorator import null_decorator


def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result

    return wrapper


@uppercase
def greet():
    return 'Hello!'


# greet = uppercase(greet)
print(greet())

print(greet)
print(null_decorator(greet))
print(uppercase(greet))
