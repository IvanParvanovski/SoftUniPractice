class ContextIllustration:
    def __enter__(self):
        print('entering context')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('leaving context')

        if exc_type is None:
            print('with no errors')
        else:
            print(f'with an error ({exc_val})')


with ContextIllustration():
    print('inside')

print('-----')

with ContextIllustration():
    raise RuntimeError('no time')
