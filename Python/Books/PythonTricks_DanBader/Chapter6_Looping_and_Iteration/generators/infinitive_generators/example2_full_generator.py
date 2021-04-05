def repeater(value):
    counter = 0
    while True:
        yield value
        counter += 1
        print(counter)


generator_obj = repeater('Hey')
print(next(generator_obj))
print(next(generator_obj))
print(next(generator_obj))
