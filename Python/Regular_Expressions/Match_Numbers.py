import re

pattern = r"((^|(?<=\s))-?\d+(.\d+)?($|(?=\s)))"
result = re.findall(pattern, input())
for numbers in result:
    print(numbers[0], end=" ")
