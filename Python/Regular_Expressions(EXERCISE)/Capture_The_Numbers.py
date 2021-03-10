import re

pattern = r"\d+"

while True:
    text = input()

    if not text:
        break
    result = re.findall(pattern, text)
    for num in result:
        print(num, end=" ")
