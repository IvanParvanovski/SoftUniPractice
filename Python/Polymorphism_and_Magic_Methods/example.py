from abc import ABC, abstractmethod


class Animal(ABC):
    """
    ------ Abstraction example ------

    Every animal makes sound and has appearances.
    """

    def __init__(self,
                 name,
                 age):

        self.name = name
        self.age = age

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass

# ------ Polymorphism example ------
# Different classes with same methods and variables, but
# with different solutions. The cat makes 'Meow', The dog 'Bau'


class Cat(Animal):
    """
    Polymorphism
    """
    def __init__(self, name, age):
        super().__init__(name, age)

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog(Animal):
    """
    Polymorphism
    """
    def __init__(self, name, age):
        super().__init__(name, age)

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


# ------ Duck-typing example ------
# We don't care of animal class, name or age
# We care that they have same methods
cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()
