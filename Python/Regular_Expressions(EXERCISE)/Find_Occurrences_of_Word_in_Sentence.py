import re
text = input()
key_word = input()
pattern = rf"\b{key_word}\b"
result = re.findall(pattern, text, re.IGNORECASE)
print(len(result))