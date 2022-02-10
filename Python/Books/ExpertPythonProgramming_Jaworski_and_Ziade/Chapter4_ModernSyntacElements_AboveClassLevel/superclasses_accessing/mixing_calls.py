class A:
    def __init__(self):
        print('A', end=' ')
        super().__init__()


class B:
    def __init__(self):
        print('B', end=' ')
        super().__init__()


class C(A, B):
    def __init__(self):
        print('C', end=' ')
        A.__init__(self)
        B.__init__(self)


print('MRO:', [x.__name__ for x in C.__mro__])
C()
