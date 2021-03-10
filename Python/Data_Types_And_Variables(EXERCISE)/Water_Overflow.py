numbers = int(input())
total = 0

for num_counter in range(numbers):
    litters = int(input())
    total += litters
    if total > 255:
        total -= litters
        print("Insufficient capacity!")
print(total)