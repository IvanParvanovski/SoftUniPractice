from itertools import count

sequence = filter(
    lambda square: square % 3 == 0 and square % 2 == 1,
    map(
        lambda number: number ** 2,
        count()
    )
)

print(next(sequence))
print(next(sequence))

sequence = (
    square for square
    in (number ** 2 for number in count())
    if square % 3 == 0 and square % 2 == 1
)

print(next(sequence))
print(next(sequence))
