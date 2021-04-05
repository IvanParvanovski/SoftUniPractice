def bounded_repeater(value, max_repeats):
    count = 0
    while True:
        if count >= max_repeats:
            return
        count += 1
        yield value


# def bounded_repeater(value, max_repeats):
#     for _ in range(max_repeats):
#         yield value

for x in bounded_repeater('Hey', 5):
    print(x)
