first_string = input()
second_string = input()
string = ''

for string_index in range(len(first_string)):
    if first_string[string_index] != second_string[string_index]:
        for str_two_index in range(string_index + 1):
            print(second_string[str_two_index], end="")

        for str_one_index in range(string_index + 1, len(first_string)):
            print(first_string[str_one_index], end="")
        print()