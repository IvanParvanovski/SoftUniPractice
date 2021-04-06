list_comp = ['Hello' for _ in range(3)]
generator = ('Hello' for _ in range(3))

print(list_comp)
print(generator)

# print(next(generator))
# print(next(generator))
# print(next(generator))

print(list(generator))

