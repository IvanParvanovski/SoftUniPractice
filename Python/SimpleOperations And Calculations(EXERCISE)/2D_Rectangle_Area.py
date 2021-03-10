x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
b = 0

if y1 > y2:
    b = y1 - y2
else:
    b = y2 - y1

if x1 > x2:
    a = x1 - x2
else:
    a = x2 - x1

area = a * b
perimeter = (a + b) * 2

print(f"{area:.2f}")
print(f"{perimeter:.2f}")
