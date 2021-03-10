def parse_input_to_int():
    return [int(num) for num in input().split()]


print([x for x in parse_input_to_int() if x % 2 == 0])
print(list(filter(lambda x: x % 2 == 0, parse_input_to_int())))
