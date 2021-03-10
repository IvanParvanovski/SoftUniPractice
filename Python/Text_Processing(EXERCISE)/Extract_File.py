file_items = input().split('\\')
file_name = file_items[len(file_items) - 1].split(".")[0]
file_extension = file_items[len(file_items) - 1].split(".")[1]
print(f"File name: {file_name}")
print(f"File extension: {file_extension}")