my_list = [1, 2, 3, 4, 5]

original_list = my_list
my_list[:] = [7, 8, 9]

print(my_list)
print(original_list)
print(original_list is my_list)
