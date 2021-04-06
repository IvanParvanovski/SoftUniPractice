def integers():
    for i in range(1, 10):
        print(f'Integers: {i}')
        yield i


def squared(seq):
    for i in seq:
        yield i * i


def negated(seq):
    for i in seq:
        yield -i


chain = negated(squared(integers()))
print(list(chain))
