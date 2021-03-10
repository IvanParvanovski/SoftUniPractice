class Person:
    @staticmethod
    def sleep():
        return "sleeping..."


class Employee:
    @staticmethod
    def get_fired():
        return "fired..."


class Teacher(Employee, Person):
    @staticmethod
    def teach():
        return "teaching..."
