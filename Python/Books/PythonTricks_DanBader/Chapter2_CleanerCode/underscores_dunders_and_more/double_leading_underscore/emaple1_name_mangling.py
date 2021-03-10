class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 42


t = Test()
print(dir(t))

print(t.foo)
print(t._bar)
print(t._Test__baz)
print(t.__baz)

