def input_and_operations():
    first_character = input()
    second_character = input()

    unicode_of_first_char = ord(first_character)
    unicode_of_second_char = ord(second_character)
    symbols_between_first_char_and_second_char(unicode_of_first_char, unicode_of_second_char)


def symbols_between_first_char_and_second_char(int_first_symbol, int_second_symbol):
    for _ in range(int_first_symbol + 1, int_second_symbol):
        print(chr(_), end=" ")


input_and_operations()