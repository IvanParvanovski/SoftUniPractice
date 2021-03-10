import sys

num_count = int(input())
i = 1
min_num = sys.maxsize

while i < num_count:
    num = int(input())

    if num < min_num:
        min_num = num

    i += 1
print(min_num)