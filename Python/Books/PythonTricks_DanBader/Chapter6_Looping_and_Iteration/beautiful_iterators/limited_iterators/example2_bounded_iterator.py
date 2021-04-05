class BoundedRepeater:
    def __init__(self, value, max_length):
        self.value = value
        self.max_length = max_length
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_length:
            raise StopIteration
        self.count += 1
        return self.value


repeater = BoundedRepeater('Hello', 3)
for item in repeater:
    print(item)

print()

repeater = BoundedRepeater('Hello', 3)
iterator = iter(repeater)
while True:
    try:
        item = next(iterator)
    except StopIteration:
        break

    print(item)
