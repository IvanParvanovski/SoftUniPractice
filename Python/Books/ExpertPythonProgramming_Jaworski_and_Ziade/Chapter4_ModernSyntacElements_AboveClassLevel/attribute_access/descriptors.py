class RevealAccess:
    """
    A data descriptor that sets and returns values
    normally and print a message logging their access.
    """

    def __init__(self, init_val=None, name='var'):
        self.val = init_val
        self.name = name

    def __get__(self, instance, owner):
        print('Retrieving', self.name)
        return self.val

    def __set__(self, obj, val):
        print('Updating', self.name)
        self.val = val


class MyClass:
    x = RevealAccess(10, 'var "x"')
    y = 5


m = MyClass()
print(m.x)
m.x = 20

