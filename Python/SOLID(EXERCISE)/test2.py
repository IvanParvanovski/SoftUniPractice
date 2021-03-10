"""
>>> g = Girl('Mimi')
>>> b = Boy('Peter')
>>> g.outfit()
'Girl: T-Shirt + Skirt'
>>> b.outfit()
'Boy: Coat + flip-flops'
"""

from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def outfit(self):
        pass


class Girl(Person):
    def __init__(self, name):
        super().__init__(name)

    def outfit(self):
        return "Girl: T-Shirt + Skirt"


class Boy(Person):
    def __init__(self, name):
        super().__init__(name)

    def outfit(self):
        return "Boy: Coat + flip-flops"
