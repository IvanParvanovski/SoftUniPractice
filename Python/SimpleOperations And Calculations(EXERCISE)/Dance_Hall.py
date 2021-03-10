from math import ceil, floor

L1 = float(input())
W1 = float(input())
A1 = float(input())

A = A1 * 100
W = W1 * 100
L = L1 * 100

area = (L * W)
bench = (area / 10)
wardrobe = (A * A)

free_area = area-(bench + wardrobe)
area_for_dancers = floor(free_area / (40 + 7000) )
print(area_for_dancers)
