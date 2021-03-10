class vowels:
    VOWELS_LIST = ('a',
                   'e',
                   'i',
                   'o',
                   'u',
                   'y')

    def __init__(self, text):
        self.text_vowels = vowels.__filter_vowels_from_text(text)
        self.counter = 0

    @staticmethod
    def __filter_vowels_from_text(text):
        return [sym for sym in text if sym.lower() in vowels.VOWELS_LIST]

    def __is_iter_finished(self):
        return self.counter == len(self.text_vowels)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__is_iter_finished():
            raise StopIteration()

        symbol = self.text_vowels[self.counter]
        self.counter += 1
        return symbol


my_string = vowels('HEllo')
for char in my_string:
    print(char)
