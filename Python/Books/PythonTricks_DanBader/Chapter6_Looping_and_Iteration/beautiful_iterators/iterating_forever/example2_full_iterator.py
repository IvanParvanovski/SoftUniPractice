class RepeaterIterator:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.value


class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return RepeaterIterator(self)


# repeater = Repeater('Hello')
# iterator = repeater.__iter__()
# while True:
#     item = iterator.__next__()
#     print(item)

repeater = Repeater('Hello')
iterator = iter(repeater)
while True:
    item = next(iterator)
    print(item)
