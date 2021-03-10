numbers_count = int(input())
p1_counter = 0
p2_counter = 0
p3_counter = 0

for counter in range(numbers_count):
    numnbers = int(input())
    if numnbers % 2 == 0:
        p1_counter += 1
    if numnbers % 3 == 0:
        p2_counter += 1
    if numnbers % 4 == 0:
        p3_counter += 1

p1 = p1_counter / numbers_count * 100
p2 = p2_counter / numbers_count * 100
p3 = p3_counter / numbers_count * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")