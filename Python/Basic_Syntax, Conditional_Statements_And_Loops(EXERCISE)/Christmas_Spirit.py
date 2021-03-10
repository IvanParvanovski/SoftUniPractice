quantity = int(input())
days = int(input())
total_sum = 0
total_spirit = 0

for counter in range(1, days + 1):
    if counter % 2 == 0:
        total_sum += 2 * quantity
        total_spirit += 5 * quantity

    if counter % 3 == 0:
        total_sum += 8 * quantity
        total_spirit += 13

    if counter % 5 == 0:
        if counter % 3 == 0:
            total_spirit += 30
        else:
            total_spirit += 17
        total_sum += 15 * quantity

    if counter % 10 == 0:
        total_spirit -= 20
        total_sum += 23

    if counter % 11 == 0:
        quantity += 2

if days % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_sum}")
print(f"Total spirit: {total_spirit}")
