class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23


t = Test()
print(t.foo)
print(t._bar)
