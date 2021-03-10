class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, entire_name):
        (self.first_name, self.last_name) = entire_name.split()


my_p = Person("Ivan", "Parvanovski")
print(my_p.full_name)
my_p.full_name = "Gosho Petrov"
print(my_p.full_name)
