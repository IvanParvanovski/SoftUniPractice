string = input()
each_element = string.split(", ")
beggars = int(input())
sum_list = list()
count = 0

for each_beggar in range(beggars):
    beggar_total = 0
    for index in range(count, len(each_element), beggars):
        beggar_total += int(each_element[index])
    sum_list.append(beggar_total)
    count += 1
print(sum_list)