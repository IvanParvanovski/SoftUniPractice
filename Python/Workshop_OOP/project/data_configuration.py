import sys
from collections.abc import Iterable

from project.index import Index


class DataConfiguration:
    # Data

    @staticmethod
    def __does_data_exist(current_list, data):
        return data in current_list

    @staticmethod
    def _is_data_iterable(obj):
        return isinstance(obj, Iterable)

    @staticmethod
    def data_not_iterable_error(iterable):
        if not DataConfiguration._is_data_iterable(iterable):
            raise TypeError(f'{type(iterable).__name__} is not iterable!')

    @staticmethod
    def does_data_exist_in_list_raise_error(current_list, data):
        if not DataConfiguration.__does_data_exist(current_list, data):
            raise ValueError(f'{data} not in {current_list}!')

    # Values

    @staticmethod
    def _is_value_greater_than_biggest_value(value, biggest_value):
        return value > biggest_value

    @staticmethod
    def _is_value_less_than_smallest_value(value, smallest_value):
        return value < smallest_value

    @staticmethod
    def set_value(element):
        value = element
        if not DataConfiguration.is_element_number(element):
            value = len(element)

        return value

    # Elements

    @staticmethod
    def is_element_number(element):
        return DataConfiguration._is_element_int(element) or \
               DataConfiguration._is_element_float(element)

    @staticmethod
    def find_biggest_or_smallest_element_index(current_list, command):
        Index.index_checks(current_list, 0)

        functions = {
            'biggest': DataConfiguration._is_value_greater_than_biggest_value,
            'smallest': DataConfiguration._is_value_less_than_smallest_value}

        size = {
            'biggest': -sys.maxsize,
            'smallest': sys.maxsize
        }

        func = functions[command]

        result_element_index = 0
        result_element_value = size[command]

        for index in range(len(current_list)):
            element = current_list[index]
            current_value = DataConfiguration.set_value(element)

            if func(current_value, result_element_value):
                result_element_index = index
                result_element_value = current_value

        return result_element_index

    @staticmethod
    def _is_element_int(element):
        return isinstance(element, int)

    @classmethod
    def _is_element_float(cls, element):
        return isinstance(element, float)
