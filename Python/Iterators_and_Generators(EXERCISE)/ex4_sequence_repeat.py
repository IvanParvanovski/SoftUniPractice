class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.counter = 0
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.number:
            raise StopIteration()

        if self.index % len(self.sequence) == 0:
            self.index = 0

        self.current_index = self.index
        self.counter += 1
        self.index += 1
        return self.sequence[self.current_index]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
