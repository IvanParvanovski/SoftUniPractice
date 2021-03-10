string_count = int(input())
special_word = input()
full_list = list()

for _ in range(string_count):
    text = str(input())
    full_list.append(text)
print(full_list)

for i in range(len(full_list) - 1, -1, -1):
    element = full_list[i]
    if special_word not in element:
        full_list.remove(element)

print(full_list)