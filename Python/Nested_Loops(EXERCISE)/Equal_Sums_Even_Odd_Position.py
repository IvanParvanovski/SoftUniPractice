first_num = int(input())
second_num = int(input())
for numbers in range(first_num, second_num + 1):
    string_numbers = str(numbers)

    even_sum = 0
    odd_sum = 0
    for digits, index in enumerate(string_numbers):

        if digits % 2 == 0:
            odd_sum += int(index)
        else:
            even_sum += int(index)

    if even_sum == odd_sum:
        print(f"{numbers}", end=" ")
