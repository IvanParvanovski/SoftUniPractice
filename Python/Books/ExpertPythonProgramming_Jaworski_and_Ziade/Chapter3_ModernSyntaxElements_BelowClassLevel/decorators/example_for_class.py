class DisplayMyName:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Hello Ivan')

        result = self.func(*args, **kwargs)

        return result


@DisplayMyName
def display_last_name():
    print('Parvanovski')


display_last_name()
