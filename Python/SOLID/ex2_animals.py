animals_specification = {'cat': 'meow',
                         'dog': 'woof-woof',
                         'snake': 'ssss'}


class Animal:
    def __init__(self, species):
        self.__species = species

    @property
    def species(self):
        return self.__species


def animal_sound(animals: list):

    for animal in animals:
        try:
            return animals_specification[animal]
        except KeyError:
            return "No such animal!"
