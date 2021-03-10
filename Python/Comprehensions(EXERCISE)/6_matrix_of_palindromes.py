def read_columns(columns, row):
    element = 97 + row
    return [create_output_string(element, column) for column in range(columns)]


def create_output_string(element, column):
    return f"{chr(element)}{chr(element + column)}{chr(element)}"


(rows, columns) = map(int, input().split())

matrix = [read_columns(columns, row) for row in range(rows)]
[print(' '.join(element)) for element in matrix]