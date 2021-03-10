import os


def replace(file, old_text, new_text):
    try:
        reading_file = open(file, 'r')

        new_file_content = ""
        for line in reading_file:
            stripped_line = line.strip()
            new_line = stripped_line.replace(old_text, new_text)
            new_file_content += new_line + "\n"
        reading_file.close()

        writing_file = open(file, "w")
        writing_file.write(new_file_content)
        writing_file.close()

    except FileNotFoundError:
        print('An error occurred')
    return


def append_to_file(file, text):
    with open(file, 'a') as f:
        f.write(f'{text}\n')
    return


def empty_file(name):
    with open(name, 'w') as f:
        f.write("")
    return


def delete_file(path):
    try:
        os.remove(path)
    except FileNotFoundError:
        print('An error occurred')
    return


command = input()
while command != 'End':
    command_list = command.split('-')
    if command_list[0] == 'Create':
        empty_file(command_list[1])

    elif command_list[0] == 'Add':
        file_name = command_list[1]
        content = command_list[2]
        append_to_file(file_name, content)

    elif command_list[0] == 'Replace':
        file_name = command_list[1]
        old_string = command_list[2]
        new_string = command_list[3]
        replace(file_name, old_string, new_string)

    elif command_list[0] == 'Delete':
        delete_file(command_list[1])

    command = input()
