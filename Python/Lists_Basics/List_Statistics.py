numbers = int(input())
positive = list()
negative = list()

for number_counter in range(numbers):
    num = int(input())
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)

print(positive)
print(negative)
print(f"Count of positives: {len(positive)}. Sum of negatives: {sum(negative)}")