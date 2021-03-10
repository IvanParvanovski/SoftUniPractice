class reverse_iter:
    def __init__(self, itr):
        self.itr = itr
        self.counter = len(itr)

    def __iter__(self):
        return self

    def __next__(self):
        self.counter -= 1
        if self.counter < 0:
            raise StopIteration()

        return self.itr[self.counter]


reversed_list = reverse_iter([1, 2, 3, 50, 2200])
for item in reversed_list:
    print(item)
