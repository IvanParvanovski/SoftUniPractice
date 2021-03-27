from array import array

from DanBader_PythonTricks.check_time import calculate_time


@calculate_time
def shift_zeros(numbers_):
    counter = 0

    for num in numbers_[::-1]:
        if num == 0:
            counter += 1
            numbers_.remove(0)

    numbers_.extend([0] * counter)
    return None


# numbers = [5, 10, 0, 0, 15] * 15000
# numbers2 = array('i', (5, 10, 0, 0, 15) * 15000)

numbers = array('i', map(int, input().split(', ')))
assert numbers, 'Empty numbers!'

shift_zeros(numbers)
print(numbers)

# shift_zeros(numbers2)
# print(numbers2)

