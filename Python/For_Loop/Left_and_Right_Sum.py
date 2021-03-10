num_counter = int(input())
left_side_total = 0
right_side_total = 0

for left_side_counter in range(num_counter):
    num = int(input())
    left_side_total += num
for right_side_counter in range(num_counter, num_counter * 2):
    num = int(input())
    right_side_total += num

if left_side_total == right_side_total:
    print(f"Yes, sum = {right_side_total}")

else:
    if left_side_total > right_side_total:
        diff = left_side_total - right_side_total
    else:
        diff = right_side_total - left_side_total
    print(f"No, diff = {diff}")