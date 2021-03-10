text = "I just created my first file!"
with open('files/my_first_file.txt', 'w') as file:
    print(text, file=file)
    file.write(text)
