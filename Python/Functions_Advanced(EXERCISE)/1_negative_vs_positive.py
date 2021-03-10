def positive_numbers_sum(numbers):
    return sum([num for num in numbers if num >= 0])


def negative_numbers_sum(numbers):
    return sum([num for num in numbers if num < 0])


numbers = [int(x) for x in input().split()]
negative_numbers = negative_numbers_sum(numbers)
positive_numbers = positive_numbers_sum(numbers)
print(negative_numbers)
print(positive_numbers)

if abs(negative_numbers) > positive_numbers:
    print(f"The negatives are stronger than the positives")
else:
    print(f"The positives are stronger than the negatives")
