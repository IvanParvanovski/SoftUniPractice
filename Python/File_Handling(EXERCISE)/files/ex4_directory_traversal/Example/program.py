import os
path = input()
result_dict = dict()

for root, dirs, files in os.walk(path):
    if root.count(os.path.sep) > 1:
        continue
    for file in files:
        extension = file.split('.')[1]
        if extension not in result_dict:
            result_dict[extension] = list()
        result_dict[extension].append(file)

result_str = ""
for key, value in sorted(result_dict.items()):
    result_str += f".{key}\n"
    for file in sorted(value):
        result_str += f"- - - {file}\n"
print(result_str)
