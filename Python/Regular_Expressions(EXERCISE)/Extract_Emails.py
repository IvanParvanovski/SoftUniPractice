import re

user_pattern = r"(( |^)[a-z0-9]+([\.\-_][a-z0-9]+)*"
host_pattern = r"@[a-z]+(-[a-z]+)*([\.][a-z]+(-[a-z]+)*)+)"
result = re.findall(user_pattern + host_pattern, input())
for match in result:
    mail = match[0].strip()
    print(mail)
