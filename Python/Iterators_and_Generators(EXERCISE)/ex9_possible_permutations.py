from itertools import permutations


def possible_permutations(numbers):

    for per in permutations(numbers):
        yield list(per)


[print(n) for n in possible_permutations([1, 2, 3])]
