# def create_triangle(num):
#     for row in range(1, num + 1):
#         for col in range(1, num + 1):
#             if row == col:
#                 [print(x + 1, end=" ") for x in range(col)]
#         print()
#
#     for row in range(num - 1, 0, -1):
#         for col in range(num - 1, 0, -1):
#             if row == col:
#                 [print(x, end=" ") for x in range(1, col + 1)]
#         print()
#
#
# num = int(input())
# create_triangle(num)

from triangle import print_line, print_triangle

print_line(1, 10)
print_triangle(4)
