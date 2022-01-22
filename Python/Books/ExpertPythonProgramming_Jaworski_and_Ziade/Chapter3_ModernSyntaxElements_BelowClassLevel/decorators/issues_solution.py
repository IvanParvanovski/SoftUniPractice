from functools import wraps


def preserving_decorator(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        """Internal wrapped function documentation."""
        return func(*args, **kwargs)
    return wrapped


@preserving_decorator
def function_with_important_docstring():
    """This is important docstring we do not want to lose."""


print(function_with_important_docstring.__name__)
print(function_with_important_docstring.__doc__)
