def calculate_numbers_sum(file_path):
    file = open(file_path, 'r')
    result = 0

    for number_str in file:
        result += int(number_str)
    return result


print(calculate_numbers_sum("files/File Reader/numbers.txt"))
