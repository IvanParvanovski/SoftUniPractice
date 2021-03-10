languages = input().split()
languages_dict = dict()

for element in languages:
    if element.lower() not in languages_dict:
        languages_dict[element.lower()] = 1
    else:
        languages_dict[element.lower()] += 1

for element in languages_dict:
    if languages_dict[element] % 2 != 0:
        print(element, end=" ")
