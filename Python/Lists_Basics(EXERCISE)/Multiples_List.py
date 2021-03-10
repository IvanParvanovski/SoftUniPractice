factor = int(input())
count = int(input())
num_list = list()
first_factor_num = factor

for number_counter in range(count):
    if number_counter == 0:
        num_list.append(factor)
    else:
        num_list.append(factor + first_factor_num)
        first_factor_num += factor

print(num_list)