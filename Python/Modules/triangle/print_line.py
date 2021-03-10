def print_line(from_num, to_number):
    step = +1 if from_num <= to_number else -1
    print(
        ' '.join(str(x) for x in range(from_num, to_number + 1, step))
    )
