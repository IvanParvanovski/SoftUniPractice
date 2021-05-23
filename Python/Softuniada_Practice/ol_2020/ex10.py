def calculate_permutation(length):
    if length == 1:
        return 1

    return length * calculate_permutation(length - 1)


word_length = int(input())

digits = int(input())
small_letters = int(input())
big_letters = int(input())
result = list()

if word_length < digits + small_letters + big_letters:
    print(0)
else:
    for _ in range(digits):
        result.append(10)

    for _ in range(small_letters):
        result.append(30)

    for _ in range(big_letters):
        result.append(30)

    permutation = 1
    expression_digits = (digits != 0 and (big_letters != 0 or small_letters != 0))
    expression_big_letters = (big_letters != 0 and (digits != 0 or small_letters != 0))
    expression_small_letters = (small_letters != 0 and (digits != 0 or big_letters != 0))

    if any((expression_digits, expression_big_letters, expression_small_letters)):
        permutation = calculate_permutation(word_length)

    result_val = 1
    for x in result:
        result_val *= x
    print(result_val * permutation)
