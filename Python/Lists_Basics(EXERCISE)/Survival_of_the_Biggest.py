import sys
num_list = input().split()

int_num_list = list()
for index in range(len(num_list)):
    int_num_list.append(int(num_list[index]))

remove_numbers = int(input())

for removed_numbers_counter in range(remove_numbers):
    min_num = sys.maxsize
    for index in range(len(int_num_list)):
        if int(int_num_list[index]) < min_num:
            min_num = int(int_num_list[index])
    int_num_list.remove(min_num)

print(int_num_list)