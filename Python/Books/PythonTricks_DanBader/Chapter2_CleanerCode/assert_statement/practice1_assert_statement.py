def sub_sum(numbers, start_index, end_index):
    # Problem - Data Validation
    assert type(numbers).__name__ == 'list', 'Not an array!'

    # Right way
    if type(numbers).__name__ != 'list':
        AssertionError('Not an array')

    # ---------------------

    # Amazing example
    assert start_index > 0, 'Start Index is less than 0!'

    # ---------------------

    # Useless example
    assert end_index < len(numbers), 'End Index is greater than array length'

    return numbers[start_index:end_index]


my_numbers = [1, 2, 3, 4, 5]
print(sub_sum(my_numbers, 2, 4))

