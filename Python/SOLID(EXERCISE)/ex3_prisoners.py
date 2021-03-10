import copy
from abc import ABC, abstractmethod

# S.O.L.I.D
# Single responsibility - Check
# Open for extensions / Closed for modifications - Check
# Liskov substitution - Check
# Interface segregation - Check
# Dependency inversion - Check


class Person(ABC):
    def __init__(self, position):
        self.position = position


class FreePerson(Person):
    def __init__(self, position):
        Person.__init__(self, position)
        self.is_free = True

    def walk_north(self, dist):
        self.position[1] += dist

    def walk_east(self, dist):
        self.position[0] += dist


class Prisoner(Person):
    PRISON_LOCATION = (3, 3)

    def __init__(self):
        super().__init__(Prisoner.PRISON_LOCATION)
        self.is_free = False


print("The prisoner trying to walk to north by 10 and east by -3.")

f_p = FreePerson([3, 3])
prisoner = Prisoner()

try:
    f_p.walk_north(10)
    f_p.walk_east(-3)
    print('in')
except:
    pass

print(f"The current position of the free person: {f_p.position}")

print('*' * 20)
try:
    prisoner.walk_north(10)
    prisoner.walk_east(-3)
    print('in')
except:
    pass

print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
print(f"The current position of the prisoner: {prisoner.position}")
