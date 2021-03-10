class Cheetah:
    def __init__(self,
                 name: str,
                 gender: str,
                 age):
        self.name = name
        self.gender = gender
        self.age = age

    @staticmethod
    def get_needs():
        return 60

    def __repr__(self):
        return f"Name: {self.name}, " \
               f"Age: {self.age}, " \
               f"Gender: {self.gender}"
