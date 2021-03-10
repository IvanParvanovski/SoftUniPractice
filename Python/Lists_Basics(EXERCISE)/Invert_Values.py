string = input()
all_numbers = string.split()
changed_numbers = list()

for index in range(len(all_numbers)):
    element = all_numbers[index]
    int_element = int(element)
    int_element *= -1
    changed_numbers.append(int_element)
print(changed_numbers)