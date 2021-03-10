from abc import ABC, abstractmethod


class Base(ABC):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass


class Concrete(Base):
    def foo(self):
        return 'foo() is called'

    # def bar(self):
    #     return 'bar() is called'


assert issubclass(Concrete, Base), 'Hi'
c = Concrete()

