class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.counter = self.start

    def __iter__(self):
        self.counter = self.start
        return self

    def __next__(self):
        current_num = self.counter

        if current_num > self.end:
            raise StopIteration()

        self.counter += 1
        return current_num


one_to_ten = custom_range(1, 10)
print(sum(one_to_ten))
print(one_to_ten)
for num in one_to_ten:
    print(num)
