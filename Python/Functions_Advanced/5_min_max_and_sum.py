def parse_input_to_int():
    return [int(num) for num in input().split()]


numbers = parse_input_to_int()
print(f"The minimum number is {min(numbers)}")
print(f"The maximum number is {max(numbers)}")
print(f"The sum number is: {sum(numbers)}")
