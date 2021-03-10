num_count = int(input())
even_total = 0
odd_total = 0

for num_counter in range(num_count):
    num = int(input())

    if num_counter % 2 == 0:
        even_total += num
    else:
        odd_total += num

if even_total == odd_total:
    print(f"Yes\nSum = {even_total}")
else:
    if even_total > odd_total:
        diff = even_total - odd_total
    else:
        diff = odd_total - even_total
    print(f"No\nDiff = {diff}")
