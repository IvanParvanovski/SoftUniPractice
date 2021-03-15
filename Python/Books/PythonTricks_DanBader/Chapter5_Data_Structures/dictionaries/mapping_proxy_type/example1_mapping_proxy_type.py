from types import MappingProxyType

writable = {'one': 1, 'two': 2, }
read_only = MappingProxyType(writable)

print(writable)
print(read_only)

writable['one'] = 23
print(writable)
print(read_only)

read_only['one'] = 48

