email = input()

command = input()

while command != "Complete":
    if command == "Make Upper":
        email = email.upper()
        print(email)
    elif command == "Make Lower":
        email = email.lower()
        print(email)
    elif "GetDomain" in command:
        count = int(command.split()[1])
        print("".join(reversed(email[:len(email) - (count + 1):-1])))
    elif command == "GetUsername":
        if "@" not in email:
            print(f"The email {email} doesn't contain the @ symbol.")
        else:
            print(email.split("@")[0])
    elif "Replace" in command:
        replaced_char = command.split()[1]
        while replaced_char in email:
            email = email.replace(replaced_char, "-")
        print(email)
    elif command == "Encrypt":
        for char in email:
            print(ord(char), end=" ")

    command = input()