class NonZero(int):
    def __new__(cls, value):
        return \
            super().__new__(cls, value) \
            if value != 0 \
            else None

    def __init__(self, skipped_val):
        print('__init__() called')
        super(NonZero, self).__init__()


print(type(NonZero(-12)))
print(type(NonZero(0)))
print(NonZero(-3.123))
