import re
command_pattern = r"\A[!](?P<command>[A-Z][a-z]{2,})\!"
separator = r":"
message_pattern = r"\[(?P<message>[A-Za-z]{8,})\]$"
pattern = command_pattern + separator + message_pattern

message_count = int(input())
for _ in range(message_count):
    message = input()
    result = re.search(pattern, message)
    if result is not None:
        print(f"{result.group('command')}: {' '.join(list(str(ord(char)) for char in (result.group('message'))))}")
    else:
        print("The message is invalid")

