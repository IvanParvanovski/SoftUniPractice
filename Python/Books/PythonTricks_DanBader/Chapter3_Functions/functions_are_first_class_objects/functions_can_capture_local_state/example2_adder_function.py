def make_adder(n):
    def add(x):
        return x + n

    return add


plus_3 = make_adder(3)
plus_5 = make_adder(5)

print(plus_3(4))
print(plus_5(4))
