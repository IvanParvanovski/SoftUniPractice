# Libraries
import os


# Functions
def replace_banned_symbols_with_at_sign(line: str, banned_symbols: set) -> str:
    for symbol in line:
        if symbol in banned_symbols:
            line = line.replace(symbol, '@')
    return line


def reverse_line_as_list(line: list) -> list:
    return [line[index] for index in range(len(line) - 1, -1, -1)]


# File location
file_path = f'files{os.path.sep}ex1_even_lines.txt'

# Structures of data
banned_symbols = {'-',
                  ',',
                  '.',
                  '!',
                  '?'}

# Check if the file exists. When you are sure it exists you can remove "try" and "except"
# There isn't such a condition in the exercise, I made it for your facilitation.
try:
    # Open and close text.txt file with "with".
    # Take every line and check if it's index can be modulus divided by 2
    # If it cans, replace banned symbols, reverse and print
    with open(file_path, 'r') as file:
        for line_index, line in enumerate(file):
            if line_index % 2 == 0:
                replaced_line_symbols = replace_banned_symbols_with_at_sign(line, banned_symbols)
                reversed_line = reverse_line_as_list(replaced_line_symbols.split())
                print(' '.join(reversed_line))

except FileNotFoundError:
    print("File not found!")
    print("Please check the file location.")
