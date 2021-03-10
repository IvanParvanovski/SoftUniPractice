class Person:
    ID = 0

    def __init__(self,
                 name: str,
                 surname: str):

        self.name = name
        self.surname = surname
        self.id = Person.ID
        Person.ID += 1

    def __add__(self, other):
        return Person(self.name, other.surname)

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __repr__(self):
        return f"Person {self.id}: {self.__str__()}"


class Group:
    def __init__(self,
                 name: str,
                 people: list):

        self.name = name
        self.people = people

    def __add__(self, other):
        return Group(other.name, self.people + other.people)

    def __len__(self):
        return len(self.people)

    def __getitem__(self, index):
        return self.people[index].__repr__()

    def __str__(self):
        return f"Group {self.name} with members {', '.join([str(person) for person in self.people])}"
