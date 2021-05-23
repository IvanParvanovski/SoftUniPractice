number_len = int(input())
digits_count = int(input())
small_letters_count = int(input())
big_letters_count = int(input())

if digits_count + small_letters_count + big_letters_count > number_len:
    print(0)
else:
    result_seq = list(10 for _ in range(digits_count))
    result_seq.extend(30 for _ in range(big_letters_count + small_letters_count))
    result_seq.extend(70 for _ in range(number_len - (digits_count + big_letters_count + small_letters_count)))

    result = 1
    for x in result_seq:
        result *= x

    if number_len > 2:
        for x in range(1, number_len + 1):
            result *= x

    print(result % 1000000007)