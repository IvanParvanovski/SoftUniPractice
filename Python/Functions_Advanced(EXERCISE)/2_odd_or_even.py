def even_sum(numbers):
    return sum([x for x in numbers if x % 2 == 0])


def odd_sum(numbers):
    return sum([x for x in numbers if x % 2 != 0])


command = input()
numbers_list = list(map(int, input().split()))
result = 0

if command == "Even":
    result = even_sum(numbers_list)
elif command == "Odd":
    result = odd_sum(numbers_list)

print(result * len(numbers_list))
