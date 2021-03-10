import os
result_str = ""
path = input()
result_dict = {}
for root, dirs, files in os.walk(path):
    if root.count(os.path.sep) > 1:
        continue
    for file in files:
        extension = file.split(".")[1]
        if extension not in result_dict:
            result_dict[extension] = []
        result_dict[extension].append(file)

for key, value in sorted(result_dict.items()):
    result_str += f".{key}\n"
    for file in sorted(value):
        result_str += f"- - - {file}\n"

desktop = os.path.join(os.path.join(os.path.expanduser('~')), "Desktop")
final_location = desktop + os.path.sep + "report.txt"

with open(final_location, "w") as file:
    file.write(result_str)

