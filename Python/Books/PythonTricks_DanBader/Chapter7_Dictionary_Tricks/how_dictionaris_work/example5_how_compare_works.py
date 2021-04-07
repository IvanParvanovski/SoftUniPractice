class SameHash:
    def __hash__(self):
        return 1


a = SameHash()
b = SameHash()
print(a == b)

print(hash(a), hash(b))

print(a)
print(b)
print(a is b)

my_dict = {a: 'a', b: 'b'}
print(my_dict)

my_dict[a] = 'c'
print(my_dict)

