class Base:
    def foo(self):
        raise NotImplementedError()

    def bar(self):
        raise NotImplementedError()


class Concrete(Base):
    def foo(self):
        return 'foo() called'

    # Oh no, we forgot to override bar()...
    # def bar(self):
    #     return 'bar() called'


# b = Base()
# b.foo()

c = Concrete()
print(c.foo())
print(c.bar())
