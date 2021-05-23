def add_first_and_last_lines(first_and_last_lines_count, text):
    first_and_last_lines = (' ' * number +
                            '#' * number * 3 +
                            ' ' * number)

    for _ in range(first_and_last_lines_count):
        text += first_and_last_lines + '\n'
    return text


number = int(input())
width = number * 5
height = number * 4 + 2
first_and_last_lines_count = number // 2

result = add_first_and_last_lines(first_and_last_lines_count, '')
for r in range(height - first_and_last_lines_count * 2):
    current_row = ''

    if r <= number * 2:
        if r == 0 or r == number * 2:
            current_row = '#' * number + \
                          ' ' * number * 3 + \
                          '#' * number

        elif r % 2 == 0:
            current_row += number * '#' + \
                           ' '

            for c in range(0, width - number * 2 - 4, 2):
                current_row += ' #'

            current_row += '  ' + \
                           number * '#'

        elif r % 2 != 0:
            current_row += number * '#'

            for c in range(0, width - number * 2 - 1, 2):
                current_row += ' #'

            current_row += ' ' + '#' * number
    else:
        if r % 2 != 0:
            current_row = width * '#'
        else:
            current_row += number * '#'

            for c in range(0, width - number * 2 - 1, 2):
                current_row += ' #'

            current_row += ' ' + '#' * number

    result += current_row + '\n'

result = add_first_and_last_lines(first_and_last_lines_count, result)
print(result)
