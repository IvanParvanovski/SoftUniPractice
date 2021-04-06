def bounded_repeater(value, max_repeats):
    for i in range(max_repeats):
        yield value


iterator = bounded_repeater('Hey', 3)
for x in iterator:
    print(x)


iterator = ('Hello' for i in range(3))

for x in iterator:
    print(x)
