import time


def detect_time(func):
    def wrapper(sequence, seq):
        detect_time_start = time.process_time()
        func(sequence, seq)
        detect_time_end = time.process_time()
        executed_time = detect_time_end - detect_time_start
        return executed_time

    return wrapper


@detect_time
def test_sequence(sequence, seq):
    for _ in seq(sequence):
        pass


sequence = [*range(1, 10000000)]
print('Set time: \n')
print(test_sequence(sequence, set))
print('-' * 20)

print('List time: \n')
print(test_sequence(sequence, list))
print('-' * 20)

print('Str time: \n')
print(test_sequence(sequence, str))


