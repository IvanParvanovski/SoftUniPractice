evens = filter(lambda number: number % 2 == 0, range(10))
odd = filter(lambda number: number % 2 != 0, range(10))

print(f'Even numbers in range 0 to 9 are: {list(evens)}')
print(f'Odd numbers in range 0 to 9 are: {list(odd)}')
