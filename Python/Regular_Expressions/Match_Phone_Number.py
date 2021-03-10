import re
pattern = r"(\+359([-| ])2\2\d{3}\2\d{4}\b)"
result = re.findall(pattern, input())
print(", ".join(list(phone for phone, sep in result)))
