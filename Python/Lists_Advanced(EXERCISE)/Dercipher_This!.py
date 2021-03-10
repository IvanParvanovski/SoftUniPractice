string = input().split()
string_list = list()
for element in string:
    code = ""
    for letter in element:
        if letter.isdigit():
            code += letter

    element = element.replace(code, "")
    first_letter = element[0]
    last_letter = element[len(element) - 1]
    local_list = list(element)
    local_list[0], local_list[len(local_list) - 1] = local_list[len(local_list) - 1], local_list[0]
    element = "".join(local_list)
    element = chr(int(code)) + element
    string_list.append(element)

print(" ".join(string_list))
