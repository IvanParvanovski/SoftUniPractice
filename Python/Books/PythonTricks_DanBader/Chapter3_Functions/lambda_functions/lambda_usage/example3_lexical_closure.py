def make_adder(n):
    return lambda x: x + n


plus_3 = make_adder(3)
print(plus_3(4))
print(plus_3(5))
