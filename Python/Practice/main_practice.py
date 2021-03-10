class Person:
    def __init__(self):
        self.age = 5

    def talk(self, word):
        return f'Hello, {word}!'

    def __gt__(self, other):
        return self.age > other

    def __iter__(self):
        pass

# class Student(Person):
#     pass


ivan = Person()
print(for element in ivan)
print(ivan > 10)

