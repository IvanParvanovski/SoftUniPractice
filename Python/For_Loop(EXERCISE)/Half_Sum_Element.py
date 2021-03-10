import sys

num_count = int(input())
number2 = 0
biggest_number = -sys.maxsize
total = 0

for counter in range(num_count):
    numbers = int(input())

    if numbers > biggest_number:
        biggest_number = numbers
    total += numbers

total -= biggest_number

if biggest_number == total:
    print(f"Yes\nSum = {total}")
else:
    diff = biggest_number - total
    diff = abs(diff)
    print(f"No\nDiff = {diff}")