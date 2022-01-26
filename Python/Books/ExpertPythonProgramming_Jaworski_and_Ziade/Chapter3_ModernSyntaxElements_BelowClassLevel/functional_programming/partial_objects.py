from functools import partial
from itertools import count

powers_of_2 = partial(pow, 2)
print(powers_of_2(2))
print(powers_of_2(5))
print(powers_of_2(10))

infinite_powers_of_2 = map(partial(pow, 2), count())
print(next(infinite_powers_of_2))
print(next(infinite_powers_of_2))
print(next(infinite_powers_of_2))
