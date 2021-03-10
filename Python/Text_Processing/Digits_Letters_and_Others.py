user_input = input()
digits = ""
letters = ""
other = ""
for element in user_input:
    if element.isdigit():
        digits += element
    elif element.isalpha():
        letters += element
    else:
        other += element

print(f"{digits}\n{letters}\n{other}")