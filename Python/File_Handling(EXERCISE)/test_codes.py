import os

while True:
    command = input().split("-")
    filename = 'files/ex3_file_manipulator_files/' + command[1]

    if command[0] == "End":
        break

    elif command[0] == "Create":
        with open(filename, "w") as file:
            file.write("")

    elif command[0] == "Add":
        file_content = command[2]
        with open(filename, "a") as file:
            file.write(file_content)
            file.write("\n")

    elif command[0] == "Replace":
        old_string = command[2]
        new_string = command[3]
        if os.path.exists(filename):
            text = ""
            with open(filename, "r") as file:
                text = file.read()
            text.replace(old_string, new_string)
            with open(filename, "w") as file:
                file.write(text)
        else:
            print("An error occurred")

    elif command[0] == "Delete":
        if os.path.exists(filename):
            os.remove(filename)
        else:
            print("An error occurred")

