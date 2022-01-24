from contextlib import contextmanager


@contextmanager
def context_illustration():
    print('entering context')

    try:
        yield
    except Exception as e:
        print('leaving context')
        print(f'with an error ({e})')
        # exception need to be reraised
        raise
    else:
        print('leaving context')
        print('with no error')
