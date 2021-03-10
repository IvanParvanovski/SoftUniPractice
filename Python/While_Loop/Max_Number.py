import sys

num_count = int(input())
i = 1

max_num = -sys.maxsize

while i <= num_count:
    num = int(input())

    if num > max_num:
        max_num = num

    i += 1
print(max_num)