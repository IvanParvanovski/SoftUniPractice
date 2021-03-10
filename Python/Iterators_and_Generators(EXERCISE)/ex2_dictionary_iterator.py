class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.index = 0

    def __is_iter_done(self):
        return self.index == len(self.dictionary)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__is_iter_done():
            raise StopIteration()

        fragment = list(self.dictionary.items())[self.index]
        self.index += 1
        return fragment


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
