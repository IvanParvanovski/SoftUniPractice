def repeat_three_times(value):
    yield value
    yield value
    yield value


for x in repeat_three_times('Hey there'):
    print(x)

print()

generator = repeat_three_times('Hey there')
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
