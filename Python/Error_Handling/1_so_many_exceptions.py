numbers_list = '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11'.split(", ")
result = 1

for i in range(len(numbers_list) - 1):
    number = int(numbers_list[i + 1])
    if number <= 5:
        result *= number
    elif 5 < number < 10:
        result /= number

print(result)
