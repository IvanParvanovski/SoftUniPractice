from time import process_time


def test(func) -> None:
    start_time = process_time()
    func()
    end_time = process_time()

    execution_time = end_time - start_time
    print(execution_time)


def test_tuple(*args):
    args = tuple(args[0])

    @test
    def wrapper():
        for _ in args:
            pass

    return 'hi'


def test_set(*args):
    args = set(args[0])

    @test
    def wrapper():
        for _ in args:
            pass

    return 'hi'


numbers = [x for x in range(100000)]
print(f'Test tuple: {test_tuple(numbers)}')
print(f'Test set: {test_set(numbers)}')
# test_tuple(numbers)
# test_set(numbers)
