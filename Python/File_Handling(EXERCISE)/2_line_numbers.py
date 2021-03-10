# Functions and libraries
import string
import os


def count_characters(text: str) -> int:
    return sum([1 for symbol in text if symbol.isalpha()])


def count_punctuation_marks(text: str, punctuation_marks: tuple) -> int:
    return sum([1 for symbol in text if symbol in punctuation_marks])


# Files locations
input_file_path = f'files{os.path.sep}ex2_line_numbers_input.txt'
output_file_path = f'files{os.path.sep}ex2_line_numbers_output.txt'

# Structures of data
punctuation_marks = tuple(string.punctuation)
error = "File not found!\nPlease check the file location."
texts_info_dict = dict()

# Check if the file exists. When you are sure it exists you can remove "try" and "except"
# There isn't such a condition in the exercise, I made it for your facilitation.
try:
    # Open and close the input.txt file with "with"
    # Get the index as int and the line as string
    # Increase the index with 1 because it starts from 0
    # Create new plot in our texts_info_dict and append the new data
    with open(input_file_path, 'r') as input_file:
        for line_index, line in enumerate(input_file):
            index = line_index + 1
            texts_info_dict[index] = list()
            text_characters = count_characters(line)
            punctuation_marks_count = count_punctuation_marks(line, punctuation_marks)
            texts_info_dict[index].extend((line, text_characters, punctuation_marks_count))

except FileNotFoundError:
    print(error)

# Check if the file exists. When you are sure it exists you can remove "try" and "except"
# There isn't such a condition in the exercise, I made it for your facilitation.
try:
    # Open and close the output.txt file with "with"
    # Get every key from our dict
    # Get every symbol from our text (tokens[0]) without '\n'
    # Import the data in our text file
    with open(output_file_path, 'w') as output_file:
        for key in texts_info_dict:
            tokens = texts_info_dict[key]
            line_text = tokens[0][:-1]
            text_punctuation = tokens[2]
            text_characters = tokens[1]
            output_file.writelines(f"Line {key}: {line_text} ({text_characters})({text_punctuation})\n")

except FileNotFoundError:
    print(error)
