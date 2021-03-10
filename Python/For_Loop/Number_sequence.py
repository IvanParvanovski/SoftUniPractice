import sys

full_numbers_count = int(input())
min_num = sys.maxsize
max_num = -sys.maxsize

for numbers_count in range(full_numbers_count):
    numbers = int(input())

    if numbers <= min_num:
        min_num = numbers

    if numbers >= max_num:
        max_num = numbers

print(f"Max number: {max_num}")
print(f"Min number: {min_num}")