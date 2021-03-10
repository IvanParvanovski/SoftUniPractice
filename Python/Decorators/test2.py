def decorator_function(n):
    def decorator(original_function):
        print(original_function)

        def wrapped_function(*args, **kwargs):
            print(f"wrapper executed this before {original_function.__name__}")
            return original_function(*args, **kwargs)

        return wrapped_function

    print('Step 1')
    return decorator


@decorator_function(1)
def display():
    print('display function ran')


@decorator_function(1)
def display_info(name, age):
    print(f'display_info ran with arguments ({name}, {age})')


display()

# display()
# display_info('Jhon', 15)
