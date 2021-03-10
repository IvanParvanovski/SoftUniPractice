def logged(func):
    def wrapped(*args):
        str_args = (str(a) for a in args)
        changed_args = ', '.join(str_args)

        func_name = f"you called {func.__name__}({changed_args})"
        func_execution = f"it returned {func(*args)}"

        return f"{func_name}\n{func_execution}"

    return wrapped


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))

#
# @logged
# def sum_func(a, b):
#     return a + b
#
#
# print(sum_func(1, 4, a=4))

