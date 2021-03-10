class IntegerList:
    def __init__(self, *args):
        self.numbers = list()
        for x in args:
            if IntegerList.__is_new_item_int(x):
                self.numbers.append(x)

    @staticmethod
    def __is_new_item_int(item):
        return isinstance(item, int)

    def __is_index_in_of_range(self, index):
        return 0 <= index < len(self.numbers)

    def add(self, item):
        if not IntegerList.__is_new_item_int(item):
            raise ValueError()

        self.numbers.append(item)

    def remove_index(self, index):
        if not self.__is_index_in_of_range(index):
            raise IndexError()

        return self.numbers.pop(index)

    def get(self, index):
        return self.numbers[index]

    def insert(self, index, element):
        if not self.__is_index_in_of_range(index):
            raise IndexError()

        if not IntegerList.__is_new_item_int(element):
            raise ValueError()

        self.numbers.insert(index, element)

    def get_biggest(self):
        return max(self.numbers)

    def get_index(self, element):
        return self.numbers.index(element)
