import re
pattern = r"\b(_[a-zA-Z0-9]+\b)"
text = input()

result = re.findall(pattern, text)
variables = (element.replace("_", "") for element in result)
variables = (element.replace(" ", "") for element in variables)
print(",".join(variables))