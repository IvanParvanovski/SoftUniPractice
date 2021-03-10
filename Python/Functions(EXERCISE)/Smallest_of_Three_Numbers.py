import sys


def smallest_number():
    first_num = int(input())
    second_num = int(input())
    last_num = int(input())

    smallest_num = sys.maxsize
    if first_num < smallest_num:
        smallest_num = first_num
    if second_num < smallest_num:
        smallest_num = second_num
    if last_num < smallest_num:
        smallest_num = last_num

    return smallest_num


print(smallest_number())
