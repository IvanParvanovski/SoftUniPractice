def fibonacci():
    previous_num = 0
    current_num = 1

    while True:
        yield previous_num
        previous_num, current_num = current_num, previous_num + current_num


generator = fibonacci()

for i in range(5):
    print(next(generator))
