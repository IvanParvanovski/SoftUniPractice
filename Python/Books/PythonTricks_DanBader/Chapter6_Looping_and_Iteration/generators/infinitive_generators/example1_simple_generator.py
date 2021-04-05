def repeater(value):
    while True:
        yield value


for x in repeater('Hello'):
    print(x)
