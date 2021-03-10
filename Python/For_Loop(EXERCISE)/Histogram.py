numbers_count = int(input())
p1_under_200 = 0
p2_to_399 = 0
p3_to_599 = 0
p4_to_799 = 0
p5_moreThan_800 = 0

for counter in range(numbers_count):
    numbers = int(input())

    if numbers < 200:
        p1_under_200 += 1

    elif 200 <= numbers <= 399:
        p2_to_399 += 1

    elif 400 <= numbers <= 599:
        p3_to_599 += 1

    elif 600 <= numbers < 800:
        p4_to_799 += 1

    elif numbers >= 800:
        p5_moreThan_800 += 1

p1 = p1_under_200 / numbers_count * 100
p2 = p2_to_399 / numbers_count * 100
p3 = p3_to_599 / numbers_count * 100
p4 = p4_to_799 / numbers_count * 100
p5 = p5_moreThan_800 / numbers_count * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")