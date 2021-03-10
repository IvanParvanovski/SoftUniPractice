def input_and_operations():
    password = input()
    right_length = check_password_length(password)
    right_symbols = check_password_symbols(password)
    right_digits = check_password_digits(password)

    if not right_length:
        print("Password must be between 6 and 10 characters")

    if not right_symbols:
        print("Password must consist only of letters and digits")

    if not right_digits:
        print("Password must have at least 2 digits")

    if right_length is True and right_symbols is True and right_digits is True:
        print("Password is valid")


def check_password_length(password):
    
    right_length = False
    counter = 0
    for index in range(len(password)):
        counter += 1
    if 6 <= counter <= 10:
        right_length = True
    return right_length


def check_password_symbols(password):

    right_symbols = False
    for index in range(len(password)):
        if 48 <= ord(password[index]) <= 57 or 65 <= ord(password[index]) <= 90 or 97 <= ord(password[index]) <= 122:
            right_symbols = True
        else:
            right_symbols = False
            break
    return right_symbols


def check_password_digits(password):

    right_digits = False
    counter = 0
    for index in range(len(password)):
        if 48 <= ord(password[index]) <= 57:
            counter += 1
    if counter >= 2:
        right_digits = True
    return right_digits


input_and_operations()
