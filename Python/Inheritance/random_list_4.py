import random


class RandomList(list):

    def get_random_element(self):
        element = random.choice(self)
        self.remove(element)
        return element
