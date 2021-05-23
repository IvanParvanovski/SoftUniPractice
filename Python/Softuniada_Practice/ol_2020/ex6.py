import sys
from queue import PriorityQueue

sorted_numbers = PriorityQueue()

array_len = int(input())
numbers_count = int(input())

for _ in range(numbers_count):
    sorted_numbers.put(int(input()))

numbers_list = list()
while not sorted_numbers.empty():
    numbers_list.append(sorted_numbers.get())

smallest_difference = sys.maxsize
while len(numbers_list) >= array_len:
    biggest_num = numbers_list.pop()
    expression = biggest_num - numbers_list[1 - array_len]
    if expression < smallest_difference:
        smallest_difference = expression

print(smallest_difference)
