def reverse_text(string):
    for s in string[::-1]:
        yield s


for char in reverse_text("step"):
    print(char, end='')
