# Harmful
print(list(filter(lambda x: x % 2 == 0, range(16))))

# print(['even' if x % 2 == 0 else f'odd' for x in range(16)])
# Better
print([x for x in range(16) if x % 2 == 0])

