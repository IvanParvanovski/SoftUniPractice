def sequence_repeat(seq):
    index = 0
    while True:
        if index == len(seq):
            index = 0

        yield seq[index]
        index += 1


res = sequence_repeat('abc')
for i in range(5):
    print(next(res), end='')
