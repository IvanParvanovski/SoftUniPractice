from math import pi

figure_type = input()
area = 0

if figure_type == "square":
    square_lenght = float(input())
    area = square_lenght * square_lenght
if figure_type == "rectangle":
    rectangle_lenght = float(input())
    rectangle_width = float(input())
    area = rectangle_lenght * rectangle_width
if figure_type == "circle":
    radius = float(input())
    area = pi * radius ** 2
if figure_type == "triangle":
    triangleSide_lenght = float(input())
    triangle_lenght = float(input())
    area = (triangle_lenght * triangleSide_lenght) / 2

print(f"{area:.3f}")