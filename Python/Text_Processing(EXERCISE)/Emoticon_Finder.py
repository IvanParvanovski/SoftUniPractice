text = input()
my_list = list()
for index in range(len(text)):
    if text[index] == ":":
        if index + 1 < len(text):
            if text[index + 1] != "":
                my_list.append(text[index] + text[index + 1])
for element in my_list:
    print(element)