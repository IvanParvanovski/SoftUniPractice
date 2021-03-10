input_num = input()
input_num = int(input_num)
input_num += 1
input_num = str(input_num)

while True:
    symbols_count = len(input_num)
    unique_count = len(set(input_num))

    if symbols_count == unique_count:
        break
    else:
        input_num = int(input_num)
        input_num += 1
        input_num = str(input_num)
print(input_num)