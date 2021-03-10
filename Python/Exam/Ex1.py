from math import ceil
a = float(input())
b = float(input())
bar_side = float(input())

full_area = a * b
bar_area = bar_side * bar_side
dancing_area = 19 / 100 * full_area
free_area = full_area - (dancing_area + bar_area)

people = free_area / 3.2
people_ceiled = ceil(people)
print(people_ceiled)

