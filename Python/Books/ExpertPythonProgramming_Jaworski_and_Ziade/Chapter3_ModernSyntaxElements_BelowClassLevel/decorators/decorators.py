class WithoutDecorators:
    def some_static_method(self):
        print('this is static method')

    some_static_method = staticmethod(some_static_method)

    def some_class_method(cls):
        print('this is class method')

    some_class_method = classmethod(some_class_method)


class WithDecorators:
    @staticmethod
    def some_static_method():
        print('this is static method')

    @classmethod
    def some_class_method(cls):
        print('this is class method')