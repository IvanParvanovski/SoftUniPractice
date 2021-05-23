from itertools import permutations


def expression(combination, numbers_sum):
    return int(''.join(map(str, combination))) % numbers_sum == 0


first_num = int(input())
second_num = int(input())
third_num = int(input())

numbers = (first_num, second_num, third_num)
combinations = list(permutations(numbers, 3))
numbers_sum = sum(numbers)

result = False
if not (len(set(numbers)) == 1 and 0 in numbers):
    for combination in combinations:
        if expression(combination, numbers_sum):
            result = True

print('Digitivision successful!' if result else 'No digitivision possible.')
