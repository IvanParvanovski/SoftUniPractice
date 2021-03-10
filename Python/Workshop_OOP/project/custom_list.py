from project.index import Index
from project.data_configuration import DataConfiguration
import copy


class CustomList(Index,
                 DataConfiguration):

    def __init__(self, *args):
        self.my_list = list(args)
        self.iter_index = 0

    def append(self, value) -> list:
        self.my_list.append(value)
        return self.my_list

    def remove(self, index):
        Index.index_checks(self.my_list, index)

        return self.my_list.pop(index)

    def get(self, index):
        Index.index_checks(self.my_list, index)

        return self.my_list[index]

    def extend(self, iterable) -> list:
        DataConfiguration.data_not_iterable_error(iterable)

        self.my_list.extend(iterable)
        return self.my_list

    def insert(self, index, value) -> list:
        Index.index_not_integer_error(index)
        Index.out_of_range_error(self.my_list, index)

        self.my_list.insert(index, value)
        return self.my_list

    def pop(self):
        Index.empty_list_error(self.my_list)

        return self.my_list.pop()

    def clear(self):
        self.my_list = list()

    def index(self, value):
        DataConfiguration.does_data_exist_in_list_raise_error(self.my_list, value)

        return self.my_list.index(value)

    def count(self, value):
        DataConfiguration.does_data_exist_in_list_raise_error(self.my_list, value)

        return self.my_list.count(value)

    def reverse(self):
        return list(reversed(self.my_list))

    def copy(self):
        new_list = copy.deepcopy(self.my_list)
        return new_list

    def size(self):
        return len(self.my_list)

    def add_first(self, value):
        self.my_list.insert(0, value)

    def dictionize(self):
        my_dict = {}

        for index in range(0, len(self.my_list), 2):
            key = self.my_list[index]

            if Index._is_index_even:
                try:
                    my_dict[key] = self.my_list[index + 1]
                except IndexError:
                    my_dict[key] = ' '

        return my_dict

    def move(self, amount):
        Index.empty_list_error(self.my_list)
        expression = [self.my_list.pop(0) for _ in range(amount)]
        self.my_list.extend(expression)
        return self.my_list

    def sum(self):
        current_sum = 0
        for element in self.my_list:
            if not DataConfiguration.is_element_number(element):
                current_sum += len(element)
                continue

            current_sum += element

        return current_sum

    def overbound(self):
        return DataConfiguration.\
            find_biggest_or_smallest_element_index(self.my_list, 'biggest')

    def underbound(self):
        return DataConfiguration.\
            find_biggest_or_smallest_element_index(self.my_list, 'smallest')

    def __iter__(self):
        return self

    def __next__(self):
        current_index = self.iter_index
        self.iter_index += 1

        if Index._is_index_out_of_range(self.my_list, self.iter_index):
            self.iter_index = 0
            raise StopIteration()

        return self.my_list[current_index]

    def __str__(self):
        return str(list(self.my_list))

    def __repr__(self):
        return CustomList.__str__(self)
