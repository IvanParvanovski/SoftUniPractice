def dummy_decorator(function):
    def wrapped(*args, **kwargs):
        """Internal wrapped function documentation."""
        return function(*args, **kwargs)

    return wrapped


@dummy_decorator
def function_with_important_docstring():
    """This is important docstring we do not want to lose."""


print(function_with_important_docstring.__name__)
print(function_with_important_docstring.__doc__)
