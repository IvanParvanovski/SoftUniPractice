class Keeper:
    def __init__(self,
                 name: str,
                 age,
                 salary):

        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Name: {self.name}, " \
               f"Age: {self.age}, " \
               f"Salary: {self.salary}"
