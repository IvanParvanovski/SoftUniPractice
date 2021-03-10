import re
pattern_username = r"U\$(?P<username>[A-Z][a-z]{2,})U\$"
pattern_password = r"P\@\$(?P<password>[A-Za-z]{5,}[0-9]+)P\@\$"
pattern = pattern_username + pattern_password

count = int(input())
counter = 0

for _ in range(count):
    output = ""
    email = input()
    result = re.search(pattern, email)
    if result is None:
        output = "Invalid username or password"
    else:
        output = f"Registration was successful\nUsername: {result.group('username')}, Password: {result.group('password')}"
        counter += 1
    print(output)

print(f"Successful registrations: {counter}")

