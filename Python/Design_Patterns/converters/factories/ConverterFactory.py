from converters.CsvConverter import CsvConverter
from converters.JsonConverter import JsonConverter


class ConverterFactory:
    def __init__(self):
        self.converters = {
            'application/json': JsonConverter(),
            'application/vnd.ms-excel': CsvConverter(),
        }

    def get_converter(self, type):
        if type not in self.converters:
            raise ValueError(f'No converter for type {type}')

        return self.converters[type]
