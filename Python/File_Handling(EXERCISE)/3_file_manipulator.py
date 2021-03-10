import os


def create_file(file_path: str) -> None:
    open(file_path, 'w').close()


def add_data(file_path: str, content: str) -> None:
    with open(file_path, 'a') as file:
        file.write(content + "\n")


def replace_data(file_path: str, old_content: str, new_content: str) -> None:
    with open(file_path, 'r') as file:
        text = file.read()

    text_with_new_content = text.replace(old_content, new_content)
    with open(file_path, 'w') as file:
        file.write(text_with_new_content)


def delete_file(file: str) -> None:
    os.remove(file)


# Files location
files_path = 'files/ex3_file_manipulator_files/'

# Structures of data
error = "An error occurred"

while True:
    raw_data = input()
    if raw_data == "End":
        break

    split_raw_data = raw_data.split('-')
    command = split_raw_data[0]
    file_name = split_raw_data[1]
    full_file_path = files_path + file_name

    if command == "Create":
        create_file(full_file_path)

    elif command == "Add":
        content = split_raw_data[2]
        add_data(full_file_path, content)

    elif command == "Replace":
        if os.path.exists(full_file_path):
            old_string = split_raw_data[2]
            new_string = split_raw_data[3]
            replace_data(full_file_path, old_string, new_string)
        else:
            print(error)

    elif command == "Delete":
        if os.path.exists(full_file_path):
            delete_file(full_file_path)
        else:
            print(error)
