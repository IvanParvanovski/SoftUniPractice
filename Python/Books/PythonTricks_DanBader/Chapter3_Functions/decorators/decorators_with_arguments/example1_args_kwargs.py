def proxy(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + ' (Changed) '

    return wrapper


@proxy
def greet(name):
    return 'Hello, {name}!'.format(name=name)


print(greet('Ivan'))