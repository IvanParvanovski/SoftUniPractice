# from ex1_person.project.person import Person
from project.person import Person


class Child(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
